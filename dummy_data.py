import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand, Product, ProductImages, Review
from django.contrib.auth.models import User

def seed_brand(n):
    fake = Faker('en_US')

    images =['1.png', '11.png', '12.png', '13.png', '18.png', '3.png', '4.png', '5.png', '7.png', '9.png', '10.jpg', '16.jpg', '17.jpg', '8.jpg', '14.webp', '15.webp', '2.webp', '6.webp']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image = f'brands/{images[random.randint(0,17)]}'
        )

    print(f"Seed {n} Brands Successfully")


def seed_product(n):
    fake = Faker()

    # for phermancy
    images =  [
    "1.webp",
    "10.webp",
    "11.webp",
    "12 (2).webp",
    "12.webp",
    "13.webp",
    "14.jpg",
    "15.webp",
    "16.jpg",
    "17.jpg",
    "18.png",
    "19.webp",
    "2.webp",
    "20.webp",
    "21.webp",
    "22.webp",
    "23.jpeg",
    "24.webp",
    "25.webp",
    "26.webp",
    "3.webp",
    "4.jpg",
    "4.webp",
    "5.webp",
    "6.webp",
    "7.webp",
    "8.webp",
    "9.webp"
]
    
    medicine_names = [
    "Benylin", "Tussivan-N", "Bronchicum", "Mucosolvan", "Ventolin",
    "Codeine", "Tussidex", "Fluimucil", "Prospan", "Ascoril",
    "Xanax", "Lexotanil", "Cipralex", "Lustral", "Depakine",
    "Tegretol", "Neurontin", "Lyrica", "Gabapentin", "Carbamazepine",
    "Panadol", "Paracetamol", "Brufen", "Cataflam", "Voltaren",
    "Diclofenac", "Aspirin", "Celebrex", "Nurofen", "Ponstan",
    "Augmentin", "Amoxicillin", "Zinnat", "Klaforan", "Tavanic",
    "Ciprocin", "Azithromycin", "Erythromycin", "Flagyl", "Vibramycin",
    "Omeprazole", "Nexium", "Motilium", "Gaviscon", "Buscopan"
]
#     images = ['14.png', '36.png', '40.png', '5.png', '7.png', '70.png', '10.jpg', '19.jpg', 
                # '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '29.jpg', '37.jpg', '38.jpg', '39.jpg', '41.jpg',
                #  '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', 
                # '47.jpg', '48.jpg', '49.jpg', 
                # '5.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg', '58.jpg', '59.jpg', '6.jpg', '60.jpg', '61.jpg',
                #  '62.jpg', '63.jpg', '64.jpg', '65.jpg', '66.jpg', '67.jpg', '68.jpg', '69.jpg', '8.jpg', '9.jpg', '100.jpeg', '101.jpeg', '102.jpeg', '103.jpeg',
                #  '104.jpeg', '105.jpeg', '106.jpeg', '107.jpeg', '108.jpeg', '109.jpeg', '11.jpeg', '110.jpeg', '111.jpeg', 
                # '112.jpeg', '113.jpeg', '114.jpeg', '115.jpeg', '116.jpeg', '117.jpeg', '118.jpeg', '119.jpeg', '12.jpeg', '120.jpeg', '121.jpeg', '122.jpeg', '123.jpeg',
                #  '124.jpeg', '125.jpeg', '126.jpeg', '127.jpeg', '128.jpeg', '129.jpeg', '13.jpeg', '130.jpeg', '131.jpeg', '15.jpeg', '16.jpeg', '17.jpeg', '18.jpeg', '2.jpeg', '25.jpeg',
                #  '26.jpeg', '27.jpeg', '28.jpeg', '3.jpeg', '30.jpeg', '31.jpeg', '32.jpeg', '33.jpeg', '34.jpeg', '35.jpeg', '50.jpeg', '71.jpeg', '72.jpeg', '73.jpeg', '74.jpeg', '75.jpeg',
                #  '76.jpeg', '77.jpeg', '78.jpeg', '79.jpeg', '8.jpeg', '80.jpeg', '81.jpeg', '82.jpeg', '83.jpeg', '84.jpeg', '85.jpeg', '86.jpeg', '87.jpeg', '88.jpeg', '89.jpeg', '90.jpeg', '91.jpeg', 
                # '92.jpeg', '93.jpeg', '94.jpeg', '95.jpeg', '96.jpeg', '97.jpeg', '98.jpeg', '99.jpeg', '18.webp', '19.webp', '32.webp', '5.webp']
   
    flags = ['new', 'sale', 'feature']
    for _ in range(n):
        Product.objects.create(
            name = f"{random.choice(medicine_names)} {random.randint(1, 10000)}",
            image = f'products/{images[random.randint(0,26)]}',
            flag = flags[random.randint(0, 2)],
            price = round(random.uniform(20.99, 99.99),2),
            sku = random.randint(1000,100000) ,
            rate = random.randint(0,4) ,
            subtitle = fake.text(max_nb_chars=250),
            description = fake.text(max_nb_chars=2000),
            quantity = random.randint(0,30),
            brand = Brand.objects.get(id=random.randint(1,5)),

        )

    print(f"Seed {n} Products Successfully")


