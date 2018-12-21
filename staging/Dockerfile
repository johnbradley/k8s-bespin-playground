FROM python:3-alpine
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /app
WORKDIR /app
COPY . /app
CMD python
