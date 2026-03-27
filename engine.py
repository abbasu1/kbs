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

def inference_engine(facts):
    """
    Applies simple forward chaining based on patient facts.
    """
    conclusions = []

    if facts.get("fever") and facts.get("cough") and facts.get("breath_shortness"):
        conclusions.append("suspect_pneumonia")

    if facts.get("oxygen", 100) < 92:
        conclusions.append("high_risk")

    return conclusions

def decision_fusion(conclusions, ai_score):
    """
    Combines rule-based conclusions and AI score to reach a final decision.
    """
    if "high_risk" in conclusions or ai_score > 0.8:
        return "High Risk Pneumonia"
    
    elif "suspect_pneumonia" in conclusions:
        return "Medium Risk"
    
    else:
        return "Low Risk"
