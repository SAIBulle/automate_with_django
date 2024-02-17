from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints Hello World!"

    def handle(self,*args, **kwargs):
        # We write the logic
        # testing git
        self.stdout.write("Hello World!!!")