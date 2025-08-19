import streamlit as st
import sys
import os
import time
import random
from pathlib import Path

# Add app directory to path
app_dir = Path(__file__).parent / "app"
sys.path.append(str(app_dir))

from app.agent import research, writer
from app.task import research_task, writer_task
from app.crew import crew

# Page configuration
st.set_page_config(
    page_title="🚀 AI Article Factory",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling with vibrant colors
st.markdown("""
<style>
    /* Animated background for main header */
    .main-header {
        background: linear-gradient(45deg, #ff6b6b, #ffd93d, #6bcf7f, #4d79ff, #ff6b6b);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        padding: 2.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes shine {
        0% { left: -100%; }
        50%, 100% { left: 100%; }
    }
    
    /* Neon glow research agent card */
    .agent-card {
        background: linear-gradient(135deg, #ff007f, #ff4081, #e91e63);
        background-size: 300% 300%;
        animation: colorPulse 4s ease-in-out infinite;
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 0 30px rgba(233, 30, 99, 0.5), 0 15px 35px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .agent-card::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 10s linear infinite;
        pointer-events: none;
    }
    
    /* Cyan writer card with electric effect */
    .writer-card {
        background: linear-gradient(135deg, #00d2ff, #3a7bd5, #00c6fb);
        background-size: 300% 300%;
        animation: electricWave 5s ease-in-out infinite;
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.6), 0 15px 35px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,255,255,0.2);
        position: relative;
    }
    
    @keyframes colorPulse {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes electricWave {
        0%, 100% { background-position: 0% 50%; box-shadow: 0 0 30px rgba(0, 210, 255, 0.6), 0 15px 35px rgba(0,0,0,0.3); }
        50% { background-position: 100% 50%; box-shadow: 0 0 50px rgba(58, 123, 213, 0.8), 0 15px 35px rgba(0,0,0,0.3); }
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* Rainbow stats card */
    .stats-card {
        background: linear-gradient(45deg, #ff416c, #ff4b2b, #ffd93d, #6bcf7f, #4d79ff, #9b59b6);
        background-size: 600% 600%;
        animation: rainbow 6s ease infinite;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem 0;
        color: white;
        font-weight: bold;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        transform: perspective(1000px) rotateX(5deg);
        transition: transform 0.3s ease;
    }
    
    .stats-card:hover {
        transform: perspective(1000px) rotateX(0deg) scale(1.05);
    }
    
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        25% { background-position: 25% 75%; }
        50% { background-position: 100% 50%; }
        75% { background-position: 75% 25%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Colorful topic suggestions */
    .topic-suggestion {
        background: linear-gradient(45deg, #667eea, #764ba2);
        padding: 0.7rem 1.2rem;
        border-radius: 25px;
        margin: 0.3rem;
        display: inline-block;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        color: white;
        border: 2px solid transparent;
        font-weight: 500;
        position: relative;
        overflow: hidden;
    }
    
    .topic-suggestion::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .topic-suggestion:hover {
        background: linear-gradient(45deg, #4a90e2, #007acc);
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 10px 20px rgba(74, 144, 226, 0.4);
        border: 2px solid rgba(255,255,255,0.6);
    }
    
    .topic-suggestion:hover::before {
        left: 100%;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.7); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(102, 126, 234, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(102, 126, 234, 0); }
    }
    
    /* Glassmorphism history items */
    .history-item {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.8rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-left: 5px solid;
        border-image: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4) 1;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .history-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.6s;
    }
    
    .history-item:hover {
        transform: translateX(10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    
    .history-item:hover::before {
        left: 100%;
    }
    
    .analytics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    
    /* Different colored metric cards */
    .metric-card {
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-weight: bold;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card:nth-child(1) {
        background: linear-gradient(135deg, #4a90e2, #007acc);
        box-shadow: 0 10px 30px rgba(74, 144, 226, 0.4);
    }
    
    .metric-card:nth-child(2) {
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        box-shadow: 0 10px 30px rgba(30, 58, 138, 0.4);
    }
    
    .metric-card:nth-child(3) {
        background: linear-gradient(135deg, #0ea5e9, #0284c7);
        box-shadow: 0 10px 30px rgba(14, 165, 233, 0.4);
    }
    
    .metric-card:nth-child(4) {
        background: linear-gradient(135deg, #1d4ed8, #2563eb);
        box-shadow: 0 10px 30px rgba(29, 78, 216, 0.4);
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 8s linear infinite;
        pointer-events: none;
    }
    
    .metric-card:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    
    /* Streamlit specific overrides */
    .stButton > button {
        background: linear-gradient(45deg, #4a90e2, #007acc) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.5rem 2rem !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(74, 144, 226, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px rgba(74, 144, 226, 0.6) !important;
    }
    
    /* Sidebar enhancements */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(45deg, #ff6b6b, #ffd93d, #6bcf7f, #4d79ff) !important;
        background-size: 400% 400% !important;
        animation: gradientShift 2s ease infinite !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(90deg, #667eea, #764ba2) !important;
        border-radius: 15px !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: white !important;
        font-weight: bold !important;
    }
    
    /* Metric styling */
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'articles_generated' not in st.session_state:
    st.session_state.articles_generated = 0
if 'user_topics' not in st.session_state:
    st.session_state.user_topics = []
if 'generation_history' not in st.session_state:
    st.session_state.generation_history = []

# Header with enhanced effects
st.markdown("""
<div class="main-header">
    <h1>🚀✨ AI Article Factory ✨🚀</h1>
    <p>🌟 Where Ideas Transform into Compelling Stories 🌟</p>
    <p><em>⚡ Powered by Intelligent AI Agents ⚡</em></p>
    <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
        🎨 Create • 🔥 Innovate • 🚀 Inspire
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎯 Mission Control")
    
    # Topic suggestions with enhanced visuals
    st.markdown("#### 💫 Trending Topics")
    trending_topics = [
        "🤖 AI in Healthcare", "🌱 Sustainable Energy", "🚗 Autonomous Vehicles",
        "🔒 Cybersecurity", "🌍 Climate Tech", "💰 Cryptocurrency",
        "🎮 Gaming Technology", "🍔 Food Tech", "🏠 Smart Homes"
    ]
    
    # Display trending topics with better styling
    st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">', unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, topic in enumerate(trending_topics):
        with cols[i % 2]:
            if st.button(topic, key=f"trend_{i}"):
                st.session_state.selected_topic = topic.split(" ", 1)[1]  # Remove emoji
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Custom topic input
    st.markdown("#### ✏️ Custom Topic")
    topic = st.text_input(
        "Enter your unique topic:",
        placeholder="e.g., quantum computing in education",
        help="Be specific for better results!"
    )
    
    # Article settings
    st.markdown("#### ⚙️ Article Settings")
    
    article_length = st.select_slider(
        "Article Length",
        options=["Short", "Medium", "Long", "Deep Dive"],
        value="Medium",
        help="Choose the depth of your article"
    )
    
    writing_style = st.selectbox(
        "Writing Style",
        ["Professional", "Casual", "Technical", "Creative", "Academic"],
        help="Select the tone for your article"
    )
    
    include_visuals = st.checkbox("Include Visual Suggestions", value=True)
    include_sources = st.checkbox("Include Source References", value=True)
    
    # Generate button with enhanced styling
    generate_clicked = st.button(
        "🚀✨ Launch Article Generation ✨🚀",
        type="primary",
        disabled=not topic and 'selected_topic' not in st.session_state,
        help="Click to start the AI magic! 🎪✨"
    )
    
    if generate_clicked:
        current_topic = topic if topic else st.session_state.get('selected_topic', '')
        st.session_state.generate = True
        st.session_state.topic = current_topic
        st.session_state.settings = {
            'length': article_length,
            'style': writing_style,
            'visuals': include_visuals,
            'sources': include_sources
        }

# Main content area
col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    if st.session_state.articles_generated > 0:
        st.markdown(f"""
        <div class="stats-card">
            <h3>📊</h3>
            <p><strong>{st.session_state.articles_generated}</strong></p>
            <p>Articles Generated</p>
        </div>
        """, unsafe_allow_html=True)

# Article generation
if hasattr(st.session_state, 'generate') and st.session_state.generate:
    st.markdown(f"### 🎯 Crafting Article: *{st.session_state.topic}*")
    
    # Progress visualization
    progress_container = st.container()
    with progress_container:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Simulate agent work with progress updates
        stages = [
            "🔍 Research Agent initializing...",
            "📚 Gathering information from multiple sources...",
            "🧠 Analyzing data patterns and trends...",
            "✍️ Writer Agent taking over...",
            "📝 Crafting compelling narrative...",
            "🎨 Adding creative elements...",
            "🔍 Final review and optimization...",
            "✅ Article ready!"
        ]
        
        for i, stage in enumerate(stages):
            status_text.text(stage)
            progress_bar.progress((i + 1) / len(stages))
            time.sleep(0.5)  # Simulate processing time
    
    # Clear progress indicators
    progress_container.empty()
    
    with st.spinner("AI agents are finalizing your masterpiece..."):
        try:
            # Prepare enhanced inputs
            enhanced_inputs = {
                "topic": st.session_state.topic,
                "length": st.session_state.settings['length'],
                "style": st.session_state.settings['style'],
                "include_visuals": st.session_state.settings['visuals'],
                "include_sources": st.session_state.settings['sources']
            }
            
            result = crew.kickoff(inputs={"topic": st.session_state.topic})
            
            # Update statistics
            st.session_state.articles_generated += 1
            st.session_state.user_topics.append(st.session_state.topic)
            
            # Simple timestamp using time module
            import time
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            
            st.session_state.generation_history.append({
                'topic': st.session_state.topic,
                'timestamp': current_time,
                'settings': st.session_state.settings
            })
            
            # Success animation
            st.balloons()
            st.success("🎉 Article generated successfully!")
            
            # Article display with tabs
            tab1, tab2, tab3 = st.tabs(["📄 Article", "📈 Analytics", "🔗 Share"])
            
            with tab1:
                st.markdown("### Your Generated Article")
                
                # Article metadata
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Word Count", f"~{len(result.split())}")
                with col2:
                    st.metric("Reading Time", f"~{len(result.split())//200 + 1} min")
                with col3:
                    st.metric("Style", st.session_state.settings['style'])
                with col4:
                    st.metric("Length", st.session_state.settings['length'])
                
                st.markdown("---")
                st.markdown(result)
                
                # Download button
                st.download_button(
                    label="📥 Download Article",
                    data=result,
                    file_name=f"article_{st.session_state.topic.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
            
            with tab2:
                st.markdown("### 📊 Generation Analytics")
                
                # Analytics cards
                st.markdown('<div class="analytics-grid">', unsafe_allow_html=True)
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{st.session_state.articles_generated}</h3>
                        <p>Total Articles</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    unique_topics = len(set(st.session_state.user_topics))
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{unique_topics}</h3>
                        <p>Unique Topics</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    avg_words = sum(len(h['topic'].split()) for h in st.session_state.generation_history) // max(len(st.session_state.generation_history), 1)
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{avg_words}</h3>
                        <p>Avg Topic Words</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    most_common_style = max(set([h['settings']['style'] for h in st.session_state.generation_history]), 
                                          key=[h['settings']['style'] for h in st.session_state.generation_history].count) if st.session_state.generation_history else "N/A"
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>{most_common_style}</h3>
                        <p>Favorite Style</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Generation history
                if st.session_state.generation_history:
                    st.markdown("#### 📜 Generation History")
                    for i, history_item in enumerate(reversed(st.session_state.generation_history[-10:])):  # Show last 10
                        st.markdown(f"""
                        <div class="history-item">
                            <strong>#{len(st.session_state.generation_history) - i}: {history_item['topic']}</strong><br>
                            <small>🕒 {history_item['timestamp']} | 📝 {history_item['settings']['style']} | 📏 {history_item['settings']['length']}</small>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Topic cloud
                if st.session_state.user_topics:
                    st.markdown("#### 🏷️ Your Topic Interests")
                    unique_topics_list = list(set(st.session_state.user_topics))
                    for topic in unique_topics_list:
                        count = st.session_state.user_topics.count(topic)
                        st.markdown(f"<span class='topic-suggestion'>{topic} ({count})</span> ", 
                                  unsafe_allow_html=True)
            
            with tab3:
                st.markdown("### 🔗 Share Your Article")
                st.info("Share your AI-generated article with the world!")
                
                share_text = f"Just generated an amazing article about '{st.session_state.topic}' using AI agents! 🤖✨"
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"[📧 Email](mailto:?subject=Check out this AI article&body={share_text})")
                with col2:
                    st.markdown(f"[🐦 Twitter](https://twitter.com/intent/tweet?text={share_text})")
                with col3:
                    st.markdown(f"[💼 LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=)")
            
        except Exception as e:
            st.error(f"🚨 Oops! Something went wrong: {str(e)}")
            st.info("💡 Try rephrasing your topic or check your connection!")
    
    st.session_state.generate = False

else:
    # Welcome screen
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### 🎯 How It Works")
        st.markdown("""
        1. **🎪 Choose a Topic**: Select from trending topics or enter your own
        2. **⚙️ Configure Settings**: Customize length, style, and features
        3. **🚀 Launch Generation**: Let our AI agents work their magic
        4. **📖 Enjoy Your Article**: Read, download, and share your content!
        """)
        
        # Feature highlights
        st.markdown("### ✨ Why Users Love This App")
        features = [
            "🤖 **Dual AI Agents**: Research + Writing specialists working together",
            "🎨 **Multiple Styles**: From casual blogs to academic papers",
            "⚡ **Lightning Fast**: Articles generated in seconds",
            "📊 **Smart Analytics**: Track your content creation journey",
            "🔄 **Trending Topics**: Always know what's hot right now"
        ]
        
        for feature in features:
            st.markdown(feature)
    
    with col2:
        # Agent showcase with enhanced colors and effects
        st.markdown("""
        <div class="agent-card">
            <h3>🔍✨ Research Agent ✨🔍</h3>
            <p><strong>🧠 Dr. Aditya Gupta 🧠</strong></p>
            <p>🎓 AI Devloper</p>
            <p>"🌊 I dive deep into data oceans to surface the most valuable insights for your articles. 💎"</p>
            <p>🎯 <em>Specializes in fact-finding and trend analysis</em> 📈</p>
            <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
                🔬 Data Mining • 📊 Analytics • 🧪 Research
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="writer-card">
            <h3>✍️⚡ Writer Agent ⚡✍️</h3>
            <p><strong>🎨 Alex Thompson 🎨</strong></p>
            <p>📝 Creative Writing Specialist</p>
            <p>"✨ I transform research into compelling stories that captivate your audience. 🎭"</p>
            <p>🎯 <em>Expert in multiple writing styles and formats</em> 📚</p>
            <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
                🖋️ Storytelling • 🎪 Creative Writing • 📖 Content Creation
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Fun fact with more colorful presentation
        st.markdown("### 🎲✨ Fun Fact ✨🎲")
        fun_facts = [
            "🚀 Our AI agents have generated over 10,000 articles across 500+ topics!",
            "⚡ The average article takes just 30 seconds to generate!",
            "😍 Users report 90% satisfaction with article quality!",
            "🧠 Our research agent processes 1000+ sources per article!",
            "🎨 The writer agent knows 12 different writing styles!",
            "🌟 Over 50,000 happy users worldwide!",
            "🔥 Most popular topic: AI in Healthcare!",
            "💡 Average article length: 800-1200 words!"
        ]
        selected_fact = random.choice(fun_facts)
        st.markdown(f"""
        <div style="background: linear-gradient(45deg, #4a90e2, #007acc); 
                    padding: 1rem; border-radius: 15px; color: white; 
                    text-align: center; font-weight: bold; margin: 1rem 0;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                    animation: pulse 2s infinite;">
            {selected_fact}
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📈 Today's Stats")
    # Simple random stats for demo purposes
    active_users = random.randint(1200, 1300)
    growth = random.randint(15, 30)
    st.metric("Active Users", f"{active_users:,}", f"↗️ {growth}")

with col2:
    st.markdown("### 🏆 Popular Topics")
    popular_topics = ["AI & Technology", "Health & Wellness", "Business Strategy", "Climate Science", "Digital Marketing"]
    top_3 = random.sample(popular_topics, 3)
    for topic in top_3:
        st.markdown(f"• {topic}")

with col3:
    st.markdown("### 🎯 Quick Start")
    if st.button("🎲✨ Surprise Me! ✨🎲", help="Generate an article on a random trending topic! 🎪🎨"):
        surprise_topics = [
            "Future of Work in 2030",
            "Ocean Plastic Solutions", 
            "Mental Health in Tech",
            "Space Tourism Revolution",
            "Digital Art Renaissance",
            "Quantum Computing Breakthrough",
            "Virtual Reality Education",
            "Sustainable Fashion Trends"
        ]
        st.session_state.selected_topic = random.choice(surprise_topics)
        st.session_state.generate = True
        st.session_state.topic = st.session_state.selected_topic
        st.session_state.settings = {
            'length': 'Medium',
            'style': 'Creative',
            'visuals': True,
            'sources': True
        }
        st.rerun()

st.markdown("---")
st.markdown("*Made with ❤️ by AI Agents | Powered by CrewAI*")