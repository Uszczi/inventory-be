FROM python:3.10
WORKDIR /app
COPY ./requirements/prod.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
run 	python -m pip install -e .
RUN chmod +x ./deployment/prod/start.sh
CMD ["./deployment/prod/start.sh"]
