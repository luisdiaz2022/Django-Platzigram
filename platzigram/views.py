"""Platzigram View"""

# Django
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a warning."""
    return HttpResponse('Oh hi! Current server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def sorted_numbers(request):
    #My Solution
    # """Return Json as list of strings that we get from the HTTP"""
    # numbers_str = request.GET.get('numbers', '')
    # numbers = [int(num) for num in numbers_str.split(',') if num.isdigit()]
    # sorted_numbers = sorted(numbers)
    # return JsonResponse(sorted_numbers, safe=False)

    """Return a JSON response with sorted integers"""
    numbers = [int(num) for num in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! welcome to Platzigram'.format(name)

    return HttpResponse(message)