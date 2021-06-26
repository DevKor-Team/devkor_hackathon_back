#!/bin/sh
set -e
# aws configure set default.region ap-northeast-2
python3 manage.py makemigrations --settings=devathon.settings.production
python3 manage.py migrate --settings=devathon.settings.production
python3 manage.py collectstatic --settings=devathon.settings.production --no-input
# aws s3 cp s3://$AWS_BUCKET_NAME/staticfiles.json .
uwsgi --socket 127.0.0.1:8000 wsgiSetting.ini
exec "$@"
