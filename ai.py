import os
import sys

# ----------------------------
# Ensure gpt4all DLLs can be found when frozen with PyInstaller
if getattr(sys, 'frozen', False):
    # Path to the DLLs inside the frozen EXE
    dll_path = os.path.join(sys._MEIPASS, "gpt4all", "llmodel_DO_NOT_MODIFY", "build")
    os.add_dll_directory(dll_path)
# ----------------------------

from gpt4all import GPT4All

# Helper to locate resources inside exe or dev environment
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Path to your local LLaMA 3.2 model
model_file = resource_path("models/Llama-3.2-1B-Instruct-Q4_0.gguf")

# Load the model locally without attempting downloads
model = GPT4All(model_file, allow_download=False, n_threads=4)

class AICharacter:
    def __init__(self, name, personality, backstory, capabilities=None):
        self.name = name
        self.personality = personality
        self.backstory = backstory
        self.capabilities = capabilities if capabilities else []

    def respond_to_event(self, dm_text, other_ai_texts=None):
        """
        Generates an in-character response using the local LLaMA model.
        RULES:
        - Only react to DM and other AI character dialogue
        - Never add dice rolls or game mechanics explanations
        - Stay in-character
        - Max 4 sentences
        """
        other_text = "\n".join(other_ai_texts) if other_ai_texts else ""
        abilities_text = ", ".join(self.capabilities) if self.capabilities else "None"

        prompt = (
            f"You are a D&D character named {self.name}.\n"
            f"Personality: {self.personality}\n"
            f"Backstory: {self.backstory}\n"
            f"Abilities: {abilities_text}\n"
            f"The DM describes: '{dm_text}'\n"
            f"Other party members have said:\n{other_text}\n"
            "Rules:\n"
            "- Only respond in-character.\n"
            "- Do not narrate dice rolls or outcomes.\n"
            "- Max 4 sentences.\n"
            "- Be creative and entertaining, focusing on dialogue and personality.\n"
            "Your response:"
        )
        response = model.generate(prompt, max_tokens=150, temp=0.7)
        response = response.split("\n")[0].strip()
        return response
