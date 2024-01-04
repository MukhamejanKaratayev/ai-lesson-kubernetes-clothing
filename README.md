# Урок 74-78. Kubernetes 

pipenv install grpcio==1.42.0 flask gunicorn keras-image-helper
pipenv install tensorflow protobuf==3.19


# To get read off sudo before docker 
sudo usermod -aG docker <your-username>
newgrp docker


docker build -t ai-lesson-clothing-model:xception-v4-001 -f image-model.dockerfile .

docker run -it --rm -p 8500:8500 ai-lesson-clothing-model:xception-v4-001

docker build -t ai-lesson-gateway:001 -f image-gateway.dockerfile .

docker run -it --rm -p 9696:9696 ai-lesson-gateway:001


# Docker compose

sudo chmod +x docker-compose

docker-compose up

docker-compose up -d
docker-compose down

docker build -t ping:v001 .
docker run -it --rm -p 9696:9696 ping:v001

kind create cluster

kubectl get service
kubectl get pod
kubectl get deployment

# add deployment
sudo kubectl apply -f deployment.yaml
sudo kubectl get deployment
sudo kubectl get pod
sudo kubectl describe pod ping-deployment-7795dd4bc5-pvbfj

kind load docker-image ping:v001
kubectl port-forward ping-deployment-7795dd4bc5-pvbfj 9696:9696

kubectl apply -f service.yaml
kubectl port-forward service/ping 8080:80

# Deploy clothing model to kuber

kind load docker-image zoomcamp-10-model:xception-v4-001

kubectl port-forward tf-serving-clothing-model-85cd4b7fc9-rntfw 8500:8500

kubectl port-forward service/tf-serving-clothing-model 8500:8500

kind load docker-image zoomcamp-10-gateway:002

kubectl exec -it ping-deployment-577d56ccf5-p2bdq -- bash

apt update
apt install curl telnet 
telnet tf-serving-clothing-model.default.svc.cluster.local 8500

kubectl port-forward service/gateway 8080:80