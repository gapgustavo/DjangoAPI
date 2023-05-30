from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def math(request):
    if request.method == 'POST':
        try:
            number1 = int(request.POST.get('number1'))
            number2 = int(request.POST.get('number2'))
            operation = request.POST.get('operation')

            if operation in ['sum', '+']:
                result = number1 + number2
            elif operation in ['subtraction', '-']:
                result = number1 - number2
            elif operation in ['division', '/']:
                result = number1 / number2
            elif operation in ['multiplication', 'x', '*']:
                result = number1 * number2
            else:
                return JsonResponse({'error': 'INVALID OPERATION'})

            return JsonResponse({'result': result})
        except (ValueError, ZeroDivisionError):
            return JsonResponse({'error': 'INVALID INPUT'})


def DocPage(request):
    return render(request, "apimath/scanapi-report.html")