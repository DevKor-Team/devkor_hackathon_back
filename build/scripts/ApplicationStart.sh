docker run -dit \
-e SECRET_KEY=$SECRET_KEY \
-e GOOGLE_OAUTH_CLIENT_ID=$GOOGLE_OAUTH_CLIENT_ID \
-e GOOGLE_OAUTH_SECRET=$GOOGLE_OAUTH_SECRET \
--rm --name hackathon-back \
-p 8000:8000 \
-v /home/ec2-user/hackathon/back:/app \
hackathon-back:latest
