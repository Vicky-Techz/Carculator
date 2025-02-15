from django import forms

class CarsForm(forms.Form):
  MODELS = {
    "":"",
    "001": "Lounge",
    "010": "Pop",
    "100": "Sports",
}
  model = forms.ChoiceField(required=True, choices=MODELS)
  previous_owners	= forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'text', 'inputmode':'numeric','placeholder':'eg:1'}))
  kilometers = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'text', 'inputmode':'numeric'}))
  engine_power = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'text', 'inputmode':'numeric'}))
  age_in_days = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'text', 'inputmode':'numeric'}))

  def clean(self):
    cleaned_data = super().clean()
    if cleaned_data:
      self.cleaned_data['model_lounge']	= self.cleaned_data['model'][2]
      self.cleaned_data['model_pop']	= self.cleaned_data['model'][1]
      self.cleaned_data['model_sport'] = self.cleaned_data['model'][0]


