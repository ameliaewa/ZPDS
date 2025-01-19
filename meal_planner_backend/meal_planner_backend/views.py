# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# from meal_planner_backend.GPT_API import generate_meal_plan, read_key


def create_prompt(data):
    # Extracting data from the JSON
    days = ', '.join(data['days'])
    meals_per_day = data['mealsPerDay']
    calories_per_day = data['caloriesPerDay']
    cooking_days = days
    cooking_time = data['cookingTime']
    budget = data['budget']
    allergies = data['allergies'] or "brak"
    breakfast_time = data['breakfastTime']
    cuisine = data['cuisine']
    preferences = data['preferences']
    fridge_items = data['fridgeItems']

    # Creating the formatted string
    output = (
        "Przygotuj mi plan żywieniowy i listę zakupów na cały tydzień oraz rozpiskę co kiedy mam ugotować i przepisy.\n\n"
        "Ilość posiłków dziennie: {}. Dziennie jem {} kcal. Czas na gotowanie obiadów mam w {} i mogę przeznaczyć na to {} minut dziennie, "
        "Mój budżet wynosi: {} zł. Mam uczulenie lub nie lubię: {}. Na przygotowanie śniadania mam {} minut. "
        "Chcę aby posiłki były inspirowane kuchnią {}. Moje preferencje dotyczące jedzenia to: {}. "
        "W lodówce mam {}, więc układając plan weź to pod uwagę."
        "Przedstaw rozpiskę w formie jsona o takiej strukturze: .")

    # Filling in the placeholders
    formatted_output = output.format(
        meals_per_day,
        calories_per_day,
        cooking_days,
        cooking_time,
        budget,
        allergies,
        breakfast_time,
        cuisine,
        preferences,
        fridge_items
    )
    return formatted_output


@csrf_exempt
def process_meal_plan(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            prompt = create_prompt(data)
            print(prompt)

            # testowy json (docelowo ma taki powstawać z chata)
            # API_KEY = read_key("key.txt")
            # response = generate_meal_plan(API_KEY, prompt)
            test_response = {
                              "days": [
                                {
                                  "day": "Monday",
                                  "meals": ["Breakfast: Skyr with fruit", "Lunch: Polish dumplings", "Dinner: Italian pasta"]
                                },
                                {
                                  "day": "Tuesday",
                                  "meals": ["Breakfast: Oatmeal with milk", "Lunch: Tomato soup", "Dinner: Grilled chicken"]
                                }
                              ],
                              "shoppingList": ["Skyr", "Fruit", "Dumplings", "Pasta", "Milk", "Tomatoes", "Chicken"]
                            }

            # Return the same data back to React
            return JsonResponse({
                'status': 'success',
                'message': 'Meal plan generated successfully',
                'received_data': test_response
            })

        except json.JSONDecodeError as e:
            print("JSON Decode Error:", str(e))
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)

    return JsonResponse({
        'status': 'error',
        'message': 'Only POST requests are allowed'
    }, status=405)