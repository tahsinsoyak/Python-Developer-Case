from sqlalchemy import create_engine, Column, String, Float, Text, MetaData, Table
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Veritabanı bağlantısı oluştur
engine = create_engine('sqlite:///trendyol_products.db', echo=True)

# Metadata ve Session oluştur
metadata = MetaData()
Session = sessionmaker(bind=engine)

# Ürünler tablosunu tanımla
products = Table('products', metadata,
    Column('id', String, primary_key=True),
    Column('brand', String),
    Column('name', String),
    Column('price', String),
    Column('image', String),
    Column('link', Text)
)

# Tabloyu oluştur
metadata.create_all(engine)

# DataFrame'deki ürünleri veritabanına ekleyin
def add_products_to_database(product_data):
    session = Session()

    for product in product_data:
        product_id = abs(hash(product['Link']))  # Benzersiz bir ID
        session.execute(products.insert().values(
            id=str(product_id),
            brand=product['Brand'],
            name=product['Name'],
            price=product['Price'],
            image=product['Image'],
            link=product['Link']
        ))

    session.commit()
    session.close()

from scrapping import scraped_data

# DataFrame'deki ürünleri veritabanına ekleyin
add_products_to_database(scraped_data)
