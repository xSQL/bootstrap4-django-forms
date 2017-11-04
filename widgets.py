from django.forms import widgets
from django.utils.module_loading import import_string


class JinjaWidgetMixin(widgets.Widget):
    """
    Set Jinja2 as default widget renderer. 
    Priority to use FORM_RENDERER = 'django.forms.renderers.Jinja2'
    in setting.py, but then forms in bootstrap_admin return error
    """
    def _render(self, template_name, context, renderer=None):
        """
        Forcibly set Jinja2 as default renderer
        """
        renderer_class = import_string('django.forms.renderers.Jinja2')
        return super()._render(
            template_name,
            context,
            renderer=renderer_class()
        )


class FormControlMixin(widgets.Widget):
    """
    Add css class 'form-control'
    """
    def __init__(self, *args, **kwargs):
        """
        Update class attribute
        """
        kwargs.update({'attrs': {
            'class': 'form-control'
            }
        })
        return super().__init__(*args, **kwargs)


class Select(widgets.Select):
    """
    Add css classes "form-control custom-select" to select-tag
    """
    def __init__(self, *args, **kwargs):
        """..."""
        kwargs.update({'attrs': {
            'class': 'form-control custom-select'
            }
        })
        super().__init__(*args, **kwargs)


class TextInput(FormControlMixin, widgets.TextInput):
    """
    Add css class 'form-control' to input-tag
    """
    pass


class Textarea(FormControlMixin, widgets.Textarea):
    """
    Add css class 'form-control' to textarea-tag
    """
    pass


class NumberInput(FormControlMixin, widgets.NumberInput):
    """
    Add css class 'form-control' to input-tag
    """
    pass


class EmailInput(FormControlMixin, widgets.EmailInput):
    """
    Add css class 'form-control' to input[type=email]
    """
    pass


class URLInput(FormControlMixin, widgets.URLInput):
    """
    Add css class 'form-control' to input[type=url]
    """
    pass


class PasswordInput(FormControlMixin, widgets.PasswordInput):
    """
    Add css class 'form-control' to input[type=password]
    """
    pass


class RadioSelect(JinjaWidgetMixin, widgets.RadioSelect):
    """
    Change markup form radio buttons
    """
    template_name = 'bs4/radio.jinja'
    option_template_name = 'bs4/radio_option.jinja'


class CheckboxInput(JinjaWidgetMixin, widgets.CheckboxInput):
    """
    Change markup for input[type=checkbox]
    """
    template_name = 'bs4/checkbox.jinja'
    

class CheckboxSelectMultiple(JinjaWidgetMixin, widgets.CheckboxSelectMultiple):
    """
    CHange markup multi-checkbox
    """
    template_name = 'bs4/checkbox_select.jinja'
    option_template_name = 'bs4/checkbox_option.jinja'


class FileInput(JinjaWidgetMixin, widgets.FileInput):
    """
    Change markup for input[type=file]
    """
    template_name = 'bs4/file.jinja'

class ClearableFileInput(JinjaWidgetMixin, widgets.ClearableFileInput):
    """..."""
    template_name = 'bs4/clearable_file_input.jinja'
