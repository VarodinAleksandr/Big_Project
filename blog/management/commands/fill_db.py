from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

from ...models import Post


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('number_users', type=int, choices=range(2, 11),
                            help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_users = kwargs['number_users']
        bulk = []
        for i in range(number_users):
            name = fake.name()
            full_name_list = name.split()
            first_name = full_name_list[0]
            last_name = full_name_list[1]
            username = f'{first_name[0].lower()}{last_name.lower()}'
            email = f'{username}@example.com'
            password = fake.password()
            bulk.append(User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password))
        User.objects.bulk_create(bulk)

        description = '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce faucibus velit mauris. Quisque libero dolor,
        fermentum vitae ultricies a, scelerisque vel sem. Cras facilisis convallis pellentesque. Quisque euismod dolor
        ut efficitur laoreet. Etiam et dictum lacus. Cras viverra ex sagittis, vehicula augue quis, malesuada ante.
         Ut scelerisque lacus nec tortor scelerisque malesuada. Nam ex urna, imperdiet at lorem eget, pharetra
         efficitur sapien. Morbi ac libero eu velit volutpat egestas. Integer ac lorem vehicula, fermentum nisl tempus,
          sollicitudin sapien. Praesent egestas pharetra dignissim. Morbi sed arcu et sem feugiat tincidunt. Fusce
          tempor pellentesque elit eget interdum.

        Nulla facilisi. Integer vestibulum nec tortor vitae hendrerit. Nullam bibendum luctus pulvinar. Vestibulum
        rutrum
        eros in aliquam sagittis. Ut feugiat, ipsum ac ultricies finibus, sapien massa iaculis ante, a sodales odio erat
        vitae purus. Duis molestie scelerisque dui et fermentum. Donec sit amet pretium diam. Ut eu metus bibendum,
         vestibulum
        ante non, tincidunt enim. Praesent rutrum tempor pretium. Vivamus rhoncus tortor neque, id elementum urna
        facilisis et.

        Vestibulum sit amet dui nibh. Phasellus sed lorem ipsum. Sed mattis laoreet ante vel vulputate. Etiam fermentum
        rhoncus turpis, eget commodo mauris faucibus at. Sed vehicula blandit metus, a dictum libero commodo vel.
        Suspendisse
        dapibus condimentum nunc, vitae imperdiet tellus faucibus ut. Pellentesque rutrum, erat sit amet dapibus
        scelerisque,
         mauris est viverra nulla, non faucibus libero tellus et magna. Proin dignissim vestibulum est, quis
         ultrices sem
         volutpat ultricies. Sed aliquam volutpat congue. Nunc eget venenatis arcu. Maecenas accumsan urna vel
         vulputate
         viverra. Curabitur lacinia arcu ut nunc porttitor, vel rutrum ipsum viverra. Praesent tempor lacus neque,
          sed euismod turpis congue quis.

        '''

        short_dscription = 'Lorem ipsum dolor'

        all_users = User.objects.all()
        for user in all_users:
            for i in range(10):
                Post.objects.create(title=f'some title{i}', discription=description, owner=user, is_published=True,
                                    short_discription=short_dscription)
