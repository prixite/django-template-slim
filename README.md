# Backend Template For Django

This application uses micro-services architecture. Here is the list of different
services we use in dev environment:

- *Django* - This serves the API.
- *PostgreSQL* - The DB service.

For production, we have the following services:

- *Nginx* - This is used as reverse proxy.
- *Gunicorn/Django* - This is the application server. It runs the Python Django
  application.
- *PostgreSQL* - The DB service.

## Installation
The easiest way to start development is through Docker setup. If you have
Docker, run the following command to setup everything:

```
docker-compose build
docker-compose up -d
```

You can access the application at http://localhost:8000/


## Production Deployment
Production deployment is also done using Docker. All the files associated with
prod deployment are present in prod folder. To start prod build, do:

```
cd prod
docker-compose build
docker-compose up -d
````
