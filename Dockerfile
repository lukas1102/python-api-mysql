FROM python:3-onbuild
COPY api.py /usr/src/app
CMD ["python","api.py"]
EXPOSE 80