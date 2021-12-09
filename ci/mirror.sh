#!/bin/bash

REPO_PATH="${PROJECT_HOME}/devoxx2021-redhat-amadeus-contest/"

cd "${REPO_PATH}" && git pull origin master || :
git push github master 
git push pgitlab master
exit 0
