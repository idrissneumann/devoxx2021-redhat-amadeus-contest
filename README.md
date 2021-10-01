# DevoxxFR RedHat for developer's and Amadeus contest

![devoxxfr](./img/devoxxfr.jpg)

## Instructions

![instructions1](./img/instructions1.jpg)

![instructions2](./img/instructions2.jpg)

## Used technologies

* Amadeus API SDK: https://github.com/amadeus4dev/amadeus-python
* RedHat developer sandbox: https://developers.redhat.com/developer-sandbox


## Local deployment with docker-compose

```shell
$ cp .env.dist .env #replace the variable content by your own credentials
$ docker-compose up -d --force-recreate
```

Then you can go to:
* http://localhost:8011 : for the api
* http://localhost:8012 : for the frontend

## Openshift deployment

![oc](./img/openshift.png)

![api](./img/api.png)

![ui](./img/ui.png)
