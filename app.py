## import libraries and load the model
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model


## Load the imdb dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}


## Load the pretrained model

model=load_model('artifacts\RNN_Model.keras')


## Step 2 - Helper Functions
## Function to decode reviews

def decode_review(encoded_review):
  return ' '.join([reverse_word_index.get(i - 3, '?' ) for i in encoded_review])

## Function to preprocess user_input

def preprocess_text(text):
    words = text.lower().split()
    # Use min(9999, ...) to ensure indices do not exceed 9999
    encoded_review = [min(word_index.get(word, 2) + 3, 9999) for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=350)
    return padded_review


## Prediction Function

def predict_sentiment(review):
    # Preprocess the review (tokenize, pad, etc.)
    preprocessed_input = preprocess_text(review)

    # Get prediction score from model
    prediction = model.predict(preprocessed_input)

    # Determine sentiment based on prediction score
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

    return sentiment, prediction[0][0]




import streamlit as st
## creating streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as Positive or Negative')

## user input
user_input=st.text_area('Movie Review')

if st.button('Classify'):
   preprocessed_input=preprocess_text(user_input)

   # Make Prediction

   prediction=model.predict(preprocessed_input)

   sentiment='Positive' if prediction[0][0] > 0.50 else 'Negative'


   ## Displaying the result

   st.write(f'Sentiment: {sentiment}')
   st.write(f'Prediction Score: {prediction[0][0]}')

else:
   st.write('Please enter a movie review')