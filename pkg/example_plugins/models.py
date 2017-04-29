from django.db import models
from django.conf import settings

from cms.models.pluginmodel import CMSPlugin

class TableauView(CMSPlugin):

    site_root = models.CharField('Site Root',
        blank=False,
        default=settings.TABLEAU_SITE,
        help_text='The site root of the Tableau site hosting the View',
        max_length=50
    )

    workbook_name = models.CharField('Workbook Name',
        blank=False,
        default='',
        help_text='The Workbook that contains the View',
        max_length=50
    )

    view_name = models.CharField('View Name',
        blank=False,
        default='',
        help_text='The name of the View',
        max_length=50
    )
