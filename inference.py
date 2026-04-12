def run_rules(fact_base):
    """
    Apply forward chaining rules to infer internal state.
    Returns:
        tuple (bool, bool): (is_suspect_pneumonia, is_high_risk)
    """
    fever = fact_base.get("fever", False)
    cough = fact_base.get("cough", False)
    breath_shortness = fact_base.get("breath_shortness", False)
    oxygen = fact_base.get("oxygen", 98)
    
    # Rule 1: fever + cough + breath_shortness -> suspect_pneumonia
    is_suspect_pneumonia = fever and cough and breath_shortness
    
    # Rule 2: oxygen < 92 -> high_risk
    is_high_risk = oxygen < 92
    
    return is_suspect_pneumonia, is_high_risk

def decision_fusion(is_suspect, is_high_risk, ai_result=None):
    """
    Combine AI prediction and rule-based system results into a final diagnosis.
    Returns:
        str: Diagnosis string.
    """
    ai_label, ai_conf = ai_result if ai_result is not None else (None, 0.0)
    
    # 1. High Risk Scenario
    if is_high_risk or (ai_label == "Pneumonia" and ai_conf > 0.8):
        return "High Risk: Pneumonia Detected"
    
    # 2. Medium Risk / Lung Opacity
    if ai_label == "Lung Opacity" and ai_conf > 0.7:
        return "Medium Risk: Lung Opacity Detected"
    
    if is_suspect or (ai_label == "Pneumonia" and ai_conf > 0.5):
        return "Medium Risk: Suspected Pneumonia"
    
    # 3. Low Risk
    if ai_label == "Normal" and ai_conf > 0.8 and not is_suspect:
        return "Low Risk: X-ray appears Normal"
        
    return "Low Risk"
