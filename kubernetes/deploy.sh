kubectl apply -f namespace.yaml \
-f posts-service-config-map.yaml \
-f posts-service-secrets.yaml \
-f deployment.yaml \
-f ingress.yaml \
-f posts-service-service.yaml \
-f posts-service-mongodb-config-map.yaml \
-f posts-service-mongodb-secrets.yaml \
-f posts-service-mongodb-persistent-volume-claim.yaml \
-f posts-service-mongodb-service.yaml \
-f stateful-set.yaml


kubectl apply -f namespace.yaml -f posts-service-config-map.yaml -f posts-service-secrets.yaml -f deployment.yaml -f ingress.yaml -f posts-service-service.yaml -f posts-service-mongodb-config-map.yaml -f posts-service-mongodb-secrets.yaml -f posts-service-mongodb-persistent-volume-claim.yaml -f posts-service-mongodb-service.yaml -f stateful-set.yaml

