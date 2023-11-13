import sqlite3
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def get_click_data_from_database():
    conn = sqlite3.connect('trendyol_products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT product_id FROM viewed_products")
    viewed_products = [product[0] for product in cursor.fetchall()]

    full_click_data = []
    for product_id in viewed_products:
        cursor.execute("SELECT name, brand, price, link, image FROM products WHERE id=?", (product_id,))
        product_info = cursor.fetchone()
        full_click_data.append((product_id, *product_info))

    conn.close()

    return full_click_data

# Ürün verilerini içeren DataFrame
products_df = pd.DataFrame(get_click_data_from_database(), columns=['product_id', 'name', 'brand', 'price', 'link', 'image'])
products_df = products_df.fillna('')

# TfidfVectorizer kullanarak ürün isimleri üzerinde vektörleştirme yapalım
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(products_df['name'])

# Cosine Similarity matrisini hesaplayalım
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# Ürün ismi ve indexini eşleştirelim
indices = pd.Series(products_df.index, index=products_df['name']).drop_duplicates()

def get_recommendations(product_name):
    idx = indices[product_name]
    sim_scores = list(enumerate(cosine_similarities[idx]))

    if isinstance(sim_scores[0][1], np.ndarray):
        # If sim_scores is an array of arrays, use the first element of each array
        sim_scores = [(index, score[0]) for index, score in sim_scores]
    else:
        # If sim_scores is a simple 2D array, use it as is
        sim_scores = [(index, score) for index, score in sim_scores]

    # Now sort based on the extracted scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Exclude the first item as it's the same product
    sim_scores = sim_scores[1:6]

    recommended_products = []
    for i, score in sim_scores:
        product_info = {
            'id': products_df['product_id'].iloc[i],
            'name': products_df['name'].iloc[i],
            'brand': products_df['brand'].iloc[i],
            'price': products_df['price'].iloc[i],
            'link' : products_df['link'].iloc[i],
            'image' : products_df['image'].iloc[i],
            # Add other fields as needed
        }
        recommended_products.append(product_info)

    return recommended_products



def get_recommendations_json(product_name):
    idx = indices[product_name]
    sim_scores = list(enumerate(cosine_similarities[idx]))

    if isinstance(sim_scores[0][1], np.ndarray):
        sim_scores = [(index, score[0]) for index, score in sim_scores]
    else:
        sim_scores = [(index, score) for index, score in sim_scores]

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]

    recommended_products = []
    for i, score in sim_scores:
        product_info = {
            'id': str(products_df['product_id'].iloc[i]),  # Convert product_id to string
            'name': str(products_df['name'].iloc[i]),      # Convert name to string
            'brand': str(products_df['brand'].iloc[i]),    # Convert brand to string
            'price': str(products_df['price'].iloc[i]),    # Convert price to string
            'link': str(products_df['link'].iloc[i]),      # Convert link to string
            'image': str(products_df['image'].iloc[i]),    # Convert image to string
        }
        recommended_products.append(product_info)

    return recommended_products




# Örnek kullanım:
product_name = "5'li yüksek bel Koyu Soft 5 renk kadın külot"
product_name_str = str(product_name)

recommendations = get_recommendations(product_name_str)
print(recommendations)
