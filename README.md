### Minikube Install
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64

sudo install minikube-darwin-amd64 /usr/local/bin/minikube
```

### Minikube Start and Open DashBoard
```
minikube start

minikube dashboard
```

### Addons
```
# Nginx Ingress Controller
# 이걸 활성화해야 nginx ingress를 사용할 수 있다
minikube addons enable ingress

# CPU, MEMORY Monitoring
minikube addons enable metrics-server
```

### K9S For CLI Manager
```
# Via Homebrew
brew install derailed/k9s/k9s

# k9s 실행
k9s

# k9s에서 namespace 보기
:ns
```

### Minikube에서 Local Docker Image 사용하기
```
# 1. docker랑 minikube랑 연결
eval $(minikube -p minikube docker-env)

# 2. 동일한 터미널에서 이미지 빌드, 
# (1)이 적용되지 않은 터미널에서는 minikube에 image가 안 올라간다
docker build -f Dockerfile.nginx -t nginx_app:1.0.0 .
docker build -f Dockerfile.django -t django_app:1.0.0 .

# 3. minikube에서 이용가능한 이미지 확인
minikube image ls --format table
```

## Server 올리기

### Docker Image 생성
```
eval $(minikube -p minikube docker-env)

docker build -f Dockerfile.django -t django_app:1.0.0 .
docker build -f Dockerfile.nginx -t nginx_app:1.0.0 .
```

### kubernetes namespace 생성
```
# kubernetes 폴더에서
kubectl apply -f namespace.yml
```

### postgresql controller, service 생성
```
# kubernetes 폴더에서
kubectl apply -f ./postgresql
```

### django controller, service 생성
```
# kubernetes 폴더에서
kubectl apply -f ./django
```

### nginx controller, service, ingress 생성
```
# kubernetes 폴더에서
kubectl apply -f ./nginx

# 생성한 ingress 확인
kubectl get ingress -n django-app
```

### 외부접속 터널 생성
```
minikube addons enable ingress // 최초 한번만 활성화 하면된다

minikube tunnel
```

### Job을 통한 static 파일 생성, Migrate
```
# kubernetes 폴더에서
kubectl apply -f ./django-batch/collectstatic.yml

kubectl apply -f ./django-batch/migrate.yml
```