def seed_product_images(n):
    fake = Faker()
    
    # for phermancy
    images =  [
    "1.webp",
    "10.webp",
    "11.webp",
    "12 (2).webp",
    "12.webp",
    "13.webp",
    "14.jpg",
    "15.webp",
    "16.jpg",
    "17.jpg",
    "18.png",
    "19.webp",
    "2.webp",
    "20.webp",
    "21.webp",
    "22.webp",
    "23.jpeg",
    "24.webp",
    "25.webp",
    "26.webp",
    "3.webp",
    "4.jpg",
    "4.webp",
    "5.webp",
    "6.webp",
    "7.webp",
    "8.webp",
    "9.webp"
]
    
#     images = ['14.png', '36.png', '40.png', '5.png', '7.png', '70.png', '10.jpg', '19.jpg', 
# '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '29.jpg', '37.jpg', '38.jpg', '39.jpg', '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '5.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg', '58.jpg', '59.jpg', '6.jpg', '60.jpg', '61.jpg', '62.jpg', '63.jpg', '64.jpg', '65.jpg', '66.jpg', '67.jpg', '68.jpg', '69.jpg', '8.jpg', '9.jpg', '100.jpeg', '101.jpeg', '102.jpeg', '103.jpeg', '104.jpeg', '105.jpeg', '106.jpeg', '107.jpeg', '108.jpeg', '109.jpeg', '11.jpeg', '110.jpeg', '111.jpeg', '112.jpeg', '113.jpeg', '114.jpeg', '115.jpeg', '116.jpeg', '117.jpeg', '118.jpeg', '119.jpeg', '12.jpeg', '120.jpeg', '121.jpeg', '122.jpeg', '123.jpeg', '124.jpeg', '125.jpeg', '126.jpeg', '127.jpeg', '128.jpeg', '129.jpeg', '13.jpeg', '130.jpeg', '131.jpeg', '15.jpeg', '16.jpeg', '17.jpeg', '18.jpeg', '2.jpeg', '25.jpeg', '26.jpeg', '27.jpeg', '28.jpeg', '3.jpeg', '30.jpeg', '31.jpeg', '32.jpeg', '33.jpeg', '34.jpeg', '35.jpeg', '50.jpeg', '71.jpeg', '72.jpeg', '73.jpeg', '74.jpeg', '75.jpeg', '76.jpeg', '77.jpeg', '78.jpeg', '79.jpeg', '8.jpeg', '80.jpeg', '81.jpeg', '82.jpeg', '83.jpeg', '84.jpeg', '85.jpeg', '86.jpeg', '87.jpeg', '88.jpeg', '89.jpeg', '90.jpeg', '91.jpeg', '92.jpeg', '93.jpeg', '94.jpeg', '95.jpeg', '96.jpeg', '97.jpeg', '98.jpeg', '99.jpeg', '18.webp', '19.webp', '32.webp', '5.webp']
   
    for _ in range(n):
        ProductImages.objects.create(
            product = Product.objects.get(id=random.randint(141,190)),
            image = f'product_images/{images[random.randint(0,26)]}'
        )

    print(f"Seed {n} images in product Successfully")


def seed_reviews(n):
    fake = Faker()
    users = User.objects.all()

    for _ in range(n):
        Review.objects.create(
            user=fake.random_element(users),
            product = Product.objects.get(id=random.randint(141,190)),
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
    

# seed_brand(5)
# seed_product(50)
# seed_product_images(100)
seed_reviews(80)
# create_users(5)

        