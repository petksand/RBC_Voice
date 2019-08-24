FROM continuumio/anaconda3
WORKDIR /app
COPY . .
RUN /bin/bash -cl "pip install -r requirements.txt"
ENTRYPOINT ["/bin/bash", "-l"]
CMD ["python", "app.py"]
