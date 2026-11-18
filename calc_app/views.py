from django.shortcuts import render, redirect
from .models import CalculationHistory

def index(request):
    result = ""
    expression = ""
    
    if request.method == "POST":
        if "clear_history" in request.POST:
            CalculationHistory.objects.all().delete()
            return redirect('index')
            
        expression = request.POST.get("expression", "")
        try:
            allowed_chars = "0123456789+-*/.() "
            if all(char in allowed_chars for char in expression) and expression.strip() != "":
                result = str(eval(expression))
                CalculationHistory.objects.create(expression=expression, result=result)
            else:
                result = "Invalid Input"
        except Exception:
            result = "Error"

    history = CalculationHistory.objects.all().order_by('-created_at')[:10]
    
    return render(request, 'calc_app/index.html', {
        'result': result,
        'expression': expression,
        'history': history
    })
