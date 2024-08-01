from transformers import MarianMTModel, MarianTokenizer
import streamlit as st

#Loding models
model_fr = 'Helsinki-NLP/opus-mt-en-fr'
model_hi = 'Helsinki-NLP/opus-mt-en-hi'

#loading Pre-trained model and tokenizer for french
model_en_fr = MarianMTModel.from_pretrained(model_fr)
tokenizer_en_fr = MarianTokenizer.from_pretrained(model_fr)
#loading Pre-trained model and tokenizer for hindi
model_en_hi = MarianMTModel.from_pretrained(model_hi)
tokenizer_en_hi = MarianTokenizer.from_pretrained(model_hi)

def translate_word(word, model_en_hi,tokenizer_en_hi,model_en_fr,tokenizer_en_fr):
    if len(word) != 10:
        st.write("This feature works only for 10-letter words.")
    else:
        # Tokenize and translate to French
        encoded_word_fr = tokenizer_en_fr(word, return_tensors='pt')
        translated_tokens_fr = model_en_fr.generate(**encoded_word_fr)
        translated_word_fr = tokenizer_en_fr.decode(translated_tokens_fr[0], skip_special_tokens=True)
    
        # Tokenize and translate to Hindi
        encoded_word_hi = tokenizer_en_hi(word, return_tensors='pt')
        translated_tokens_hi = model_en_hi.generate(**encoded_word_hi)
        translated_word_hi = tokenizer_en_hi.decode(translated_tokens_hi[0], skip_special_tokens=True)
    
        st.write(f"French: {translated_word_fr}")
        st.write(f"Hindi: {translated_word_hi}")

st.title("Task 3: Creating a Feature to Translate English to French and Hindi Simultaneously")

#user input 10 letters of word
word = st.text_input("Enter an 10 letter word")
if word!="":
    #using our funtion
    translate_word(word, model_en_hi,tokenizer_en_hi, model_en_fr, tokenizer_en_fr)



