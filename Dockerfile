FROM apache/airflow:2.4.1 AS prod

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


FROM prod as dev

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*