"""Verify the ADR 0010 shared-asset reference contract.

Every HTML document must reference /assets/base.css and /assets/orison.js with
a query value equal to the first twelve characters of that file's current
SHA-256 digest. Run from anywhere before any deployment that changes a shared
asset or an HTML reference:

    python3 deploy/verify_asset_versions.py

Exits 0 and prints a JSON summary when the contract holds; exits 1 with one
line per violation otherwise. Standard library only.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ASSETS = {
    "base.css": ROOT / "assets" / "base.css",
    "orison.js": ROOT / "assets" / "orison.js",
}

REFERENCE = re.compile(r"/assets/(base\.css|orison\.js)(?:\?v=([0-9a-f]*))?")


def html_documents():
    for path in sorted(ROOT.rglob("*.html")):
        relative = path.relative_to(ROOT)
        if any(part in {".git", ".serena"} for part in relative.parts):
            continue
        yield path


def main():
    digests = {
        name: hashlib.sha256(path.read_bytes()).hexdigest()[:12]
        for name, path in ASSETS.items()
    }
    violations = []
    documents = 0
    for document in html_documents():
        documents += 1
        source = document.read_text()
        found = {name: 0 for name in ASSETS}
        for match in REFERENCE.finditer(source):
            name, query = match.group(1), match.group(2)
            found[name] += 1
            if query != digests[name]:
                line = source.count("\n", 0, match.start()) + 1
                violations.append(
                    f"{document.relative_to(ROOT)}:{line}: {match.group(0)!r} "
                    f"does not match current digest ?v={digests[name]}"
                )
        for name, count in found.items():
            if count == 0:
                violations.append(
                    f"{document.relative_to(ROOT)}: no reference to /assets/{name}"
                )
    if documents == 0:
        violations.append("no HTML documents found; wrong working tree?")
    if violations:
        print("\n".join(violations), file=sys.stderr)
        return 1
    print(json.dumps({"documents": documents, "assets": digests, "status": "pass"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
