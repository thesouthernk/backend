# Food Data Api Builded in Fastapi Framework and documented in swagger

To access documentation run app and access go  http://localhost:8000/docs


#You will se something like this:
<img width="1596" alt="Captura de Pantalla 2022-11-08 a las 00 03 14" src="https://user-images.githubusercontent.com/38993747/200479739-65cb52c6-5f28-4340-95be-12920130e5aa.png">


#API Doc
<img width="1606" alt="Captura de Pantalla 2022-11-08 a las 00 03 24" src="https://user-images.githubusercontent.com/38993747/200479816-1f760505-8b00-40f7-95db-e218a2483a02.png">

Instructions tu run.

#Build Docker Image 
docker build -t food-api .

#Run Containr
docker run -d -p 80:80 -e WORKERS_PER_CORE="4" food-api
