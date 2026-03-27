# 📘 **Project Documentation**

## **Hybrid Knowledge-Based Pneumonia Diagnosis System**

---

# 1. 🎯 **System Overview**

This system is a **Hybrid Knowledge-Based System (KBS)** that combines:

* **Rule-based reasoning (KBS)**
* **AI-based X-ray analysis (ML model)**
* **Explainability layer**

### ✅ Goal

Provide an **explainable pneumonia risk diagnosis** using:

* Symptoms
* Vital signs
* Chest X-ray

---

# 2. 🧱 **High-Level Architecture**

```
[ Streamlit UI ]
        ↓
[ Input Processing Layer ]
        ↓
[ Fact Base (Patient Data) ]
        ↓
 ┌─────────────────────────────┐
 │      Knowledge Base         │
 │ (Medical Rules)             │
 └────────────┬────────────────┘
              ↓
      [ Inference Engine ]
              ↓
 ┌─────────────────────────────┐
 │ AI Model (X-ray Analysis)   │
 └────────────┬────────────────┘
              ↓
      [ Decision Fusion ]
              ↓
      [ Explanation Module ]
              ↓
        Final Output
```

---

# 3. 🖥️ **UI Design (Streamlit)**

Your UI is part of KBS → it acts as **User Interface + Data Collector**

## 🧩 Layout Structure

### **Section 1: Patient Info**

* Age (number input)
* Gender (select box)
* Existing diseases (multiselect)

### **Section 2: Symptoms (checkboxes)**

* Fever
* Cough
* Shortness of breath
* Chest pain
* Fatigue

### **Section 3: Vital Signs**

* Oxygen level (slider)
* Temperature (input)
* Respiratory rate (input)

### **Section 4: X-ray Upload**

* File uploader (image)

### **Section 5: Button**

* `Diagnose`

---

# 4. 📥 **Input Data Structure (Fact Base)**

When user clicks diagnose → store everything in a dictionary:

```python
patient_data = {
    "age": 45,
    "fever": True,
    "cough": True,
    "breath_shortness": True,
    "oxygen": 89,
    "temperature": 38.5,
    "xray_uploaded": True
}
```

This is your **Fact Base**.

---

# 5. 🧠 **Knowledge Base (Rules)**

Create rule set manually (Python-based KBS):

```python
rules = [
    {
        "conditions": ["fever", "cough", "breath_shortness"],
        "conclusion": "suspect_pneumonia"
    },
    {
        "conditions": ["oxygen_low"],
        "conclusion": "high_risk"
    },
    {
        "conditions": ["ai_positive", "suspect_pneumonia"],
        "conclusion": "confirmed_pneumonia"
    }
]
```

---

# 6. ⚙️ **Inference Engine (Forward Chaining)**

## 🔁 Logic Flow

```python
def inference_engine(facts):
    conclusions = []

    if facts["fever"] and facts["cough"] and facts["breath_shortness"]:
        conclusions.append("suspect_pneumonia")

    if facts["oxygen"] < 92:
        conclusions.append("high_risk")

    return conclusions
```

---

# 7. 🤖 **AI Model Integration**

## Option 1 (Simple for now)

Mock AI:

```python
def ai_prediction(xray):
    return 0.85  # probability
```

## Option 2 (Later)

* Use pretrained CNN
* Use API

---

# 8. 🔗 **Decision Fusion Logic**

Combine AI + Rules:

```python
def decision_fusion(conclusions, ai_score):
    
    if "high_risk" in conclusions or ai_score > 0.8:
        return "High Risk Pneumonia"
    
    elif "suspect_pneumonia" in conclusions:
        return "Medium Risk"
    
    else:
        return "Low Risk"
```

---

# 9. 🔍 **Explanation Module**

## Build explanation dynamically:

```python
def generate_explanation(facts, conclusions, ai_score):
    explanation = []

    if facts["fever"]:
        explanation.append("Fever detected")

    if facts["oxygen"] < 92:
        explanation.append("Low oxygen level")

    if ai_score > 0.8:
        explanation.append("AI detected lung infection")

    return explanation
```

---

# 10. 📤 **Final Output UI**

Display in Streamlit:

```python
st.success(f"Diagnosis: {result}")

for reason in explanation:
    st.write(f"• {reason}")
```

---

# 11. 🔄 **Full Flow Summary**

1. User enters data (UI)
2. Data → Fact Base
3. Inference Engine applies rules
4. AI processes X-ray
5. Decision Fusion combines both
6. Explanation Module generates reasoning
7. Output shown

---

# 12. 🚀 **MVP Implementation Plan (Step-by-Step)**

### Step 1

Build UI only (Streamlit)

### Step 2

Add rule-based logic (no AI)

### Step 3

Add mock AI score

### Step 4

Add explanation system

### Step 5

Improve UI + design

---

# 13. 🧠 **Key Design Decisions**

* ✔ Forward chaining (simple + medical-friendly)
* ✔ Hybrid system (AI + rules)
* ✔ Explainability first
* ✔ Modular design (easy to extend)

