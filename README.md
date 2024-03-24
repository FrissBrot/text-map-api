# Map Text API

This Docker image provides an API for calculating the time and path between two points on a map. 

DockerHub Repository: https://hub.docker.com/r/frissbrot/map-api

## Docker Compose Example

```yaml
version: '3'

services:
  app:
    image: frissbrot/map-api:latest
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - DB_USER=*YOUR DB USER*
      - DB_PASSWORD=*YOUR DB USER PASSWORD*
      - DB_DATABASE=*YOUR DATABASE NAME*
```

## API Call Example

Here's an example API call:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"start": 16, "target": 1}' http://127.0.0.1:5000/api
```

## Setting Up the Postgres Database

This project exclusively runs on Postgres. You can either use a dedicated database or integrate the database into your project. If it doesn't exist, the setup will create the "chunk" and "savedRoute" tables and populate them with some example data, which you can later edit.

### Database Diagram

![Database Diagram](https://github.com/FrissBrot/text-map-api/assets/60073321/23037a58-5a5a-4c8b-b467-1f607bc2f7bf)

## Example Data

The data for the map is provided as example data in the "chunk" table.

![Map Example](https://github.com/FrissBrot/text-map-api/assets/60073321/f0405b33-e868-4ed2-8c89-afb2dd9739ea)

## Docker Compose Example with Postgres and pgAdmin

```yaml
version: '3'

services:
  app:
    image: frissbrot/map-api:latest
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=db
      - DB_USER=postgres
      - DB_PASSWORD=db123
      - DB_DATABASE=ep-planer

  db:
    image: postgres
    environment:
      POSTGRES_DB: ep-planer
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: db123
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: example@example.com
      PGADMIN_DEFAULT_PASSWORD: db123
    ports:
      - "8080:80"
    depends_on:
      - db

volumes:
  postgres_data:
```

Feel free to let me know if you need further enhancements!
