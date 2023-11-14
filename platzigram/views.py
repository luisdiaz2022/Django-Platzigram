"""Platzigram View"""

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a warning."""
    return HttpResponse('Oh hi! Current server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def hi(request):
    """Return as a json a list of strings that we get from the HTTP"""
    numbers_str = request.GET.get('numbers', '')
    numbers = [int(num) for num in numbers_str.split(',') if num.isdigit()]
    sorted_numbers = sorted(numbers)
    return JsonResponse(sorted_numbers, safe=False)