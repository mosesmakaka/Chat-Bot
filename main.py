import google.generativeai as genai

def configure_model():
    """Configure the Generative AI model with API key and settings."""
    genai.configure(api_key="AIzaSyDzQFr_vE-lrWgc28eHjyuSlxWV-97kFCs")

def setup_model():
    """Set up the Generative AI model with generation and safety settings."""
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    return model

def get_user_input():
    """Prompt the user for input and return the entered message."""
    return input("You: ")

def main():
    """Main function to run the Generative AI script."""
    configure_model()
    generative_model = setup_model()

    # Start a conversation with an empty history
    conversation = generative_model.start_chat(history=[])

    while True:
        # Get user input
        user_input = get_user_input()

        # Send user input to the model
        conversation.send_message(user_input)

        # Print the model's generated response
        print("Model:", conversation.last.text)

if __name__ == "__main__":
    main()
