from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from django.conf import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
@require_http_methods(["POST"])
def generate_meal_plan(request):
    print("View was called!")  # Basic debug print
    try:
        print("Request headers:", request.headers)  # Print headers
        data = json.loads(request.body)
        print("Received data:", data)  # Debug print

        # Your meal plan generation logic here
        meal_plan = {
            'status': 'success',
            'message': 'Received form data successfully'
        }

        return JsonResponse(meal_plan)
    except Exception as e:
        print("Error:", str(e))  # Debug print
        return JsonResponse({'error': str(e)}, status=500)