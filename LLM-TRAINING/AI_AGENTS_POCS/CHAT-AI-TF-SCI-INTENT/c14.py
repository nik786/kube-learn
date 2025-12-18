import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import nltk
from flask import Flask, render_template, request

app = Flask(__name__)

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
        self.ignore_words = ['?']

        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                w = nltk.word_tokenize(pattern)
                self.words.extend(w)
                self.documents.append((' '.join(w), intent['tag']))
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        self.words = sorted(list(set(self.words)))
        self.classes = sorted(list(set(self.classes)))

        self.vectorizer = CountVectorizer(max_features=len(self.words))
        self.X = self.vectorizer.fit_transform([doc[0] for doc in self.documents])
        self.y = np.array([self.classes.index(doc[1]) for doc in self.documents])

    def train_classifier(self):
        self.classifier = RandomForestClassifier(n_estimators=100)
        self.classifier.fit(self.X.toarray(), self.y)

    def predict_intent(self, message):
        message_vectorized = self.vectorizer.transform([message])
        prediction = self.classifier.predict(message_vectorized.toarray())[0]
        predicted_tag = self.classes[prediction]
        return predicted_tag

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    message = request.form["msg"]
    predicted_tag = chatbot.predict_intent(message)
    print("Predicted tag:", predicted_tag)  # Debugging: Print predicted tag
    
    # Find the corresponding intent in the intents JSON
    for intent in chatbot.intents['intents']:
        if intent['tag'] == predicted_tag:
            print("Matched tag:", intent['tag'])  # Debugging: Print matched tag
            # Return a random response from the available responses for the predicted tag
            response = np.random.choice(intent['responses'])
            print("Response:", response)  # Debugging: Print selected response
            return response

# Example usage
if __name__ == "__main__":
    chatbot = ChatBot("intents.json")
    app.run(host='0.0.0.0', port=8080)

