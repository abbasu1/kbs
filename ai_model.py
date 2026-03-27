def ai_prediction(xray):
    """
    Mock AI prediction for X-ray analysis.
    Returns a dummy probability score.
    """
    if xray is not None:
        return 0.85  # probability
    return 0.0
