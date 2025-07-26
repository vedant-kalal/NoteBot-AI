import os
import json
import google.generativeai as genai

# Load Gemini API key and model from JSON config
config_path = os.path.join(os.path.dirname(__file__), 'gemini_model_config.json')

if not os.path.exists(config_path):
    raise FileNotFoundError(f"Gemini model config file not found at {config_path}")

with open(config_path, 'r') as f:
    config = json.load(f)

api_key = config.get("api_key")
model_name = config.get("model_name", "gemini-2.5-pro")  # default fallback

if not api_key:
    raise ValueError("Gemini API key not found in the config file")

# Configure Gemini and export model instance
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name)
