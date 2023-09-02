### Install dependencies


[//]: # (pip install uvicorn)

[//]: # (pip install asgiref)
`pip install -r requirements.txt`


### Running the app

`docker build -t test-flask-app .`

`docker run -p 80:8000 test-flask-app`


### Swagger UI
http://localhost/ui/