from django import forms

class CheckoutForm(forms.Form):
    addressfield = forms.CharField(widget=forms.Textarea,required=True)
    provice = forms.CharField(required=True)
    city = forms.CharField(required=True)
    town = forms.CharField(required=True)
    postCode = forms.CharField(required=True)
    telephone = forms.CharField(required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput())

    def clean_postCode(self):
        data = self.cleaned_data.get('postCode')
        if not len(data) == 10 or not data.isdigit():
            raise forms.ValidationError('کد پستی باید ده رقمی بوده و شامل حروف نباشد')
        return data

class PromoCodeForm(forms.Form):
    promoCode = forms.CharField(required=False)