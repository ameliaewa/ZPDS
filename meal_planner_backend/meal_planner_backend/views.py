# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from meal_planner_backend.GPT_API import generate_meal_plan, read_key


def create_prompt(data):
    # Extracting data from the JSON
    days = ', '.join(data.get('days', [])) if data.get('days') else None
    meals_per_day = data.get('mealsPerDay')
    calories_per_day = data.get('caloriesPerDay')
    cooking_days = days
    cooking_time = data.get('cookingTime')
    budget = data.get('budget')
    allergies = data.get('allergies') or "brak"
    breakfast_time = data.get('breakfastTime')
    cuisine = data.get('cuisine')
    preferences = data.get('preferences')
    fridge_items = data.get('fridgeItems')

    response = {
                "mealPlan": {
                    "days": [
                        {
                            "day": "Monday",
                            "meals": [
                                {
                                    "name": "Breakfast",
                                    "time": "08:00",
                                    "meal": "Name of the meal",
                                    "recipe": "Step-by-step instructions here.",
                                    "ingredients": "ingredient1, ingredient2"
                                }
                            ]
                        },
                    ]
                },
                "shoppingList": [ "ingredient1 - quantity", "ingredient2 - quantity" ],
            }


    # Building the output dynamically
    instructions = ["Przygotuj mi plan żywieniowy i listę zakupów na cały tydzień oraz rozpiskę co kiedy mam ugotować i przepisy."]

    if meals_per_day:
        instructions.append(f"Ilość posiłków dziennie: {meals_per_day}.")
    if calories_per_day:
        instructions.append(f"Dziennie jem {calories_per_day} kcal.")
    if cooking_days and cooking_time:
        instructions.append(f"Czas na gotowanie obiadów mam w {cooking_days} i mogę przeznaczyć na to {cooking_time} minut.")
    if budget:
        instructions.append(f"Mój budżet wynosi: {budget} zł.")
    if allergies:
        instructions.append(f"Mam uczulenie lub nie lubię: {allergies}.")
    if breakfast_time:
        instructions.append(f"Na przygotowanie śniadania mam {breakfast_time} minut.")
    if cuisine:
        instructions.append(f"Chcę aby posiłki były inspirowane kuchnią {cuisine}.")
    if preferences:
        instructions.append(f"Moje preferencje dotyczące jedzenia to: {preferences}.")
    if fridge_items:
        instructions.append(f"W lodówce mam {fridge_items}, więc układając plan weź to pod uwagę.")

    instructions.append(f"Przedstaw rozpiskę w formie jsona o takiej strukturze: {response}")
    instructions.append("Nie dodawaj żadnych dodatkowych komentarzy po udzieleniu odpwoiedzi w formacie JSON. "
                        "Pisz po Polsku. W liście zakupów trzymaj się narzuconego formatu")
    return " ".join(instructions)

