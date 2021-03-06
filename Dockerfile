from ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python2.7 python-pip
# Matches user on host
RUN useradd -u 20000 teabot
RUN chown -R teabot:teabot /srv

COPY requirements.txt /srv/requirements.txt
RUN pip install -r /srv/requirements.txt

COPY teabot_endpoints /srv/teabot_endpoints

WORKDIR /srv/
USER teabot
CMD ["gunicorn", "--log-level", "debug", "-w", "4", "-b", "0.0.0.0:8000", "teabot_endpoints.endpoints:app"]
