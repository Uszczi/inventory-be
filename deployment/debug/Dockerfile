FROM python:3.10
WORKDIR /app
COPY ./requirements/prod.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install debugpy
COPY . .

RUN chmod +x ./deployment/develop/start.sh
CMD ["./deployment/debug/start.sh"]
