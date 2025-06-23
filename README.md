# 🖼️ Smart AI Image Caption Generator

A powerful Streamlit web application that generates creative, stylized captions for your images using state-of-the-art AI models. Upload any image and get funny, poetic, aesthetic, or Instagram-ready captions instantly!

## ✨ Features

- **Image Captioning**: Uses Salesforce's BLIP model for accurate image description
- **Style Customization**: Transform basic captions into creative styles:
  - 🤣 **Funny** - Humorous and entertaining captions
  - 🎭 **Poetic** - Beautiful, artistic descriptions
  - 💫 **Aesthetic** - Trendy, visually appealing captions
  - 📱 **Instagram** - Social media optimized with hashtags
- **AI-Powered Styling**: Leverages Hugging Face's Zephyr-7B model for caption enhancement
- **User-Friendly Interface**: Clean, intuitive Streamlit interface
- **Real-time Processing**: Fast caption generation and styling

## 🌐 Live App

[🖼️ Try the AI Caption Generator](https://ai-caption-generator-j5uugvebbkyc4jls8xcpzt.streamlit.app/)


## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Hugging Face API Token (free tier available)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-ai-caption-generator.git
   cd smart-ai-caption-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Hugging Face API token**
   
   Create a `.streamlit/secrets.toml` file in your project directory:
   ```toml
   hf_api_token = "your_hugging_face_api_token_here"
   ```
   
   > 🔑 Get your free API token from [Hugging Face](https://huggingface.co/settings/tokens)

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 📋 Requirements

```
streamlit
torch
transformers
pillow
requests
```

## 🎯 Usage

1. **Upload an Image**: Click "Upload your image" and select a JPG, JPEG, or PNG file
2. **Choose Style**: Select your preferred caption style from the dropdown
3. **Generate Caption**: The app will automatically generate a basic caption and then stylize it
4. **Copy & Share**: Use your generated caption for social media or any other purpose!

## 🔧 Configuration

### Environment Variables

The application uses Streamlit secrets for secure API key management. Make sure to set up your `secrets.toml` file as shown in the installation steps.

### Model Information

- **Image Captioning**: Salesforce/blip-image-captioning-base
- **Text Styling**: HuggingFaceH4/zephyr-7b-beta

## 🚀 Deployment

### Streamlit Cloud

1. Fork this repository
2. Connect your GitHub account to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy the app and add your `hf_api_token` in the secrets section
4. Your app will be live at `https://yourapp.streamlit.app`

### Other Platforms

This application can be deployed on various platforms like Heroku, Railway, or any cloud service that supports Python applications.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add more caption styles (Professional, Romantic, Technical, etc.)
- Implement batch processing for multiple images
- Add support for video thumbnails
- Create a REST API version
- Improve UI/UX design
- Add caption history/favorites

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) for image captioning
- [Hugging Face Zephyr](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) for text generation
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Hugging Face](https://huggingface.co/) for providing free AI model APIs

## 🐛 Issues & Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/smart-ai-caption-generator/issues) page
2. Create a new issue with a detailed description
3. Include error messages and steps to reproduce

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/smart-ai-caption-generator?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/smart-ai-caption-generator?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/smart-ai-caption-generator)
![Python version](https://img.shields.io/badge/python-3.8+-blue.svg)

## 🔮 Future Enhancements

- [ ] Multi-language caption support
- [ ] Caption editing interface
- [ ] Image filters and effects
- [ ] Caption analytics and performance metrics
- [ ] Mobile app version
- [ ] Integration with social media platforms

---

**Made with ❤️ and lots of ☕**

> ⭐ If you found this project helpful, please give it a star!
