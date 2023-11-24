from django import forms
from .models import CustomUser
from .models import District 
from .models import WaterProduct
from .models import Order
from .models import Address
from .models import OrderAddress
from django.forms.widgets import DateTimeInput
from .models import City
from .models import WorkerProfile
from .models import AddService
from .models import WaterOrder
from .models import Assignment 

class WorkerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name','role']

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['district_name']

class WaterProductForm(forms.ModelForm):
    class Meta:
        model = WaterProduct
        fields = ['product_name','price']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']


class OrderForm(forms.ModelForm):
    

    class Meta:
        model = Order
        fields = ['user', 'product', 'quantity', 'delivery_date_time']

        widgets = {
            'user': forms.HiddenInput(),  # Hidden field for the user
            'delivery_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['mobile_number', 'pincode', 'City_ID', 'street', 'district']

   
    
class OrderAddressForm(forms.ModelForm):
    class Meta:
        model = OrderAddress
        fields = ['order', 'address']




class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        fields = [
            'profile_picture',
            'gender',
            'mobile_number',
            'district',
            
            'bio',
            'services',
            'experience',
            'availability',
            'terms',
        ]

        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}), 
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'services': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'availability': forms.TextInput(attrs={'class': 'form-control'}),
            'terms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = AddService
        fields = ['name', 'price']




from .models import ServiceRequest

class CleaningRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['user', 'service_name', 'length', 'width', 'water_level', 'street', 'city', 'district', 'zip_code', 'request_date_time']
        widgets = {
            'user': forms.HiddenInput(), 
             'service_name': forms.HiddenInput(),  # Hidden field for the user
            'request_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

from .models import UploadedFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['description', 'pdf_file']

    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4}),
    )

    pdf_file = forms.FileField(
        label='Upload PDF Files',
        required=False,
        widget=forms.FileInput(),  # Use the default FileInput widget
    )



class FileEditForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['description']

        
from .models import DrinkingWaterProduct

class DrinkingWaterProductForm(forms.ModelForm):
    class Meta:
        model = DrinkingWaterProduct
        fields = ['name', 'price', 'quantity']


class WaterOrderForm(forms.ModelForm):
    class Meta:
        model = WaterOrder
        fields = ['user','product', 'quantity', 'delivery_date_time', 'city', 'district', 'street','zip_code']  
        widgets = {
            'user': forms.HiddenInput(), 
             'product': forms.HiddenInput(),  # Hidden field for the user
            'delivery_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# class AssignWorkerForm(forms.ModelForm):
#     selected_workers = forms.ModelMultipleChoiceField(
#         queryset=WorkerProfile.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )

#     class Meta:
#         model = AssignedWorker
#         fields = ['selected_workers']

# forms.py
class AssignWorkerForm(forms.ModelForm):
    selected_workers = forms.ModelMultipleChoiceField(
        queryset=WorkerProfile.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Assignment  # Update this to point to the correct model
        fields = ['selected_workers']



from django import forms
from django.forms.widgets import DateInput
from .models import LeaveApplication

class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['start_date', 'end_date', 'reason', 'medical_certificate']

        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date must be equal to or after the start date.")

        return cleaned_data


