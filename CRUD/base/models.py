from django.db import models

#Font https://stackoverflow.com/questions/10539026/how-to-create-a-django-floatfield-with-maximum-and-minimum-limits
class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class Target(models.Model):
   name = models.CharField(max_length=100)
   latitude = MinMaxFloat(min_value=-180.0, max_value=180.0)
   longitude = MinMaxFloat(min_value=-90.0, max_value=90.0)
   expiration = models.DateTimeField()