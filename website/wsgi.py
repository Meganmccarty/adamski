import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application


project_folder = os.path.expanduser('~/davidadamski.pythonanywhere.com')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

application = get_wsgi_application()
