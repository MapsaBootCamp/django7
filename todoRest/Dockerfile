FROM basedockerimage

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000