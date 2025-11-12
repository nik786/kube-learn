
docker-compose -f chatter-bot.yml up

docker-compose -f chatter-bot.yml up --build


docker build -t cb/chatterbot01 -f chatterbotfile .
