FROM python:3.5-onbuild
EXPOSE 8000
CMD [ "python", "./rocketsite/manage.py", "runserver", "0.0.0.0:8000" ]
