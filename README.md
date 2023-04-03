# SQL Code Generation Example

This repository contains an example of how to use the TextCortex API to generate SQL code.
This functionality allows you to ask questions directly to your database using natural language, making it much easier
and faster for developers and non-technical users alike.

## Features

* Generate SQL code from natural language queries
* Easily query databases without having to learn complex syntax
* Save time by quickly getting answers from your database

## Setup Guide

1. Sign up for a TextCortex account [here](https://app.textcortex.com/user/dashboard).
2. Click on the settings -> API tab to get your API key.
3. Copy the API key and paste it into the `api_key` variable in `main.py`.
4. Install dependencies with `pip install -r requirements.txt`.
5. Connect to a database, in our case its a dummy database called `bikeStores.db` that we create
   using `generate_dummy_db.py`. Its already in the repo so you don't need to create it again. But if you want to
   experiment with it, first delete the `bike_store.db` file and then run `generate_dummy_db.py`.
6. Running this script will create a `bikeStores.db` file in the same directory as `main.py`. This will be our database
   that we will be querying.
7. Use the `main.py` script in this repository as a starting point for creating queries in natural language that can be
   translated into SQL statements automatically!

## Documentation

For more information on how to generate code and sql queries with the TextCortex API, please see
our [documentation](https://docs.textcortex.com).
