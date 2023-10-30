

# Dj-AmazonClone

![](https://github.com/Mohamed00Abdelmonem/Dj-AmazonClone/raw/main/static/images/logo.png)

Dj-AmazonClone is a web application built with Django and JavaScript, designed to mimic the core functionality and design of the popular e-commerce platform, Amazon. This project serves as a demonstration of how to create an Amazon-like shopping experience using modern web development technologies. It includes features such as product listings, a shopping cart, user authentication, and a streamlined checkout process.

## Features

- **Product Listings**: Display a wide range of products with details such as product name, price, and images.

- **User Authentication**: Users can create accounts, log in, and log out, enabling personalized shopping experiences and secure transactions.

- **Shopping Cart**: Add products to your cart, update quantities, and proceed to checkout with ease.

- **Search Functionality**: Quickly find the products you're looking for using the search bar.

- **Product Details**: Get more information about each product by clicking on its listing.

- **Checkout Process**: A simplified checkout process where users can provide shipping information and complete their purchase.

- **Order History**: Registered users can view their order history.

## Tech Stack

- **Django**: A Python web framework that provides a robust and scalable foundation for building web applications.

- **HTML/CSS**: For creating the structure and style of the web pages.

- **JavaScript**: Used to enhance the user interface and handle client-side interactions.

- **Bootstrap**: A front-end framework for designing responsive and visually appealing web pages.

- **SQLite**: A lightweight and built-in database management system for data storage.

- **Stripe**: Integrated for handling payments and transactions securely.

## Getting Started

1. Clone this repository to your local machine.

2. Set up a virtual environment to isolate project dependencies:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the migrations to create the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Visit `http://localhost:8000` in your web browser to access the application.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub flow:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and test thoroughly.

4. Create a pull request to merge your changes into the main branch.

5. Provide a clear and detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was created by [Mohamed Abdelmonem](https://github.com/Mohamed00Abdelmonem) as a learning exercise and demonstration of Django web development.

- Thanks to Amazon for the inspiration!

If you have any questions or issues, please don't hesitate to open an [issue](https://github.com/Mohamed00Abdelmonem/Dj-AmazonClone/issues). We hope you find this project educational and useful for your web development journey!


## Project Demo

![](screenshot1.png)




![](screenshot2.png)