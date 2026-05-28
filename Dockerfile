FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY lambda/index.py /app/app.py

RUN useradd -m appuser

USER appuser

EXPOSE 5000

HEALTHCHECK CMD python --version || exit 1

CMD ["python", "app.py"]