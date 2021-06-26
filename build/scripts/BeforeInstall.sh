rm -rf /home/ec2-user/hackathon/back
docker stop hackathon-back || true && docker rmi hackathon-back || true
