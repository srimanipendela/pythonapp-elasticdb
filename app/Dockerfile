FROM python:3.6-slim

EXPOSE 5000

RUN useradd -ms /bin/bash g42

WORKDIR /home/g42/app/

COPY app.py requirements.txt /home/g42/app/

RUN chown -R g42:g42 /home/g42/app/

RUN chmod -R 711 /home/g42/app/

USER g42

RUN python -m pip install --no-cache-dir -r requirements.txt

CMD python app.py
