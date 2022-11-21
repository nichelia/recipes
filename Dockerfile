FROM python:python3.9-slim AS build
 
WORKDIR /app

COPY requirements.txt ./

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

FROM build as development

RUN apt-get update \
    && apt-get install -y --no-install-recommends git
