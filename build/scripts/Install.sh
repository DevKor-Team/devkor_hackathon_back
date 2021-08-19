aws ecr get-login-password --region ap-northeast-2 | sudo docker login --username AWS --password-stdin 792939917746.dkr.ecr.ap-northeast-2.amazonaws.com
docker pull 792939917746.dkr.ecr.ap-northeast-2.amazonaws.com/devkor-hackathon-back:latest
docker pull 792939917746.dkr.ecr.ap-northeast-2.amazonaws.com/devkor-hackathon-front:latest
docker tag 792939917746.dkr.ecr.ap-northeast-2.amazonaws.com/devkor-hackathon-back:latest devkor-hackathon-back:latest
docker tag 792939917746.dkr.ecr.ap-northeast-2.amazonaws.com/devkor-hackathon-front:latest devkor-hackathon-front:latest
