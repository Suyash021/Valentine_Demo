import streamlit as st
import base64
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="For My Beloved Rekha ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default styling
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background: transparent;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Custom CSS for Streamlit background
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4e9 100%);
    }
    </style>
""", unsafe_allow_html=True)

# HTML Content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For My Beloved Rekha ❤️</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: transparent;
            color: #b13e6b;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            text-align: center;
            padding: 40px 20px 20px;
        }
        
        h1 {
            font-size: 3.5rem;
            color: #d44e7a;
            margin-bottom: 10px;
            font-weight: 600;
            letter-spacing: 1px;
        }
        
        .hearts {
            font-size: 2rem;
            color: #f28b9f;
            letter-spacing: 15px;
            margin: 15px 0;
        }
        
        .letter-section {
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
        
        .letter-content {
            font-size: 1.25rem;
            color: #6d3b4f;
            margin: 25px 0;
            white-space: pre-line;
        }
        
        .signature {
            font-size: 1.8rem;
            color: #d44e7a;
            margin-top: 30px;
            font-style: italic;
        }
        
        .photos-section {
            margin: 40px 0;
        }
        
        .photos-title {
            text-align: center;
            font-size: 2.2rem;
            color: #c4456e;
            margin-bottom: 30px;
        }
        
        .photo-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 25px;
            padding: 10px;
        }
        
        .photo-card {
            background: white;
            border-radius: 25px;
            padding: 20px;
            box-shadow: 0 8px 20px rgba(210, 77, 120, 0.1);
            border: 2px solid #ffcdd6;
            text-align: center;
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
            position: relative;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .photo-frame:hover {
            background: #ffdee6;
            border-color: #d44e7a;
        }
        
        .photo-frame img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
        }
        
        .upload-icon {
            font-size: 3rem;
            color: #f28b9f;
            margin-bottom: 10px;
            z-index: 1;
        }
        
        .upload-text {
            color: #b13e6b;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.8);
            padding: 5px 15px;
            border-radius: 50px;
            z-index: 1;
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
        
        .file-input {
            display: none;
        }
        
        .reset-btn {
            background: #f28b9f;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 1.1rem;
            cursor: pointer;
            margin: 20px auto;
            display: block;
            transition: background 0.3s ease;
            border: 2px solid #ffcdd6;
        }
        
        .reset-btn:hover {
            background: #d44e7a;
        }
        
        footer {
            text-align: center;
            padding: 30px;
            color: #b13e6b;
            font-size: 1.2rem;
        }
        
        .photo-added {
            border: 3px solid #d44e7a;
            background: #fff;
        }
        
        @media (max-width: 700px) {
            h1 {
                font-size: 2.5rem;
            }
            
            .photo-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .letter-section {
                padding: 30px 20px;
            }
            
            .greeting {
                font-size: 1.6rem;
            }
        }
        
        @media (max-width: 480px) {
            h1 {
                font-size: 2rem;
            }
            
            .hearts {
                letter-spacing: 8px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="hearts">❤️ ❤️ ❤️</div>
            <h1>For My Beloved Rekha</h1>
            <div class="hearts">❤️ ❤️ ❤️</div>
        </header>
        
        <div class="letter-section">
            <div class="greeting">My Dearest Rekha,</div>
            
            <div class="letter-content">
                On this Valentine's Day, my heart is overflowing with love for you. 
                
                From the moment you came into my life, everything became more beautiful. Your smile lights up my darkest days, and your laughter is the sweetest music to my ears. 
                
                As my fiancée, you've shown me what true love means - patient, kind, and unconditional. Every moment spent with you feels like a blessing, and I cherish every single memory we've created together.
                
                I promise to stand by you through all of life's adventures, to support your dreams, to make you laugh when you're sad, and to love you more with each passing day.
                
                You're not just my love - you're my best friend, my confidante, and my home. I can't wait to spend the rest of my life making you happy.
                
                Happy Valentine's Day, my love!
            </div>
            
            <div class="signature">
                Forever yours,<br>
                Your Valentine ❤️
            </div>
        </div>
        
        <div class="photos-section">
            <h2 class="photos-title">Our Beautiful Memories</h2>
            <p style="text-align: center; margin-bottom: 20px; color: #b13e6b;">Click on any frame to add your photo 📸</p>
            
            <div class="photo-grid" id="photoGrid">
                <!-- Photo 1 -->
                <div class="photo-card" id="card1">
                    <div class="photo-frame" onclick="document.getElementById('file1').click()">
                        <div class="upload-icon">📸</div>
                        <div class="upload-text">Click to add photo</div>
                    </div>
                    <input type="file" id="file1" class="file-input" accept="image/*" onchange="uploadPhoto(event, 'img1', this)">
                    <img id="img1" style="display: none;">
                    <div class="photo-label">Our First Date</div>
                    <div class="photo-sub">The day it all began ✨</div>
                </div>
                
                <!-- Photo 2 -->
                <div class="photo-card" id="card2">
                    <div class="photo-frame" onclick="document.getElementById('file2').click()">
                        <div class="upload-icon">📸</div>
                        <div class="upload-text">Click to add photo</div>
                    </div>
                    <input type="file" id="file2" class="file-input" accept="image/*" onchange="uploadPhoto(event, 'img2', this)">
                    <img id="img2" style="display: none;">
                    <div class="photo-label">Best Picture</div>
                    <div class="photo-sub">When I fell harder for you😘</div>
                </div>
                
                <!-- Photo 3 -->
                <div class="photo-card" id="card3">
                    <div class="photo-frame" onclick="document.getElementById('file3').click()">
                        <div class="upload-icon">📸</div>
                        <div class="upload-text">Click to add photo</div>
                    </div>
                    <input type="file" id="file3" class="file-input" accept="image/*" onchange="uploadPhoto(event, 'img3', this)">
                    <img id="img3" style="display: none;">
                    <div class="photo-label">Our Favorite Moment</div>
                    <div class="photo-sub">Just us being happy together 🌸</div>
                </div>
                
                <!-- Photo 4 -->
                <div class="photo-card" id="card4">
                    <div class="photo-frame" onclick="document.getElementById('file4').click()">
                        <div class="upload-icon">📸</div>
                        <div class="upload-text">Click to add photo</div>
                    </div>
                    <input type="file" id="file4" class="file-input" accept="image/*" onchange="uploadPhoto(event, 'img4', this)">
                    <img id="img4" style="display: none;">
                    <div class="photo-label">Recent Memory</div>
                    <div class="photo-sub">Making new memories with you 💕</div>
                </div>
            </div>
            
            <button class="reset-btn" onclick="resetAllPhotos()">Reset All Photos</button>
        </div>
        
        <footer>
            <p>Made with all my love, especially for you</p>
            <p style="margin-top: 15px; font-size: 1.4rem;">14 February 2026</p>
            <div style="margin-top: 20px; font-size: 1.8rem;">❤️</div>
        </footer>
    </div>

    <script>
        function uploadPhoto(event, imgId, inputElement) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    const photoCard = inputElement.closest('.photo-card');
                    const photoFrame = photoCard.querySelector('.photo-frame');
                    const imgElement = photoCard.querySelector('#' + imgId);
                    
                    imgElement.src = e.target.result;
                    imgElement.style.display = 'block';
                    
                    photoFrame.innerHTML = '';
                    photoFrame.appendChild(imgElement);
                    photoFrame.classList.add('photo-added');
                    
                    const removeBtn = document.createElement('span');
                    removeBtn.innerHTML = '✕';
                    removeBtn.style.position = 'absolute';
                    removeBtn.style.top = '5px';
                    removeBtn.style.right = '5px';
                    removeBtn.style.background = '#d44e7a';
                    removeBtn.style.color = 'white';
                    removeBtn.style.width = '25px';
                    removeBtn.style.height = '25px';
                    removeBtn.style.borderRadius = '50%';
                    removeBtn.style.display = 'flex';
                    removeBtn.style.alignItems = 'center';
                    removeBtn.style.justifyContent = 'center';
                    removeBtn.style.cursor = 'pointer';
                    removeBtn.style.fontSize = '14px';
                    removeBtn.style.zIndex = '10';
                    removeBtn.onclick = function(e) {
                        e.stopPropagation();
                        removePhoto(photoCard, imgId, inputElement);
                    };
                    
                    photoFrame.appendChild(removeBtn);
                }
                
                reader.readAsDataURL(file);
            }
        }
        
        function removePhoto(photoCard, imgId, inputElement) {
            const photoFrame = photoCard.querySelector('.photo-frame');
            const imgElement = photoCard.querySelector('#' + imgId);
            
            photoFrame.innerHTML = '';
            photoFrame.innerHTML = '<div class="upload-icon">📸</div><div class="upload-text">Click to add photo</div>';
            
            imgElement.src = '';
            imgElement.style.display = 'none';
            inputElement.value = '';
            photoFrame.classList.remove('photo-added');
            
            photoFrame.onclick = function() {
                inputElement.click();
            };
        }
        
        function resetAllPhotos() {
            for (let i = 1; i <= 4; i++) {
                const photoCard = document.getElementById(`card${i}`);
                const photoFrame = photoCard.querySelector('.photo-frame');
                const imgElement = photoCard.querySelector(`#img${i}`);
                const inputElement = photoCard.querySelector(`#file${i}`);
                
                photoFrame.innerHTML = '';
                photoFrame.innerHTML = '<div class="upload-icon">📸</div><div class="upload-text">Click to add photo</div>';
                
                imgElement.src = '';
                imgElement.style.display = 'none';
                inputElement.value = '';
                photoFrame.classList.remove('photo-added');
                
                photoFrame.onclick = function() {
                    inputElement.click();
                };
            }
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            for (let i = 1; i <= 4; i++) {
                const inputElement = document.getElementById(`file${i}`);
                const photoFrame = document.querySelector(`#card${i} .photo-frame`);
                
                if (photoFrame && inputElement) {
                    photoFrame.onclick = function() {
                        inputElement.click();
                    };
                }
            }
        });
    </script>
</body>
</html>
"""

