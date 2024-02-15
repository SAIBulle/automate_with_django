from django.core.management.base import BaseCommand, CommandParser


# proposed command = python manage.py greeting Raju
# Proposed output = Hi {name}, Good morning
class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('name', type=str, help='Specifies user name')

    def handle(self, *args, **kwargs):
        # We write the logic
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        self.stdout.write(self.style.SUCCESS(greeting))


        # User sai admin