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
![drawSQL-image-export-2024-03-21 (1)](https://github.com/FrissBrot/text-map-api/assets/60073321/23037a58-5a5a-4c8b-b467-1f607bc2f7bf)
