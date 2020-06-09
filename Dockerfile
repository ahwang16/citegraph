FROM python:3.6
COPY . /citegraph
WORKDIR /citegraph
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "flask-test.py"]