#!/bin/bash

docker run \
  -it \
  -e ZUUL_PROJECT=mediawiki/extensions/AchievementBadges \
  -v "$(pwd)"/ref:/srv/git:ro \
  -v "$(pwd)"/cache:/cache \
  -v "$(pwd)"/log:/workspace/log \
  -v "$(pwd)"/src:/workspace/src \
  --entrypoint bash \
  --rm \
  docker-registry.wikimedia.org/releng/quibble-stretch-php73:latest
