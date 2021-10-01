FROM python:3-alpine AS devoxxfr_amadeus_api

ENV FLASK_APP=/api/api.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=8080 \
    WERKZEUG_RUN_MAIN=true \
    MANIFEST_FILE_PATH=/manifest.json

COPY api /api
COPY manifest.json /

WORKDIR /api

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "-m", "flask", "run"]
