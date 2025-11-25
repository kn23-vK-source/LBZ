FROM python:3.12-trixie
WORKDIR /Kazanetskiy
COPY . .
RUN pip install --no-cache-dir -r requirements.txt  

ENTRYPOINT ["sh", "-c", "python ./zav2.py && python ./zav3.py"]
