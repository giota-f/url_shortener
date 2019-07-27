# Custom URL shortener
## Microk8s setup
Microk8s is a single node Kubernetes setup which is used to deploy MySQL and Flask apps.
More info on microk8s here [Microk8s](https://microk8s.io)

## MySQL set up on Kubernetes
The deployment of MySQL on Kubernetes is based on [MySQL deployment](https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/)
Note: Because SQLite is serveless the database and the application run on the same process thus not the best choice for deploying on Kubernetes

### Steps to install microk8s on an Ubuntu server:
```
setup env:
sudo apt -y update
sudo apt -y install snapd
sudo snap install docker
sudo snap install microk8s --classic
sudo microk8s.start
```
### Steps to deploy MySQL on Kubernetes:
```
git clone https://github.com/giota-f/url_shortener.git
cd url_shortener/microk8s/
microk8s.kubectl create -f mysql-pv.yaml
microk8s.kubectl create -f mysql-deployment.yaml
```
### Access DB using MySQL client:
How to get the MySQL host IP:
```
microk8s.kubectl get pods
microk8s.kubectl describe pod mysql-*
microk8s.kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h hostip -ppassword
```
### Build Flask app Dockerfile:
Code under url_shortener/restapi/ is the python code.
Dockerizing our app and uploading image to docker registry.
But first we install docker:
```

sudo apt-get install docker.io
sudo usermod -aG docker ubuntu
su - ubuntu
docker login
sudo docker build -f Dockerfile -t thecuriousdoggo/restapi:public .
docker images
docker tag imageid thecuriousdoggo/restapi:public
docker push thecuriousdoggo/restapi
```
### Deploy restapi app on Kubernetes

```
microk8s.kubectl create -f mysql-deployment.yaml
```

Notes!
In a real env deployment DB credentials would be hibben also there will not be any hardocoded configuration in the code and they will discovered by kubernetes and passed as env variables
