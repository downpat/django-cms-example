from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import TableauView
from .forms import TableauViewForm

class TableauPlugin(CMSPluginBase):
    form = TableauViewForm
    model = TableauView
    name = _("Tableau View")
    render_template = "tableau.html"

    def render(self, context, instance, placeholder):
        context['site_root'] = instance.site_root
        context['workbook_name'] = instance.workbook_name
        context['view_name'] = instance.view_name

        return context


plugin_pool.register_plugin(TableauPlugin)
