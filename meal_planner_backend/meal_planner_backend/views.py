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
    diet = data.get('diet')
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
                                },
                                {
                                    "name": "Dinner",
                                    "time": "18:00",
                                    "meal": "Name of the meal",
                                    "recipe": "Step-by-step instructions here.",
                                    "ingredients": "ingredient1, ingredient2"
                                }
                            ]
                        },
                        {
                            "day": "Tusday",
                            "meals": [
                                {
                                    "name": "Breakfast",
                                    "time": "08:00",
                                    "meal": "Name of the meal",
                                    "recipe": "Step-by-step instructions here.",
                                    "ingredients": "ingredient1, ingredient2"
                                },
                                {
                                    "name": "Dinner",
                                    "time": "18:00",
                                    "meal": "Name of the meal",
                                    "recipe": "Step-by-step instructions here.",
                                    "ingredients": "ingredient1, ingredient2"
                                }
                            ]
                        },
                        {
                            "day": "Sunday",
                            "meals": [
                                {
                                    "name": "Breakfast",
                                    "time": "08:00",
                                    "meal": "Name of the meal",
                                    "recipe": "Step-by-step instructions here.",
                                    "ingredients": "ingredient1, ingredient2"
                                },
                                {
                                    "name": "Dinner",
                                    "time": "18:00",
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
    instructions = ["Przygotuj mi plan żywieniowy i jedną listę zakupów na cały tydzień oraz rozpiskę co kiedy mam ugotować i przepisy."]

    if meals_per_day:
        instructions.append(f"Ilość posiłków dziennie: {meals_per_day}.")
    if calories_per_day:
        instructions.append(f"Dziennie jem {calories_per_day} kcal.")
    if cooking_days and cooking_time:
        instructions.append(f"Czas na gotowanie obiadów mam w {cooking_days} i mogę przeznaczyć na to {cooking_time} minut dziennie.")
    if budget:
        instructions.append(f"Mój budżet wynosi: {budget} zł.")
    if diet:
        instructions.append(f"Moja dieta to: {diet}.")    
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
    instructions.append("Nie dodawaj żadnych dodatkowych komentarzy po udzieleniu odpwoiedzi w formacie JSON ani w samej jego strukturze. "
                        "Pisz po Polsku. W liście zakupów trzymaj się narzuconego formatu")
    return " ".join(instructions)

@csrf_exempt
def process_meal_plan(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            prompt = create_prompt(data)

            # Testowy JSON (docelowo ma taki powstawać z chata)
            API_KEY = read_key("key.txt")
            response = generate_meal_plan(API_KEY, prompt)
            response = json.loads(response.removeprefix("```json").removesuffix("```"))
            # print(response)
            # response = { "mealPlan": { "days": [ { "day": "Monday", "meals": [ { "name": "Breakfast", "time": "08:00", "meal": "Owsianka z owocami i orzechami", "recipe": "1. Zagotuj 1 szklankę wody i 1 szklankę mleka w garnku. 2. Dodaj 100g płatków owsianych i gotuj na małym ogniu przez 5 minut. 3. Dodaj pokrojone w kostkę jabłko, garść borówek i łyżkę orzechów włoskich. 4. Gotuj przez kolejne 2-3 minuty, aż owoce lekko zmiękną. 5. Podaj z miodem lub syropem klonowym.", "ingredients": "płatki owsiane, mleko, jabłko, borówki, orzechy włoskie, miód" }, { "name": "Lunch", "time": "13:00", "meal": "Sałatka z tuńczykiem i fasolą", "recipe": "1. Odsącz jedną puszkę tuńczyka w sosie własnym i jedną puszkę czerwonej fasoli. 2. Wymieszaj je w dużej misce. 3. Dodaj pokrojone w kostkę pomidory, ogórka i czerwoną cebulę. 4. Dodaj sok z połowy cytryny, 2 łyżki oliwy z oliwek i dopraw solą i pieprzem. 5. Podawaj schłodzone.", "ingredients": "tuńczyk w puszce, czerwona fasola, pomidory, ogórek, czerwona cebula, cytryna, oliwa z oliwek" }, { "name": "Dinner", "time": "18:00", "meal": "Makaron z warzywami i sosem pomidorowym", "recipe": "1. Ugotuj 200g makaronu pełnoziarnistego zgodnie z instrukcją na opakowaniu. 2. Na patelni rozgrzej 2 łyżki oliwy i podsmaż pokrojoną w plastry cukinię, paprykę i marchewkę przez około 5 minut. 3. Dodaj przeciśnięty przez praskę czosnek, 400g pomidorów z puszki i gotuj na wolnym ogniu przez 10 minut. 4. Dodaj ugotowany makaron i wymieszaj. 5. Dopraw solą, pieprzem i bazylią.", "ingredients": "makaron pełnoziarnisty, cukinia, papryka, marchew, czosnek, pomidory z puszki, oliwa z oliwek, bazylia" } ] }, { "day": "Tuesday", "meals": [ { "name": "Breakfast", "time": "08:00", "meal": "Jajecznica z pomidorami i szpinakiem", "recipe": "1. Rozgrzej łyżkę masła na patelni. 2. Dodaj pokrojone w kostkę 2 pomidory i garść świeżego szpinaku, smaż przez 3-4 minuty. 3. Dodaj 3 rozmącone jajka i smaż, mieszając, aż jajka się zetną. 4. Dopraw solą, pieprzem i ulubionymi ziołami.", "ingredients": "jajka, pomidory, szpinak, masło" }, { "name": "Lunch", "time": "13:00", "meal": "Krem z dyni i marchewki", "recipe": "1. Obierz i pokrój w kostkę dynię (500g) i 2 marchewki. 2. Podsmaż je na łyżce masła w garnku przez około 5 minut. 3. Dodaj 1 litr bulionu warzywnego i gotuj 20 minut. 4. Zblenduj zupę na gładki krem, dopraw solą, pieprzem i gałką muszkatołową.", "ingredients": "dynia, marchew, bulion warzywny, masło, gałka muszkatołowa" }, { "name": "Dinner", "time": "18:00", "meal": "Curry z ciecierzycą", "recipe": "1. Na patelni rozgrzej 2 łyżki oliwy. 2. Podsmaż pokrojoną cebulę, czosnek i imbir przez 3 minuty. 3. Dodaj 1 łyżkę curry i smaż chwilę. 4. Dodaj puszkę ciecierzycy, 400ml mleka kokosowego i dusz 15 minut. 5. Dopraw solą i podawaj z ryżem.", "ingredients": "cebulę, czosnek, imbir, curry, ciecierzyca, mleko kokosowe, ryż" } ] }, { "day": "Wednesday", "meals": [ { "name": "Breakfast", "time": "08:00", "meal": "Grzanki z awokado i pomidorem", "recipe": "1. Podpiecz 2 kromki chleba pełnoziarnistego w tosterze. 2. Nałóż na nie rozgniecione awokado, pokrojonego pomidora i posiekaną bazylię. 3. Skrop oliwą, dopraw solą i pieprzem.", "ingredients": "chleb pełnoziarnisty, awokado, pomidor, bazylia, oliwa" }, { "name": "Lunch", "time": "13:00", "meal": "Gulasz warzywny z ziemniakami", "recipe": "1. Pokrój w kostkę 3 ziemniaki, 2 marchewki, paprykę i cebulę. 2. Podsmaż warzywa na 2 łyżkach oliwy przez 10 minut. 3. Dodaj 1 szklankę bulionu warzywnego, łyżkę koncentratu pomidorowego i gotuj przez 15 minut. 4. Dopraw solą, pieprzem i papryką wędzoną.", "ingredients": "ziemniaki, marchew, papryka, cebula, bulion warzywny, koncentrat pomidorowy, papryka wędzona" }, { "name": "Dinner", "time": "18:00", "meal": "Risotto z pieczarkami i groszkiem", "recipe": "1. Podsmaż pokrojoną cebulę i czosnek na oliwie. 2. Dodaj 200g ryżu arborio i smaż przez 2 minuty. 3. Dodawaj stopniowo 750ml bulionu warzywnego, mieszając, aż ryż wchłonie cały płyn. 4. Dodaj 200g pokrojonych pieczarek i 100g mrożonego groszku. 5. Gotuj do miękkości składników. 6. Dopraw solą, pieprzem i parmezanem.", "ingredients": "ryż arborio, pieczarki, groszek, cebula, czosnek, bulion warzywny, parmezan" } ] }, { "day": "Thursday", "meals": [ { "name": "Breakfast", "time": "08:00", "meal": "Smoothie bananowo-szpinakowe", "recipe": "1. Zblenduj 2 banany z garścią szpinaku, 250ml mleka roślinnego i łyżką masła orzechowego. 2. Podawaj natychmiast.", "ingredients": "banan, szpinak, mleko roślinne, masło orzechowe" }, { "name": "Lunch", "time": "13:00", "meal": "Wrap z falafelem i warzywami", "recipe": "1. Podgrzej 2 placki tortilla. 2. Nałóż na nie hummus, pokrojone ogórki, pomidory i czerwoną cebulę. 3. Dodaj wcześniej przygotowane falafele i zawijaj.", "ingredients": "tortilla, hummus, ogórek, pomidor, czerwona cebula, falafel" }, { "name": "Dinner", "time": "18:00", "meal": "Chili sin carne", "recipe": "1. Podsmaż cebulę, czosnek i paprykę na oliwie przez 5 minut. 2. Dodaj 2 puszki czerwonej fasoli, 1 puszkę pomidorów, 1 łyżkę koncentratu pomidorowego i przyprawy: kumin, chili w proszku, oregano. 3. Dusz przez 20 minut. 4. Podawaj z pieczywem.", "ingredients": "czerwona fasola, pomidory z puszki, cebula, czosnek, papryka, koncentrat pomidorowy, pieczywo" } ] }, { "day": "Friday", "meals": [ { "name": "Breakfast", "time": "08:00", "meal": "Placki owsiane z owocami", "recipe": "1. Zmiksuj 200g płatków owsianych na mąkę. 2. Dodaj 2 jajka, 200ml mleka, łyżkę cukru i wymieszaj na gładką masę. 3. Smaż na patelni bez tłuszczu. 4. Podawaj z jogurtem i owocami.", "ingredients": "płatki owsiane, jajka, mleko, cukier, jogurt, owoce" }, { "name": "Lunch", "time": "13:00", "meal": "Makaron z pesto bazyliowym", "recipe": "1. Ugotuj makaron pełnoziarnisty (200g) zgodnie z instrukcją na opakowaniu. 2. Wymieszaj z 3 łyżkami pesto bazyliowego i pokrojonymi suszonymi pomidorami. 3. Dopraw solą i pieprzem.", "ingredients": "makaron pełnoziarnisty, pesto bazyliowe, suszone pomidory" }, { "name": "Dinner", "time": "18:00", "meal": "Tarta warzywna", "recipe": "1. Przygotuj ciasto kruche z mąki, masła i soli. 2. Pokrój cukinię, brokuły i paprykę. 3. Wymieszaj z 2 jajkami, śmietaną, startym serem. 4. Wyłóż formę ciastem, dodaj farsz i piecz 30 minut w 180°C.", "ingredients": "mąka, masło, cukinia, brokuły, papryka, jajka, śmietana, ser" } ] }, { "day": "Saturday", "meals": [ { "name": "Breakfast", "time": "08:00", "meal": "Jogurt z granolą i owocami", "recipe": "1. Do miski wlej 200ml jogurtu naturalnego. 2. Dodaj garść granoli i pokrojone owoce sezonowe. 3. Skrop miodem.", "ingredients": "jogurt naturalny, granola, owoce sezonowe, miód" }, { "name": "Lunch", "time": "13:00", "meal": "Zupa minestrone", "recipe": "1. Posiekaj cebulę, czosnek, marchew, seler i pomidory. 2. Podsmaż na oliwie przez 10 minut. 3. Dodaj 1 litr bulionu warzywnego, 200g fasoli i makaronu małego. 4. Gotuj przez 20 minut.", "ingredients": "cebula, czosnek, marchew, seler, pomidory, bulion warzywny, fasola, makaron" }, { "name": "Dinner", "time": "18:00", "meal": "Zapiekanka z bakłażanem i serem feta", "recipe": "1. Pokrój 2 bakłażany w plastry, posól i odstaw na 10 minut. 2. Opłucz i osusz plastry. 3. Podsmaż je na oliwie po 2 minuty z każdej strony. 4. W naczyniu żaroodpornym układaj warstwami bakłażana, pokrojone pomidory i fetę. 5. Zapiekaj 30 minut w 180°C.", "ingredients": "bakłażan, pomidory, ser feta, oliwa" } ] }, { "day": "Sunday", "meals": [ { "name": "Breakfast", "time": "08:00", "meal": "Omlet z warzywami", "recipe": "1. Roztrzep 3 jajka, dodaj sól i pieprz. 2. Na patelni podsmaż cebulę, paprykę i pieczarki na oliwie. 3. Dodaj jajka, smaż omlet do ścięcia.", "ingredients": "jajka, cebula, papryka, pieczarki, oliwa" }, { "name": "Lunch", "time": "13:00", "meal": "Kasza kuskus z warzywami", "recipe": "1. Zalej 200g kuskusu wrzącym bulionem warzywnym i odstaw pod przykryciem na 10 minut. 2. Dodaj pokrojone w kostkę pomidory, ogórki, paprykę i czerwoną cebulę. 3. Skrop oliwą z oliwek i dopraw według smaku.", "ingredients": "kuskus, bulion warzywny, pomidory, ogórek, papryka, cebula, oliwa" }, { "name": "Dinner", "time": "18:00", "meal": "Pizza domowa z warzywami", "recipe": "1. Wyrob ciasto na pizzę z mąki, wody, drożdży i soli. 2. Nałóż sos pomidorowy, pokrojone oliwki, paprykę, cebulę i starty ser. 3. Piecz w 220°C przez 15 minut.", "ingredients": "mąka, woda, drożdże, sos pomidorowy, oliwki, papryka, cebula, ser" } ] } ] }, "shoppingList": [ "płatki owsiane - 200g", "mleko - 2 litry", "jabłko - 1 sztuka", "borówki - 100g", "orzechy włoskie - 50g", "miód - 150g", "tuńczyk w puszce - 1 puszka", "czerwona fasola - 2 puszki", "pomidory - 1kg", "ogórek - 1 sztuka", "czerwona cebula - 3 sztuki", "cytryna - 2 sztuki", "oliwa z oliwek - 500ml", "makaron pełnoziarnisty - 400g", "cukinia - 2 sztuki", "papryka - 4 sztuki", "marchew - 4 sztuki", "czosnek - 1 główka", "pomidory z puszki - 2 puszki", "bazylia - pęczek", "jajka - 12 sztuk", "szpinak - 200g", "masło - 250g", "dynia - 500g", "bulion warzywny - 2 litry", "gałka muszkatołowa - 20g", "cebulę - 4 sztuki", "imbir - 50g", "curry - 20g", "ciecierzyca - 1 puszka", "mleko kokosowe - 1 puszka", "ryż - 200g", "chleb pełnoziarnisty - 1 bochenek", "awokado - 2 sztuki", "bazylia - pęczek", "tortilla - 4 sztuki", "hummus - 200g", "falafel - 200g", "chili - 20g", "oregano - 20g", "pieczywo - 1 bochenek", "mąka - 1kg", "cukier - 250g", "jogurt naturalny - 1kg", "owoce sezonowe - 500g", "granola - 250g", "makaron - 500g", "pesto bazyliowe - 150g", "pomidory suszone - 100g", "mleko roślinne - 1 litr", "masło orzechowe - 200g", "bulion warzywny - 1 litr", "fasola - 1 puszka", "makaron - 200g", "bakłażan - 2 sztuki", "ser feta - 200g", "oliwa - 500ml", "kuskus - 200g", "oliwki - 100g", "sos pomidorowy - 200g", "ser - 300g", "drożdże - 50g" ] }
            print(type(response))
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