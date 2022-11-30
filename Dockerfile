FROM python:3.10
# Path: DockerFile
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "df8task1.py" ]