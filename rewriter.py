import base64
import os
from google import genai
from google.genai import types

def generate():
    client = genai.Client(
api_key="AIzaSyCqJvTFuB5-zOrwwD7lygeT65XA7iJJ_6k",
    )

    model = "gemini-2.0-flash"
    text_to_rewrite = " ".join(os.sys.argv[1:]) or input("Enter text to rewrite: ")

    custom_prompt = """I want you to rewrite the following text in a way that will reduce AI detection by mimicking natural human writing, specifically using the following proven techniques:

- Use moderately formal tone — not casual or slangy, but not robotic.
- Vary sentence length and structure — include long sentences, short fragments, and some rhythm changes.
- Insert passive voice or inverted phrasing occasionally (e.g., “is faced by many,” “are most affected”).
- Remove or soften obvious transitional phrases like “However,” or “In conclusion.”
- Add reflective or philosophical phrasing at the beginning or end (e.g., “It remains one of the...,” or “That’s what must be addressed.”).
- Use slightly more advanced vocabulary and varied word choice.
- Break up overly polished structure — avoid clean intro–body–conclusion flow.

Text:
""" + text_to_rewrite

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=custom_prompt)],
        ),
    ]

    tools = [types.Tool(googleSearch=types.GoogleSearch())]
    config = types.GenerateContentConfig(tools=tools)

    print("\n--- Rewritten output ---\n")
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=config,
    ):
        if chunk.text:
            print(chunk.text, end="")

if __name__ == "__main__":
    generate()
