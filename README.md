# Map Text API

This Dockerimage provides a API to calculate time and path of two points on a map.
GitHub: https://github.com/FrissBrot/text-map-api

## Docker Compose example
```
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
## API Call
A example API call.
```
curl -X POST -H "Content-Type: application/json" -d '{"start": 16, "target": 1}' http://127.0.0.1:5000/api
```
## SetUp Postgres database
This Porject runs only on Postgres. You can use a dedicated database or integrate the database in your project. If not exeist, the setup will create the tables "chunk" and "savedRoute" and fill it with some example data. You can edit the data later.

### Database diagram
![drawSQL-image-export-2024-03-21 (1)](https://github.com/FrissBrot/text-map-api/assets/60073321/23037a58-5a5a-4c8b-b467-1f607bc2f7bf)

## example Data
The Data for the following map is provided as example data in the "chunk" table.
![Map-Test-Map-Costs-Test-Map-Costs drawio](https://github.com/FrissBrot/text-map-api/assets/60073321/f0405b33-e868-4ed2-8c89-afb2dd9739ea)

## Docker Compose example with postres and pgAdmin
```
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
