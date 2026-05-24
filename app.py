import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="The Daily Helper", page_icon="🔥", layout="centered")

st.title("🔥 The Daily Helper App")
st.write("Welcome! Let's explore the power of the Holy Spirit together.")

# --- FEATURE 1: THE LANGUAGE MIXER ---
st.header("1. The Pentecost Language Mixer")
st.write("Speak or type a sentence to hear how the Holy Spirit shared the Good News with everyone at Pentecost!")

user_phrase = st.text_input("Type a cool phrase (e.g., 'God loves you and gives you courage!'):", 
                            placeholder="God loves you!")

if st.button("✨ Activate Pentecost Mixer"):
    if user_phrase:
        st.write("🔊 *Simulating simultaneous Holy Spirit translation...*")
        
        # Simulating multimodal translation output
        translations = {
            "Spanish 🇪🇸": f"¡Dios te ama! (Translating: '{user_phrase}')",
            "Swahili 🇰🇪": f"Mungu anakupenda! (Translating: '{user_phrase}')",
            "German 🇩🇪": f"Gott liebt dich! (Translating: '{user_phrase}')",
            "Tagalog 🇵🇭": f"Mahal ka ng Diyos! (Translating: '{user_phrase}')"
        }
        
        for lang, text in translations.items():
            time.sleep(0.5)
            st.success(f"**{lang}:** {text}")
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
    
    # Custom AI response generation logic based on 2 Timothy 1:7
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
