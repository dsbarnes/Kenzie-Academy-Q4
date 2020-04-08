from django.core.management.base import BaseCommand, CommandError
from api.models import ShoeType, ShoeColor

class Command(BaseCommand):
    # help = 'adds colors and styles to the ShoeColor and ShoeStyle tables'

    # def add_arguments(self, parser):
    #     pass

    def handle(self, *args, **options):

        ShoeTypes = ['boot', 'sneaker', 'sandal', 'dress', 'other']
        ShoeColors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'white', 'black']

        for item in ShoeTypes:
            ShoeColor.objects.create(color_name=item)

        for item in ShoeColors:
            ShoeType.objects.create(style=item)