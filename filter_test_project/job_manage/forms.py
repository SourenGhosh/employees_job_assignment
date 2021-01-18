from django.forms import ModelForm
from .models import Joballocation

class JobForm(ModelForm):
    class Meta:
        model = Joballocation
        fields='__all__'