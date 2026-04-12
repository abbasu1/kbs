def generate_explanation(fact_base, is_suspect, is_high_risk, ai_result=None, result=""):
    """
    Generate user-friendly explanations for the diagnosis.
    """
    reasons = []
    
    # 1. Vital Signs
    oxygen = fact_base.get("oxygen", 98)
    if is_high_risk: # O2 < 92
        reasons.append(f"Critically low oxygen level ({oxygen}% O2 detected - below 92% threshold).")
    
    # 2. Symptoms
    if is_suspect:
        reasons.append("Clinical triad detected: simultaneous fever, persistent cough, and shortness of breath.")
    else:
        # Partial symptom explanations
        if fact_base.get("fever"):
            reasons.append("Fever detected, indicating possible inflammation or infection.")
        if fact_base.get("cough"):
            reasons.append("Coughing reported, indicative of respiratory tract irritation.")
        if fact_base.get("breath_shortness"):
            reasons.append("Shortness of breath reported, requiring close attention.")
            
    # 3. AI Influence
    if ai_result is not None:
        ai_label, ai_conf = ai_result
        conf_pct = ai_conf * 100
        
        if ai_label == "Pneumonia":
            if ai_conf > 0.8:
                reasons.append(f"AI Model detected severe pneumonia patterns in the X-ray ({conf_pct:.1f}% confidence).")
            else:
                reasons.append(f"AI Model found indicators of pneumonia in the X-ray ({conf_pct:.1f}% confidence).")
        elif ai_label == "Lung Opacity":
            reasons.append(f"AI Model detected Lung Opacity, which can be an early indicator of inflammation ({conf_pct:.1f}% confidence).")
        elif ai_label == "Normal":
            if ai_conf > 0.8:
                reasons.append(f"AI Model found the X-ray to be clear and within normal parameters ({conf_pct:.1f}% confidence).")
            else:
                reasons.append(f"AI Model found no significant pneumonia markers, though confidence is low ({conf_pct:.1f}%).")
                
    elif fact_base.get("xray_uploaded", False):
        reasons.append("X-ray was uploaded, but AI analysis was unavailable.")
    else:
        reasons.append("No X-ray uploaded; diagnosis based purely on clinical vitals and symptoms.")
        
    return reasons
