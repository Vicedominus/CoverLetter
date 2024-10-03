import streamlit as st
import openai

import os

from crew.crews import get_cover_letter

st.write("Upwork Cover Letter Generator")

# Get info for the cover letter
name_text = st.sidebar.text_input("Your Name", key="name")
client_name_text = st.sidebar.text_input("Client's Name", key="client_name")
job_title_text = st.sidebar.text_input("Your Title", key="job_title")
profile_text = st.sidebar.text_input("Your Profile", key="profile", placeholder="Text")
job_post_text = st.sidebar.text_input("The Job Post", key="job_post", placeholder="Text")
OPENAI_API_KEY = st.sidebar.text_input("Your OpenAI api key", key="api_key", placeholder="Text")

if (name_text and client_name_text and profile_text and job_post_text and OPENAI_API_KEY):
    # Asignar la clave de API directamente
    os.environ['OPENAI_API_KEY'] = st.session_state.api_key
    name = st.session_state.name
    client_name = st.session_state.client_name
    job_title = st.session_state.job_title
    profile = st.session_state.profile
    job_post = st.session_state.job_post

    cover_letter = get_cover_letter(name, client_name, job_title, profile, job_post)
    st.write(cover_letter)
else:
    st.write("Complete the required info")

