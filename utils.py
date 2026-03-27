def generate_explanation(fact_base, is_suspect, is_high_risk, ai_score=None, result=""):
    """
    Generate user-friendly explanations for the diagnosis.
    """
    reasons = []
    
    # 1. Vital Signs
    oxygen = fact_base.get("oxygen", 98)
    if is_high_risk: # O2 < 92
        reasons.append(f"Critically low oxygen level ({oxygen}% O2 detected - below 92% threshold).")
    
    # 2. Symptoms
    fever = fact_base.get("fever", False)
    cough = fact_base.get("cough", False)
    breath_shortness = fact_base.get("breath_shortness", False)
    
    if is_suspect:
        reasons.append("Clinical triad detected: simultaneous fever, persistent cough, and shortness of breath.")
    else:
        # Partial symptom explanations
        if fever:
            reasons.append("Fever detected, indicating possible inflammation or infection.")
        if cough:
            reasons.append("Coughing reported, indicative of respiratory tract irritation.")
        if breath_shortness:
            reasons.append("Shortness of breath reported, requiring close attention.")
            
    # Additional Context
    chest_pain = fact_base.get("chest_pain", False)
    if chest_pain:
        reasons.append("Chest pain present, contributing to respiratory distress index.")
        
    # 3. AI Influence
    if ai_score is not None:
        if ai_score > 0.8:
            reasons.append(f"AI Model detected severe lung infection patterns from the X-ray (Confidence: {ai_score * 100:.1f}%).")
        elif ai_score > 0.5:
            reasons.append(f"AI Model found moderate abnormalities in the X-ray (Confidence: {ai_score * 100:.1f}%).")
        else:
            reasons.append(f"AI Model found no significant signs of pneumonia in the X-ray.")
    elif fact_base.get("xray_uploaded", False):
        reasons.append("X-ray was uploaded, but AI model wasn't loaded or trained properly so it was ignored.")
    else:
        reasons.append("No X-ray uploaded, diagnosis was performed purely based on clinical symptoms and vitals.")
        
    return reasons
