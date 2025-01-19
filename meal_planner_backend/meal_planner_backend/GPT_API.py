from openai import OpenAI
import json

def chat_with_gpt(prompt):

    client = OpenAI()

    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract content from the response
        raw_response = response['choices'][0]['message']['content']
        print("Raw API Response:\n", raw_response)

        # Split the response by days of the week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meal_plan = {day: {} for day in days}
        grocery_list = set()  # Use a set to avoid duplicates

        current_day = None
        current_meal = None

        # Parse the response (simple text-based parsing example)
        for line in raw_response.split("\n"):
            line = line.strip()
            if line in days:
                current_day = line
            elif current_day and ":" in line:
                if line.startswith(("Breakfast", "Lunch", "Dinner")):
                    # Split the meal and add to the meal plan
                    meal_type, meal_desc = line.split(":", 1)
                    current_meal = meal_type.strip()
                    meal_plan[current_day][current_meal] = {"meal": meal_desc.strip(), "recipe": ""}
                elif "Recipe:" in line:
                    # Add recipe to the last added meal
                    if current_meal and current_day:
                        recipe = line.replace("Recipe:", "").strip()
                        meal_plan[current_day][current_meal]["recipe"] = recipe
                        # Extract grocery items (basic parsing)
                        for ingredient in recipe.split(","):
                            grocery_list.add(ingredient.strip().split(" ")[-1])  # Simplified parsing
        print(json.dumps(response, indent=4))

        return {"meal_plan": meal_plan, "grocery_list": list(grocery_list)}

    except Exception as e:
        print("Error:", str(e))
        return None

def read_key(file_path):
    with open(file_path, 'r') as file:
        key = file.read()
    return key

def main(API_KEY, prompt):
        response = chat_with_gpt(prompt, API_KEY)
        print(f"GPT: {response}")

if __name__ == "__main__":
    prompt = """
    Create a weekly meal plan for a healthy diet. Split it into days of the week (Monday to Sunday),
    and include three meals per day: breakfast, lunch, and dinner. For each meal, provide a recipe with ingredients and steps.
    """
    chat_with_gpt(prompt)

