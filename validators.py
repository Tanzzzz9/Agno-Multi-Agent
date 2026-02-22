def no_hallucination_validator(response: str, context: str) -> str:
    if not context.strip():
        if "I don't know" not in response and "not sure" not in response.lower():
            return "I don't have that information in my knowledge base."
    return response
