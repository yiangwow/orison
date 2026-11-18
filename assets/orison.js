(() => {
  "use strict";

  const LEGACY_COOKIE = "orison_trace";
  const STORAGE_KEY = "orison_trace_v2";
  const MAX_STATE_BYTES = 2048;
  const DAY_MS = 86400000;
  const ROUTES = [
    "root",
    "missing",
    "inode",
    "exam",
    "archive",
    "mirror",
    "weather",
    "integrity",
    "choir",
    "staff",
    "letter",
    "operator",
    "extent",
    "fragments",
  ];
  const FLAGS = [
    "unpacked",
    "invited",
    "examined",
    "mirror-route",
    "forecast",
    "forecast-returned",
    "forecast-held",
    "warning-armed",
    "checksum-match",
    "checksum-drift",
    "aperture-slip",
    "heard",
    "letter",
    "operator-probe",
    "operator-occupied",
    "response-attached",
    "orphan-released",
    "fragment-probe-013",
    "fragment-probe-027",
    "fragment-probe-058",
    "probed",
  ];
  const ANSWER_GROUPS = [
    ["valuable", "dangerous", "system"],
    ["record", "memory", "contradiction"],
    ["compliant", "forward", "parallel"],
    ["process", "operator", "interruption"],
    ["earlier", "changed", "comparison"],
  ];
  const HELD_ROOMS = ["mirror", "weather", "integrity", "choir", "staff"];
  const MODES = ["unknown", "keyboard", "pointer", "touch", "mixed"];
  const COMMANDS = {
    recovery: 1,
    inspect: 2,
    process: 4,
    mount: 8,
    utility: 16,
  };
  let pageConfig = null;
  let enteredAt = Date.now();
  let currentState = null;
  let erased = false;
  let focusTimer = null;
  let audioContext = null;
  let audioWasRunningBeforeHide = false;
  const activeSoundStops = new Set();
  let receiverFrame = 0;
  let keyboardNavigation = false;

  const today = () => Math.floor(Date.now() / DAY_MS);

  function makeId() {
    const values = new Uint16Array(2);
    crypto.getRandomValues(values);
    return [...values]
      .map((value) => value.toString(16).padStart(4, "0"))
      .join("")
      .toUpperCase();
  }

  const freshState = () => ({
    v: 2,
    id: makeId(),
    firstDay: today(),
    expiresDay: today() + 30,
    visits: 0,
    seen: {},
    order: [],
    last: "",
    returns: 0,
    attention: 0,
    activity: 0,
    answers: [],
    flags: [],
    witness: "",
    obs: {
      mode: "unknown",
      commands: 0,
      refused: 0,
      held: [],
    },
  });

  const isPlainObject = (value) =>
    value !== null && typeof value === "object" && !Array.isArray(value);

  function boundedInteger(value, maximum) {
    return Number.isFinite(value)
      ? Math.min(maximum, Math.max(0, Math.floor(value)))
      : 0;
  }

  function sanitizeWitness(value) {
    return typeof value === "string" && /^[A-Za-z0-9_-]{1,16}$/.test(value)
      ? value
      : "";
  }

  function normalizeSeen(value) {
    if (!isPlainObject(value)) return {};
    return Object.fromEntries(
      ROUTES.filter(
        (route) => Number.isFinite(value[route]) && value[route] > 0,
      ).map((route) => [
        route,
        Math.max(1, boundedInteger(value[route], 3)),
      ]),
    );
  }

  function normalizeOrder(value) {
    if (!Array.isArray(value)) return [];
    return [...new Set(value.filter((route) => ROUTES.includes(route)))].slice(
      0,
      ROUTES.length,
    );
  }

  function normalizeAnswers(value) {
    const source = Array.isArray(value) ? value : [];
    return ANSWER_GROUPS.map((group) =>
      group.find((answer) => source.includes(answer)),
    ).filter(Boolean);
  }

  function normalizeFlags(value) {
    if (!Array.isArray(value)) return [];
    return [...new Set(value.filter((flag) => FLAGS.includes(flag)))];
  }

  function normalizeHeld(value) {
    if (!Array.isArray(value)) return [];
    return [...new Set(value.filter((room) => HELD_ROOMS.includes(room)))];
  }

  function normalizeState(value) {
    const source = isPlainObject(value) ? value : {};
    const obs = isPlainObject(source.obs) ? source.obs : {};
    const currentDay = today();
    return {
      v: 2,
      id: /^[A-F0-9]{8}$/.test(source.id) ? source.id : makeId(),
      firstDay:
        Number.isFinite(source.firstDay) &&
        source.firstDay >= 0 &&
        source.firstDay <= currentDay
        ? Math.floor(source.firstDay)
        : currentDay,
      expiresDay: Number.isFinite(source.expiresDay)
        ? Math.min(currentDay + 30, Math.floor(source.expiresDay))
        : currentDay + 30,
      visits: boundedInteger(source.visits, 31),
      seen: normalizeSeen(source.seen),
      order: normalizeOrder(source.order),
      last: ROUTES.includes(source.last) ? source.last : "",
      returns: boundedInteger(source.returns, 7),
      attention: boundedInteger(source.attention, 3),
      activity: boundedInteger(source.activity, 31),
      answers: normalizeAnswers(source.answers),
      flags: normalizeFlags(source.flags),
      witness: sanitizeWitness(source.witness),
      obs: {
        mode: MODES.includes(obs.mode) ? obs.mode : "unknown",
        commands: boundedInteger(obs.commands, 31),
        refused: boundedInteger(obs.refused, 3),
        held: normalizeHeld(obs.held),
      },
    };
  }

  function migrateLegacy(state) {
    const migrated = freshState();
    migrated.firstDay =
      Number.isFinite(state.first) && state.first >= 0 && state.first <= Date.now()
      ? Math.floor(state.first / DAY_MS)
      : migrated.firstDay;
    migrated.visits = boundedInteger(state.visits, 31);
    migrated.seen = normalizeSeen(state.seen);
    delete migrated.seen.fragments;
    migrated.order = normalizeOrder(state.order).filter(
      (route) => route !== "fragments",
    );
    migrated.last =
      ROUTES.includes(state.last) && state.last !== "fragments" ? state.last : "";
    migrated.returns = boundedInteger(state.returns, 7);
    migrated.attention = boundedInteger(state.focus, 3);
    migrated.activity = Number.isFinite(state.seconds)
      ? boundedInteger(Math.floor(state.seconds / 30), 31)
      : 0;
    migrated.answers = normalizeAnswers(state.answers);
    migrated.flags = normalizeFlags(state.flags).filter(
      (flag) =>
        flag !== "response-attached" &&
        flag !== "orphan-released" &&
        !flag.startsWith("fragment-probe-"),
    );
    migrated.witness = sanitizeWitness(state.invited);
    return migrated;
  }

  function readLegacyCookie() {
    const prefix = `${LEGACY_COOKIE}=`;
    const raw = document.cookie
      .split("; ")
      .find((part) => part.startsWith(prefix))
      ?.slice(prefix.length);

    if (!raw) return null;

    try {
      const state = JSON.parse(decodeURIComponent(raw));
      return isPlainObject(state) && state.v === 1 ? state : null;
    } catch {
      return null;
    }
  }

  function deleteLegacyCookie() {
    const secure = window.location.protocol === "https:" ? "; Secure" : "";
    document.cookie = `${LEGACY_COOKIE}=; Max-Age=0; Path=/; SameSite=Lax${secure}`;
  }

  function byteLength(value) {
    return new TextEncoder().encode(value).length;
  }

  function readStoredState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      if (byteLength(raw) > MAX_STATE_BYTES) {
        localStorage.removeItem(STORAGE_KEY);
        return null;
      }
      const parsed = JSON.parse(raw);
      if (!isPlainObject(parsed) || parsed.v !== 2) {
        localStorage.removeItem(STORAGE_KEY);
        return null;
      }
      if (!Number.isFinite(parsed.expiresDay) || parsed.expiresDay < today()) {
        localStorage.removeItem(STORAGE_KEY);
        return null;
      }
      return normalizeState(parsed);
    } catch {
      return null;
    }
  }

  function storeState(state) {
    try {
      const normalized = normalizeState(state);
      normalized.expiresDay = today() + 30;
      const serialized = JSON.stringify(normalized);
      if (byteLength(serialized) > MAX_STATE_BYTES) return null;
      localStorage.setItem(STORAGE_KEY, serialized);
      if (localStorage.getItem(STORAGE_KEY) !== serialized) return null;
      return normalized;
    } catch {
      return null;
    }
  }

  function readState() {
    const stored = readStoredState();
    if (stored) {
      deleteLegacyCookie();
      currentState = stored;
      return stored;
    }

    const legacy = readLegacyCookie();
    const candidate = legacy ? migrateLegacy(legacy) : freshState();
    const saved = storeState(candidate);
    if (saved) {
      deleteLegacyCookie();
      currentState = saved;
      return saved;
    }

    currentState = currentState || candidate;
    return normalizeState(currentState);
  }

  function writeState(state) {
    if (erased) return normalizeState(state);
    const saved = storeState(state);
    currentState = saved || normalizeState(state);
    if (saved) deleteLegacyCookie();
    return currentState;
  }

  function hasFlag(state, flag) {
    return state.flags.includes(flag);
  }

  function addFlag(state, flag) {
    if (!hasFlag(state, flag)) state.flags.push(flag);
  }

  function awareness(state) {
    const distinct = Object.keys(state.seen).length;
    return Math.min(
      5,
        Math.floor(distinct / 2) +
        (state.returns > 1 ? 1 : 0) +
        (state.attention >= 3 ? 1 : 0) +
        (hasFlag(state, "letter") ? 1 : 0),
    );
  }

  function navigationType() {
    return performance.getEntriesByType("navigation")[0]?.type || "navigate";
  }

  function visit(page) {
    const state = readState();
    const previous = state.last;
    const isReturn =
      state.seen[page] > 0 || navigationType() === "back_forward";

    state.visits = Math.min(31, state.visits + 1);
    state.seen[page] = Math.min(3, (state.seen[page] || 0) + 1);
    if (!state.order.includes(page)) state.order.push(page);
    if (isReturn) state.returns = Math.min(7, state.returns + 1);
    state.last = page;

    const query = new URLSearchParams(window.location.search);
    const fragment = new URLSearchParams(window.location.hash.slice(1));
    const invitation = sanitizeWitness(
      query.get("witness") || fragment.get("witness") || "",
    );
    if (invitation && !state.witness) {
      state.witness = invitation;
      addFlag(state, "invited");
    }
    if (query.has("witness") || fragment.has("witness")) {
      const url = new URL(window.location.href);
      url.searchParams.delete("witness");
      url.hash = "";
      history.replaceState(history.state, "", `${url.pathname}${url.search}`);
    }

    writeState(state);
    enteredAt = Date.now();
    return { state, previous, isReturn };
  }

  function baseRender(state) {
    document.documentElement.dataset.awareness = String(awareness(state));
    document.querySelectorAll("[data-trace-id]").forEach((node) => {
      node.textContent = state.id;
    });
    document.querySelectorAll("[data-visit-count]").forEach((node) => {
      node.textContent =
        state.visits >= 31 ? "031+" : String(state.visits).padStart(3, "0");
    });
    document.querySelectorAll("[data-observed-activity]").forEach((node) => {
      node.textContent =
        state.activity >= 31
          ? "15m30s+"
          : `${String(state.activity * 30).padStart(4, "0")}–${String(
              state.activity * 30 + 29,
            ).padStart(4, "0")}s`;
    });
    document.querySelectorAll("[data-local-time]").forEach((node) => {
      node.textContent = new Date().toLocaleTimeString("en-GB", {
        hour12: false,
      });
    });
  }

  function receiverStatus(state) {
    const level = awareness(state);
    if (hasFlag(state, "orphan-released")) return "PARENT TRACE / RETAINED";
    if (hasFlag(state, "response-attached")) return "RESPONSE SOURCE / ATTACHED";
    if (hasFlag(state, "operator-occupied")) return "AUTHORITY CHANNEL / OCCUPIED";
    if (hasFlag(state, "operator-probe")) return "SUBJECT CHANNEL / OPEN";
    if (hasFlag(state, "forecast")) return "WATCHDOG / RETURN CONFIRMED";
    if (level >= 3) return `TRACE ${state.id} / ATTACHED`;
    if (level >= 2) return "INPUT VECTOR / RETAINED";
    return "RECEIVER FIELD / ACQUIRING";
  }

  function recoveryDepth(state) {
    const rooms = ["mirror", "weather", "integrity", "choir", "staff"];
    const completedRooms = rooms.filter((room) => state.seen[room]).length;
    if (
      hasFlag(state, "checksum-match") ||
      hasFlag(state, "checksum-drift") ||
      hasFlag(state, "letter") ||
      hasFlag(state, "operator-probe") ||
      hasFlag(state, "forecast-held")
    ) {
      return 3;
    }
    if (
      completedRooms >= 2 ||
      hasFlag(state, "heard") ||
      hasFlag(state, "forecast-returned")
    ) {
      return 2;
    }
    return hasFlag(state, "unpacked") || hasFlag(state, "examined") ? 1 : 0;
  }

  function restartFieldMotion(field) {
    field.classList.remove("is-running");
    void field.offsetWidth;
    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      window.requestAnimationFrame(() => field.classList.add("is-running"));
    }
  }

  function renderRecoveryField(state) {
    let field = document.querySelector(".root-infrastructure");
    if (!field) {
      field = document.createElement("div");
      field.className = "root-infrastructure";
      field.setAttribute("aria-hidden", "true");
      field.innerHTML = `
        <span class="root-scan"></span>
        <div class="root-processes"></div>
        <span class="root-missing-block"></span>
      `;
      document.body.prepend(field);
    }

    const depth = recoveryDepth(state);
    field.dataset.depth = String(depth);
    const rows = [
      ["00000000", depth >= 1 ? "detached buffer / retained" : "scan pending"],
      ["carrier/44", hasFlag(state, "heard") ? "phase source / open" : "output / muted"],
      [
        "front/19",
        hasFlag(state, "forecast-returned")
          ? "history return / retained"
          : hasFlag(state, "forecast-held")
            ? "source remains / attached"
            : "arrival / unresolved",
      ],
      [
        "operator",
        hasFlag(state, "orphan-released")
          ? `parent trace/${state.id} / retained`
          : hasFlag(state, "response-attached")
            ? "response source / attached"
            : hasFlag(state, "operator-occupied")
              ? "authority channel / occupied"
              : hasFlag(state, "operator-probe")
                ? "input source / inferred"
                : "wait channel / empty",
      ],
    ];
    const processRows = field.querySelector(".root-processes");
    processRows.replaceChildren();
    rows.forEach(([channel, status]) => {
      const row = document.createElement("span");
      const name = document.createElement("span");
      const reading = document.createElement("span");
      name.textContent = channel;
      reading.textContent = status;
      row.append(name, reading);
      processRows.append(row);
    });
    restartFieldMotion(field);
  }

  function installReceiverField(state) {
    if (pageConfig?.ambient === false) return;

    let field = document.querySelector(".receiver-field");
    if (field) {
      field.querySelector(".receiver-field__status").textContent =
        receiverStatus(state);
      restartFieldMotion(field);
      return;
    }

    field = document.createElement("div");
    field.className = "receiver-field";
    field.setAttribute("aria-hidden", "true");
    field.innerHTML = `
      <span class="receiver-field__rail receiver-field__rail--left"></span>
      <span class="receiver-field__rail receiver-field__rail--right"></span>
      <span class="receiver-field__status"></span>
      <span class="receiver-field__coordinates">0000:0000</span>
      <i class="receiver-field__reticle"></i>
    `;
    document.body.prepend(field);

    const status = field.querySelector(".receiver-field__status");
    const coordinates = field.querySelector(".receiver-field__coordinates");
    const reticle = field.querySelector(".receiver-field__reticle");
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let targetX = window.innerWidth * 0.5;
    let targetY = window.innerHeight * 0.5;
    let currentX = targetX;
    let currentY = targetY;

    status.textContent = receiverStatus(state);
    field.dataset.active = "false";
    restartFieldMotion(field);

    function renderReticle() {
      const ease = reduced ? 1 : 0.11;
      currentX += (targetX - currentX) * ease;
      currentY += (targetY - currentY) * ease;
      reticle.style.transform = `translate3d(${currentX}px, ${currentY}px, 0)`;
      receiverFrame = window.requestAnimationFrame(renderReticle);
    }

    document.addEventListener(
      "pointermove",
      (event) => {
        targetX = event.clientX;
        targetY = event.clientY;
        coordinates.textContent =
          `${String(Math.round(targetX)).padStart(4, "0")}:` +
          `${String(Math.round(targetY)).padStart(4, "0")}`;
        field.dataset.active = "true";
      },
      { passive: true },
    );

    document.documentElement.addEventListener("pointerleave", () => {
      field.dataset.active = "false";
      status.textContent = "INPUT VECTOR / OUTSIDE FIELD";
    });

    document.documentElement.addEventListener("pointerenter", () => {
      status.textContent = receiverStatus(readState());
    });

    document.addEventListener("pointerdown", () => {
      status.textContent = "INTERRUPT / ACCEPTED";
      window.setTimeout(() => {
        status.textContent = receiverStatus(readState());
      }, reduced ? 0 : 540);
    });

    window.cancelAnimationFrame(receiverFrame);
    renderReticle();
  }

  function enter() {
    if (!pageConfig) return;
    const context = visit(pageConfig.name);
    baseRender(context.state);
    renderRecoveryField(context.state);
    installReceiverField(context.state);
    pageConfig.render?.(context.state, context);
  }

  function page(config) {
    pageConfig = config;
    window.addEventListener("pageshow", enter);
  }

  function update(mutator) {
    const state = readState();
    mutator(state);
    const saved = writeState(state);
    baseRender(saved);
    return saved;
  }

  function flag(name) {
    return update((state) => addFlag(state, name));
  }

  function answer(value) {
    return update((state) => {
      if (!state.answers.includes(value)) state.answers.push(value);
    });
  }

  function observeCommand(category, refused = false) {
    return update((state) => {
      if (COMMANDS[category]) state.obs.commands |= COMMANDS[category];
      if (refused) state.obs.refused = Math.min(3, state.obs.refused + 1);
    });
  }

  function hold(room) {
    if (!HELD_ROOMS.includes(room)) return readState();
    return update((state) => {
      if (!state.obs.held.includes(room)) state.obs.held.push(room);
    });
  }

  function recordMode(mode) {
    if (!MODES.includes(mode) || mode === "unknown") return;
    const state = readState();
    const next =
      state.obs.mode === "unknown"
        ? mode
        : state.obs.mode === mode
          ? mode
          : "mixed";
    if (state.obs.mode === next) return;
    state.obs.mode = next;
    writeState(state);
  }

  function countLabel(value, maximum) {
    return value >= maximum ? `${maximum}+` : String(value);
  }

  function attentionLabel(value) {
    return ["none", "single", "repeated", "persistent"][value] || "none";
  }

  function reset() {
    erased = true;
    window.clearTimeout(focusTimer);
    window.cancelAnimationFrame(receiverFrame);
    stopAudio();
    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch {
      // Browser storage may already be unavailable.
    }
    deleteLegacyCookie();
    currentState = null;
    window.location.replace("/");
  }

  function browserName() {
    const agent = navigator.userAgent;
    if (/Edg\//.test(agent)) return "EDGE-CLASS";
    if (/Firefox\//.test(agent)) return "FIREFOX-CLASS";
    if (/Chrome\//.test(agent)) return "CHROMIUM-CLASS";
    if (/Safari\//.test(agent) && !/Chrome\//.test(agent)) return "WEBKIT-CLASS";
    return "UNRESOLVED";
  }

  function platformName() {
    const platform = navigator.userAgentData?.platform || navigator.platform || "";
    const agent = `${platform} ${navigator.userAgent}`;
    if (/Windows/i.test(agent)) return "WINDOWS-CLASS";
    if (/Android/i.test(agent)) return "ANDROID-CLASS";
    if (/iPhone|iPad|iPod/i.test(agent)) return "IOS-CLASS";
    if (/Mac/i.test(agent)) return "MAC-CLASS";
    if (/Linux/i.test(agent)) return "LINUX-CLASS";
    return "UNRESOLVED";
  }

  function profile() {
    const date = new Intl.DateTimeFormat().resolvedOptions();
    return {
      browser: browserName(),
      platform: platformName(),
      locale: navigator.language || date.locale || "UNRESOLVED",
      zone: date.timeZone || "UNRESOLVED",
      screen: `${screen.width} × ${screen.height}`,
      viewport: `${window.innerWidth} × ${window.innerHeight}`,
      threads: navigator.hardwareConcurrency || "WITHHELD",
      memory: navigator.deviceMemory ? `~${navigator.deviceMemory} GiB` : "WITHHELD",
      touch: navigator.maxTouchPoints > 0 ? `${navigator.maxTouchPoints} POINT` : "INDIRECT",
      contrast: window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "DARK PREFERENCE"
        : "LIGHT PREFERENCE",
      motion: window.matchMedia("(prefers-reduced-motion: reduce)").matches
        ? "REDUCED"
        : "UNRESTRICTED",
    };
  }

  function ensureAudio() {
    const Audio = window.AudioContext || window.webkitAudioContext;
    if (!Audio) return null;
    if (!audioContext || audioContext.state === "closed") {
      audioContext = new Audio();
    }
    if (audioContext.state === "suspended") audioContext.resume();
    return audioContext;
  }

  function soundPulse(variant = "relay") {
    const context = ensureAudio();
    if (!context) return false;

    const voices = {
      relay: [
        [41.2, 0],
        [61.8, 0.045],
      ],
      weather: [
        [61.8, 0],
        [82.4, 0.07],
      ],
      retained: [
        [41.2, 0],
        [82.4, 0.11],
      ],
    };
    const now = context.currentTime;
    const gain = context.createGain();
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.exponentialRampToValueAtTime(0.014, now + 0.025);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.34);
    gain.connect(context.destination);

    (voices[variant] || voices.relay).forEach(([frequency, delay], index) => {
      const oscillator = context.createOscillator();
      oscillator.type = index ? "triangle" : "sine";
      oscillator.frequency.value = frequency;
      oscillator.connect(gain);
      oscillator.start(now + delay);
      oscillator.stop(now + 0.36);
    });
    return true;
  }

  function openCarrier(variant = "carrier") {
    const context = ensureAudio();
    if (!context) return () => {};

    const master = context.createGain();
    const frequencies = [41.2, 61.8, 82.4];
    const detune = variant === "weather" ? [-4, 3, -2] : [0, 0, 0];
    const oscillators = frequencies.map((frequency, index) => {
      const oscillator = context.createOscillator();
      const voice = context.createGain();
      oscillator.type = index === 1 ? "triangle" : "sine";
      oscillator.frequency.value = frequency;
      oscillator.detune.value = detune[index];
      voice.gain.value = 0.55 / (index + 1);
      oscillator.connect(voice).connect(master);
      oscillator.start();
      return oscillator;
    });
    master.gain.value = variant === "weather" ? 0.018 : 0.035;
    master.connect(context.destination);

    let stopped = false;
    const stop = () => {
      if (stopped) return;
      stopped = true;
      activeSoundStops.delete(stop);
      oscillators.forEach((oscillator) => oscillator.stop());
      master.disconnect();
    };
    activeSoundStops.add(stop);
    return stop;
  }

  function stopAudio() {
    [...activeSoundStops].forEach((stop) => stop());
    if (audioContext && audioContext.state !== "closed") audioContext.close();
    audioContext = null;
    audioWasRunningBeforeHide = false;
  }

  function keyClick(event) {
    if (
      event.repeat ||
      event.ctrlKey ||
      event.metaKey ||
      event.altKey ||
      ["Shift", "Control", "Alt", "Meta", "CapsLock", "Tab"].includes(event.key)
    ) {
      return;
    }

    const context = ensureAudio();
    if (!context) return;

    const now = context.currentTime;
    const sharp = context.createOscillator();
    const body = context.createOscillator();
    const gain = context.createGain();
    sharp.type = "square";
    sharp.frequency.value = 1250 + Math.random() * 550;
    body.type = "triangle";
    body.frequency.value = event.key === "Enter" ? 105 : 155 + Math.random() * 35;
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.exponentialRampToValueAtTime(0.018, now + 0.002);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.028);
    sharp.connect(gain);
    body.connect(gain);
    gain.connect(context.destination);
    sharp.start(now);
    body.start(now);
    sharp.stop(now + 0.018);
    body.stop(now + 0.03);
  }

  function terminalInput(input) {
    const form = input.closest("form");
    const updateWaiting = () => {
      if (form) form.dataset.empty = String(input.value.length === 0);
    };
    input.addEventListener("keydown", keyClick);
    input.addEventListener("input", updateWaiting);
    updateWaiting();
  }

  function drawSignal(canvas, variant = "inode") {
    const context = canvas.getContext("2d");
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let frame = 0;
    let pointerX = 0.5;
    let pointerY = 0.5;

    function resize() {
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      const rect = canvas.getBoundingClientRect();
      canvas.width = Math.max(1, Math.floor(rect.width * ratio));
      canvas.height = Math.max(1, Math.floor(rect.height * ratio));
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
    }

    function render(time = 0) {
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      const state = currentState || readState();
      const level = awareness(state);
      const cx = width * (0.5 + (pointerX - 0.5) * 0.04);
      const cy = height * (variant === "mirror" ? 0.47 : 0.5);
      const radius = Math.min(width, height) * 0.22;

      context.clearRect(0, 0, width, height);
      context.save();
      context.globalCompositeOperation = "screen";

      for (let ring = 0; ring < 15 + level * 2; ring += 1) {
        const points = 90;
        const ringRadius = radius * (0.28 + ring / 17);
        context.beginPath();

        for (let point = 0; point <= points; point += 1) {
          const angle = (point / points) * Math.PI * 2;
          const wave =
            Math.sin(angle * (3 + (ring % 5)) + time * 0.00045) *
              (3 + ring * 0.23) +
            Math.cos(angle * 13 - time * 0.00019) * (1.5 + level);
          const x = cx + Math.cos(angle) * (ringRadius + wave);
          const flatten = variant === "mirror" ? 1.17 : 0.78;
          const y = cy + Math.sin(angle) * (ringRadius * flatten + wave);
          point === 0 ? context.moveTo(x, y) : context.lineTo(x, y);
        }

        const red = level >= 4 && ring % 6 === 0;
        context.strokeStyle = red
          ? "rgba(171,46,54,.35)"
          : `rgba(205,220,211,${0.035 + ring * 0.008})`;
        context.lineWidth = ring % 4 === 0 ? 0.8 : 0.42;
        context.stroke();
      }

      if (variant === "mirror" && hasFlag(state, "forecast")) {
        const offset = 22 + Math.sin(time * 0.0004) * 6;
        context.globalAlpha = 0.2 + level * 0.035;
        context.strokeStyle = "#a5aab3";
        context.strokeRect(
          cx - radius * 0.42 + offset,
          cy - radius * 0.73,
          radius * 0.84,
          radius * 1.46,
        );
      }

      context.restore();
      frame = window.requestAnimationFrame(render);
    }

    canvas.addEventListener("pointermove", (event) => {
      const rect = canvas.getBoundingClientRect();
      pointerX = (event.clientX - rect.left) / rect.width;
      pointerY = (event.clientY - rect.top) / rect.height;
    });
    window.addEventListener("resize", resize);
    window.addEventListener("pagehide", () => cancelAnimationFrame(frame));
    resize();
    render(reduced ? 1 : performance.now());
  }

  document.addEventListener("visibilitychange", () => {
    window.clearTimeout(focusTimer);
    if (document.visibilityState === "hidden") {
      audioWasRunningBeforeHide = audioContext?.state === "running";
      if (audioWasRunningBeforeHide) audioContext.suspend();
      focusTimer = window.setTimeout(() => {
        update((state) => {
          state.attention = Math.min(3, state.attention + 1);
        });
      }, 750);
    } else {
      if (audioWasRunningBeforeHide && audioContext?.state === "suspended") {
        audioContext.resume();
      }
      audioWasRunningBeforeHide = false;
      const status = document.querySelector(".receiver-field__status");
      if (status) {
        status.textContent = "RETURN EVENT / RETAINED";
        window.setTimeout(() => {
          status.textContent = receiverStatus(readState());
        }, 900);
      }
    }
  });

  window.addEventListener("pagehide", () => {
    window.clearTimeout(focusTimer);
    document.querySelector(".root-infrastructure")?.classList.remove("is-running");
    document.querySelector(".receiver-field")?.classList.remove("is-running");
    stopAudio();
    if (erased) return;
    const elapsed = Math.min(120, Math.floor((Date.now() - enteredAt) / 1000));
    const state = readState();
    state.activity = Math.min(31, state.activity + Math.floor(elapsed / 30));
    writeState(state);
  });

  document.addEventListener(
    "pointerdown",
    (event) => {
      if (!event.target.closest("a, button, input, select, textarea")) return;
      keyboardNavigation = false;
      recordMode(event.pointerType === "touch" ? "touch" : "pointer");
    },
    { passive: true },
  );

  document.addEventListener("keydown", (event) => {
    if (event.key === "Tab") {
      keyboardNavigation = true;
      return;
    }
    const control = event.target.closest("a, button, input, select, textarea");
    if (!control) return;
    const activatesWithSpace = control.matches(
      "a, button, input[type='radio'], input[type='checkbox']",
    );
    if (event.key === "Enter" || (event.key === " " && activatesWithSpace)) {
      recordMode("keyboard");
    }
  });

  document.addEventListener("focusin", (event) => {
    if (
      keyboardNavigation &&
      event.target.closest("a, button, input, select, textarea")
    ) {
      recordMode("keyboard");
    }
    keyboardNavigation = false;
  });

  window.addEventListener("storage", (event) => {
    if (event.key !== STORAGE_KEY) return;
    if (event.newValue === null) {
      erased = true;
      window.clearTimeout(focusTimer);
      window.cancelAnimationFrame(receiverFrame);
      stopAudio();
      currentState = null;
      window.location.replace("/");
      return;
    }
    currentState = readStoredState();
  });

  window.ORISON = {
    page,
    update,
    flag,
    answer,
    observeCommand,
    hold,
    reset,
    profile,
    terminalInput,
    soundPulse,
    openCarrier,
    stopAudio,
    read: readState,
    hasFlag,
    awareness,
    countLabel,
    attentionLabel,
    drawSignal,
    renderRecoveryField,
  };
})();
