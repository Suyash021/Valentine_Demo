import streamlit as st
import base64
from PIL import Image
import io
import uuid
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="Valentine's Surprise ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize database
if 'valentine_database' not in st.session_state:
    st.session_state.valentine_database = {}

# Custom CSS for stunning design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Playfair+Display:wght@400;700;900&family=Poppins:wght@300;400;600&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%);
        background-attachment: fixed;
    }
    
    /* Floating Hearts Animation */
    .heart {
        position: fixed;
        font-size: 20px;
        color: #ff6b81;
        animation: heartFloat 5s infinite;
        pointer-events: none;
        z-index: 999;
    }
    
    @keyframes heartFloat {
        0% { transform: translateY(100vh) scale(1); opacity: 0; }
        50% { transform: translateY(50vh) scale(1.2); opacity: 0.8; }
        100% { transform: translateY(-20vh) scale(1); opacity: 0; }
    }
    
    /* Main Title */
    .main-title {
        font-family: 'Dancing Script', cursive;
        font-size: 5rem;
        background: linear-gradient(45deg, #ff0844, #ff4567, #ff6b81);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 20px 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.1);
        animation: titleGlow 2s ease-in-out infinite;
    }
    
    @keyframes titleGlow {
        0%, 100% { filter: drop-shadow(0 0 10px rgba(255, 107, 129, 0.5)); }
        50% { filter: drop-shadow(0 0 20px rgba(255, 68, 132, 0.8)); }
    }
    
    /* Subtitle */
    .sub-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8rem;
        color: #fff;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(255, 68, 132, 0.3);
        margin-bottom: 30px;
        background: rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 60px;
        backdrop-filter: blur(10px);
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background: rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 60px;
        backdrop-filter: blur(10px);
        margin-bottom: 30px;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Poppins', sans-serif;
        font-size: 1.3rem;
        color: white;
        background: linear-gradient(45deg, #ff6b81, #ff4567);
        border-radius: 50px;
        padding: 10px 30px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 68, 132, 0.3);
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 68, 132, 0.5);
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(255, 68, 132, 0.1);
        animation: cardFloat 3s ease-in-out infinite;
    }
    
    @keyframes cardFloat {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    /* Love Letter Box */
    .letter-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 40px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 20px 60px rgba(255, 68, 132, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.5);
        position: relative;
        overflow: hidden;
    }
    
    .letter-box::before {
        content: "❤️";
        position: absolute;
        top: -20px;
        left: -20px;
        font-size: 100px;
        opacity: 0.1;
        transform: rotate(-15deg);
    }
    
    .letter-box::after {
        content: "❤️";
        position: absolute;
        bottom: -20px;
        right: -20px;
        font-size: 100px;
        opacity: 0.1;
        transform: rotate(15deg);
    }
    
    .greeting {
        font-family: 'Dancing Script', cursive;
        font-size: 2.8rem;
        color: #ff4567;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(255, 68, 132, 0.2);
    }
    
    .love-message {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        color: #4a4a4a;
        line-height: 1.8;
        text-align: center;
        white-space: pre-line;
        background: rgba(255, 245, 247, 0.8);
        padding: 30px;
        border-radius: 30px;
        margin: 20px 0;
    }
    
    .signature {
        font-family: 'Dancing Script', cursive;
        font-size: 2.2rem;
        color: #ff4567;
        text-align: right;
        margin-top: 20px;
    }
    
    /* Photo Cards */
    .photo-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 10px 30px rgba(255, 68, 132, 0.2);
        border: 2px solid white;
        transition: all 0.3s ease;
        animation: photoPulse 3s ease-in-out infinite;
    }
    
    .photo-card:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 40px rgba(255, 68, 132, 0.4);
    }
    
    @keyframes photoPulse {
        0%, 100% { box-shadow: 0 10px 30px rgba(255, 68, 132, 0.2); }
        50% { box-shadow: 0 15px 40px rgba(255, 68, 132, 0.4); }
    }
    
    .photo-frame {
        width: 100%;
        aspect-ratio: 1;
        background: linear-gradient(45deg, #ffe6e9, #ffd9e2);
        border-radius: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 4px solid white;
        overflow: hidden;
        box-shadow: inset 0 0 20px rgba(255, 68, 132, 0.2);
    }
    
    .photo-label {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        color: #ff4567;
        font-weight: 600;
        margin: 10px 0 5px;
    }
    
    .photo-sub {
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem;
        color: #888;
    }
    
    /* Code Display */
    .code-box {
        background: linear-gradient(135deg, #ff6b81, #ff4567);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 20px 50px rgba(255, 68, 132, 0.4);
        animation: codePulse 2s ease-in-out infinite;
    }
    
    @keyframes codePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .code-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8rem;
        color: white;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .share-code {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 900;
        color: white;
        background: rgba(255, 255, 255, 0.2);
        padding: 30px 50px;
        border-radius: 60px;
        display: inline-block;
        letter-spacing: 15px;
        border: 4px solid white;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
        margin: 20px 0;
    }
    
    /* Input Styling */
    .stTextInput input {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem !important;
        text-align: center;
        letter-spacing: 8px;
        border-radius: 60px !important;
        border: 3px solid #ff4567 !important;
        background: rgba(255, 255, 255, 0.95) !important;
        padding: 15px !important;
    }
    
    .stTextInput input:focus {
        border-color: #ff0844 !important;
        box-shadow: 0 0 20px rgba(255, 68, 132, 0.3) !important;
    }
    
    /* Button Styling */
    .stButton button {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        background: linear-gradient(45deg, #ff6b81, #ff4567);
        color: white;
        border: none;
        padding: 15px 40px;
        border-radius: 60px;
        box-shadow: 0 10px 30px rgba(255, 68, 132, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        font-weight: 600;
        letter-spacing: 1px;
    }
    
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(255, 68, 132, 0.5);
    }
    
    /* Info Box */
    .info-box {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: #ff4567;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Divider */
    .divider {
        text-align: center;
        font-size: 2rem;
        color: white;
        margin: 30px 0;
        text-shadow: 2px 2px 4px rgba(255, 68, 132, 0.3);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 30px;
        font-family: 'Dancing Script', cursive;
        font-size: 1.8rem;
        color: white;
        text-shadow: 2px 2px 4px rgba(255, 68, 132, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Floating hearts animation
def add_floating_hearts():
    hearts_html = ""
    for i in range(15):
        left = random.randint(0, 100)
        delay = random.randint(0, 5)
        size = random.randint(15, 30)
        hearts_html += f"""
            <div class="heart" style="left: {left}%; animation-delay: {delay}s; font-size: {size}px;">❤️</div>
        """
    st.markdown(hearts_html, unsafe_allow_html=True)

add_floating_hearts()

# Main Title
st.markdown('<h1 class="main-title">💕 Valentine\'s Day Surprise 💕</h1>', unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["🎨 Create Your Valentine", "💝 View Your Valentine"])

with tab1:
    st.markdown('<p class="sub-title">✨ Create a magical surprise for your loved one ✨</p>', unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            recipient_name = st.text_input("💕 Recipient's Name:", value="My Love", key="recipient")
            greeting = st.text_input("💌 Greeting:", value="My Dearest,")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            sender_name = st.text_input("💖 Your Name:", value="Your Valentine", key="sender")
            signature = st.text_input("✨ Signature:", value="Forever yours,")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        message = st.text_area(
            "📝 Your Love Message:", 
            value="On this Valentine's Day, my heart is overflowing with love for you.\n\nFrom the moment you came into my life, everything became more beautiful. Your smile lights up my darkest days, and your laughter is the sweetest music to my ears.\n\nI promise to stand by you through all of life's adventures, to support your dreams, and to love you more with each passing day.\n\nHappy Valentine's Day, my love!",
            height=200
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider">❤️ ❤️ ❤️</div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">📸 Add Your Special Photos</p>', unsafe_allow_html=True)
    
    photo_labels = [
        ("Our First Date", "The day it all began ✨"),
        ("Engagement Day", "When I said 'Yes' to forever 💍"),
        ("Our Favorite Moment", "Just us being happy together 🌸"),
        ("Recent Memory", "Making new memories with you 💕")
    ]
    
    uploaded_photos = []
    
    # Create photo grid
    cols = st.columns(2)
    for i in range(4):
        with cols[i % 2]:
            st.markdown(f'<div class="photo-card">', unsafe_allow_html=True)
            st.markdown(f"**{photo_labels[i][0]}**")
            st.markdown(f"*{photo_labels[i][1]}*")
            
            uploaded_file = st.file_uploader(
                f"Choose photo", 
                type=['jpg', 'jpeg', 'png', 'gif'], 
                key=f"upload_{i}",
                label_visibility="collapsed"
            )
            
            if uploaded_file is not None:
                bytes_data = uploaded_file.getvalue()
                b64 = base64.b64encode(bytes_data).decode()
                st.image(bytes_data, width=200)
                uploaded_photos.append({
                    'name': photo_labels[i][0],
                    'subtitle': photo_labels[i][1],
                    'data': b64,
                    'type': uploaded_file.type
                })
            else:
                uploaded_photos.append(None)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider">❤️ ❤️ ❤️</div>', unsafe_allow_html=True)
    
    # Generate code
    if st.button("🎁 Generate Your Unique Code", use_container_width=True):
        if any(uploaded_photos):
            # Generate unique 6-digit code
            while True:
                code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
                if code not in st.session_state.valentine_database:
                    break
            
            # Save to database
            st.session_state.valentine_database[code] = {
                'recipient': recipient_name,
                'sender': sender_name,
                'greeting': greeting,
                'message': message,
                'signature': signature,
                'photos': uploaded_photos,
                'created': datetime.now().strftime("%B %d, %Y at %I:%M %p"),
                'views': 0
            }
            
            # Display code
            st.balloons()
            st.markdown(f"""
                <div class="code-box">
                    <div class="code-title">✨ Your Valentine is Ready! ✨</div>
                    <div class="share-code">{code}</div>
                    <p style="color: white; font-size: 1.3rem;">Share this code with {recipient_name}</p>
                    <p style="color: rgba(255,255,255,0.8);">They can enter it in the "View Your Valentine" tab</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Preview
            with st.expander("👀 Preview Your Creation", expanded=True):
                st.markdown(f'<div class="letter-box">', unsafe_allow_html=True)
                st.markdown(f'<div class="greeting">{greeting}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="love-message">{message}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="signature">{signature}<br>❤️ {sender_name}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("⚠️ Please upload at least one photo!")

with tab2:
    st.markdown('<p class="sub-title">💝 Enter your code to see your surprise 💝</p>', unsafe_allow_html=True)
    
    # Create a form for code input
    with st.form(key="code_form"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            code_input = st.text_input(
                "Enter your 6-digit code:", 
                max_chars=6,
                placeholder="e.g., LOVE12",
                help="Enter the code you received from your loved one"
            ).upper()
            
            submit_button = st.form_submit_button("🔓 Open My Valentine", use_container_width=True)
    
    if submit_button:
        if len(code_input) == 6:
            if code_input in st.session_state.valentine_database:
                data = st.session_state.valentine_database[code_input]
                data['views'] += 1
                
                # Celebration effects
                st.balloons()
                st.snow()
                
                # Display the Valentine
                st.markdown(f"""
                    <div class="code-box" style="background: linear-gradient(135deg, #ff4567, #ff0844);">
                        <h1 style="color: white; font-size: 3rem; font-family: 'Dancing Script', cursive;">
                            💝 For {data['recipient']} 💝
                        </h1>
                        <p style="color: white; font-size: 1.5rem;">With love from {data['sender']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Love letter
                st.markdown(f"""
                    <div class="letter-box">
                        <div class="greeting">{data['greeting']}</div>
                        <div class="love-message">{data['message']}</div>
                        <div class="signature">{data['signature']}<br>❤️ {data['sender']}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Photos
                if any(data['photos']):
                    st.markdown('<h2 style="text-align: center; color: white; margin: 40px 0; font-family: Dancing Script; font-size: 2.5rem;">📸 Our Beautiful Memories</h2>', unsafe_allow_html=True)
                    
                    # Display photos in grid
                    cols = st.columns(2)
                    for idx, photo in enumerate(data['photos']):
                        if photo:
                            with cols[idx % 2]:
                                st.markdown(f"""
                                    <div class="photo-card">
                                        <div class="photo-frame">
                                """, unsafe_allow_html=True)
                                
                                st.image(base64.b64decode(photo['data']), use_column_width=True)
                                
                                st.markdown(f"""
                                        </div>
                                        <div class="photo-label">{photo['name']}</div>
                                        <div class="photo-sub">{photo['subtitle']}</div>
                                    </div>
                                """, unsafe_allow_html=True)
                
                # Created date
                st.markdown(f"""
                    <div style="text-align: center; margin-top: 40px; padding: 20px; background: rgba(255,255,255,0.2); border-radius: 60px;">
                        <p style="color: white; font-size: 1.2rem;">
                            ✨ Created with love on {data['created']} ✨
                        </p>
                        <p style="color: white; font-size: 1rem;">
                            This has been viewed {data['views']} time{'s' if data['views'] != 1 else ''}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
            else:
                st.error("❌ Invalid code! Please try again.")
                st.markdown("""
                    <div class="info-box">
                        <p style="color: #ff4567;">💡 Tips:</p>
                        <ul style="color: #4a4a4a;">
                            <li>Make sure you entered the code exactly as given (6 characters)</li>
                            <li>Codes are case-sensitive - use capital letters</li>
                            <li>Ask your loved one to double-check the code</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a 6-digit code!")

# Sidebar with stats
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="font-size: 3rem;">❤️</h1>
            <h2 style="font-family: Dancing Script; color: #ff4567;">Valentine's</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    active_count = len(st.session_state.valentine_database)
    st.markdown(f"<h2 style='text-align: center;'>Active Valentines: {active_count}</h2>", unsafe_allow_html=True)
    
    if active_count > 0:
        total_views = sum(data['views'] for data in st.session_state.valentine_database.values())
        st.markdown(f"<p style='text-align: center;'>Total Views: {total_views}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h3 style="text-align: center;">✨ How it works ✨</h3>
            <ol style="color: #4a4a4a;">
                <li>Create your Valentine</li>
                <li>Get a unique 6-digit code</li>
                <li>Share the code with your love</li>
                <li>They enter it to see the surprise!</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Made with infinite love ❤️</p>
        <p style="font-size: 1rem;">Create magic, share love, make memories</p>
    </div>
""", unsafe_allow_html=True)
