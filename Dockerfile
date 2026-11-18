FROM nginx:alpine

COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY assets /usr/share/nginx/html/assets
COPY .lost+found /usr/share/nginx/html/.lost+found
COPY erase /usr/share/nginx/html/erase
COPY elias /usr/share/nginx/html/elias
COPY mihai /usr/share/nginx/html/mihai
COPY index.html 404.html privacy.txt robots.txt /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget --spider -q http://127.0.0.1/robots.txt || exit 1
