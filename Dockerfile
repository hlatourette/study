FROM python:3
COPY . /usr/local/src/nn-handwriting
WORKDIR /usr/local/src/nn-handwriting
RUN pip install --no-cache-dir -r requirements.txt && \
    make test