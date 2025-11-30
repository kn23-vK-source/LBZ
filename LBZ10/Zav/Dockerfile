FROM python:3.12-trixie
WORKDIR /Kazanetskiy
COPY . .
RUN pip install --no-cache-dir -r requirements.txt  

ENTRYPOINT ["sh", "-c", "python ./lbz10/manage.py makemigrations && python ./lbz10/manage.py migrate && python ./lbz10/manage.py load_data && python ./lbz10/manage.py runserver 0.0.0.0:8100"]


