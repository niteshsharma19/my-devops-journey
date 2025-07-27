# Use Nginx as a base Image
FROM ngnix:alpine

# Remove file from container
RUN rm -rf /usr/share/ngnix/html/*

# Copy website to the Container
COPY web/ /usr/share/ngnix/html

# Expose  port  80 to the host
EXPOSE 80

# Start Nginx Server 
CMD ["ngnix", "-g","daemon off;"]