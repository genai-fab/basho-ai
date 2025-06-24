import streamlit as st
import requests
import json

st.title("Basho AI - Haiku Challenge")
st.write("Get an AI-generated theme, write a haiku, and see how you did!")

# Button to get a new AI-generated theme
if st.button("Get New Theme"):
    # API call to generate a theme
    theme_prompt = "Generate a simple, poetic theme for writing a haiku. Give just 2-4 words that describe something in nature, daily life, or emotions. Examples: 'morning coffee steam', 'autumn leaves falling', 'first snowfall'. Just give the theme, nothing else."
    
    theme_response = requests.post(
        "http://localhost:11434/api/generate",
        headers={"Content-Type": "application/json"},
        json={
            "model": "llama3.2",
            "prompt": theme_prompt,
            "stream": False
        }
    )
    
    if theme_response.status_code == 200:
        theme_result = theme_response.json()
        st.session_state.current_theme = theme_result["response"].strip()
    else:
        st.error("Error generating theme")

# Display current theme
if 'current_theme' in st.session_state:
    st.subheader(f"Your Theme: {st.session_state.current_theme}")
    
    # Text area for user's haiku
    user_haiku = st.text_area("Your haiku (remember: 5-7-5 syllables):", 
                              placeholder="Enter your haiku here...\nLine 1 (5 syllables)\nLine 2 (7 syllables)\nLine 3 (5 syllables)")
    
    if st.button("Submit Haiku"):
        if user_haiku:
            # Enhanced API call: Count syllables and evaluate
            evaluation_prompt = f"""Analyze this haiku: "{user_haiku}"

            Please do the following:
            1. Count the syllables in each line (show your work)
            2. Tell me if it follows the 5-7-5 pattern
            3. Give encouraging feedback about the content and structure
            
            Format your response like this:
            Line 1: [count syllables] = X syllables
            Line 2: [count syllables] = Y syllables  
            Line 3: [count syllables] = Z syllables
            
            Pattern: [X-Y-Z] (✓ or ✗ for correct 5-7-5)
            
            Feedback: [your thoughts]"""
            
            evaluation_response = requests.post(
                "http://localhost:11434/api/generate",
                headers={"Content-Type": "application/json"},
                json={
                    "model": "llama3.2",
                    "prompt": evaluation_prompt,
                    "stream": False
                }
            )
            
            # Second API call: AI creates its own haiku about the same theme
            ai_haiku_prompt = f"""Write a haiku about "{st.session_state.current_theme}". Make it beautiful and follow the 5-7-5 syllable pattern. Put each line on a separate line."""
            
            ai_haiku_response = requests.post(
                "http://localhost:11434/api/generate",
                headers={"Content-Type": "application/json"},
                json={
                    "model": "llama3.2",
                    "prompt": ai_haiku_prompt,
                    "stream": False
                }
            )
            
            # Display results
            if evaluation_response.status_code == 200 and ai_haiku_response.status_code == 200:
                eval_result = evaluation_response.json()
                ai_result = ai_haiku_response.json()
                
                st.write("## Your Haiku:")
                st.text(user_haiku)
                
                st.write("## AI Analysis:")
                st.text(eval_result["response"])
                
                st.write("## AI's Haiku on the Same Theme:")
                st.text(ai_result["response"])
            else:
                st.error("Error connecting to AI")
        else:
            st.warning("Please enter your haiku")
else:
    st.write("Click 'Get New Theme' to start!")