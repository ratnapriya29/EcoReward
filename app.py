import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import qrcode
import io

# ------------------ LOAD MODEL ------------------
model = tf.keras.models.load_model("plastic_model.h5")

# ------------------ SESSION STATE ------------------
if "total_items" not in st.session_state:
    st.session_state.total_items = 0

if "money" not in st.session_state:
    st.session_state.money = 0

if "co2" not in st.session_state:
    st.session_state.co2 = 0.0

# ------------------ TITLE ------------------
st.title("♻️ AI Plastic Reward System")

# ------------------ DASHBOARD ------------------
st.subheader("📊 Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Items", st.session_state.total_items)
col2.metric("Earnings (₹)", st.session_state.money)
col3.metric("CO2 Saved", st.session_state.co2)

# ------------------ IMAGE UPLOAD ------------------
st.subheader("📤 Upload Plastic Image")

uploaded_file = st.file_uploader("Choose image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # ------------------ PREPROCESS ------------------
    img = image.resize((150, 150))   # MUST match training size
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # ------------------ PREDICTION ------------------
    prediction = model.predict(img_array)[0][0]

    # ------------------ RESULT ------------------
    if prediction > 0.5:
        st.success("♻️ Recyclable Plastic")

        reward = 5
        st.session_state.total_items += 1
        st.session_state.money += reward
        st.session_state.co2 += 0.1

        st.info(f"💰 You earned ₹{reward}")

    else:
        st.error("❌ Non-Recyclable Plastic")

        reward = 2
        st.session_state.total_items += 1
        st.session_state.money += reward

        st.info(f"💰 You earned ₹{reward}")

# ------------------ REWARD SECTION ------------------
st.subheader("🎁 Redeem Reward")

if st.session_state.total_items > 0:
    qr_data = f"Items: {st.session_state.total_items}, Money: ₹{st.session_state.money}"

    qr = qrcode.make(qr_data)

    # Convert to bytes (no error)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    buf.seek(0)

    st.image(buf, width=200)

else:
    st.info("Upload plastic to start earning rewards ♻️")