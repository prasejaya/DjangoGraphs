from django import forms
from django.forms import TextInput
from django.utils.translation import gettext as _

from .models import *


class GraphForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = ('name', 'title', 'dashboard', 'public', 'selector', 'order')

        help_texts = {
            'name': _('Name of the Graph. Is displayed if no title is given.'),
            'title': _('If not all information contained in the name should be displayed in the graph, set a title.'),
            'dashboard': _('If true, this graph is displayed on the home page.'),
            'public': _('If true, this graph can be seen by everyone.'),
            'selector': _('Choose any number of selectors that should be displayed in this graph.'),
            'order': _('Higher order Graphs are loaded before lower order Graphs. If empty order is defined by the id.'),
        }


class DisplayForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = ('name', 'title', 'dashboard', 'public', 'selector', 'order')

        help_texts = {
            'name': _('Name of the Graph. Is displayed if no title is given.'),
            'title': _('If not all information contained in the name should be displayed in the display, set a title.'),
            'public': _('If true, this display can be seen by everyone.'),
            'dashboard': _('If true, this display is displayed on the home page.'),
            'selector': _('Choose the selector that is displayed by the display.'),
            'order': _('Higher order Displays are loaded before lower order Displays. If empty order is defined by the id.'),
        }


class GraphSelectorForm(forms.ModelForm):
    class Meta:
        model = GraphSelector
        fields = ('name', 'title', 'type', 'instance', 'color', 'order')
        widgets = {'color': TextInput(attrs={'type': 'color'})}
        help_texts = {
            'name': _('Name of the Selector. Is displayed if no title is given.'),
            'title': _('If not all information contained in the name should be displayed in the selector, set a title.'),
            'type': _('Which type of data should be selected.'),
            'instance': _('From which instance should the data be selected.'),
            'color': _('Choose the color that this selector should use.'),
            'order': _('Higher order Graph Selectors are loaded before lower order Graph Selectors. If empty order is defined by the id.'),
        }


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ('name', 'description', 'unit')

        help_texts = {
            'name': _('Name of the Type.'),
            'description': _('At the moment just for personal information about this type.'),
            'unit': _('Unit displayed alongside data of this type.'),
        }


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ('name', 'description')

        help_texts = {
            'name': _('Name of the Instance.'),
            'description': _('At the moment just for personal information about this type.'),
        }


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('title',)

        help_texts = {
            'title': _('Base page title of this website.'),
        }


class TypeChangeForm(forms.Form):
    old_type = forms.ModelChoiceField(Type.objects.all(), label=_('Old type'), help_text=_('All entries associated with this type will be changed to the new type'))
    new_type = forms.ModelChoiceField(Type.objects.all(), label=_('New type'))


class InstanceChangeForm(forms.Form):
    old_instance = forms.ModelChoiceField(Instance.objects.all(), label=_('Old instance'), help_text=_('All entries associated with this instance will be changed to the new instance'))
    new_instance = forms.ModelChoiceField(Instance.objects.all(), label=_('New instance'))
