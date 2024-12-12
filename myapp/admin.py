from django.contrib import admin
from  .models import role , user_detail,country,furniture_category,state,city,user_address,feedback_details,complain_details,brand_table,new_furniture,old_furniture,rent_furniture,new_furniture_buying,old_furniture_buying,rent_furniture_order


# Register your models here.

class showrole(admin.ModelAdmin):
    list_display = ("id","user_typename")

admin.site.register(role,showrole)

class showuser_detail(admin.ModelAdmin):
    list_display = ('u_name','u_dp','u_gender','u_email','u_phone','u_type','u_status')

admin.site.register(user_detail,showuser_detail)


class showfurniture(admin.ModelAdmin):
    list_display = ('cat_name','cat_image','category_add')

admin.site.register(furniture_category,showfurniture)

class showcountry(admin.ModelAdmin):
    list_display = ('id','country_name')

admin.site.register(country,showcountry)

class showstate(admin.ModelAdmin):
    list_display = ('country_id','state_name')

admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):
    list_display = ('state_id','city_name')

admin.site.register(city,showcity)


class show_user_address(admin.ModelAdmin):
    list_display = ('u_id','building_name','street_name','city_name','pincode')

admin.site.register(user_address,show_user_address)

class showfeedback(admin.ModelAdmin):
    list_display = ('f_title','f_description','f_by','f_on')

admin.site.register(feedback_details,showfeedback)

class showcomplain(admin.ModelAdmin):
    list_display = ('c_name','c_detail','c_photo','c_on')

admin.site.register(complain_details,showcomplain)


class show_brand_table(admin.ModelAdmin):
    list_display = ('brand_table','brand_description','brand_logo')

admin.site.register(brand_table,show_brand_table)


class show_new_furniture(admin.ModelAdmin):
    list_display = ('furniture_name','brand_name','furniture_description','furniture_price','furniture_price','furniture_image','furniture_type','available_quntity')

admin.site.register(new_furniture,show_new_furniture)


class show_old_furniture(admin.ModelAdmin):
    list_display = ('old_furniture_name','old_furniture_name_f','old_furniture_description','old_furniture_price','old_furniture_image','old_furniture_type','old_furniture_qunitiy')

admin.site.register(old_furniture,show_old_furniture)


class show_rent_furniture(admin.ModelAdmin):
    list_display = ('rent_furniture_name','rent_brand_name','rent_furniture_description','rent_furniture_image','rent_furniture_type','available_quntity')

admin.site.register(rent_furniture,show_rent_furniture)

class show_new_furniture_buying(admin.ModelAdmin):
    list_display = ('furniture_id','user_id','booking_date')

admin.site.register(new_furniture_buying,show_new_furniture_buying)

class show_old_furniture_buying(admin.ModelAdmin):
    list_display = ('old_furniture_id','user_booking_id','old_booking_datetime')

admin.site.register(old_furniture_buying,show_old_furniture_buying)

class show_rent_furniture_order(admin.ModelAdmin):
    list_display = ('rent_furniture','rent_user_id','rent_star_date','rent_end_date','rent_booking_datetime')
