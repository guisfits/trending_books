# Trending Books

Search for books based on daily Google Trends of Brazil

This project is a solution for **FIAP's Solution Architecture MBA**, phase 2: _Data Architecture_.  


## Requirements

- [Docker](https://www.docker.com/products/docker-desktop/) up and running
- **MongoDB** as database. You can use [Mongo Compass](https://www.mongodb.com/pt-br/products/tools/compass) to inspect the data.
- [asdf](https://asdf-vm.com/) as `python` version manager, or `v3.11` installed. 

## Instructions

### Running on Docker 🐳
Run `docker compose up`. When it's finished it'll print `✅ Done` on the logs

### Running Locally 💻
- Create `.env` at the root of this repository like `.env.example`
- Run `docker compose up -d database`
- Run `python ./app/main.py`

## Progress

### trending_books
**Guilherme**: 04/fev ✅
- Connect with MongoDb
- Save books
- Save trends
- Add Dockerfile

### Azure
**Máximo**: 08/fev ⏳
- trends_books app [AzureFunction]
- books_recommendation app [AzureFunction]
- MongoDb

### DataAnalysis ⏳
**Rafael**: 15/fev
- PowerBI
    – Connect with MongoDB
    - ETL
    - Process books and trends
    - Recommend books

### Documentation ⏳
**Diego**: 15/fev
- Documentation 
- Architecture Design
- Presentation 

### books_recommendation ❌
**Diego/Rafael/Guilherme/Maximo**: 18/fev
- Create the app

### Review ❌
**Diego/Rafael/Guilherme/Maximo**: 23/fev
- Test everything 
- Document Review
- Pitch call
- Discussion   
