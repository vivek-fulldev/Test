from django import forms  
from .models import User_creation  
  
class User_creationform(forms.ModelForm):  
    class Meta:  
        model = User_creation  
        fields = "__all__"  