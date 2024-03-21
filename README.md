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
