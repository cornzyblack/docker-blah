#!/bin/bash
BASEDIR=$(dirname $0)
# Set Environmental variables
source $BASEDIR/.env # What do you need to fix here and why?
echo $MYNAME;
echo 'This is the present working directory' $PWD;
echo $FAVOURITE_COLOR;
echo 'Hope you are having fun with Docker 😅?';
