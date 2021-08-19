sudo docker kill $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
docker-compose -f /home/ec2-user/hackathon/back/build/docker-compose.yml up -d
