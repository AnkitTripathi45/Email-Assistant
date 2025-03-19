from openai import OpenAI

def generate_email_content(api_key, prompt, tone, model="gpt-3.5-turbo"):
    """
    Generate email response, subject, and summary using OpenAI API
    
    Args:
        api_key (str): OpenAI API key
        prompt (str): The email thread and context
        tone (str): Desired tone for the response
        model (str): OpenAI model to use (default: gpt-3.5-turbo)
    
    Returns:
        dict: Contains response, subject, summary, and any error messages
    """
    if not api_key:
        return {'error': "OpenAI API Key is not set, Please Enter it",
                'response': None}
    try:
        # Generate Response for the Email Thread
        client = OpenAI(api_key=api_key)
        response_messages = [
            {"role": "system", "content": f"You are a helpful assistant that generates email responses. Generate a {tone} tone response"},
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model=model,
            messages=response_messages,
            temperature=0.7
        )
        email_response = response.choices[0].message.content
        
        # Generate Subject Line
        subject_messages = [
            {"role": "system", "content": "Generate a concise, appropriate and engaging subject line for the following email response"},
            {"role": "user", "content": f"Email Response: \n {email_response}"}
        ]
        subject_response = client.chat.completions.create(
            model=model,
            messages=subject_messages,
            temperature=0.7
        )
        subject_line = subject_response.choices[0].message.content
        
        # Generate Thread Summary
        summary_messages = [
            {"role": "system", "content": "Generate a concise summary of the email thread"},
            {"role": "user", "content": f"Original Thread:\n{prompt}\n\n Response:\n{email_response}"}
        ]
        summary_response = client.chat.completions.create(
            model=model,
            messages=summary_messages,
            temperature=0.7           
        )
        thread_summary = summary_response.choices[0].message.content
        
        return {
            "error": None,
            "response": email_response,
            "subject": subject_line,
            "summary": thread_summary
        }
    except Exception as e:
        return {'error': str(e), 'response': None} 