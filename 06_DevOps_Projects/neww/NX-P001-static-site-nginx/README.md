# NX-P001 Static Website With Nginx 

## Description

This project is a basic example of serving a static website using the nginx web server inside the Docker container. It demonstrates how to deploy a simple a simple HTML page efficiently.

## features 

<pre><code>
 
## Project Structure

'''
.
|--- Dockerfile
|--- web/
|      |__ index.html
|      |__ style.css
'''

## Build Docker Images 

'''bash
docker build -t nginx:s1 .
'''

## To run a Docker container

'''bash
docker run -d -p 8080:80 --name os1 nginx:s1 .
'''

## Access the Website
open your browser and visit: http://localhost:8080

 
