from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CarsForm
from .models import Cars
from accounts.views import user_login
import os
import pickle


# Create your views here.
def home(request):
  if request.user.is_authenticated:
    history_data = Cars.objects.filter(user=request.user).order_by('-id')
  else:
    history_data = {}

  if request.method == "POST":
    form = CarsForm(request.POST)
    if form.is_valid():
      form = form.cleaned_data
      model_lounge = int(form['model_lounge'])
      model_pop = int(form['model_pop'])
      model_sport = int(form['model_sport'])
      previous_owners = int(form['previous_owners'])
      km = int(form['kilometers'])
      engine_power = int(form['engine_power'])
      age_in_days = int(form['age_in_days'])
      user = request.user
      predicted_price = 0
      data = [[engine_power, age_in_days, km, previous_owners, model_lounge, model_pop, model_sport]]
      # Load trained model
      model_path = os.path.join(settings.BASE_DIR, 'cars','models','cars','model.pkl')
      with open(model_path, "rb") as file:
        model = pickle.load(file)
        predicted_price = model.predict(data)
      if request.user.is_authenticated:
        form_data = Cars.objects.create( model_lounge=model_lounge,model_pop=model_pop,model_sport=model_sport,previous_owners=previous_owners,km=km,engine_power=engine_power,age_in_days=age_in_days, price=predicted_price, user=user)
      
      return render(request, 'cars/price.html',{'indexform':int(predicted_price[0]), 'submitted_data':form, 'history':history_data}) 
  else:
    loginform = user_login(request)
    form = CarsForm()
    return render(request, 'cars/index.html', {'indexform':form, 'history':history_data})
  
def delete(request, id):
  if request.method == 'POST':
    car = get_object_or_404(Cars, id=id)
    car.delete()
    return HttpResponseRedirect(reverse('home'))