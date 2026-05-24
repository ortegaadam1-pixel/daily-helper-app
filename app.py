import streamlit as st
import os

# This line automatically installs the sound generator so the app doesn't crash
try:
    from gtts import gTTS
except ImportError:
    os.system('pip install gtts')
    from gtts import gTTS

# App Configuration
st.set_page_config(page_title="The Daily Helper", page_icon="🔥", layout="centered")

st.title("🔥 The Daily Helper App")
st.write("Welcome! Let's explore the power of the Holy Spirit together.")

# --- FEATURE 1: THE LANGUAGE MIXER ---
st.header("1. The Pentecost Language Mixer")
st.write("Type a sentence to hear how the Holy Spirit shared the Good News out loud in different languages at Pentecost!")

user_phrase = st.text_input("Type a cool phrase (like 'God gives you courage!'):", placeholder="God loves you!")

if st.button("✨ Activate Pentecost Mixer"):
    if user_phrase:
        st.write("🔊 **The Holy Spirit makes the message heard! Click play below:**")
        
        # Real translation map for actual spoken audio generation
        translations = {
            "Spanish 🇪🇸": ("es", "¡Dios te ama! Él te da fuerza."),
            "Swahili 🇰🇪": ("sw", "Mungu anakupenda! Anakupa nguvu."),
            "German 🇩🇪": ("de", "Gott liebt dich! Er gibt dir Kraft."),
            "Tagalog 🇵🇭": ("tl", "Mahal ka ng Dios! Binibigyan ka niya ng lakas.")
        }
        
        for lang_name, (lang_code, translated_text) in translations.items():
            st.write(f"**{lang_name}:**")
            
            # Generating real audio voice files dynamically
            tts = gTTS(text=translated_text, lang=lang_code, slow=False)
            filename = f"{lang_code}_audio.mp3"
            tts.save(filename)
            
            # Displaying an actual playable sound bar widget for the kids to listen to
            with open(filename, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")
                
            # Clean up files securely
            os.remove(filename)
            
        st.balloons()
    else:
        st.warning("Please type a phrase first!")

st.markdown("---")

# --- FEATURE 2: PLAYGROUND COURAGE GENERATOR ---
st.header("2. Playground Courage Generator")
st.write("Pick a situation where you need some giant-sized courage this week:")

scenario = st.selectbox(
    "What's going on?",
    ["Select a situation...",
     "Kids are being mean on the playground at recess",
     "I have a big test coming up and I am super nervous",
     "Someone in my family is sick or having a sad day",
     "I feel lonely and don't know who to sit with at lunch"]
)

if scenario != "Select a situation...":
    st.subheader("Your Holy Spirit Gameplan:")
    
    if "playground" in scenario:
        response = "Hey champ! Remember, the Holy Spirit is right there with you by the swings. He gave Peter the bravery to speak to thousands, and He is giving you the power to stand tall right now. You don't have to be afraid!"
    elif "test" in scenario:
        response = "Take a deep breath! The Holy Spirit is the ultimate Helper. He clears up confusion. Before you start your test, whisper: 'Hey God, help my mind stay calm.' He's got you!"
    elif "family" in scenario:
        response = "God is closer than a cozy blanket. Right now, His Spirit lives inside your heart. You can pray for your family right here, and His comfort will cover your whole house."
    else:
        response = "You are never alone. The Holy Spirit loves you completely. Walk into that lunchroom knowing the King of the universe is walking right next to you!"
        
    st.info(response)
    st.markdown("> **Scripture to Lock in Your Heart:** *'God did not give us a spirit that makes us afraid. He gave us a spirit of power and love.' — 2 Timothy 1:7*")
