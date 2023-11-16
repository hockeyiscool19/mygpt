# gcloud auth login
# gcloud auth activate-service-account ACCOUNT --key-file=KEY-FILE

docker build -t mygpt .
# docker run -p 8000:80 mygpt
docker tag mygpt mygpt/mygpt:tagname
docker tag mygpt gcr.io/postman-69e12/mygpt:mygpt
docker push gcr.io/postman-69e12/mygpt:mygpt
