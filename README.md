# SRE Techincal Assessment 

## Description:

Its a simple python application which maintains a list of cities and their population. This application uses elasticsearch as database. 

This application with elastic DB is containerized, and packaged for deployment to Kubernetes with hem and for deployment to docker environment with docker-compose(>1.29).


### Available API in Python APP

/health     - Endpoint for checking health of APP

/add_data   - Endpoint for inserting a city and its population

/get        - Endpoint for retrieving the population of a city



## Modes of installation

1. Docker-compose
2. K8s (Helm)



# Usage

We can use install_app.sh to install application either through docker-compose or through helm in k8s.
Steps:
1. Exexute the install_app.sh
2. select deployment type (docker-compose/k8s)



Note: Installation mode docker-compose only supports with docker-compose > 1.29 

Note: Change necessary values in ./helm/values.yaml before deployment in k8s

Note: Currently running Elastic DB as single node cluster

