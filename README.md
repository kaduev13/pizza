# Pizza ordering backend

## The task

Imagine a pizza ordering services with following functionality:

* Order pizza. Order data:
    * pizza id
    * pizza size (30cm/50cm)
    * customer name
    * customer address (just plain text)
* Update order
* Remove order
* See a list of customer orders

Tasks:

* Design Model/DB structure (PostgreSQL) 
* Design and implement API with Django Rest Framework for the described web service. Please note:
    * You don’t have to take care about authentication etc, we are just interested in structure and data modelling.
    * You don’t have to implement any UI, just the API endpoints
* Write test(s) for at least one of these endpoint(s)

Notes:
* Use viewsets where possible
* Keep your endpoints as restful as possible

## Running the application

```bash
$ git clone https://github.com/kaduev13/pizza.git
$ cd pizza
$ docker-compose -f docker-compose.yml up --build
```

By default application is running on `localhost:8992`.


## Tests

```bash
$ docker-compose -f docker-compose.yml -f docker-compose.test.yml up --build --abort-on-container-exit
```


## Development

```bash
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```
