import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()  # Converting all characters to lowercase
    text = nltk.word_tokenize(text)  # Tokenizing all the characters

    y = []
    for i in text:
        if i.isalnum():  # removing  special characters
            y.append(i)

    text = y[:]  # Cloning[shallow copy]
    y.clear()

    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tf = pickle.load(open("vectorizer.pkl","rb"))
model = pickle.load(open("model.pkl","rb"))

st.title("Email Spam Classifier")

input_email = st.text_input("Enter the message")

if st.button("Predict"):

    #Preprocess
    transformed_email = transform_text(input_email)
    #Vectorize
    vector_input = tf.transform([transformed_email])
    #Predict
    result = model.predict(vector_input)[0]
    #Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")