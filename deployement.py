import streamlit as st
import base64
from PIL import Image
import io
import hashlib
import datetime
import json
import uuid

# Page configuration
st.set_page_config(
    page_title="Valentine's Day Love Letter ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state for storing shared data
if 'shared_photos' not in st.session_state:
    st.session_state.shared_photos = {}

if 'current_share_code' not in st.session_state:
    st.session_state.current_share_code = None

# Custom CSS
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
        background: #f28b9f;
        color: white;
        padding: 20px;
        border-radius: 20px;
        font-size: 2.5rem;
        font-weight: bold;
        letter-spacing: 5px;
        margin: 20px 0;
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
    }
    .stButton button:hover {
        background: #d44e7a;
    }
    .info-box {
        background: #fff0f5;
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #f28b9f;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="hearts">❤️ ❤️ ❤️</div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">💝 Valentine\'s Day Love Letter 💝</h1>', unsafe_allow_html=True)
st.markdown('<div class="hearts">❤️ ❤️ ❤️</div>', unsafe_allow_html=True)

# Create tabs for different modes
tab1, tab2 = st.tabs(["✍️ Create & Share", "💕 View Shared"])

with tab1:
    st.markdown('<h2 class="sub-title">Create a Valentine\'s Day surprise for your love!</h2>', unsafe_allow_html=True)
    
    # Get creator's name
    creator_name = st.text_input("Your Name (or your girlfriend's name):", value="Rekha", key="creator_name")
    
    # Customize letter
    with st.expander("✏️ Customize the love letter (optional)", expanded=False):
        custom_greeting = st.text_input("Greeting:", "My Dearest,")
        custom_message = st.text_area("Your message:", 
            "On this Valentine's Day, my heart is overflowing with love for you.\n\nFrom the moment you came into my life, everything became more beautiful. Your smile lights up my darkest days, and your laughter is the sweetest music to my ears.\n\nI promise to stand by you through all of life's adventures, to support your dreams, to make you laugh when you're sad, and to love you more with each passing day.\n\nHappy Valentine's Day, my love!")
        custom_signature = st.text_input("Signature:", "Forever yours,")
    
    # Photo upload section
    st.markdown("### 📸 Add Your Photos")
    st.markdown("Upload 4 special photos for your loved one:")
    
    col1, col2 = st.columns(2)
    
    photo_labels = [
        ("Our First Date", "The day it all began ✨"),
        ("Engagement Day", "When I said 'Yes' to forever 💍"),
        ("Our Favorite Moment", "Just us being happy together 🌸"),
        ("Recent Memory", "Making new memories with you 💕")
    ]
    
    uploaded_photos = []
    
    for i in range(4):
        with col1 if i < 2 else col2:
            st.markdown(f"**{photo_labels[i][0]}**")
            st.markdown(f"*{photo_labels[i][1]}*")
            uploaded_file = st.file_uploader(f"Choose photo {i+1}", type=['jpg', 'jpeg', 'png', 'gif'], key=f"create_upload_{i}")
            if uploaded_file is not None:
                # Convert to base64 for storage
                bytes_data = uploaded_file.getvalue()
                b64 = base64.b64encode(bytes_data).decode()
                uploaded_photos.append({
                    'name': photo_labels[i][0],
                    'subtitle': photo_labels[i][1],
                    'data': b64,
                    'type': uploaded_file.type
                })
                st.success(f"✅ Photo {i+1} uploaded!")
            else:
                uploaded_photos.append(None)
    
    # Generate share code
    if st.button("🎁 Generate Share Code & Create Valentine", use_container_width=True):
        if any(uploaded_photos):  # At least one photo uploaded
            # Generate unique share code
            share_code = str(uuid.uuid4())[:8].upper()
            
            # Store all data
            st.session_state.shared_photos[share_code] = {
                'creator': creator_name,
                'greeting': custom_greeting,
                'message': custom_message,
                'signature': custom_signature,
                'photos': uploaded_photos,
                'created': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            st.session_state.current_share_code = share_code
            
            # Display share code
            st.markdown("---")
            st.markdown("""
                <div class="share-box">
                    <h3 style="color: #d44e7a;">🎉 Your Valentine's Day Surprise is Ready!</h3>
                    <p style="color: #b13e6b;">Share this code with your loved one:</p>
            """, unsafe_allow_html=True)
            
            st.markdown(f'<div class="share-code">{share_code}</div>', unsafe_allow_html=True)
            
            st.markdown("""
                    <p style="color: #6d3b4f;">They can enter this code in the "View Shared" tab to see their surprise!</p>
                    <p style="color: #f28b9f; font-size: 1.2rem;">💝 The photos will be there waiting for them! 💝</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Show preview
            with st.expander("👀 Preview your creation", expanded=True):
                st.markdown(f"### For: {creator_name}")
                st.markdown(f"**{custom_greeting}**")
                st.markdown(custom_message)
                st.markdown(f"*{custom_signature}*")
                
                if any(uploaded_photos):
                    st.markdown("#### Your Photos:")
                    preview_cols = st.columns(4)
                    for idx, photo in enumerate(uploaded_photos):
                        if photo:
                            with preview_cols[idx]:
                                st.image(base64.b64decode(photo['data']), caption=photo['name'], use_column_width=True)
        else:
            st.warning("⚠️ Please upload at least one photo before generating the share code!")

with tab2:
    st.markdown('<h2 class="sub-title">View your Valentine\'s Day surprise</h2>', unsafe_allow_html=True)
    
    # Enter share code
    share_code = st.text_input("Enter the share code you received:", placeholder="e.g., AB12CD34", key="view_code").upper()
    
    if share_code:
        if share_code in st.session_state.shared_photos:
            data = st.session_state.shared_photos[share_code]
            
            st.balloons()
            st.snow()
            
            # Display the Valentine
            st.markdown(f"""
                <div class="share-box">
                    <h1 style="color: #d44e7a; font-size: 2.5rem;">💝 For {data['creator']} 💝</h1>
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
                        ❤️
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Photos
            st.markdown("<h2 style='text-align: center; color: #c4456e; margin: 40px 0;'>Our Memories Together</h2>", unsafe_allow_html=True)
            
            # Display photos in grid
            photo_cols = st.columns(2)
            for idx, photo in enumerate(data['photos']):
                if photo:
                    with photo_cols[idx % 2]:
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
                <p style="text-align: center; color: #d88ca0; margin-top: 30px;">
                    Created with love on {data['created']}
                </p>
            """, unsafe_allow_html=True)
            
        else:
            st.error("❌ Invalid share code! Please check and try again.")
            st.markdown("""
                <div class="info-box">
                    <p style="color: #b13e6b;">💡 Make sure you:</p>
                    <ul style="color: #6d3b4f;">
                        <li>Entered the code exactly as given (including capital letters)</li>
                        <li>Got the code from the person who created the Valentine</li>
                        <li>Try copying and pasting the code</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <footer style="text-align: center; padding: 20px; color: #b13e6b;">
        <p>Made with ❤️ for everyone in love</p>
        <p style="font-size: 0.9rem;">Share a code, share the love!</p>
    </footer>
""", unsafe_allow_html=True)
