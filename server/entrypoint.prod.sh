#! /bin/bash

if [ "$DATABASE" == "postgres" ]; then
    echo "Waiting for postgres to start ..."

    timeout=60
    interval=1
    count=0

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
        if [ "$count" -ge "$timeout" ]; then
            echo -e "Timeout reached. Postgres failed to start within $timeout seconds.\n❌️Exiting ..."
            exit 1
        else
            echo "❗️waiting for a tcp connection ..."
            sleep "$interval"
            count=$(expr "$count" + "$interval")
        fi
    done

    echo "🔥️🚀️ Postgresql started successfully"

fi

exec "$@"
