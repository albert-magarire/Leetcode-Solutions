import openai

def is_openai_api_key_valid(api_key):
    openai.api_key = api_key
    try:
        # Attempt a simple API call, e.g., listing models
        openai.models.list()
        return True
    except openai.AuthenticationError:
        return False
    except openai.APIConnectionError as e:
        print(f"API Connection Error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Replace 'YOUR_API_KEY' with the key you want to verify
api_key_to_check = "sk-project-XXXXXXXXXXXXXXXXXXXXXX"

if is_openai_api_key_valid(api_key_to_check):
    print("OpenAI API key is valid.")
else:
    print("OpenAI API key is invalid or an error occurred.")