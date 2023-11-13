import sqlite3

def create_viewed_products_table():
    # SQLite veritabanına bağlanın
    conn = sqlite3.connect('trendyol_products.db')  # 'your_database.db' kısmını kendi veritabanı dosyanızın adıyla değiştirin.
    cursor = conn.cursor()

    # Örnek SQL sorgusu: viewed_products tablosunu oluştur
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viewed_products (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')

    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()

# Tabloyu oluştur
create_viewed_products_table()