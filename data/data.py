from random import randint
import os


class Data:
    email = 'vladimir.kuznetsov@white-test.com'
    password = 'Automation@test2023'
    invalid_email = 'something@gmail.com'
    invalid_password = '123123123'
    link = 'https://readyhubb.com/'
    invalid_login_message = 'Wrong login or password'
    border_color_invalid_login = '#f36a46'
    location = 'Atlanta'

    image_formats = ['jpg', 'png']
    path = fr'C:\QA courses\Python\ReadyHubb-Python-Tests\profile_images\valid\{randint(1, 5)}.{image_formats[randint(0,1)]}'
