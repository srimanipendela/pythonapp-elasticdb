#!/bin/bash
set -e
log()
{
         echo "[$(date --rfc-3339=seconds)]: $*"
}

error()
{
         echo "[$(date --rfc-3339=seconds)]: $*"
         exit 1
}


get_inputs()
{       
	read -p 'Deployment Type (docker-compose/k8s) ' deployment_type
        case $deployment_type in
           (docker-compose|k8s)      ;;
                (*)             error "Invalid selection '$deployment_type' for deployment type. Should be 'docker-compose' or 'k8s'. ";;
        esac
}

get_inputs

if [ "${deployment_type}" = "docker-compose" ]; then
    if ! docker ps > /dev/null 2>&1 ; then
       error "Docker service down. Please check the service status and try the installation"
    fi 
    docker-compose up -d
else
    if [ ! -f ~/.kube/config || $KUBECONFIG ]; then
       error "Cant find kube config in this location ~/.kube/config. Please add config to ~/.kube/config or export config as $KKUBECONFG and run the task" 
    fi
    helm install sreassignment ./helm/   --render-subchart-notes   
fi

log "#############################################"
log "Deployiment finsished using $deployment_type"
log "#############################################"
