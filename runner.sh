#!/usr/bin/env bash

REBUILD=${1:-False}

if [ "$REBUILD" = "true" ] || [ "$REBUILD" = "True" ]
then
  echo "Rebuild docker containers nginx & flask_dash"
  docker-compose up --build --remove-orphans --abort-on-container-exit
else
  echo "starting docker containers nginx & flask_dash"
  docker-compose up nginx flask_dash redis
fi
