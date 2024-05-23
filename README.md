# Trendyol Product Scraper and Recommender

## Project Overview

This project involves creating a web application that scrapes product data from Trendyol, stores it in a SQLite database, and provides a web interface for users to view and interact with the data. The project includes a recommendation system based on TF-IDF and cosine similarity and uses Flask for the web interface.

## Features

1. **Data Scraping**: The project uses Selenium to scrape product data from Trendyol. The `scrape_trendyol` function takes a URL, navigates to the page, extracts product information from product cards, and returns a list of product details.

2. **Database Operations (SQLite)**: The project uses SQLite as the database management system. A `products` table with columns `(id, brand, name, price, image, link)` is defined using SQLAlchemy, and the `add_products_to_database` function is used to add products to the database.

3. **Web Interface (Flask)**: A web application is developed using Flask with several routes:
   - `index`: Home page displaying products.
   - `product_detail`: Detailed view of a single product.
   - `add_to_history`: Adds a viewed product to the user's history.
   - `history`: Displays previously viewed products.
   - `get_product_recommendations`: Provides product recommendations based on user interactions.

4. **Recommendation System**: A content-based recommendation system using TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity is implemented in the `machinelearning.py` module. Recommendations are fetched and displayed on the web page based on user interactions.

5. **API Integration**: An API integration is added using Flask-RESTful. The `GetRecommendationsResource` class provides an endpoint for fetching recommendations in JSON format, allowing interaction with the project via an API.

## Usage

1. Go to the home page (`index`) to view products.
2. Click on a product to see its detailed information (`product_detail`).
3. Viewed products will be added to the user's history (`history`).
4. Get recommendations based on user interactions (`get_product_recommendations`).

## API Endpoint

- **Get Recommendations**: `/api/get_recommendations/<int:product_id>` - Fetch recommendations for the given product ID.


## Requirements

Before running the project, you need to have the following installed:

- Anaconda

## Installation

### Cloning the Project
```bash
git clone https://github.com/tahsinsoyak/Python-Developer-Case.git
cd Python-Developer-Case
```

### Creating and Activating the Anaconda Environment
```bash
conda env create -f environment.yml
conda activate jobcase
```

### Database Setup

#### Creating the Database

Navigate to the Step1 directory and run the database script:
```bash 
cd ./Step1/
python database.py 
```
This step will add all data to the database.

#### Copying the Database and Moving to Step 2 
```bash 
cd ..
cd ./Step2/
python db.py 
```
This step adds example products to the database.

### Running and Testing The Project 

```bash 
python test.py 
```

The project should now be running.


## License

This project is licensed under the [MIT License](LICENSE).

## Support

If you like this app, please give it a star. If you have any questions or suggestions, please open an issue.

## Author

Tahsin Soyak
