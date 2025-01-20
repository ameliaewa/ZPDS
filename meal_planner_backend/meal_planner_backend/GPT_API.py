from openai import OpenAI

def chat_with_gpt(prompt, key):
    """
    Funkcja do komunikacji z modelem GPT przez API.

    Args:
        prompt (str): Treść zapytania wysyłanego do modelu.
        key (str): Klucz do API.

    Returns:
        str: Odpowiedź wygenerowana przez model.
    """
    client = OpenAI(api_key=key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Błąd podczas komunikacji z API: {e}"


def read_key(file_path):
    with open(file_path, 'r') as file:
        key = file.read()
    return key

def generate_meal_plan(API_KEY, prompt):
        response = chat_with_gpt(prompt, API_KEY)
        print(f"GPT: {response}")
        return response



if __name__ == "__main__":
    API_KEY = read_key("key.txt")
    prompt = "Tell me what I can do for dinner in less than 20 minutes"
    main(API_KEY, prompt)

