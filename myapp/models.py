from django.db import models
from django.utils.safestring import mark_safe


user_type =[('1','user'),
            ('2','buyer'),
            ('3','seller'),
            ('4','rent')]

status = [('0','active'),
          ('1','inactive')]

gender =[('1','male'),
         ('2','female')]


# Create your models here.
class role(models.Model):
    user_typename =models.CharField(max_length=30,choices=user_type)

    def __str__(self):
        return self.user_typename

class user_detail(models.Model):
    u_name= models.CharField(max_length=30)
    u_dp =models.ImageField(upload_to='photo')
    u_gender = models.CharField( max_length=10,choices=gender)
    u_email = models.CharField(max_length=10)
    u_phone = models.IntegerField()
    u_type = models.ForeignKey(role, on_delete=models.CASCADE)
    u_status = models.CharField(max_length=1,choices=status)

    def __str__(self):
        return self.u_name

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.u_dp.url))


    admin_photo.allow_tags = True
#
class furniture_category(models.Model):
    cat_name =models.CharField(max_length=30)
    cat_image=models.ImageField(upload_to='photo')
    category_add= models.DateTimeField()

    def __str__(self):
        return self.cat_name

    def furniture_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.cat_image.url))

    furniture_photo.alters_data = True


class country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name

class state(models.Model):
    country_id = models.ForeignKey(country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return  self.state_name

class city(models.Model):
    state_id = models.ForeignKey(state,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30)


    def __str__(self):
        return self.city_name


class user_address(models.Model):
    u_id = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    building_name= models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    city_name = models.ForeignKey(city,on_delete=models.CASCADE)
    pincode = models.IntegerField()


class feedback_details(models.Model):
    f_title =models.CharField(max_length=30)
    f_description = models.TextField()
    f_by = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    f_on = models.DateTimeField()


class complain_details(models.Model):
    c_name = models.CharField(max_length=30)
    c_detail = models.CharField(max_length=30)
    c_photo = models.ImageField(upload_to='photo')
    c_on = models.DateTimeField()

    def complain_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.c_photo.url))

    complain_photo.allow_tags = True


class brand_table(models.Model):
    brand_table = models.CharField(max_length=30)
    brand_description = models.TextField()
    brand_logo = models.ImageField(upload_to='photo')


    def brand_image(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.brand_logo.url))

    brand_image.allow_tags = True

    def __str__(self):
        return self.brand_table

quntity =[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),
          ('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20')]

class new_furniture(models.Model):
    furniture_name = models.CharField(max_length=30)
    brand_name = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    furniture_description = models.TextField()
    furniture_price = models.IntegerField()
    furniture_image = models.ImageField(upload_to='photo')
    furniture_type =models.ForeignKey(furniture_category, on_delete=models.CASCADE)
    available_quntity = models.CharField(max_length=30,choices=quntity)

    def f_image(self):
      return mark_safe('<img src="{}" width="100"/>'.format(self.furniture_image.url))

    f_image.allow_tags = True

    def __str__(self):
        return self.furniture_name



class old_furniture(models.Model):
        old_furniture_name = models.CharField(max_length=30)
        old_furniture_name_f = models.ForeignKey(brand_table,on_delete=models.CASCADE,default=1)
        old_furniture_description =models.TextField()
        old_furniture_price = models.IntegerField()
        old_furniture_image = models.ImageField(upload_to='photo', null=True)
        old_furniture_type = models.ForeignKey(furniture_category, on_delete=models.CASCADE)
        old_furniture_qunitiy = models.CharField(max_length=30,choices=quntity)

        def __str__(self):
            return self.old_furniture_name

        def old_image(self):
            return mark_safe('<img src="{}" width="100"/>'.format(self.old_furniture_image.url))

        old_image.allow_tags = True


class rent_furniture(models.Model):
    rent_furniture_name = models.CharField(max_length=30)
    rent_brand_name = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    rent_furniture_description = models.TextField()
    rent_furniture_image = models.ImageField(upload_to='photo')
    rent_furniture_type = models.ForeignKey(furniture_category,on_delete=models.CASCADE)
    available_quntity = models.CharField(max_length=30,choices=quntity)

    def rent_furniture_image(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.rent_furniture_image.url))

    rent_furniture_image.allow_tags = True

    def __str__(self):
        return self.rent_furniture_name

class new_furniture_buying(models.Model):
    furniture_id = models.ForeignKey(new_furniture,on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    booking_date = models.DateTimeField()


class old_furniture_buying(models.Model):
    old_furniture_id = models.ForeignKey(old_furniture, on_delete=models.CASCADE)
    user_booking_id = models.ForeignKey(user_detail, on_delete=models.CASCADE)
    old_booking_datetime = models.DateTimeField()


class rent_furniture_order(models.Model):
    rent_furniture = models.ForeignKey(rent_furniture,on_delete=models.CASCADE)
    rent_user_id = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    rent_star_date = models.DateField()
    rent_end_date = models.DateField()
    rent_booking_datetime = models.DateTimeField()

