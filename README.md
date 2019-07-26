# url_shortener
```

setup env:
sudo apt -y update
sudo apt -y install snapd
sudo snap install docker
sudo snap install microk8s --classic
sudo microk8s.start


git clone https://github.com/giota-f/url_shortener.git
cd url_shortener/
microk8s.kubectl create -f mysql-pv.yaml
microk8s.kubectl create -f mysql-deployment.yaml

microk8s.kubectl describe pod mysql-7d7fdd478f-4dpv7
microk8s.kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h 10.1.1.14 -ppassword

restapi docker image create:
sudo apt-get install docker.io
sudo usermod -aG docker ubuntu
su - ubuntu
docker login
sudo docker build -f Dockerfile -t thecuriousdoggo/restapi:public .
docker images
docker tag 9b88be309e9a thecuriousdoggo/restapi:public
docker push thecuriousdoggo/restapi
```