@csrf_exempt
def process_meal_plan(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)

            prompt = create_prompt(data)
            print(prompt)

            # Testowy JSON (docelowo ma taki powstawać z chata)
            #API_KEY = read_key("key.txt")
            #response = generate_meal_plan(API_KEY, prompt)
            response = {
  "mealPlan": {
    "days": [
      {
        "day": "Monday",
        "meals": [
          {
            "name": "Breakfast",
            "meal": "Shake",
            "time": "08:00",
            "recipe": "Shake: Blend 1 banana, 1 cup of spinach, 1/2 cup of Greek yogurt, 1 cup of almond milk, and 1 tbsp peanut butter until smooth.",
            "ingredients": "banana, spinach, Greek yogurt, almond milk, peanut butter"
          },
          {
            "name": "Lunch",
            "meal": "Quinoa Salad",
            "time": "13:00",
            "recipe": "Quinoa Salad: Cook 1/2 cup quinoa. Mix with 1/2 cup cherry tomatoes, 1/2 cucumber, 1/4 cup feta cheese, 2 tbsp olive oil, and 1 tbsp lemon juice.",
            "ingredients": "quinoa, cherry tomatoes, cucumber, feta cheese, olive oil, lemon juice"
          },
          {
            "name": "Dinner",
            "meal": "Stir-fry",
            "time": "18:00",
            "recipe": "Stir-fry: Sauté 200g chicken breast with 1 bell pepper, 1/2 onion, 2 cloves garlic, and 1 tbsp soy sauce.",
            "ingredients": "chicken breast, bell pepper, onion, garlic, soy sauce"
          }
        ]
      },
      {
        "day": "Tuesday",
        "meals": [
          {
            "name": "Breakfast",
            "meal": "Oatmeal",
            "time": "08:00",
            "recipe": "Oatmeal: Cook 1/2 cup oats with 1 cup water. Add 1/4 cup blueberries, 1 tbsp honey, and 1 tbsp almond butter.",
            "ingredients": "oats, blueberries, honey, almond butter"
          },
          {
            "name": "Lunch",
            "meal": "Grilled cheese",
            "time": "13:00",
            "recipe": "Grilled cheese: Grill 2 slices whole-grain bread with 2 slices cheddar cheese. Serve with 1 cup tomato soup.",
            "ingredients": "whole-grain bread, cheddar cheese, tomato soup"
          },
          {
            "name": "Dinner",
            "meal": "Pasta",
            "time": "18:00",
            "recipe": "Pasta: Cook 100g whole-wheat pasta. Mix with 1/2 cup marinara sauce, 1/4 cup parmesan cheese, and 1 tbsp basil.",
            "ingredients": "whole-wheat pasta, marinara sauce, parmesan cheese, basil"
          }
        ]
      },
      {
        "day": "Wednesday",
        "meals": [
          {
            "name": "Breakfast",
            "meal": "Avocado toast",
            "time": "08:00",
            "recipe": "Avocado toast: Mash 1 avocado on 2 slices whole-grain bread. Top with 1/4 tsp chili flakes and 1/2 lemon juice.",
            "ingredients": "avocado, whole-grain bread, chili flakes, lemon juice"
          },
          {
            "name": "Lunch",
            "meal": "Chicken Wrap",
            "time": "13:00",
            "recipe": "Chicken Wrap: Fill 1 tortilla with 100g grilled chicken, 1/4 cup spinach, 1/4 bell pepper, and 1 tbsp tzatziki.",
            "ingredients": "tortilla, grilled chicken, spinach, bell pepper, tzatziki"
          },
          {
            "name": "Dinner",
            "meal": "Taco",
            "time": "18:00",
            "recipe": "Taco: Cook 100g minced beef with 1/2 onion, 1 clove garlic, and taco seasoning. Serve in 2 taco shells.",
            "ingredients": "minced beef, onion, garlic, taco seasoning, taco shells"
          }
        ]
      },
      {
        "day": "Thursday",
        "meals": [
          {
            "name": "Breakfast",
            "meal": "Smoothie Bowl",
            "time": "08:00",
            "recipe": "Smoothie Bowl: Blend 1 banana, 1/2 cup berries, and 1/2 cup almond milk. Top with 2 tbsp granola.",
            "ingredients": "banana, berries, almond milk, granola"
          },
          {
            "name": "Lunch",
            "meal": "Veggie Sandwich",
            "time": "13:00",
            "recipe": "Veggie Sandwich: Fill 2 slices whole-grain bread with 1/4 avocado, 1/2 tomato, cucumber slices, and lettuce.",
            "ingredients": "whole-grain bread, avocado, tomato, cucumber, lettuce"
          },
          {
            "name": "Dinner",
            "meal": "Rice Bowl",
            "time": "18:00",
            "recipe": "Rice Bowl: Cook 1/2 cup brown rice. Top with 100g tofu, 1/4 cup broccoli, 1/2 carrot, and 1 tbsp soy sauce.",
            "ingredients": "brown rice, tofu, broccoli, carrot, soy sauce"
          }
        ]
      },
      {
        "day": "Friday",
        "meals": [
          {
            "name": "Breakfast",
            "meal": "Fruit Salad",
            "time": "08:00",
            "recipe": "Fruit Salad: Mix 1 apple, 1 orange, 1/2 banana, and 1 tbsp honey.",
            "ingredients": "apple, orange, banana, honey"
          },
          {
            "name": "Lunch",
            "meal": "Lentil Soup",
            "time": "13:00",
            "recipe": "Lentil Soup: Cook 1/2 cup lentils with 1/2 onion, 1 carrot, 1 stalk celery, and 2 cups vegetable broth.",
            "ingredients": "lentils, onion, carrot, celery, vegetable broth"
          },
          {
            "name": "Dinner",
            "meal": "Fish Fillet",
            "time": "18:00",
            "recipe": "Fish Fillet: Bake 200g fish fillet with 1 tbsp olive oil, 1/2 lemon juice, and herbs.",
            "ingredients": "fish fillet, olive oil, lemon juice, herbs"
          }
        ]
      },
      {
        "day": "Saturday",
        "meals": [
          {
            "name": "Breakfast",
            "meal": "Pancakes",
            "time": "08:00",
            "recipe": "Pancakes: Mix 1 cup flour, 1 egg, 1 cup milk, and fry on non-stick pan. Serve with 1 tbsp maple syrup.",
            "ingredients": "flour, egg, milk, maple syrup"
          },
          {
            "name": "Lunch",
            "meal": "Caprese Salad",
            "time": "13:00",
            "recipe": "Caprese Salad: Arrange 1/2 cup mozzarella, 1/2 cup cherry tomatoes, and 1 tbsp basil. Drizzle with balsamic vinegar.",
            "ingredients": "mozzarella, cherry tomatoes, basil, balsamic vinegar"
          },
          {
            "name": "Dinner",
            "meal": "Burger",
            "time": "18:00",
            "recipe": "Burger: Grill 1 beef patty. Serve in a whole-grain bun with lettuce, tomato, and 1 tbsp ketchup.",
            "ingredients": "beef patty, whole-grain bun, lettuce, tomato, ketchup"
          }
        ]
      },
      {
        "day": "Sunday",
        "meals": [
          {
            "name": "Breakfast",
            "meal": "Yogurt Parfait",
            "time": "08:00",
            "recipe": "Yogurt Parfait: Layer 1 cup Greek yogurt with 1/2 cup granola and 1/2 cup mixed berries.",
            "ingredients": "Greek yogurt, granola, mixed berries"
          },
          {
            "name": "Lunch",
            "meal": "Chicken Caesar Salad",
            "time": "13:00",
            "recipe": "Chicken Caesar Salad: Mix 100g grilled chicken with lettuce, 1/4 cup croutons, and Caesar dressing.",
            "ingredients": "grilled chicken, lettuce, croutons, Caesar dressing"
          },
          {
            "name": "Dinner",
            "meal": "Veggie Stir-fry",
            "time": "18:00",
            "recipe": "Veggie Stir-fry: Sauté 1/2 cup tofu with 1 bell pepper, 1/2 zucchini, 1 tbsp soy sauce, and 1 tbsp sesame oil.",
            "ingredients": "tofu, bell pepper, zucchini, soy sauce, sesame oil"
          }
        ]
      }
    ]
  },
  "shoppingList": [
    "banana - 3",
    "spinach - 1 cup",
    "Greek yogurt - 3 cups",
    "almond milk - 2 cups",
    "peanut butter - 2 tbsp",
    "quinoa - 1 cup",
    "cherry tomatoes - 2 cups",
    "cucumber - 2",
    "feta cheese - 1/2 cup",
    "olive oil - 5 tbsp",
    "lemon juice - 5 tbsp",
    "chicken breast - 400g",
    "bell pepper - 4",
    "onion - 2",
    "garlic - 5 cloves",
    "soy sauce - 5 tbsp",
    "oats - 1/2 cup",
    "blueberries - 1/4 cup",
    "honey - 4 tbsp",
    "almond butter - 1 tbsp",
    "whole-grain bread - 12 slices",
    "cheddar cheese - 4 slices",
    "tomato soup - 2 cups",
    "whole-wheat pasta - 100g",
    "marinara sauce - 1/2 cup",
    "parmesan cheese - 1/4 cup",
    "basil - 4 tbsp",
    "avocado - 2",
    "chili flakes - 1/4 tsp",
    "tortilla - 1",
    "grilled chicken - 300g",
    "tzatziki - 1 tbsp",
    "minced beef - 100g",
    "taco seasoning - 1 tsp",
    "taco shells - 2",
    "berries - 1/4 cup",
    "granola - 5 tbsp",
    "lettuce - 1",
    "tomato - 3",
    "broccoli - 1 bunch",
    "carrot - 4",
    "brown rice - 1 cup",
    "tofu - 200g",
    "apple - 1",
    "orange - 1",
    "lentils - 1/2 cup",
    "celery - 1 stalk",
    "vegetable broth - 2 cups",
    "fish fillet - 200g",
    "herbs - 2 tbsp",
    "flour - 1 cup",
    "egg - 1",
    "milk - 1 cup",
    "maple syrup - 1 tbsp",
    "mozzarella - 1 cup",
    "balsamic vinegar - 1 tbsp",
    "beef patty - 1",
    "whole-grain bun - 1",
    "ketchup - 1 tbsp",
    "mixed berries - 1/2 cup",
    "croutons - 1/4 cup",
    "Caesar dressing - 1 tbsp",
    "zucchini - 1",
    "sesame oil - 1 tbsp"
  ]
}
# Return the same data back to React
            return JsonResponse({
                'status': 'success',
                'message': 'Meal plan generated successfully',
                'received_data': response
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