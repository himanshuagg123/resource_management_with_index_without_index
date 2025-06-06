# data_app/views.py
import time
from django.http import JsonResponse
from data_app.models import LargeData

def query_performance_test(request):
    query_type = request.GET.get('type', 'get')  
    uid = request.GET.get('user_id')

    # Validate user_id parameter
    try:
        uid = int(uid)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid user_id'}, status=400)


    start = time.time()

    try:
        if query_type == 'get':
            obj = LargeData.objects.get(user_id=uid)
            result = {'name': obj.name, 'user_id': obj.user_id}
        else:  # filter query
            obj = LargeData.objects.filter(user_id=uid).values('name', 'user_id','pan_id').first()
            result = obj if obj else {}
    except LargeData.DoesNotExist:
        result = {'error': 'Not found'}
    except LargeData.MultipleObjectsReturned:
        result = {'error': 'Multiple records found'}

    end = time.time()
    duration = round(end - start, 4)

    return JsonResponse({
        'query_type': query_type,
        'user_id': uid,
        'result': result,
        'execution_time_seconds': duration
    })
