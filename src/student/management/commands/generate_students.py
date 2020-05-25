from django.core.management.base import BaseCommand, CommandError

from group.models import Group
from student.models import Student

class Command(BaseCommand):
    help = 'Generate N fake students'

    def add_arguments(self, parser):
        parser.add_argument('num students', default=10, type=int)

    def handle(self, *args, **options):
        num_st = options['num students']
        group = list(Group.objects.all())
        for _ in range(num_st):
            Student.gen_student(group)

        self.stdout.write(self.style.SUCCESS('Successfully generate student "%s"' % num_st))
