from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

class TableauPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Tableau View")
    render_template = "tableau.html"

    def render(self, context, instance, placeholder):
        context['site_root'] = 'downpatproductions'
        context['workbook_name'] = 'GoogleAnalytics'
        context['view_name'] = 'OverallTrends'

        return context


plugin_pool.register_plugin(TableauPlugin)
