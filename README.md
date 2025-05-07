# 🎬 Lottie Animation Viewer

A streamlined web application for viewing, customizing, and analyzing Lottie animations built with Streamlit.

![Lottie Animation Viewer](https://img.shields.io/badge/Lottie-Animation%20Viewer-blue)

## 📋 Overview

Lottie Animation Viewer is a user-friendly tool that allows you to:

- Upload and display Lottie animation files (.json or .lottie)
- Load animations directly from URLs
- Adjust playback settings (speed, looping, direction)
- Resize animations
- View detailed animation metadata

## 🔧 Features

- **Multiple Input Methods**: Upload local files or load from URLs
- **Robust File Handling**: Multiple decoding strategies for different file formats
- **Interactive Controls**:
  - Adjustable playback speed
  - Toggle looping
  - Reverse playback
  - Selectable quality settings
  - Customizable height
- **Metadata Exploration**: View animation dimensions, frame rate, and other technical details

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lottie-animation-viewer.git
   cd lottie-animation-viewer
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Requirements

Create a `requirements.txt` file with these dependencies:

```
streamlit>=1.22.0
streamlit-lottie>=0.0.3
requests>=2.28.0
```

## 🏃‍♂️ Running the App

Launch the app with:

```bash
streamlit run app.py
```

Your browser should automatically open to `http://localhost:8501`

## 🔍 How to Use

1. **Upload a File**:
   - Select the "Upload File" tab
   - Click "Browse files" and select a .json or .lottie file
   
2. **Load from URL**:
   - Select the "From URL" tab
   - Paste a valid Lottie animation URL and press Enter

3. **Adjust Controls**:
   - Use the sidebar sliders and checkboxes to customize the animation
   - Expand the "Animation Metadata" section to view technical details

## ⚠️ Troubleshooting

- **File Loading Issues**: The app attempts multiple decoding strategies. If none work, try converting your file to a standard Lottie JSON format.
- **URL Loading Errors**: Ensure the URL points directly to a Lottie JSON file and is publicly accessible.
- **Display Problems**: If an animation doesn't display correctly, try adjusting the quality setting or checking the console for errors.

## 🛠️ Technical Details

The application includes sophisticated file handling to support various Lottie file formats:

- Direct JSON loading
- Multiple text encoding attempts (utf-8, utf-16, utf-32, latin-1, ascii)
- Binary JSON loading
- Fallback string parsing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Resources

- [Lottie Documentation](https://airbnb.io/lottie/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit-Lottie Package](https://github.com/andfanilo/streamlit-lottie)

---

Created with ❤️ by [Your Name]
