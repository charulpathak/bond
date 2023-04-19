from django.core import validators
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import fishbiodiversity_primary, fishbiodiversitysec, fishbioforexoticfish, fishtable, form, habitatparameter


class FormsRegistration(forms.ModelForm):
    class Meta:
        model = form
        fields = ("name_of_river","date","collector","locality","block","district","state","latitude","longitude","altitude")
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'})
        }

class HabitatparameterRegistration(forms.ModelForm):
    class Meta:
        model = habitatparameter
        fields = ("riverid","name_of_river","name_of_the_site","altitude_MSL","habitattype","width","depth","Substratepercent", "boulders","Cobbles","Pebbles","Gravels","Sand","SiltandClay","Aquaticpercent","Floating","Submerged","Emerged","Other","water_color","riparian_vegetation","water_velocity","temp_Air","temp_Water","pH","turbidity") 

class Fishbiodiversity_primaryRegistration(forms.ModelForm):
    class Meta:
        model = fishbiodiversity_primary
        fields = ( "riverid","name_of_river","name_of_sampling_site","date_of_collection","collection_source","sampling_area","duration_of_fishing","time_of_fishing","total_catch","number_of_species" )
        widgets = {
            'date_of_collection' : forms.DateInput(attrs={'type':'date'}),
            'duration_of_fishing' : forms.TimeInput(attrs={'type': 'time'}),
            'time_of_fishing' : forms.TimeInput(attrs={'type': 'time'}),
          

        }      


class FishbiodiversitysecRegistration(forms.ModelForm):
    class Meta:
        model = fishbiodiversitysec
        fields = ("siteid","name_of_fish","largest_size","breeding_information","known_economic","local_name","commercial_value") 


class FishbioforexoticfishRegistration(forms.ModelForm):
    class Meta:
        model = fishbioforexoticfish
        fields = ("siteid","name_of_fish_genus_and_species","local_name","family","total_number","weight","proportion_to_catch","gear_used")   



class FishtableRegistration(forms.ModelForm):
    class Meta:
        model = fishtable
        fields = ("name_of_fish","local_name","family","total_number","weight","proportion_to_catch","gear_used")

                    