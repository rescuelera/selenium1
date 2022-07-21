FROM python

WORKDIR /autotests

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["pytest"]
