#!/usr/bin/bash

lambda_dir=$PWD

set -e

printf 'Installing Python Dependencies in package...\n'
pip3 install -r requirements.txt -t ./package

printf '\nPackaging Dependencies into zip...\n'
cd package
zip -r9 $lambda_dir/function.zip .

printf '\nPackaging Code into zip file'
cd ../src/profile_scraper
zip -r ../../function.zip .
cd ../..

printf '\nUploading to Lambda\n'
aws lambda update-function-code --function-name uosc-crawler-deploy-test --zip-file fileb://function.zip

printf '\nPublishing Changes\n'
aws lambda publish-version --function-name uosc-crawler-deploy-test

printf '\nChanges deployed!\n'