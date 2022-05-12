FROM python:3-onbuild
COPY api.py /usr/src/app
#ENV SQL_HOST="127.0.0.1"
#ENV SQL_USER="root"
#ENV SQL_PWD="example"
#ENV SQL_DB="users"
CMD ["python","api.py"]
EXPOSE 5000