#!/usr/bin/env bash
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d
docker-compose -f docker-compose.prod.yml exec web ./manage.py migrate
docker-compose -f docker-compose.prod.yml exec web ./manage.py collectstatic --no-input
