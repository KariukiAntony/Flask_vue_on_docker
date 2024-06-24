#! /bin/bash

: '---- CONSTANTS ----'
COMPOSE_FILE=docker-compose.yaml

function deploy() {

    # check if the specified compose file exist
    if [ ! -e ${COMPOSE_FILE} ]; then
        echo -e "Error. docker-compose file ${COMPOSE_FILE} was not found.\nExiting ....."
        exit 1

    fi

    echo "Finally!. Your application is ready for deployment ..."

    read -p "Do you want to deploy the latest changes? " input
    lower=${input,,}

    if [ $lower == "yes" ] || [ $lower == "y" ]; then
        echo "Deploying your latest changes"
        docker compose -f ${COMPOSE_FILE} up -d --build

    elif [ $lower == "no" ] || [ $lower == "n" ]; then
        echo "Skipping deploying the latest changes .."
        exit 1

    else
        echo "Invalid input. exiting ..."
        exit 1

    fi
}

function main() {
    # deploy the latest changes ..
    deploy
}

main
