import os 
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
def generate_email_content(api_key,prompt,tone,model="gpt-3.5-turbo"):
    # Generate Email Response , subject and summary using OpenAI API
    
    if not api_key:
        return {'error': "OpenAI API Key is not set, Please Enter it",
                'response': None}
    try:
        #Generate Response for the Emial Threa
        client = OpenAI(api_key=api_key)
        response_messages = [
            {"role": "system", "content": f"You are a helpful assistant that generates email responses. Generate a {tone} tone response"},
            {"role": "user", "content": prompt}
        ]
        response= client.chat.completions.create(
            model=model,
            messages=response_messages,
            temperature=0.7
        )
        email_response = response.choices[0].message.content
        
        #Generate Subject Line
        subject_messages=[
            {"role": "system", "content": "Generate a concise,appropriate and engaging subject line for the following email response"},
            {"role": "user", "content": f"Email Response: \n {email_response}"}
        ]
        subject_response = client.chat.completions.create(
            model=model,
            messages=subject_messages,
            temperature=0.7
        )
        subject_line = subject_response.choices[0].message.content
        
        #Generate Thread Summary
        summary_messages=[
            {"role": "system", "content": "Generate a concise summary of the email thread"},
            {"role": "user", "content": f"Original Thread:\n{prompt}\n\n Response:\n{email_response}"}
        ]
        summary_response = client.chat.completions.create(
            model=model,
            messages=summary_messages,
            temperature=0.7           
        )
        thread_summary = summary_response.choices[0].message.content
        
        return{
            "error": None,
            "response": email_response,
            "subject": subject_line,
            "summary": thread_summary
        }
    except Exception as e:
        return {'error': str(e), 'response': None}

        
        
        
        
def main():
    st.set_page_config(page_title="Email Assistant", layout="wide")
    st.markdown("<h2>Email Assistant</h2>", unsafe_allow_html=True) 
    st.markdown("generate Profession Email Response with different Tones")
    
    
    if "OPENAI_API_KEY" not in st.session_state:
        st.session_state.OPENAI_API_KEY = None
        
    with st.sidebar:
        st.subheader("Settings")
        api_key = st.text_input("Enter Your OpenAI API Key",
                                type="password",
                                help="You can get your API key from https://platform.openai.com/api-keys")
        if api_key:
            st.session_state.OPENAI_API_KEY = api_key
            st.success("API Key Set Successfully")
            
        st.markdown("---")
        st.markdown("### Features")
        st.markdown("""
                    - Auto Generate Email Responses
                    - Multiple Tone Options
                    - Subject Suggestions
                    - Thread Summarization
                    """)
    col1,col2=st.columns([1,1])
    with col1:
        st.subheader("Input")
        
        #Email THread Input
        email_thread= st.text_area(
            'Enter the Email Thread(Most recent emails first)',
            height=200,
            placeholder="Paste your email thread here..."
        )
        tone_options_available=["Professional","Formal","Casual","Friendly"]
        selected_tone=st.selectbox("Select Tone", tone_options_available)
        
        #context Input
        additonal_context=st.text_area(
            "Enter Additional Context or Instructions",
            height=100,
            placeholder="e.g. 'Keep it short and concise yet impactful'"
            
        )
        
        #Generate Button
        if st.button("Generate Response"):
            if not email_thread:
                st.error("Please enter an email thread")
                return
            if not st.session_state.OPENAI_API_KEY:
                st.error("Please enter your OpenAI API Key")
                return
            
            with st.spinner("Generating Response..."):
                prompt = f"Email Thread: {email_thread}\n\nAdditional Context: {additonal_context}\n\n Generate a {selected_tone.lower()} tone response\n\n"
                
                result= generate_email_content(st.session_state.OPENAI_API_KEY,prompt,selected_tone)
                
                if result['error']:
                    st.error(result['error'])
                else:
                    st.session_state.generated_response = result
                    st.success("Response Generated Successfully")
        
    with col2:
        st.subheader("Generated Response")
        if 'generated_response' in st.session_state:
            content = st.session_state.generated_response
            
            st.markdown("**📋 Subject Line:**")
            st.code(content["subject"], language=None)

            st.markdown("**📝 Email Response:**")
            st.code(content["response"], language=None)

            st.markdown("**📌 Thread Summary:**")
            st.code(content["summary"], language=None)

            st.markdown(f"*Tone: {selected_tone}*")
            
                    
            
                    
        
        

        

if __name__ == "__main__":
    main()