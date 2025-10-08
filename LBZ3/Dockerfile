FROM python:3.12-trixie
WORKDIR /Kazanetskiy
RUN pip install --no-cache-dir googletrans==3.1.0a0
COPY . .

ENTRYPOINT ["sh", "-c", "python --version && cat /etc/os-release && ls -la / && echo \"\" && python ./gtrans3.py"]
