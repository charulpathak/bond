from django.contrib import admin

from .models import fishbiodiversity_primary, fishbiodiversitysec, fishbioforexoticfish, fishtable, form, habitatparameter

# Register your models here.
@admin.register(form)
class UserAdmin(admin.ModelAdmin):
    list_display = ('riverid','date','collector','locality','block','district','state','latitude','longitude','altitude',) 


@admin.register(habitatparameter)
class UserAdmin(admin.ModelAdmin):
    list_display = ('siteid','riverid','name_of_river','name_of_the_site','altitude_MSL','habitattype','width','depth','Substratepercent', 'boulders','Cobbles','Pebbles','Gravels','Sand','SiltandClay','Aquaticpercent','Floating','Submerged','Emerged','Other','water_color','riparian_vegetation','water_velocity','temp_Air','temp_Water','pH','turbidity') 


@admin.register(fishbiodiversity_primary)
class UserAdmin(admin.ModelAdmin):
    list_display=('siteid','riverid','name_of_river','name_of_sampling_site','date_of_collection','collection_source','sampling_area','duration_of_fishing','time_of_fishing','total_catch','number_of_species')   



@admin.register(fishbiodiversitysec)
class UserAdmin(admin.ModelAdmin):
    list_display=('riverid','siteid','name_of_fish','largest_size','breeding_information','known_economic','local_name','commercial_value') 


@admin.register(fishbioforexoticfish)
class  UserAdmin(admin.ModelAdmin):
    list_display=('afishid','siteid','name_of_fish_genus_and_species','local_name','family','total_number','weight','proportion_to_catch','gear_used')   


@admin.register(fishtable)
class UserAdmin(admin.ModelAdmin):
    list_display=('fishid','siteid','name_of_fish','local_name','family','total_number','weight','proportion_to_catch','gear_used')







