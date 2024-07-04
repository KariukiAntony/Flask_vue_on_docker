#! /bin/bash
: '---- CONSTANTS ----'
development=docker-compose.dev.yaml
staging=docker-compose.stage.yaml
production=docker-compose.prod.yaml

BLUE="\033[94m"
GREEN="\033[92m"
ENDC="\033[0m"

check_docker() {
    if ! command -v docker compose &>/dev/null; then
        echo "Make sure you have docker compose installed on your machine..."
        echo "Exiting ...."
        exit 1
    fi
}

validate_user_input() {
    input=$1
    input=${input,,}
    if [[ "$input" == "dev"* ]]; then
        echo -e "$BLUE You choose the development env.\nStarting the containers\n $ENDC"
        check_docker
        docker compose -f $development up -d --build

    elif [[ "$input" == "stage"* ]]; then
        echo -e "$BLUE You choose the staging env.\nStarting the containers\n $ENDC"
        check_docker
        docker compose -f $staging up -d --build

    elif [[ "$input" == "prod"* ]]; then
        echo -e "$BLUE You choose the production env.\nStarting the containers\n $ENDC"
        check_docker
        docker compose -f $production up -d --build
      
    fi
}

start() {
    echo -e "$BLUE\n🔥️🚀️--------------->> GETTING STARTED WITH FLASK_VUE _ON_DOCKER <<------------- 🔥️🚀️\n$ENDC"
    echo -e "$GREEN dev ====> Development\n stage ====> Stagging\n prod ====> Production\n$ENDC"
    read -r -p "Choose any of the above environments to get started.(dev/stage/prod): " input
    validate_user_input "$input"
}

start
