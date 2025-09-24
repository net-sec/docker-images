#!/bin/bash

podman rm -f images
podman run -it -d \
  -p 8082:8080 \
  --name images \
  -v $(pwd)/images:/app/images:ro,z \
  localhost/images:dev