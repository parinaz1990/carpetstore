from django import forms
from .models import Carpet

class CarpetForm(forms.ModelForm):
    class Meta:
        model = Carpet
        fields = ['name', 'size', 'stock', 'description', 'image']
        labels = {
            'name': 'نام فرش',
            'size': 'اندازه',
            'stock': 'موجودی',
            'description': 'توضیحات',
            'image': 'تصویر',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام فرش'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثلاً ۳×۲ متر'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تعداد موجود'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'توضیحاتی درباره طرح، رنگ، ویژگی‌ها و ...'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # راست‌چین کردن تمامی فیلدها
        for field_name, field in self.fields.items():
            field.widget.attrs['dir'] = 'rtl'
            field.widget.attrs['style'] = 'text-align: right;'
