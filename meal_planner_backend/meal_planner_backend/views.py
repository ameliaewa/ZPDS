# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
        "Ilość posiłków dziennie: {}. Dziennie jem {} kcal. Czas na gotowanie obiadów mam w {} i mogę przeznaczyć na to {} minut, "
        "Mój budżet wynosi: {} zł. Mam uczulenie lub nie lubię: {}. Na przygotowanie śniadania mam {} minut. "
        "Chcę aby posiłki były inspirowane kuchnią {}. Moje preferencje dotyczące jedzenia to: {}. "
        "W lodówce mam {}, więc układając plan weź to pod uwagę.\n\n"
        "Przedstaw rozpiskę w formie jsona.")

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
            # Get the raw data and print it
            print("Raw request body:", request.body)

            # Parse the JSON data
            data = json.loads(request.body)

            # Print the parsed data
            print("Received data:", data)
            prompt = create_prompt(data)
            print(prompt)

            # Return the same data back to React
            return JsonResponse({
                'status': 'success',
                'message': 'Data received successfully',
                'received_data': data
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