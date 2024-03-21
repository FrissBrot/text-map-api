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

## SetUp Postgres database
This Porject runs only on Postgres. You can use a dedicated database or integrate the database in your project. If not exeist, the setup will create the tables "chunk" and "savedRoute" and fill it with some example data. You can edit the data later.

### Database diagram
![drawSQL-image-export-2024-03-21 (1)](https://github.com/FrissBrot/text-map-api/assets/60073321/23037a58-5a5a-4c8b-b467-1f607bc2f7bf)

## example Data

## Docker Compose example with postres and pgAdmin
