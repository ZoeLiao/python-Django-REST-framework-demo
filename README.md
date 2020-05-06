# Django REST Framework Demo

## Docker and K8s
### Build image and tag it
- `docker build -t <your docker hub>/django-rest-framework-demo .`
### Test image
- `docker run -p 8001:8001 <your docker hub>/django-rest-framework-demo:latest` 

### Push to your Docker Hub
- `docker login` 
- `docker push <your docker hub>/django-rest-framework-demo:latest`

### Set up by K8s
#### Create pods and test it
- `kubectl create -f pod.yaml`
- `kubectl port-forward pod 8001:8001`
#### Create service and check it
- `kubectl create -f service.yaml`
- `kubectl get pods`
#### Create deployment and ingress
- `kubectl create -f deployment.yaml`
- `minikube addons enable ingress` 
- `kubectl create -f ingress.yaml`
#### Start minikube dashboard
- `minikube dashboard`

## Reference
- [Kubernetes 基礎教學（二）實作範例：Pod、Service、Deployment、Ingress](https://medium.com/@C.W.Hu/kubernetes-implement-ingress-deployment-tutorial-7431c5f96c3e)
