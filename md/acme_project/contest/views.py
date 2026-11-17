from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContestForm
from .models import Contest

def proposal_create(request, pk=None):
    instance = None
    if pk is not None:
        instance = get_object_or_404(Contest, pk=pk)

    is_delete = "/delete/" in request.path
    if is_delete and request.method == 'POST':
        instance.delete()
        return redirect('contest:list')

    form = ContestForm(request.POST or None, instance=instance)
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('contest:list')

    return render(request, 'contest/form.html', context)

def contest_list(request):
    contests = Contest.objects.all()
    return render(request, 'contest/list.html', {'contests': contests})