from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
    
		self.fields['first_name'].help_text = None
		self.fields['first_name'].required = True
		self.fields['last_name'].help_text = None
		self.fields['last_name'].required = True
		self.fields['username'].help_text = None
		self.fields['email'].help_text = None
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None

	class Meta:
		model = User
		fields = ('first_name','last_name','username','email', 'password1', 'password2')