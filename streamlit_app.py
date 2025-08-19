import streamlit as st
import sys
import os
from pathlib import Path

# Add app directory to path
app_dir = Path(__file__).parent / "app"
sys.path.append(str(app_dir))

from agent import research, writer
from task import research_task, writer_task
from crew import crew

st.set_page_config(
    page_title="CrewAI Article Generator",
    page_icon="📝",
    layout="wide"
)

st.title("📝 CrewAI Article Generator")
st.markdown("Generate comprehensive articles using AI agents")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    topic = st.text_input("Enter Topic:", placeholder="e.g., healthcare AI, renewable energy")
    
    if st.button("Generate Article", type="primary", disabled=not topic):
        st.session_state.generate = True
        st.session_state.topic = topic

# Main content area
if hasattr(st.session_state, 'generate') and st.session_state.generate:
    st.header(f"Generating article about: {st.session_state.topic}")
    
    with st.spinner("AI agents are working..."):
        try:
            result = crew.kickoff(inputs={"topic": st.session_state.topic})
            
            st.success("Article generated successfully!")
            st.markdown("### Generated Article")
            st.markdown(result)
            
        except Exception as e:
            st.error(f"Error generating article: {str(e)}")
    
    st.session_state.generate = False

else:
    st.info("Enter a topic in the sidebar and click 'Generate Article' to start.")
    
    # Show agent information
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 Research Agent")
        st.write("**Role:** Senior Researcher")
        st.write("**Goal:** Uncover groundbreaking technologies")
        
    with col2:
        st.subheader("✍️ Writer Agent")
        st.write("**Role:** Senior Writer")
        st.write("**Goal:** Write comprehensive articles")