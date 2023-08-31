import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand, Product


def seed_brand(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.webp', '6.webp', '7.jpg', '8.png', '9.png', '10.jpg', '11.jpg', '12.jpg', '13.png', '14.png', '15.jpg', '16.jpg', '17.png', '18.webp', '19.webp', '20.jpg', '21.jpg', '22.png', '23.jpeg', '24.jpeg' ,'25.jpeg', '26.jpeg', '27.png', '28.jpg']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brands/{images[random.randint(0,27)]}'
        )

    print(f"Seed {n} Brands Successfully")


def seed_product(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.webp', '6.webp', '7.jpg', '8.png', '9.png', '10.jpg', '11.jpg', '12.jpg', '13.png', '14.png', '15.jpg', '16.jpg', '17.png', '18.webp', '19.webp', '20.jpg', '21.jpg', '22.png', '23.jpeg', '24.jpeg' ,'25.jpeg', '26.jpeg', '27.png', '28.jpg']
    flags = ['new', 'sale', 'feature']
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'products/{images[random.randint(0,27)]}',
            flag = flags[random.randint(0, 2)],
            price = round(random.uniform(20.99, 99.99),2),
            sku = random.randint(1000,100000) ,
            rate = random.randint(0,4) ,
            subtitle = fake.text(max_nb_chars=250),
            description = fake.text(max_nb_chars=2000),
            quantity = random.randint(0,30),
            brand = Brand.objects.get(id=random.randint(1,60)),

        )

    print(f"Seed {n} Products Successfully")



seed_product(1000)