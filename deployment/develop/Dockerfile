FROM python:3.10
WORKDIR /app
COPY ./requirements/dev.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

RUN chmod +x ./deployment/develop/start.sh
CMD ["./deployment/develop/start.sh"]
