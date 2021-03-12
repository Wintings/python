from typing import Optional

from fastapi import FastAPI

from tmp import K8S_CLUSTER

app = FastAPI()


apiserver_address = "https://192.168.16.52:6443"
token = "1odcnK68ISa6cPZTQDkZKC8vOY8"


k8s_cluster = K8S_CLUSTER(apiserver_address, token)

@app.get("/")
def read_root():
    return {"Hello": "leichao"}

@app.get("/api/v1/{namespace}/{resouce_name}")
def get_resource(namespace, resouce_name):
    return k8s_cluster.get_cluster_resource(namespace, resouce_name)
