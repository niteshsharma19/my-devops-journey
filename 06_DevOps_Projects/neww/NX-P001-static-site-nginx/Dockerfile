# Use Nginx as a base Image
FROM nginx:alpine

# Remove file from container
RUN rm -rf /usr/share/nginx/html/*

# Copy website to the Container
COPY web/ /usr/share/nginx/html

# Expose  port  80 to the host
EXPOSE 80

# Start Nginx Server 
CMD ["nginx", "-g","daemon off;"]
