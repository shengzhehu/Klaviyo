from django.core.management.base import BaseCommand, CommandError
from django.core import mail
from django.core.mail import send_mail
from weather.models import Signup
from weather.utils import get_weather_data
import urllib.request as urllib2
from django.conf import settings
from django.template.loader import render_to_string
from the_weather.settings import BASE_DIR
import requests
import json

class Command(BaseCommand):
    help = 'Send email to all subscribers'

    def handle(self, *args, **options):

        subject = ""
        from_mail = settings.EMAIL_HOST_USER
        users = Signup.objects.all()

        for user in users:
            context = {}
            recipient_list = [user.email]
            geography = user.location.split(',')
            city, state = geography[0], geography[1]
            cur_record, tomr_record = get_weather_data(city)

            ''' Populate subject filed'''
            if cur_record['temperature'] - 5.0 >= tomr_record['temperature'] or 'Clear' in cur_record['description']:
                subject = "It's nice out! Enjoy a discount on us."


            elif cur_record['temperature'] + 5.0 <= tomr_record['temperature']:
                subject = "Not so nice out? That's okay, enjoy a discount on us."

            else:
                subject = "Enjoy a discount on us."



            context['city'] = city
            context['state'] = state
            context['weather'] = cur_record['description']
            context['temperature'] = cur_record['temperature']

            html_content = render_to_string(BASE_DIR + '/weather/templates/weather/newsletter.html', context=context).strip()
            # html_content = 'Check out the current weather at your location and enjoy our discount!\n' + 'Temperature: ' + str(cur_record['temperature']) + '\n' + 'Weather: ' + str(cur_record['description'])
            msg = mail.EmailMessage(subject, html_content, from_mail, recipient_list)
            msg.content_subtype = 'html'    # Main content is text/html

            ''' User Django API to sent out emails'''
            if msg.send():
                print ('Successfully sent to ' + str(user.email) + ": " + str(user.location))
            else:
                print ('Unsuccessfully sent to ' + str(user.email) + ": " + str(user.location))
