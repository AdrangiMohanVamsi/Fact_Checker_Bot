from urllib.parse import urlparse
from datetime import datetime

CREDIBLE_DOMAINS = ["reuters.com", "apnews.com", "bbc.com", "www.economist.com", "www.theguardian.com"]
NON_CREDIBLE_DOMAINS = ["dailymail.co.uk", "thesun.co.uk", "infowars.com"]

def assess_credibility(url: str, publication_date_str: str = None) -> dict:
    """Assess the credibility of a source based on its domain and publication date.

    Args:
        url: The URL of the source.
        publication_date_str: The publication date of the source as a string.

    Returns:
        A dictionary containing the credibility score and an explanation.
    """
    domain = urlparse(url).netloc
    score = 50  # Start with a neutral score
    explanation = []

    if domain in CREDIBLE_DOMAINS:
        score += 30
        explanation.append("Source is from a credible domain.")
    elif domain in NON_CREDIBLE_DOMAINS:
        score -= 30
        explanation.append("Source is from a non-credible domain.")
    else:
        explanation.append("Domain credibility is unknown.")

    if publication_date_str:
        try:
            publication_date = datetime.fromisoformat(publication_date_str)
            age = (datetime.now() - publication_date).days
            if age > 365:
                score -= 10
                explanation.append("Source is older than one year.")
            else:
                score += 10
                explanation.append("Source is recent.")
        except ValueError:
            explanation.append("Could not parse publication date.")

    return {"score": min(100, max(0, score)), "explanation": " ".join(explanation)}
