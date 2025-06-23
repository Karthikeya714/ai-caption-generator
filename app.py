import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import requests

# ✅ Securely load Hugging Face API key
HF_API_TOKEN = st.secrets["hf_api_token"]

# === Load BLIP model for image captioning ===
@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_blip_model()

# === Streamlit UI ===
st.set_page_config(page_title="Smart AI Caption Generator", layout="centered")
st.title("🖼️ Smart AI Image Caption Generator")
st.markdown("Upload an image and generate funny, poetic, or aesthetic captions using AI!")

uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])
caption_style = st.selectbox("🎨 Choose caption style", ["Funny", "Poetic", "Aesthetic", "Instagram"])

# === Generate basic caption using BLIP ===
def generate_blip_caption(image):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# === Stylize caption using Hugging Face Zephyr model ===
def style_caption_with_zephyr(blip_caption, style):
    prompt = f"""Stylize the following image caption in a {style.lower()} way.
Image caption: "{blip_caption}"
Make it social-media friendly, engaging, and add hashtags if suitable."""

    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.9,
            "do_sample": True,
        }
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()[0]["generated_text"].strip()
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# === Main logic ===
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Uploaded Image", use_container_width=True)

    with st.spinner("🧠 Generating basic caption..."):
        blip_caption = generate_blip_caption(image)

    st.success("📝 Basic Caption:")
    st.markdown(f"> *{blip_caption}*")

    with st.spinner(f"✨ Stylizing caption as {caption_style}..."):
        styled_caption = style_caption_with_zephyr(blip_caption, caption_style)

    st.success("🎉 Final Caption:")
    st.markdown(f"**{styled_caption}**")
