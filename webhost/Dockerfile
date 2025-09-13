FROM nginx:stable-alpine
COPY public /usr/share/nginx/html
RUN sed -i 's/listen\s\+80;/listen 8080;/' /etc/nginx/conf.d/default.conf \
 && sed -i 's|index  index.html index.htm;|index index.html;|' /etc/nginx/conf.d/default.conf
