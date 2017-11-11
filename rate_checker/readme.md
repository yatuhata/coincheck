# rate_checker

## requirements
- Mac OSX 10.12.6
- Python 3.6.1
- virtualenv 15.1.0

## install
```
$ git clone https://github.com/yatuhata/coincheck.git; cd coincheck/rate_checker
$ virtualenv -p python3 venv
$ source venv3/bin/activate
(venv) $ pip install -r requirements
(venv) $ docker-compose up -d --build
```

## run
```
(venv) $ python rate_checker.py
```
If run rate_checker at once, a data point is inserted to InfluxDB which is a docker-container in localhost.