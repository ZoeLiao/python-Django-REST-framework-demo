# Django REST Framework Demo

## Docker and K8s
### 1.Build image and tag it
- `docker build -t <your docker hub>/django-rest-framework-demo .`
### 2.Test image
- `docker run -p 8001:8001 <your docker hub>/django-rest-framework-demo:latest` 

### 3.Push to your Docker Hub
- `docker login` 
- `docker push <your docker hub>/django-rest-framework-demo:latest`

### 4.Set up by K8s
#### 4a.Create deployment and check it
- `kubectl create -f deployment.yaml`
- `kubectl get deployments`
#### 4b.Create service and check it
- `kubectl create -f service.yaml`
- `kubectl get services`
#### 4c.Create ingress and modify /etc/host
- `minikube addons enable ingress` 
- `kubectl create -f ingress.yaml`
- `minikube ip`
- copy ip and story in /etc/host
#### 4d.Start minikube dashboard
- `minikube dashboard`

## Reference
- [Kubernetes 基礎教學（二）實作範例：Pod、Service、Deployment、Ingress](https://medium.com/@C.W.Hu/kubernetes-implement-ingress-deployment-tutorial-7431c5f96c3e)
- [How Django can handle 100 millions of requests per day](https://medium.com/ebs-integrator/how-django-can-handle-100-millions-of-requests-per-day-c4cdbf48639e)
