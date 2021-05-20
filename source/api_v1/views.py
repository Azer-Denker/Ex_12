import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def task_1_view(request, *args, **kwargs):
    if request.method == 'POST':
        # print(request.body) проверка на то что данные приходят
        if request.body:
            numbers = json.loads(request.body)
            a_number = numbers['A']
            b_number = numbers['B']
            # print(a_number) проверка числа А
            # print(request.path) проверка адресса
            try:
                if request.path.split('/')[2] == 'add':
                    total = int(a_number)+int(b_number)
                    return JsonResponse({'answer': total})
                elif request.path.split('/')[2] == 'subtract':
                    total = int(a_number) - int(b_number)
                    return JsonResponse({'answer': total})
                elif request.path.split('/')[2] == 'multiply':
                    total = int(a_number) * int(b_number)
                    return JsonResponse({'answer': total})
                elif request.path.split('/')[2] == 'divide':
                    if b_number == 0:
                        response = JsonResponse({'error': 'Division by zero!'})
                        return response
                    else:
                        total = int(a_number) / int(b_number)
                        return JsonResponse({'answer': total})
            except ValueError:
                response = JsonResponse({'error': 'Need integer'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response
