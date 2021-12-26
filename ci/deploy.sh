#!/bin/bash

echo "AMADEUS_API_KEY=${AMADEUS_API_KEY}" > .env
echo "AMADEUS_API_SECRET=${AMADEUS_API_SECRET}" >> .env
echo "API_URL=${API_URL}" >> .env
echo "API_URL_INSIDE_CONTAINER=${API_URL}" >> .env

docker rmi -f "comworkio/devoxxfr-amadeus-api:latest" || :
docker rmi -f "comworkio/devoxxfr-amadeus-ui-nginx:latest" || :
docker-compose up -d --force-recreate
