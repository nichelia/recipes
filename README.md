# recipes

[TODO] About

## Development

### Prerequisites

- [kubectl](https://kubernetes.io/docs/reference/kubectl/)
- [helm](https://helm.sh)
- [kind](https://airflow.apache.org)
- [Docker Desktop](https://docs.docker.com/desktop/release-notes/)
- [Airflow](https://airflow.apache.org)

Assuming your machine has `kubectl`, `helm` and `kind` installed (on macOS you can install them using `brew`), create a local Kubernetes cluster using `kind` and `Docker Desktop`:
```bash
kind create cluster --image kindest/node:v1.21.1
```

Confirm the cluster is up and running:
```bash
kubectl cluster-info --context kind-kind
```

Build custom Docker image for Airflow to load required Python packages:
```bash
docker build --pull --tag airflow-gousto:0.0.0 --target prod .
```

Load the image to `kind`:
```bash
kind load docker-image airflow-gousto:0.0.0
```

Deploy an instance of Airflow to your local cluster:

```bash
helm repo add apache-airflow https://airflow.apache.org
helm repo update
helm upgrade airflow apache-airflow/airflow \
    --version=1.7.0 \
    --namespace airflow \
    --install \
    --create-namespace \
    --set images.airflow.repository=airflow-gousto \
    --set images.airflow.tag=0.0.0 \
    --set dags.gitSync.enabled=true \
    --set dags.gitSync.repo="https://github.com/nichelia/recipes.git" \
    --set dags.gitSync.branch="airflow-implementation" \
    --set dags.gitSync.subPath="dags"
```