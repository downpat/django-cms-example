from django.forms.models import ModelForm
from django.forms.widgets import Select

from .models import TableauView

class TableauViewForm(ModelForm):

    class Meta:
        model = TableauView
        fields = ['site_root', 'workbook_name', 'view_name']
        widgets = {
            'workbook_name': Select(
                choices=(
                    ("GoogleAnalytics", "Google Analytics"),
                    ("AnalyzeSuperstore", "Analyze Superstore"),
                    ("ExecutiveSalesforce", "Executive Salesforce")
                )
            ),
            
            'view_name':  Select(
                choices=(
                    ("OverallTrends", "Overall Trends"),
                    ("ContentAnalysis", "Content Analysis"),
                    ("Overview", "Overview"),
                    ("Product", "Product"),
                    ("Customers", "Customers"),
                    ("SalesSummary", "Sales Summary"),
                    ("LargeDeals", "Large Deals")
                )
            )
        }


        #def __init__(self, *args, **kwargs):
        #    super(TableauViewForm, self).__init__(*args, **kwargs)

        #    self.fields['workbook_name'].widget = Select(
        #        choices=(
        #            "GoogleAnalytics",
        #            "AnalyzeSuperstore",
        #            "ExecutiveSalesforce"
        #        )
        #    )

        #    self.fields['view_name'].widget = Select(
        #        choices=(
        #            "OverallTrends",
        #            "ContentAnalysis",
        #            "Overview",
        #            "Product",
        #            "Customers",
        #            "SalesSummary",
        #            "LargeDeals"
        #        )
        #    )
