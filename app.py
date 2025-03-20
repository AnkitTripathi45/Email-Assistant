import os 
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
from utils import generate_email_content
import time

load_dotenv()

def load_css():
    with open('src/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Email Assistant", layout="wide", page_icon="✉️")
    
    # Load CSS
    load_css()
    
    # Header with logo and title
    st.markdown("""
        <div class='app-header' style='margin-top: 2rem;'>
            <h1 style='color: #1f77b4;'>✉️ Email Assistant</h1>
            <p><h4>Generate Email Responses with Different Tones</h4></p>
        </div>
    """, unsafe_allow_html=True)
    
    if "OPENAI_API_KEY" not in st.session_state:
        st.session_state.OPENAI_API_KEY = None
        
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        api_key = st.text_input("Enter Your OpenAI API Key",
                                type="password",
                                help="You can get your API key from https://platform.openai.com/api-keys")
        if api_key:
            st.session_state.OPENAI_API_KEY = api_key
            st.success("✅ API Key Set Successfully")
            
        st.markdown("---")
        st.markdown("### ✨ Features")
        st.markdown("""
                    <ul class='feature-list'>
                    <li>📧 Auto Generate Email Responses</li>
                    <li>🎭 Multiple Tone Options</li>
                    <li>📝 Subject Suggestions</li>
                    <li>📋 Thread Summarization</li>
                    </ul>
                    """, unsafe_allow_html=True)
    
    # Create two main columns for input and output
    input_col, output_col = st.columns([1, 1])
    
    # Input Section in left column
    with input_col:
        st.markdown("<h3 class='section-header'>📥 Input</h3>", unsafe_allow_html=True)
        
        # Email Thread Input
        email_thread = st.text_area(
            'Enter the Email Thread (Most recent emails first)',
            height=150,
            placeholder="Paste your email thread here..."
        )
        
        # Two columns for tone and context
        col1, col2 = st.columns([1,1])
        with col1:
            # Tone selection with emojis
            tone_options = {
                "Professional": "👔 Professional",
                "Formal": "📜 Formal",
                "Casual": "😊 Casual",
                "Friendly": "🤝 Friendly"
            }
            selected_tone = st.selectbox("Select Tone", list(tone_options.keys()))
        
        with col2:
            #context Input
            additonal_context = st.text_area(
                "Enter Additional Context or Instructions",
                height=80,
                placeholder="e.g. 'Keep it short and concise yet impactful'"
            )
        
        #Generate Button
        if st.button("🚀 Generate Response"):
            if not email_thread:
                st.error("❌ Please enter an email thread")
                return
            if not st.session_state.OPENAI_API_KEY:
                st.error("❌ Please enter your OpenAI API Key")
                return
            
            with st.spinner("✨ Generating Response..."):
                prompt = f"Email Thread: {email_thread}\n\nAdditional Context: {additonal_context}\n\n Generate a {selected_tone.lower()} tone response\n\n"
                
                result = generate_email_content(st.session_state.OPENAI_API_KEY, prompt, selected_tone)
                
                if result['error']:
                    st.error(result['error'])
                else:
                    st.session_state.generated_response = result
                    st.success("✅ Response Generated Successfully")
    
    # Output Section in right column
    with output_col:
        st.markdown("<h3 class='section-header'>📤 Generated Response</h3>", unsafe_allow_html=True)
        
        if 'generated_response' in st.session_state:
            content = st.session_state.generated_response
            
            # Subject line
            st.markdown("**📋 Subject Line:**")
            st.code(content['subject'], language=None)
            
            # Email response
            st.markdown("**📝 Email Response:**")
            st.code(content['response'], language=None)
            
            # Thread summary below
            st.markdown("**📌 Thread Summary:**")
            st.code(content['summary'], language=None)
            
            # Tone indicator
            st.markdown(f"<div style='text-align: center; color: #666; margin-top: 10px;'>Tone: {tone_options[selected_tone]}</div>", unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style='text-align: center; color: #666; margin-top: 20px;'>
                    <p>Your generated response will appear here after clicking the Generate button.</p>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()