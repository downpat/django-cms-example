from django.conf import settings
import tableauserverclient as TSC

SERVER = None

def connect():
    tableau_auth = TSC.TableauAuth(
        settings.TABLEAU_USERNAME,
        settings.TABLEAU_PASSWORD, 
        site=settings.TABLEAU_SITE
    )

    server = TSC.Server(settings.TABLEAU_SERVER)
    server.auth.sign_in(tableau_auth)

    return server

def get_workbook_names():
    workbooks = SERVER.workbooks.get()[0]
    return [workbook.name for workbook in workbooks]

def get_view_names():
    views = SERVER.views.get()[0]
    return [view.name for view in views]

SERVER = connect()
