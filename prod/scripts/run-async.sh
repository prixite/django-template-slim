#!/usr/bin/env bash
gunicorn --worker-tmp-dir /dev/shm -k uvicorn.workers.UvicornWorker project.awsgi:application --bind unix:/dev/shm/async-gunicorn.sock
