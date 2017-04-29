from django.forms.models import ModelForm
from django.forms.widgets import Select

from .models import TableauView
from example_plugins import tableau_api as t_api


def get_workbook_choices():
    names = t_api.get_workbook_names()
    return [(name.replace(' ', ''), name) for name in names]

def get_view_choices():
    names = t_api.get_view_names()
    return [(name.replace(' ', ''), name) for name in names]

class TableauViewForm(ModelForm):

    class Meta:
        model = TableauView
        fields = ['site_root', 'workbook_name', 'view_name']
        widgets = {
            'workbook_name': Select( choices=get_workbook_choices() ),
            'view_name':  Select( choices=get_view_choices() )
        }
