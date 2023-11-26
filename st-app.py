## imports 
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_card import card
import json 

def replace_text(new_text, name):
  st.session_state["heads"] = f"Here is why you should connect with {name}!"
  st.session_state["text"] = new_text 
  
def load_data():  
  with open('data.json') as json_file:
    data = json.load(json_file)
  return data
def api(name):
  return api_dict 

def card_comp(title, i): 
        
  a = card(
      title=title,
      text='User', 
      image="https://placekitten.com/500/"+i,
      styles={
          "card": {
              "width": "350px",
              "height": "300px",
              "border-radius": "40px",
              "border-color": "#D9A6E5",
              "border-width": "5px",
              "box-shadow": "0 0 10px rgba(217,166,229,0.5)",
          },
          "filter": {
              "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore
          }
      },      
      on_click=lambda:print('clicked')
  )
  
  return a
  
# Title for the Streamlit app
st.set_page_config(
  page_title="RAGTag",
  page_icon="🧊",
  layout="wide",
)

data = load_data()

users = [i["user"] for i in data]
users.insert(0, None)
st.markdown("<h1 style='text-align: center; color: black'> Welcom to <span style='color: #355146;'> RAGTag </span> 👋</h1>", unsafe_allow_html=True)

option = st.selectbox(
    'Select a user to investigate their matches?',
    users)

cols = st.columns(3, gap='small')


if option is not None: 
  with st.container():
    st.markdown(f"<h2 style='text-align: center; color: #355146;'>Hey {option}, here are your matches!</h2>", unsafe_allow_html=True)

    for i in data: 
      if i["user"] == option: 
        matches = i["matches"]
        break
    
    # matches = [i["name"] for i in matches]
    # titles = [i["title"] for i in matches]
    # summaries = [i["summary"] for i in matches]
    
    with cols[0]:
      d = matches[0]
      res1 = card_comp(d['name'], '501')  
      if res1:
        replace_text(d['summary'], d['name'])


    with cols[1]:
      x = matches[1]
      res2 = card_comp(x['name'], '502')
      if res2:
        replace_text(x['summary'], x['name'])


    with cols[2]:
      y = matches[2]
      res3 = card_comp(y['name'], '503')
      if res3:
        replace_text(y['summary'], y['name'])
        res1 = False
        res2 = False  


    if "text" not in st.session_state:
        st.session_state["text"] = ""
    
    if "heads" not in st.session_state:
        st.session_state["heads"] = ""   
      
  st.divider()

  st.header(st.session_state["heads"])  
  st.markdown("<p style=' font-size: 20px; color: black'>"+st.session_state["text"]+"</p>", unsafe_allow_html=True)



