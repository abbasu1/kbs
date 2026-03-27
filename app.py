import streamlit as st
import inference
import utils
import model

st.set_page_config(page_title="Pneumonia Diagnosis KBS", layout="centered", page_icon="🩺")

st.title("🩺 Hybrid Knowledge-Based Pneumonia Diagnosis System")
st.markdown("Provide an explainable pneumonia risk diagnosis using symptoms, vital signs, and X-ray analysis.")

# --- UI Setup Section ---
st.header("1. Patient Info")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=45)
with col2:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# --- Symptoms ---
st.header("2. Symptoms")
col3, col4 = st.columns(2)
with col3:
    fever = st.checkbox("Fever")
    cough = st.checkbox("Cough")
    breath_shortness = st.checkbox("Shortness of breath")
with col4:
    chest_pain = st.checkbox("Chest pain")
    fatigue = st.checkbox("Fatigue")

# --- Vital Signs ---
st.header("3. Vital Signs")
oxygen = st.slider("Oxygen level (%)", min_value=50, max_value=100, value=98)
col5, col6 = st.columns(2)
with col5:
    temperature = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, value=37.0, step=0.1)
with col6:
    respiratory_rate = st.number_input("Respiratory rate (bpm)", min_value=10, max_value=60, value=16)

# --- X-ray Upload ---
st.header("4. X-ray Upload")
xray_file = st.file_uploader("Upload Chest X-ray (Optional)", type=["png", "jpg", "jpeg"])

st.markdown("---")

# --- Form Submission ---
submit = st.button("Diagnose", type="primary", use_container_width=True)

if submit:
    # Build Fact Base
    fact_base = {
        "age": age,
        "gender": gender,
        "fever": fever,
        "cough": cough,
        "breath_shortness": breath_shortness,
        "chest_pain": chest_pain,
        "fatigue": fatigue,
        "oxygen": oxygen,
        "temperature": temperature,
        "respiratory_rate": respiratory_rate,
        "xray_uploaded": xray_file is not None
    }
    
    with st.spinner("Analyzing patient facts and medical scans..."):
        ai_score = None
        
        # If X-ray image is uploaded -> run AI prediction
        if xray_file is not None:
            ai_score = model.predict_xray(xray_file)
            
        # Inference Engine applies rules
        is_suspect, is_high_risk = inference.run_rules(fact_base)
        
        # Decision Fusion combines AI prediction + rules
        result = inference.decision_fusion(is_suspect, is_high_risk, ai_score)
        
        # Explanation Module generates reasoning
        reasons = utils.generate_explanation(fact_base, is_suspect, is_high_risk, ai_score, result)
    
    # Final Output Show
    st.header("📤 Diagnosis Results")
    
    if "High Risk" in result:
        st.error(f"**Diagnosis: {result}**")
    elif "Medium Risk" in result:
        st.warning(f"**Diagnosis: {result}**")
    else:
        st.success(f"**Diagnosis: {result}**")
        
    st.markdown("### Decision Reasoning (Explainability Layer):")
    for reason in reasons:
        st.write(f"• {reason}")
