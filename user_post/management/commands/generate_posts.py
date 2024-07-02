import random
from django.core.management.base import BaseCommand
from faker import Faker
from user_post.models import Post
from django.core.files.base import ContentFile
import requests

class Command(BaseCommand):
    help = 'Generate fake posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # 10개의 예시 게시물 생성
            title = fake.sentence()
            content = fake.paragraph()
            image_url = fake.image_url()
            image_response = requests.get(image_url)
            image = ContentFile(image_response.content, 'example.jpg')
            Post.objects.create(title=title, content=content, image=image)
            self.stdout.write(self.style.SUCCESS('Successfully generated post'))
