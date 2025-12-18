# libraries
import random
import numpy as np
import pickle
import json
from flask import Flask, render_template, request
import ssl
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

class ChatBot:
    def __init__(self, intents_file):
        self.intents_file = intents_file
        self.load_intents()
        self.prepare_data()
        self.train_classifier()

    def load_intents(self):
        with open(self.intents_file, "r") as file:
            self.intents = json.load(file)

    def prepare_data(self):
        self.words = []
        self.classes = []
        self.documents = []
        self.ignore_words = set(nltk.corpus.stopwords.words('english'))

        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                # Tokenize each word in the sentence and filter out stop words
                w = [word.lower() for word in nltk.word_tokenize(pattern) if word.lower() not in self.ignore_words]
                self.words.extend(w)
                # Add the word(s) to the documents
                self.documents.append((w, intent['tag']))
                # Add the tag to classes if it's not already there
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        # Lemmatize each word, remove duplicates, and sort
        self.words = sorted(list(set(self.words)))
        # Sort classes
        self.classes = sorted(list(set(self.classes)))

    def bow(self, sentence):
        bag = [0] * len(self.words)
        for word in nltk.word_tokenize(sentence):
            if word.lower() in self.words:
                bag[self.words.index(word.lower())] = 1
        return np.array(bag)

    def train_classifier(self):
        training = []
        output_empty = [0] * len(self.classes)

        for doc in self.documents:
            bag = self.bow(' '.join(doc[0]))
            output_row = list(output_empty)
            output_row[self.classes.index(doc[1])] = 1
            training.append([bag, output_row])

        try:
            # Separate bag-of-words arrays and output rows
            bag_of_words = [item[0] for item in training]
            output_rows = [item[1] for item in training]

            # Convert bag-of-words vectors and output rows into numpy arrays
            bag_of_words_array = np.array(bag_of_words)
            output_rows_array = np.array(output_rows)

            # Combine bag-of-words arrays and output rows arrays into a single numpy array
            training_data = np.hstack((bag_of_words_array, output_rows_array))

            # Shuffle the training data
            np.random.shuffle(training_data)

            # Split features and target labels
            train_x = training_data[:, :-len(self.classes)]
            train_y = training_data[:, -len(self.classes):]

            # Convert one-hot encoded target labels to class indices
            train_y = np.argmax(train_y, axis=1)

            # Train the classifier (Random Forest)
            self.classifier = RandomForestClassifier(n_estimators=100)  # You can adjust the number of trees (n_estimators) as needed
            self.classifier.fit(train_x, train_y)
        except ValueError as e:
            print("Error occurred while preparing the training data:", e)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    
    # Predict the intent
    p = chatbot.bow(msg)
    prediction = chatbot.classifier.predict([p])[0]
    # Get the tag from the prediction
    predicted_tag = chatbot.classes[np.argmax(prediction)]
    
    # Find the corresponding responses for the predicted tag
    for intent in chatbot.intents['intents']:
        if intent['tag'] == predicted_tag:
            responses = intent['responses']
            break
    else:
        responses = ["Sorry, I couldn't understand that."]
    
    # Check if any response contains a link
    for i, response in enumerate(responses):
        if "<a href=" in response:
            # Add target="_blank" to open the link in a new tab
            responses[i] = response.replace("<a href=", "<a target='_blank' href=")
    
    return " ".join(responses)

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('server.crt', 'server.key')
    chatbot = ChatBot("intents.json")
    app.run(host='0.0.0.0', port=8080, ssl_context=context)

