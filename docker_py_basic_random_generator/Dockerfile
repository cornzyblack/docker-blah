FROM python:3.13.0a4-slim-bullseye
WORKDIR /app
# Something breaks here, what is it
# Does rerunning the container after fixing the issue fix it?
COPY requirements.txt script.py /app/
# All good?
CMD ["python", "script.py"]
