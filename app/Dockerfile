FROM python:3.11-slim

WORKDIR /app

# 필요한 라이브러리 설치 (예: paho-mqtt)
RUN pip install --no-cache-dir paho-mqtt

COPY main.py .
COPY core ./core
CMD ["python", "main.py"]
