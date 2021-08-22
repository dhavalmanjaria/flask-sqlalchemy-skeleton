#!/bin/bash

# Temporary measure but ensures that the 
# application is actually running


sleep 5
curl localhost:8000/api/v1/healthcheck