# Function to create download link for HTML
def get_html_download_link():
    b64 = base64.b64encode(html_content.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="valentine_for_rekha.html" style="background: #f28b9f; color: white; padding: 10px 20px; border-radius: 50px; text-decoration: none; display: inline-block; margin: 10px;">📥 Download HTML Version</a>'
    return href

# Main Streamlit app
def main():
    # Sidebar with customization options
    with st.sidebar:
        st.image("https://via.placeholder.com/150/ffcdd6/ffffff?text=❤️", width=150)
        st.markdown("## 💝 Customize Your Message")
        
        # Option to customize letter
        customize = st.checkbox("Customize the love letter")
        
        if customize:
            st.markdown("---")
            st.markdown("### Edit the letter:")
            
            new_greeting = st.text_input("Greeting", "My Dearest Rekha,")
            new_message = st.text_area("Your message", 
                "On this Valentine's Day, my heart is overflowing with love for you.\n\nFrom the moment you came into my life, everything became more beautiful. Your smile lights up my darkest days, and your laughter is the sweetest music to my ears.\n\nAs my fiancée, you've shown me what true love means - patient, kind, and unconditional. Every moment spent with you feels like a blessing, and I cherish every single memory we've created together.\n\nI promise to stand by you through all of life's adventures, to support your dreams, to make you laugh when you're sad, and to love you more with each passing day.\n\nYou're not just my love - you're my best friend, my confidante, and my home. I can't wait to spend the rest of my life making you happy.\n\nHappy Valentine's Day, my love!")
            new_signature = st.text_input("Signature", "Forever yours,\nYour Valentine ❤️")
            
            # Update HTML with customizations if needed
            if st.button("Update Letter"):
                st.session_state['greeting'] = new_greeting
                st.session_state['message'] = new_message
                st.session_state['signature'] = new_signature
                st.success("Letter updated! (Refresh to see changes)")
        
        st.markdown("---")
        st.markdown("### 📋 Instructions")
        st.markdown("""
        1. Click on any photo frame to upload
        2. Add your favorite memories
        3. Share this link with your love
        """)
        
        st.markdown("---")
        st.markdown(get_html_download_link(), unsafe_allow_html=True)
    
    # Main content - Display the HTML
    st.components.v1.html(html_content, height=1800, scrolling=True)
    
    # Add some Streamlit metrics at the bottom
    
    col2, col3 = st.columns(2)
    with col2:
        st.metric("Years Together", "2.5", "And counting...")
    with col3:
        st.metric("Happiness Level", "100%", "With you")

if __name__ == "__main__":
    main()
