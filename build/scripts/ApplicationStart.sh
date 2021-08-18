sudo service nginx restart
docker run -dit \
-e SECRET_KEY=123123123 \
-e GOOGLE_OAUTH_CLIENT_ID=$GOOGLE_OAUTH_CLIENT_ID \
-e GOOGLE_OAUTH_SECRET=$GOOGLE_OAUTH_SECRET \
-e DB_NAME=$DB_NAME \
-e DB_USERNAME=$DB_USERNAME \
-e DB_PASSWORD=$DB_PASSWORD \
-e DB_HOST=$DB_HOST \
--rm --name hackathon-back \
-p 8000:8000 \
-v /home/ec2-user/hackathon/back:/app \
hackathon-back:latest