import openai

def analyze_file_with_chatgpt(api_key):
    """
    Prompts the user for a file name, reads the content, sends it to ChatGPT for analysis, and displays the response.
    """
    # Authenticate with OpenAI API
    openai.api_key = api_key

    # Ask the user for the file name
    file_name = input("Enter the name of the file (in the same directory): ")

    try:
        # Read the file content
        with open(file_name, "r") as file:
            file_content = file.read()

        # Ask ChatGPT for analysis
        print("Sending file content for analysis...")
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the model
            messages=[
                {"role": "system", "content": "You are an expert at analyzing and explaining Python code."},
                {"role": "user", "content": f"Analyze the following Python file and explain what it does:\n\n{file_content}"}
            ],
            max_tokens=1500  # Adjust based on how detailed the response should be
        )

        # Print ChatGPT's response
        analysis = response["choices"][0]["message"]["content"]
        print("\nChatGPT Analysis:")
        print(analysis)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    print("Welcome to the ChatGPT File Analyzer!")
    user_api_key = input("Enter your OpenAI API key: ")
    analyze_file_with_chatgpt(user_api_key)
