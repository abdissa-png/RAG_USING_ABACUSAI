
import streamlit as st
# from abacusai import PredictionClient
import os


# client = PredictionClient()
import requests

st.set_page_config(page_title="Simple API Request UI")

text_input = st.text_input('Enter your text:')
response=""
if st.button('Submit'):
    # response = client.get_chat_response(
    #     deployment_token=os.environ['deployment_token'], 
    #     deployment_id=os.environ['deployment_id'], 
    #     messages=[{"is_user": True, "text": text_input}], 
    #     llm_name=None, 
    #     num_completion_tokens=None, 
    #     system_message=None, 
    #     temperature=0.0, 
    #     filter_key_values=None, 
    #     search_score_cutoff=None, 
    #     chat_config=None, 
    #     ignore_documents=False
    # )["messages"][1]["text"]
    url = f"https://abdissa-degefu.api.abacus.ai/api/getChatResponse?deploymentToken={st.secrets['deployment_token']}&deploymentId={st.secrets['deployment_id']}"
    headers = {"Content-Type": "application/json"}
    data = {
        "messages": [{"is_user":True,"text":text_input}],
        "llmName": None,
        "numCompletionTokens": None,
        "systemMessage": None,
        "temperature": 0.0,
        "filterKeyValues": None,
        "searchScoreCutoff": None,
        "chatConfig": None,
        "ignoreDocuments": False
    }

    response = requests.post(url, headers=headers, json=data)

    response=response.json()["result"]["messages"][1]["text"]

# Check if 'previous_conversations' exists in session state
if 'previous_conversations' not in st.session_state:
    st.session_state.previous_conversations = []

# Append current conversation to session state
if response!="":
    st.session_state.previous_conversations.append({"type":"user","res":text_input})
    st.session_state.previous_conversations.append({"type":"system","res":response})


# Display previous conversations
for res in st.session_state.previous_conversations:
    if res["type"]=="user":
        with st.chat_message('user'):
            st.write(f'You: {res["res"]}')
    else:
         with st.chat_message('System'):
            st.write(f'Bot: {res["res"]}')