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

def decision_fusion(is_suspect, is_high_risk, ai_score=None):
    """
    Combine AI prediction and rule-based system results into a final diagnosis.
    Returns:
        str: Diagnosis string ("High Risk Pneumonia", "Medium Risk", "Low Risk").
    """
    # Use 0 as default if AI score is not provided/available
    ai_prob = ai_score if ai_score is not None else 0.0
    
    # if AI > 0.8 OR high_risk → High Risk Pneumonia
    if ai_prob > 0.8 or is_high_risk:
        return "High Risk Pneumonia"
    
    # if suspect → Medium Risk
    if is_suspect:
        return "Medium Risk"
    
    # else → Low Risk
    return "Low Risk"
