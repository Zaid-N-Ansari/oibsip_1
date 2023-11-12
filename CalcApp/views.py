from django.shortcuts import render, get_object_or_404, redirect
from .models import CalcHist
from django.core.exceptions import ObjectDoesNotExist

def index(req):
    if req.method == 'POST':
        expr = req.POST.get('display')
        if expr == 'SyntaxError' or expr == 'Error':
            return render(req, 'index.html', {'result':0})
        if isinstance(expr, str):
            try:
                result = eval(expr)
                result = round(result, 18)
                CalcHist.objects.create(hist=expr)
                data = CalcHist.objects.all()
                return render(req, 'index.html', {'result': result, 'prev_hist':data})
            except SyntaxError as e:
                return render(req, 'index.html', {'result': 'Error: {}'.format(str(e))})
    else:
        data = CalcHist.objects.all()
        return render(req, 'index.html', {'result':0, 'prev_hist':data})

def delete(req, hid):
    if req.method == "POST":
        item = get_object_or_404(CalcHist, pk=hid)
        item.delete()
    return redirect('/')
