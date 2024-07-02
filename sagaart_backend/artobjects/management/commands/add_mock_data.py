import datetime

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker

from artobjects.models import Artist, ArtObject, Category, Genre, MaterialArtObject, BaseArtObject, Style
from core.models import City, Image

User = get_user_model()


class Command(BaseCommand):
    help = 'Add mock Artists, Artobjects'

    def __init__(
            self, stdout=None, stderr=None, no_color=False, force_color=False
    ):
        super().__init__(stdout, stderr, no_color, force_color)
        self.artists = list()
        self.artobjects = list()
        self.cities = City.objects.all()
        self.categories = Category.objects.all()
        self.genres = Genre.objects.all()
        self.materials = MaterialArtObject.objects.all()
        self.bases = BaseArtObject.objects.all()
        self.styles = Style.objects.all()
        self.fake = Faker('ru-RU')
        self.amount = None
        self.images = Image.objects.bulk_create(
            Image(
                name=self.fake.text(max_nb_chars=32),
                link=self.fake.url(),
                created_at=datetime.datetime.now()
            ) for _ in range(100)
        )

    def handle(self, *args, **options):
        self.amount = options.get("amount")
        self.add_data()
        self.stdout.write(
            self.style.SUCCESS(
                f"{self.amount} artists and "
                f"{self.amount * 5 } art objects have been added successfully"
            )
        )

    def add_data(self):
        self.add_artists()
        self.add_artobjects()

    def add_arguments(self, parser):
        parser.add_argument(
            "-a",
            "--amount",
            type=int,
            action="store",
            default=1,
            help=":int. Number of users. Default 1",
            required=False,
        )

    def add_artists(self) -> None:
        for _ in range(self.amount):
            date_of_birth = self.fake.date_of_birth(maximum_age=200, minimum_age=16)
            artist = Artist(
                first_name=self.fake.first_name(),
                last_name=self.fake.last_name(),
                description=self.fake.text(max_nb_chars=150),
                sex=self.fake.random_int(1, 2),
                date_of_birth=date_of_birth,
                date_of_death=self.get_date_or_none(date_of_birth),
                personal_style=self.fake.boolean(),
                city_of_birth=self.fake.random_element(self.cities),
                city_of_living=self.fake.random_element(self.cities),
                photo=self.fake.random_element(self.images),
            )
            self.artists.append(artist)
        Artist.objects.bulk_create(self.artists)

    def get_date_or_none(self, date_of_birth) -> datetime.date | None:
        date_of_death = self.fake.date_between_dates(date_of_birth, datetime.date.today())
        if (date_of_birth - date_of_death) > datetime.timedelta(weeks=52*100):
            return date_of_death
        return None

    def add_artobjects(self) -> None:
        ArtObject.objects.bulk_create(
            [
                ArtObject(
                    artist=self.fake.random_element(self.artists),
                    owner=self.create_fake_user(),
                    vendor=self.fake.random_int(1000, 999999),
                    name=self.fake.text(max_nb_chars=32),
                    date_of_creation=self.fake.date_of_birth(maximum_age=180, minimum_age=15),
                    status=self.fake.random_int(1, 3),
                    city_sold=self.fake.random_element(self.cities),
                    category=self.fake.random_element(self.categories),
                    genre=self.fake.random_element(self.genres),
                    width=self.fake.random_int(50, 1000),
                    height=self.fake.random_int(50, 1000),
                    material_art_object=self.fake.random_element(self.materials),
                    base_art_object=self.fake.random_element(self.bases),
                    style=self.fake.random_element(self.styles),
                    unique=self.fake.boolean(),
                    art_investment=self.fake.boolean(),
                    tag_size=self.fake.random_int(1, 4),
                    orientation=self.fake.random_int(1, 2)
                ) for i in range(self.amount * 5)
            ]
        )

    def create_fake_user(self):
        """Метод создает и возвращает сгенерированного пользователяю"""
        user = User(
            email=self.fake.unique.email(),
            password=self.fake.password(),
        )
        user.save()
        return user

