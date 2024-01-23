import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand, Product, ProductImages, Review
from django.contrib.auth.models import User

def seed_brand(n):
    fake = Faker('en_US')

    images = ['images (1).png', 'images (2).png', 'images (3).png', 'images.png', 'LG-Logo.png', 'original-5af3cc59251712aa06fd84eddd195de0.png', 'png-clipart-tesla-logo-tesla-motors-car-tesla-model-s-logo-tesla-angle-text-thumbnail.png', 'png-transparent-blue-hyundai-logo-hyundai-motor-company-car-logo-cars-logo-brands-blue-cdr-text.png', 'png-transparent-nutella-logo-brand-logos-brands-in-colors-icon-thumbnail.png', 'Untitled-design-5.png', 'fashion-logo-3.jpg', 'Nike-Logo-2.jpg', 'nissan-brand-logo-1200x938-1594842787.jpg', 'Toyota-101520210351-1024x640.jpg', '38269.webp', '500851a2ecad04bd32000001.webp', 'coca cola.webp', 'McDonalds_Golden_Arches.svg.webp']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image = f'brands/{images[random.randint(0,17)]}'
        )

    print(f"Seed {n} Brands Successfully")


def seed_product(n):
    fake = Faker()
    images = ['13.png', '14.png', '17.png', '22.png', '27.png', '46.png', '50.png', '8.png', '9.png', '1.jpg', '10.jpg', '11.jpg', '12.jpg', '15.jpg', '16.jpg', 
'2.jpg', '20.jpg', '21.jpg', '28.jpg', '29.jpg', '3.jpg', '30.jpg', '31.jpg', '33.jpg', '34.jpg', '4.jpg', '47.jpg', '48.jpg', '49.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '7.jpg', '23.jpeg', '24.jpeg', '25.jpeg', '26.jpeg', '35.jpeg', '36.jpeg', '37.jpeg', '38.jpeg', '39.jpeg', '40.jpeg', '41.jpeg', '42.jpeg', '43.jpeg', '44.jpeg', '45.jpeg', '18.webp', '19.webp', '32.webp', '5.webp', '6.webp']
    flags = ['new', 'sale', 'feature']
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'products/{images[random.randint(0,55)]}',
            flag = flags[random.randint(0, 2)],
            price = round(random.uniform(20.99, 99.99),2),
            sku = random.randint(1000,100000) ,
            rate = random.randint(0,4) ,
            subtitle = fake.text(max_nb_chars=250),
            description = fake.text(max_nb_chars=2000),
            quantity = random.randint(0,30),
            brand = Brand.objects.get(id=random.randint(1,195)),

        )

    print(f"Seed {n} Products Successfully")


def seed_product_images(n):
    fake = Faker()
    images =['13.png', '14.png', '17.png', '22.png', '27.png', '46.png', '50.png', '8.png', '9.png', '1.jpg', '10.jpg', '11.jpg', '12.jpg', '15.jpg', '16.jpg', 
'2.jpg', '20.jpg', '21.jpg', '28.jpg', '29.jpg', '3.jpg', '30.jpg', '31.jpg', '33.jpg', '34.jpg', '4.jpg', '47.jpg', '48.jpg', '49.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '7.jpg', '23.jpeg', '24.jpeg', '25.jpeg', '26.jpeg', '35.jpeg', '36.jpeg', '37.jpeg', '38.jpeg', '39.jpeg', '40.jpeg', '41.jpeg', '42.jpeg', '43.jpeg', '44.jpeg', '45.jpeg', '18.webp', '19.webp', '32.webp', '5.webp', '6.webp']
    for _ in range(n):
        ProductImages.objects.create(
            product = Product.objects.get(id=random.randint(1,200)),
            image = f'product_images/{images[random.randint(0,55)]}'
        )

    print(f"Seed {n} images in product Successfully")


def seed_reviews(n):
    fake = Faker()
    users = User.objects.all()

    for _ in range(n):
        Review.objects.create(
            user=fake.random_element(users),
            product = Product.objects.get(id=random.randint(1,200)),
            rate = random.randint(0,4) , 
            review = fake.text(max_nb_chars=250), 
        )

    print(f"Seed {n} Reviews Successfully")



def create_users(n):
    fake = Faker()
    for _ in range(n):
        User.objects.create_user(
            username=fake.user_name(),
            password=fake.password()
        )
        print(f"Seed {n} Reviews Successfully")
    

# seed_brand(50)
# seed_product(100)
# seed_product_images(200)
# seed_reviews(100)
# create_users(2)

        