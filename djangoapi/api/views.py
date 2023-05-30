from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def math(request):
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        operation = request.POST.get('operation')

        number1 = int(number1)
        number2 = int(number2)
        if operation == 'sum' or operation == '+':
            result = number1 + number2
        elif operation == 'subtraction' or operation == '-':
            result = number1 - number2
        elif operation == 'division' or operation == '/':
            result = number1 / number2
        elif operation == 'multiplication' or operation == 'x' or operation == '*':
            result = number1 * number2
        else:
            return JsonResponse({'error': 'INVALID OPERATION'})

        return JsonResponse({'result': result})

def DocPage(request):
    return render(request, "apimath/scanapi-report.html")