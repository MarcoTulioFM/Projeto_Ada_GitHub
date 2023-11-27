#!/bin/bash

git remote update
git fetch
git pull
git checkout main
git checkout develop -- index.html
git add .
git commit -m "Atualizando index.html"
git push