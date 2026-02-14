import streamlit as st
import base64
from PIL import Image
import io
import json
import uuid
from datetime import datetime
import pickle

# Page configuration
st.set_page_config(
    page_title="Valentine's Day Love Letter ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize persistent storage
if 'valentine_database' not in st.session_state:
    # This will persist across sessions on Streamlit Cloud
    st.session_state.valentine_database = {}

if 'current_code' not in st.session_state:
    st.session_state.current_code = None

# Custom CSS (same as above)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4e9 100%);
    }
    .main-title {
        text-align: center;
        font-size: 3rem;
        color: #d44e7a;
        margin-bottom: 10px;
        font-weight: 600;
    }
    .sub-title {
        text-align: center;
        font-size: 1.5rem;
        color: #f28b9f;
        margin-bottom: 30px;
    }
    .hearts {
        text-align: center;
        font-size: 2rem;
        color: #f28b9f;
        letter-spacing: 15px;
        margin: 15px 0;
    }
    .letter-box {
        background: white;
        border-radius: 30px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(210, 77, 120, 0.15);
        border: 2px solid #ffcdd6;
    }
    .greeting {
        font-size: 2rem;
        color: #c4456e;
        margin-bottom: 20px;
        font-weight: 600;
    }
    .signature {
        font-size: 1.8rem;
        color: #d44e7a;
        margin-top: 30px;
        font-style: italic;
    }
    .photo-card {
        background: white;
        border-radius: 25px;
        padding: 20px;
        box-shadow: 0 8px 20px rgba(210, 77, 120, 0.1);
        border: 2px solid #ffcdd6;
        text-align: center;
        height: 100%;
        margin-bottom: 20px;
    }
    .photo-frame {
        width: 100%;
        aspect-ratio: 1;
        background: #ffeef2;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border: 3px dashed #f28b9f;
        margin-bottom: 15px;
        overflow: hidden;
    }
    .photo-frame img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .photo-label {
        color: #b13e6b;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 10px 0 5px;
    }
    .photo-sub {
        color: #d88ca0;
        font-size: 0.95rem;
    }
    .share-box {
        background: white;
        border-radius: 30px;
        padding: 30px;
        margin: 20px 0;
        border: 3px solid #ffcdd6;
        text-align: center;
    }
    .share-code {
        background: linear-gradient(135deg, #f28b9f, #d44e7a);
        color: white;
        padding: 30px;
        border-radius: 20px;
        font-size: 3rem;
        font-weight: bold;
        letter-spacing: 10px;
        margin: 20px 0;
        font-family: monospace;
    }
    .code-input {
        font-size: 1.5rem !important;
        text-align: center;
        letter-spacing: 5px;
        font-family: monospace;
    }
    .stButton button {
        background: #f28b9f;
        color: white;
        border: none;
        padding: 10px 30px;
        border-radius: 50px;
        font-size: 1.1rem;
        border: 2px solid #ffcdd6;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: #d44e7a;
        transform: scale(1.02);
    }
    .info-box {
        background: #fff0f5;
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #f28b9f;
    }
    .success-box {
        background: #d4edda;
        color: #155724;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="hearts">❤️ ❤️ ❤️</div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">💝 Valentine\'s Day Surprise 💝</h1>', unsafe_allow_html=True)
st.markdown('<div class="hearts">❤️ ❤️ ❤️</div>', unsafe_allow_html=True)

# Main app with two modes
mode = st.radio("Choose what you want to do:", ["🎁 Create a Valentine", "💕 View a Valentine"], horizontal=True)

if mode == "🎁 Create a Valentine":
    st.markdown('<h2 class="sub-title">Create a beautiful surprise for your loved one!</h2>', unsafe_allow_html=True)
    
    # Step 1: Personalize
    with st.container():
        st.markdown("### Step 1: Personalize the Message")
        col1, col2 = st.columns(2)
        
        with col1:
            recipient_name = st.text_input("Recipient's Name:", value="My Love", key="recipient")
            greeting = st.text_input("Greeting:", value="My Dearest,")
        
        with col2:
            sender_name = st.text_input("Your Name:", value="Your Valentine", key="sender")
            signature = st.text_input("Signature:", value="Forever yours,")
        
        message = st.text_area("Your Love Message:", 
            value="On this Valentine's Day, my heart is overflowing with love for you.\n\nFrom the moment you came into my life, everything became more beautiful. Your smile lights up my darkest days, and your laughter is the sweetest music to my ears.\n\nI promise to stand by you through all of life's adventures, to support your dreams, and to love you more with each passing day.\n\nHappy Valentine's Day, my love!",
            height=200)
    
    # Step 2: Add Photos
    st.markdown("### Step 2: Add Your Special Photos")
    st.markdown("*Upload up to 4 photos to share with your loved one:*")
    
    photo_labels = [
        ("Our First Date", "The day it all began ✨"),
        ("Engagement Day", "When I said 'Yes' to forever 💍"),
        ("Our Favorite Moment", "Just us being happy together 🌸"),
        ("Recent Memory", "Making new memories with you 💕")
    ]
    
    uploaded_photos = []
    
    # Create 2x2 grid for photo uploads
    for row in range(2):
        cols = st.columns(2)
        for col in range(2):
            idx = row * 2 + col
            with cols[col]:
                st.markdown(f"**{photo_labels[idx][0]}**")
                st.markdown(f"*{photo_labels[idx][1]}*")
                
                uploaded_file = st.file_uploader(
                    f"Choose photo", 
                    type=['jpg', 'jpeg', 'png', 'gif'], 
                    key=f"upload_{idx}",
                    label_visibility="collapsed"
                )
                
                if uploaded_file is not None:
                    # Convert to base64 for storage
                    bytes_data = uploaded_file.getvalue()
                    b64 = base64.b64encode(bytes_data).decode()
                    
                    # Show preview
                    st.image(bytes_data, caption="Preview", width=150)
                    
                    uploaded_photos.append({
                        'name': photo_labels[idx][0],
                        'subtitle': photo_labels[idx][1],
                        'data': b64,
                        'type': uploaded_file.type,
                        'filename': uploaded_file.name
                    })
                else:
                    uploaded_photos.append(None)
    
    # Step 3: Generate
    st.markdown("### Step 3: Generate Your Valentine")
    
    if st.button("✨ Generate Unique Share Code", use_container_width=True):
        if any(uploaded_photos):  # At least one photo uploaded
            # Generate unique code
            share_code = str(uuid.uuid4())[:6].upper()
            
            # Store in database
            st.session_state.valentine_database[share_code] = {
                'recipient': recipient_name,
                'sender': sender_name,
                'greeting': greeting,
                'message': message,
                'signature': signature,
                'photos': uploaded_photos,
                'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'views': 0
            }
            
            st.session_state.current_code = share_code
            
            # Display success and share code
            st.balloons()
            
            st.markdown(f"""
                <div class="share-box">
                    <h2 style="color: #d44e7a;">🎉 Your Valentine is Ready!</h2>
                    <p style="color: #b13e6b; font-size: 1.2rem;">Share this code with {recipient_name}:</p>
                    <div class="share-code">{share_code}</div>
                    <p style="color: #6d3b4f;">They can enter this code in the "View a Valentine" tab to see their surprise!</p>
                    <div class="success-box">
                        ✨ The photos are saved and will be waiting for them! ✨
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Show preview
            with st.expander("👀 Preview Your Valentine", expanded=True):
                st.markdown(f"### For: {recipient_name}")
                st.markdown(f"**{greeting}**")
                st.markdown(message)
                st.markdown(f"*{signature}*")
                st.markdown(f"— {sender_name}")
                
                st.markdown("#### Your Photos:")
                preview_cols = st.columns(4)
                for idx, photo in enumerate(uploaded_photos):
                    if photo:
                        with preview_cols[idx]:
                            st.image(base64.b64decode(photo['data']), caption=photo['name'], use_column_width=True)
        else:
            st.error("⚠️ Please upload at least one photo before generating the code!")

else:  # View mode
    st.markdown('<h2 class="sub-title">View your Valentine\'s Day surprise</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-box">
            <p style="color: #b13e6b;">💝 Enter the 6-character code you received from your loved one</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Code input
    share_code = st.text_input(
        "Enter your code:", 
        placeholder="e.g., AB12CD", 
        key="view_code",
        max_chars=6
    ).upper()
    
    if share_code:
        if len(share_code) == 6:
            if share_code in st.session_state.valentine_database:
                data = st.session_state.valentine_database[share_code]
                
                # Increment view count
                data['views'] += 1
                
                # Celebration effects
                st.balloons()
                st.snow()
                
                # Display the Valentine
                st.markdown(f"""
                    <div class="share-box">
                        <h1 style="color: #d44e7a; font-size: 3rem;">💝 For {data['recipient']} 💝</h1>
                        <p style="color: #f28b9f;">With love from {data['sender']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Love letter
                st.markdown(f"""
                    <div class="letter-box">
                        <div class="greeting">{data['greeting']}</div>
                        <div style="font-size: 1.25rem; color: #6d3b4f; margin: 25px 0; white-space: pre-line;">
                            {data['message']}
                        </div>
                        <div class="signature">
                            {data['signature']}<br>
                            ❤️ {data['sender']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Photos
                if any(data['photos']):
                    st.markdown("<h2 style='text-align: center; color: #c4456e; margin: 40px 0;'>📸 Our Special Memories</h2>", unsafe_allow_html=True)
                    
                    # Display photos in grid
                    for row in range(2):
                        cols = st.columns(2)
                        for col in range(2):
                            idx = row * 2 + col
                            if idx < len(data['photos']) and data['photos'][idx]:
                                photo = data['photos'][idx]
                                with cols[col]:
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
                    
                    # Photo count
                    photo_count = sum(1 for p in data['photos'] if p)
                    st.markdown(f"""
                        <p style="text-align: center; color: #d88ca0; margin: 20px 0;">
                            ✨ {photo_count} beautiful memories shared with love ✨
                        </p>
                    """, unsafe_allow_html=True)
                
                # Created date
                st.markdown(f"""
                    <p style="text-align: center; color: #b13e6b; margin-top: 30px; font-style: italic;">
                        Created with love on {data['created']}
                    </p>
                """, unsafe_allow_html=True)
                
            else:
                st.error("❌ Invalid code! Please check and try again.")
                st.markdown("""
                    <div class="info-box">
                        <p style="color: #b13e6b;">💡 Tips:</p>
                        <ul style="color: #6d3b4f;">
                            <li>Make sure you entered the code exactly as given (6 characters)</li>
                            <li>Codes are case-sensitive - use capital letters</li>
                            <li>Ask the person who created it to double-check the code</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Please enter a 6-character code")

# Show active valentines count in sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/200/ffcdd6/ffffff?text=❤️", width=200)
    st.markdown("### 💝 Active Valentines")
    active_count = len(st.session_state.valentine_database)
    st.markdown(f"<h2 style='text-align: center; color: #d44e7a;'>{active_count}</h2>", unsafe_allow_html=True)
    
    if active_count > 0:
        st.markdown("### 📊 Stats")
        total_views = sum(data['views'] for data in st.session_state.valentine_database.values())
        st.markdown(f"Total views: **{total_views}**")
    
    st.markdown("---")
    st.markdown("""
        ### 📋 How it works:
        1. **Creator**: Uploads photos & generates code
        2. **Shares**: Sends the 6-digit code
        3. **Receiver**: Enters code to view surprise
        
        ✨ Photos are saved permanently!
    """)

# Footer
st.markdown("---")
st.markdown("""
    <footer style="text-align: center; padding: 20px; color: #b13e6b;">
        <p>Made with ❤️ for lovers everywhere</p>
        <p style="font-size: 0.9rem;">Create once, share forever with a special code!</p>
    </footer>
""", unsafe_allow_html=True)
