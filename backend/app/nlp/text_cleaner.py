import re


def clean_text(text: str) -> str:
    """
    Cleans extracted resume text so it can be
    processed by the skill extraction system.
    """

    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Replace common separators with spaces
    text = text.replace("|", " ")
    text = text.replace("/", " ")
    text = text.replace("\\", " ")

    # Remove URLs
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    # Remove email addresses
    text = re.sub(
        r"\S+@\S+",
        " ",
        text
    )

    # Keep letters, numbers, #, +, . and spaces
    # This helps preserve skills such as C++, C#, .NET
    text = re.sub(
        r"[^a-zA-Z0-9+#.\s-]",
        " ",
        text
    )

    # Replace multiple spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()