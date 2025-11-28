
s3

www.retinadigital.com

docker build -t retina-frontend .

ls

docker create --name retina-temp retina-frontend

docker cp retina-temp:/app/build ./build

