import streamlit as st
from proposal.cover_letter import CoverLetter

from dotenv import load_dotenv

load_dotenv()

st.write("Upwork Cover Letter Generator")

# Get info for the cover letter
name_text = st.sidebar.text_input("Your Name", key="name")
client_name_text = st.sidebar.text_input("Client's Name", key="client_name")
job_title_text = st.sidebar.text_input("Your Job Title", key="job_title")
examples_text = st.sidebar.text_input("Link of previous work (N/A if not)", key="examples", placeholder="N/A")
examples_relates_radio = st.sidebar.radio("The previous work are related to this job", options=("Yes", "No"), key="examples_related")
profile_text = st.sidebar.text_input("Your Upwork Profile", key="profile", placeholder="Text")
job_post_text = st.sidebar.text_input("The Job Post", key="job_post", placeholder="Text")
call_action_radio = st.sidebar.radio("Call to action", options=("Call", "Text"), key="call_action")

if (name_text and client_name_text and job_title_text and examples_text and examples_relates_radio and profile_text and
        job_post_text and call_action_radio):

    name = st.session_state.name
    client_name = st.session_state.client_name
    job_title = st.session_state.job_title
    examples = str(st.session_state.examples).split(",") if st.session_state.examples != "N/A" else None
    examples_related = True if st.session_state.examples_related == "Yes" else False
    profile = st.session_state.profile
    job_post = st.session_state.job_post
    call = True if st.session_state.call_action == "Call" else False

    cover_letter = CoverLetter(client_name, job_title, examples, examples_related, profile, job_post,call, name)
    st.write(cover_letter.intro() + cover_letter.work_examples() + cover_letter.about_me() +
             cover_letter.my_contribution_to_the_project() + cover_letter.call_to_action() + cover_letter.closing())

else:
    st.write("Complete the required info ")

