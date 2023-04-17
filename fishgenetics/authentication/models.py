from django.db import models


# Create your models here.
class form(models.Model):
     riverid=models.BigAutoField(primary_key=True,null=False)
     name_of_river=models.CharField(max_length=200)
     date=models.DateField()
     collector=models.CharField(max_length=200)
     locality=models.CharField(max_length=200)
     block=models.CharField(max_length=200)
     district=models.CharField(max_length=200)
     state=models.CharField(max_length=200)
     latitude=models.IntegerField()
     longitude=models.IntegerField()
     altitude=models.IntegerField() 
  

     
     
 


class habitatparameter(models.Model):
    siteid=models.BigAutoField(primary_key=True)
    riverid=models.ForeignKey(form, on_delete=models.CASCADE)
    name_of_river=models.CharField(max_length=200)
    name_of_the_site=models.CharField(max_length=200)
    altitude_MSL=models.IntegerField()
    habitattype=models.CharField(max_length=200)
    width=models.IntegerField()
    depth=models.IntegerField()
    Substratepercent=models.IntegerField()
    boulders=models.CharField(max_length=200)
    Cobbles=models.CharField(max_length=200)
    Pebbles=models.CharField(max_length=200)
    Gravels=models.CharField(max_length=200)
    Sand=models.CharField(max_length=200)
    SiltandClay=models.CharField(max_length=200)
    Aquaticpercent=models.IntegerField()
    Floating=models.CharField(max_length=200)
    Submerged=models.CharField(max_length=200)
    Emerged=models.CharField(max_length=200)
    Other=models.CharField(max_length=200)
    water_color=models.CharField(max_length=200)
    riparian_vegetation=models.IntegerField()
    water_velocity=models.IntegerField()
    temp_Air=models.IntegerField()
    temp_Water=models.IntegerField()
    pH =models.IntegerField()
    turbidity=models.IntegerField()
  

    




class fishbiodiversity_primary(models.Model):
    siteid=models.BigAutoField(primary_key=True)
    riverid=models.ForeignKey(form, on_delete=models.CASCADE)
    name_of_river=models.CharField(max_length=200)
    name_of_sampling_site=models.CharField(max_length=200)
    date_of_collection=models.DateField()
    collection_source=models.CharField(max_length=200)
    sampling_area=models.IntegerField()
    duration_of_fishing=models.DateTimeField()
    time_of_fishing=models.DateTimeField()
    total_catch=models.IntegerField()
    number_of_species=models.IntegerField()
  

    



class fishbiodiversitysec(models.Model):
    riverid=models.BigAutoField(primary_key=True)
    siteid=models.ForeignKey(fishbiodiversity_primary,on_delete=models.CASCADE)
    name_of_fish=models.CharField(max_length=200)
    largest_size=models.IntegerField()
    breeding_information=models.CharField(max_length=200)
    known_economic=models.IntegerField()
    local_name=models.CharField(max_length=200)
    commercial_value=models.CharField(max_length=200)
  

    

class fishbioforexoticfish(models.Model):
    afishid=models.BigAutoField(primary_key=True)
    siteid=models.ForeignKey(fishbiodiversity_primary,on_delete=models.CASCADE)
    name_of_fish_genus_and_species=models.CharField(max_length=200)
    local_name=models.CharField(max_length=200)
    family=models.CharField(max_length=200)
    total_number=models.IntegerField()
    weight=models.IntegerField()
    proportion_to_catch=models.IntegerField()
    gear_used=models.IntegerField()
   

    

class fishtable(models.Model):
    fishid=models.BigAutoField(primary_key=True)
    siteid=models.ForeignKey(fishbiodiversity_primary,on_delete=models.CASCADE)
    name_of_fish=models.CharField(max_length=200)
    local_name=models.CharField(max_length=200)
    family=models.CharField(max_length=200)
    total_number=models.IntegerField()
    weight=models.IntegerField()
    proportion_to_catch=models.IntegerField()
    gear_used=models.IntegerField()  
   
   