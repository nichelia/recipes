FROM python:python3.9-slim AS builder
 
WORKDIR /app

COPY requirements.txt ./

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

FROM builder as dev-envs

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
