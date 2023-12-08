FROM python:3.10-slim-buster
COPY ./tinyurl_backend /tinyurl_backend
COPY run.py .
WORKDIR /tinyurl_backend
RUN pip3 install --upgrade -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn", "run:app", "--host", "0.0.0.0"]