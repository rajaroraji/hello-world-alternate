FROM nginx:alpine
# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
# Copy the custom nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
# Copy static files
COPY hello.html /usr/share/nginx/html/hello.html
COPY world.html /usr/share/nginx/html/world.html
