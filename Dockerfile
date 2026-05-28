FROM python:3.13-slim

WORKDIR /app

COPY lambda/index.py /app/app.py

CMD ["python", "app.py"]
# clean rebuild
