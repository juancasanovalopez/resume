FROM python:3.6-alpine

RUN adduser -D resume

WORKDIR /home/resume

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY resume.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP resume.py

RUN chown -R resume:resume ./
USER resume

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]