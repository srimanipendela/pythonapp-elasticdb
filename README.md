SRE Techincal Assessment

Its a simple python application which maintains a list of cities and their population. This application uses elasticsearch as database. 

Available API in Python APP,
/health     - Endpoint for checking health of APP

/add_data   - Endpoint for inserting a city and its population

/get        - Endpoint for retrieving the population of a city


Modes of installation
Docker-compose
K8s (Helm)
Usage
We can use install_app.sh to install application either through docker-compose or through helm in k8s.

Steps:

Exexute the install_app.sh
select deployment type (docker-compose/k8s)

Note: Change necessary values in ./helm/values.yaml before deployment in k8s