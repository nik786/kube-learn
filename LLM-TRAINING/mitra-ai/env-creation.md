apt-get install -y python3-pip

apt-get install build-essential libssl-dev libffi-dev python-dev

apt-get install -y python3-venv

pip3 install virtualenv


python3 -m venv ai-demo

source ai-demo/bin/activate

pip install kaggle



deactivate


pip install "keras==2.12.0" "tensorflow==2.12.0" "transformers==4.30.2" "tokenizers==0.13.3" "sentence-transformers==2.2.2"


docker build -t my-langchain-app .

docker run --rm -it my-langchain-app

docker build -t langchain/5.0 -f langchainfile05 .

docker run -e GROQ_API_KEY="" --rm -it langchain/5.0



