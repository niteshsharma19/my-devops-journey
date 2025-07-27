# NX-P001 Static Website With Nginx 

## Description

This project is a basic example of serving a static website using the nginx web server inside the Docker container. It demonstrates how to deploy a simple a simple HTML page efficiently.

## features 



## Project Structure
 <pre><code>
  
├── Dockerfile
└── web/
    ├── index.html
    └── style.css

</code></pre>
## Build Docker Images 
 <pre><code>
docker build -t linux19/nginx:s1 .
</code></pre>
## To run a Docker container
 <pre><code>
docker run -d -p 8080:80 --name os1 linux19/nginx:s1 .
</code></pre>
## Acess to the Webiste
open your browser and visit: https://localhost:8080: 
