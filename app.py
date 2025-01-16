from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import spacy
from textblob import TextBlob

from spacy.matcher import PhraseMatcher


# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Create a PhraseMatcher object
matcher = PhraseMatcher(nlp.vocab)

# Define patterns (e.g., greeting, asking about the weather)
patterns = [nlp.make_doc(text) for text in ["hello", "hi", "how are you", "what's up"]]
matcher.add("greetings", patterns)


# user_data = {}

# Route to process incoming messages
@app.route('/chat', methods=['POST'])
def chat():
    # user_message = request.json.get('message')
    
    # # Process the message using SpaCy (simple NLP analysis here)
    # doc = nlp(user_message)
    
    # # Print the tokens (words) and their part-of-speech tags (for debugging)
    # for token in doc:
    #     print(f"Token: {token.text}, POS: {token.pos_}")
    
    # # A simple response generation example based on the named entities in the message
    # entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # response_text = "I found the following entities: " + str(entities)
    
    # for ent in doc.ents:
    #     if ent.label_ == 'PERSON':
    #         response_text += f"\nHello {ent.text}, how can I assist you today?"
    #     elif ent.label_ == 'GPE':
    #         response_text += f"\nI see you're referring to {ent.text}. Tell me more about it!"
    #     elif ent.label_ == 'DATE':
    #         response_text += f"\nI noticed the date: {ent.text}. Do you have any events for this day?"
    
    # return jsonify({'response': response_text, 'entities': entities})
    
    # user_message = request.json.get('message').lower()
    # doc = nlp(user_message)

    # # Check for specific intents
    # if "hello" in user_message or "hi" in user_message:
    #     response_text = "Hello! How can I assist you today?"
    # elif "how are you" in user_message:
    #     response_text = "I'm doing great, thank you! How about you?"
    # elif "your name" in user_message:
    #     response_text = "I am a chatbot created by a Python developer."
    # else:
    #     response_text = "I'm sorry, I didn't understand that. Can you ask something else?"

    # return jsonify({'response': response_text, 'entities': []})
    
    # user_message = request.json.get('message').lower()
    # user_id = request.json.get('user_id')  # Assume you send a unique user ID

    # # Check if the user has already been introduced
    # if user_id not in user_data:
    #     user_data[user_id] = {'name': None}

    # if "my name is" in user_message:
    #     name = user_message.replace("my name is", "").strip()
    #     user_data[user_id]['name'] = name
    #     response_text = f"Nice to meet you, {name}!"
    # elif user_data[user_id]['name']:
    #     response_text = f"Hello {user_data[user_id]['name']}, how can I help you today?"
    # else:
    #     response_text = "Hello, can you please tell me your name?"
    
    # return jsonify({'response': response_text, 'entities': []})
    
    # user_message = request.json.get('message')

    # # Sentiment analysis
    # blob = TextBlob(user_message)
    # sentiment = blob.sentiment.polarity  # Range from -1 (negative) to 1 (positive)

    # if sentiment > 0:
    #     response_text = "I'm glad you're feeling positive!"
    # elif sentiment < 0:
    #     response_text = "I'm sorry you're feeling that way. How can I help?"
    # else:
    #     response_text = "I see you're neutral. What would you like to talk about?"

    # return jsonify({'response': response_text, 'entities': []})
    
    user_message = request.json.get('message')
    doc = nlp(user_message)

    # Match patterns in the user's message
    matches = matcher(doc)
    if matches:
        response_text = "Hi there! How can I help you today?"
    else:
        response_text = "I didn't understand that. Could you ask something else?"

    return jsonify({'response': response_text, 'entities': []})

if __name__ == '__main__':
    app.run(debug=True)
