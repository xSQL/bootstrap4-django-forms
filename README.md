# bootstrap4-django-forms
Custom jinja2 form-widgets with bootstrap4 classes for django(1.11)

# How to Use

1. Clone repo into apps folder of your projects

2. In forms.py put somethink like this:

```python
from django import forms

from bs4_forms.widgets import Select, CheckboxSelectMultiple, TextInput,\
    NumberInput, Textarea, CheckboxInput, RadioSelect, FileInput, EmailInput,\
    URLInput, PasswordInput

from .models import Product


class ProductModelForm(forms.ModelForm):
    """..."""

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'tags': CheckboxSelectMultiple,
            'category': Select(),
            'user': Select(),
            'title': TextInput(),
            'meta_keywords': TextInput(),
            'meta_description': TextInput(),
            'price': NumberInput(),
            'description': Textarea(),
            'is_active': RadioSelect(choices=[
                (True, 'Yes'),
                (False, 'No')
            ])

        }
```

# List of available widgets:


* **JinjaWidgetMixin**
* **FormControlMixin**
* **SelectSelect**
* **TextInput**
* **Textarea**
* **NumberInput**
* **EmailInput**
* **URLInput**
* **PasswordInput**
* **RadioSelect**
* **CheckboxInput**
* **CheckboxSelectMultiple**
* **FileInput**
