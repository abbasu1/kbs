def generate_explanation(facts, conclusions, ai_score):
    """
    Builds a dynamic explanation based on the facts, conclusions, and AI score.
    """
    explanation = []

    if facts.get("fever"):
        explanation.append("Fever detected")
        
    if facts.get("cough"):
         explanation.append("Patient has a cough")
         
    if facts.get("breath_shortness"):
         explanation.append("Shortness of breath reported")

    if facts.get("oxygen", 100) < 92:
        explanation.append(f"Low oxygen level ({facts.get('oxygen')}%)")

    if ai_score > 0.8:
        explanation.append(f"AI detected lung infection (Score: {ai_score * 100:.1f}%)")

    if not explanation:
        explanation.append("No significant risk factors detected based on inputted medical rules and AI interpretation.")

    return explanation
