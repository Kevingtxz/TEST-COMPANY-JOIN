from .models import Target
from django.forms import ModelForm

class TargetForm(ModelForm):
    class Meta:
        model = Target
        fields = "__all__"