import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
from io import BytesIO
from typing import Optional, Dict, Any

# Configure the page
st.set_page_config(
    page_title="Lottie Animation Viewer", 
    page_icon="🎬",
    layout="centered"
)

def load_lottie_url(url: str) -> Optional[Dict[str, Any]]:
    """Load Lottie animation from URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error loading URL: {e}")
        return None

def load_lottie_file(file) -> Optional[Dict[str, Any]]:
    """Robust Lottie file loader with multiple decoding strategies"""
    try:
        # Strategy 1: Try direct JSON load
        file.seek(0)
        try:
            return json.load(file)
        except json.JSONDecodeError:
            pass
        
        # Strategy 2: Try reading as text with different encodings
        file.seek(0)
        file_content = file.read()
        
        # If content is bytes, try decoding
        if isinstance(file_content, bytes):
            encodings = ['utf-8', 'utf-16', 'utf-32', 'latin-1', 'ascii']
            for encoding in encodings:
                try:
                    decoded_content = file_content.decode(encoding)
                    return json.loads(decoded_content)
                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue
        
        # Strategy 3: Try loading as binary JSON
        file.seek(0)
        try:
            return json.load(BytesIO(file_content))
        except json.JSONDecodeError:
            pass
        
        # Strategy 4: Try parsing as string directly
        try:
            if isinstance(file_content, bytes):
                return json.loads(file_content.decode('utf-8', errors='ignore'))
            return json.loads(file_content)
        except:
            pass
            
        st.error("All decoding strategies failed for this file")
        return None
        
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

# Main App Interface
st.title("🎬 Lottie Animation Viewer")
st.markdown("Upload a Lottie file (.json or .lottie) or provide a URL")

# Input methods
tab1, tab2 = st.tabs(["📁 Upload File", "🌐 From URL"])

with tab1:
    uploaded_file = st.file_uploader(
        "Choose a Lottie animation file", 
        type=["json", "lottie"],
        accept_multiple_files=False,
        help="Supports both .json and .lottie file formats"
    )
    
    if uploaded_file:
        animation_data = load_lottie_file(uploaded_file)
    else:
        animation_data = None

with tab2:
    url = st.text_input(
        "Enter Lottie animation URL",
        placeholder="https://assets.lottiefiles.com/packages/lf20_abc123.json",
        help="Direct URL to a Lottie JSON file"
    )
    if url:
        animation_data = load_lottie_url(url)

# Display and controls
if animation_data:
    st.sidebar.header("⚙️ Animation Controls")
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        speed = st.slider("Speed", 0.1, 5.0, 1.0, 0.1)
        loop = st.checkbox("Loop", True)
    with col2:
        reverse = st.checkbox("Reverse", False)
        quality = st.selectbox("Quality", ["low", "medium", "high"], index=2)
    
    height = st.sidebar.slider("Height", 100, 800, 400, 50)

    # Display animation
    try:
        st_lottie(
            animation_data,
            speed=speed,
            reverse=reverse,
            loop=loop,
            quality=quality,
            height=height,
            key="lottie_animation"
        )
        
        # Show animation metadata
        with st.expander("📊 Animation Metadata"):
            metadata = {
                "Dimensions": f"{animation_data.get('w', 'N/A')}×{animation_data.get('h', 'N/A')}",
                "Frame Rate": animation_data.get('fr', 'N/A'),
                "Total Frames": animation_data.get('ip', 'N/A'),
                "Version": animation_data.get('v', 'N/A'),
                "Assets Count": len(animation_data.get('assets', [])),
                "Layers Count": len(animation_data.get('layers', []))
            }
            st.json(metadata)
            
    except Exception as e:
        st.error(f"Error displaying animation: {str(e)}")
else:
    st.info("ℹ️ Please upload a Lottie file or provide a URL to view an animation")
    st.markdown("""
    **Need test files? Try these:**
    - [Sample Lottie 1](https://assets1.lottiefiles.com/packages/lf20_ysrn2iwp.json)
    - [Sample Lottie 2](https://assets9.lottiefiles.com/packages/lf20_2cwDXD.json)
    """)

# Add some style
st.markdown("""
<style>
    .stLottie {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)