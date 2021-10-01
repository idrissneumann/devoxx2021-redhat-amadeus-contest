#!/bin/bash

echo "AMADEUS_API_KEY=${AMADEUS_API_KEY}" > .env
echo "AMADEUS_API_SECRET=${AMADEUS_API_SECRET}" >> .env
echo "API_URL=${API_URL}" >> .env
docker-compose up -d --force-recreate
