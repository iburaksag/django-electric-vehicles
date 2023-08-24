from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import EVDetailForm, EVSearchForm
from .models import EV


def ev_list_view(request):
    form = EVSearchForm(request.GET) 
    EVs = EV.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        manufacturer = form.cleaned_data.get('manufacturer')
        min_battery_size = form.cleaned_data.get('min_battery_size')
        max_battery_size = form.cleaned_data.get('max_battery_size')
        min_wltp_range = form.cleaned_data.get('min_wltp_range')
        max_wltp_range = form.cleaned_data.get('max_wltp_range')
        min_cost = form.cleaned_data.get('min_cost')
        max_cost = form.cleaned_data.get('max_cost')
        min_power = form.cleaned_data.get('min_power')
        max_power = form.cleaned_data.get('max_power')

        if name:
            EVs = EV.objects.filter(name__icontains=name)
        if manufacturer:
            EVs = EV.objects.filter(manufacturer__icontains=manufacturer)
        if min_battery_size and max_battery_size:
            EVs = EV.objects.filter(battery_size__range=(min_battery_size, max_battery_size))
        if min_battery_size:
            EVs = EV.objects.filter(battery_size__gte=min_battery_size)
        if max_battery_size:
            EVs = EV.objects.filter(battery_size__lte=max_battery_size)        
        if min_wltp_range and max_wltp_range:
            EVs = EV.objects.filter(wltp_range__range=(min_wltp_range, max_wltp_range))
        if min_wltp_range:
            EVs = EV.objects.filter(wltp_range__gte=min_wltp_range)
        if max_wltp_range:
            EVs = EV.objects.filter(wltp_range__lte=max_wltp_range)    
        if min_cost and max_cost:
            EVs = EV.objects.filter(cost__range=(min_cost, max_cost))            
        if min_cost:
            EVs = EV.objects.filter(cost__gte=min_cost)
        if max_cost:
            EVs = EV.objects.filter(cost__lte=max_cost)
        if min_power and max_power:
            EVs = EV.objects.filter(power__range=(min_power, max_power))            
        if min_power:
            EVs = EV.objects.filter(power__gte=min_power)    
        if max_power:
            EVs = EV.objects.filter(power__lte=max_power)        
    
    context = {
        'form' : form,
        'EVs' : EVs,
    }

    return render(request, 'ev/ev_list.html', context)


def ev_details_view(request, id):
    ev = get_object_or_404(EV, pk=id)
    
    if request.method == 'POST':
        form = EVDetailForm(request.POST, instance=ev)
        
        if form.is_valid():
            form.save()
        
            return redirect('ev_list')
    else:
        form = EVDetailForm(instance=ev)

    context = {
        'ev': ev,
        'form': form,
    }
    return render(request, 'ev/ev_details.html', context)


def ev_delete_view(request, id):
    ev = get_object_or_404(EV, id=id)
    
    if request.method == 'POST':
        ev.delete()
        # Redirect to a different page after deletion (e.g., EV list)
        return redirect('ev_list')
    
    context = {'ev': ev}
    return render(request, 'ev/ev_delete.html', context)


def ev_add_view(request):
    if request.method == 'POST':
        form = EVDetailForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('ev_list')  
    else:
        form = EVDetailForm()
    
    context = {'form': form}
    return render(request, 'ev/ev_add.html', context)



def ev_compare_view(request):
    evs = EV.objects.all()
    context = {'evs': evs}
    return render(request, 'ev/ev_compare.html', context)


def ev_comparison_result_view(request):
    ev1_id = request.GET.get('ev1')
    ev2_id = request.GET.get('ev2')
    
    if(ev1_id == ev2_id):
        messages.error(request, 'Please choose two different electric vehicles!')
        return redirect('ev_compare')

    ev1 = EV.objects.get(pk=ev1_id)
    ev2 = EV.objects.get(pk=ev2_id)
    
    attributes = ['battery_size', 'wltp_range', 'cost', 'power']
    comparison_data = []
    
    for attr in attributes:
        ev1_value = getattr(ev1, attr)
        ev2_value = getattr(ev2, attr)
        
        highest_value = max(ev1_value, ev2_value)
        lowest_value = min(ev1_value, ev2_value)
        
        comparison_data.append({
            'attribute': attr,
            'ev1_value': ev1_value,
            'ev2_value': ev2_value,
            'highest_value': highest_value,
            'lowest_value': lowest_value,
        })
    

    context = {
        'ev1': ev1,
        'ev2': ev2,
        'comparison_data': comparison_data,
    }
    return render(request, 'ev/ev_comparison_result.html', context)
