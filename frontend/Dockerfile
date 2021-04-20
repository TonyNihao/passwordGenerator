FROM python:3.8
RUN pip install flask requests uWSGI
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
WORKDIR /app
COPY app/ /app
COPY cmd.sh /cmd.sh
USER uwsgi

EXPOSE 80

CMD ["/cmd.sh"]
