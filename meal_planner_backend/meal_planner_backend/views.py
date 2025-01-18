from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def process_meal_plan(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Process your data here
        # For now, just echo it back
        return JsonResponse({
            'status': 'success',
            'received_data': data
        })
    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})
