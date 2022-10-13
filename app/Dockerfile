FROM python:3.6-slim

EXPOSE 5000

RUN useradd -ms /bin/bash pyapp

WORKDIR /home/pyapp/app/

COPY app.py requirements.txt /home/pyapp/app/

RUN chown -R pyapp:pyapp /home/pyapp/app/

RUN chmod -R 711 /home/pyapp/app/

USER pyapp

RUN python -m pip install --no-cache-dir -r requirements.txt

CMD python app.py
