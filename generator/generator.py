from faker import Faker
from data.profile_data import ProfileData

faker_en = Faker('en_US')
Faker.seed()


def generated_data():
    yield ProfileData(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name())
