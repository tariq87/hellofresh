FROM python:alpine3.7 
RUN mkdir /app
COPY hellofresh.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt 
ENTRYPOINT [ "python" ] 
CMD [ "hellofresh.py" ]
