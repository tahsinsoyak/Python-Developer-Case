# Python-Developer-Case
 

## Gereksinimler

Proje çalıştırılmadan önce aşağıdaki gereksinimleri sağlamalısınız:

- [Anaconda](https://www.anaconda.com/) yüklü olmalı.

## Kurulum

1. **Projeyi İndirme:**
    ```bash
    git clone
    cd proje-adı
    ```

2. **Anaconda Ortamını Oluşturma ve Etkinleştirme:**
    ```bash
    conda env create -f environment.yml
    conda activate jobcase
    ```

3. **Veritabanı Oluşturma:**
    ```bash
    cd ./Step1/
    python database.py
    ```

    Bu adım, tüm verileri veritabanına ekleyecektir.

4. **Veritabanını Kopyalama ve İkinci Adıma Geçme:**
    ```bash
    cd ..
    cd ./Step2/
    ```

5. **Örnek İncelenen Ürünleri Ekleyerek Veritabanını Oluşturma:**
    ```bash
    python db.py
    ```

6. **Projeyi Başlatma ve Test Etme:**
    ```bash
    python test.py
    ```

    Proje şimdi çalışıyor olmalıdır.


Veri Kazıma:

Evet, Trendyol'dan ürün verilerini çıkarmak için Selenium'u kullanarak web kazıması uygulandı. scrape_trendyol fonksiyonu, bir URL alır, sayfaya gidip ürün kartlarından bilgi çıkarır ve ürün detaylarını içeren bir liste döndürür.

Veritabanı İşlemleri (SQLite):

SQLite kullanılarak bir veritabanı oluşturuldu ve yönetildi (trendyol_products.db). Ürün bilgilerini depolamak için sütunları (id, marka, isim, fiyat, resim, bağlantı) içeren bir products tablosu tanımlandı. Bu tablo, SQLAlchemy kullanılarak oluşturuldu ve ardından ürünleri veritabanına eklemek için add_products_to_database fonksiyonu kullanıldı.

Web Arayüzü (Flask):

Flask kullanılarak bir web uygulaması geliştirildi ve birkaç rota (index, product_detail, add_to_history, history, get_product_recommendations) oluşturuldu. Uygulama, HTML şablonlarını işler ve dinamik olarak veri göstermek için Jinja templating kullanır. Kullanıcılar tarafından görüntülenen ürünleri takip etmek için bir oturum tabanlı mekanizma olan viewed_products_dict bulunmaktadır.

Öneri Sistemi:

TF-IDF ve kosinüs benzerliği kullanarak içerik tabanlı bir öneri sistemi uygulandı machinelearning.py modülünde. Öneriler, get_product_recommendations rotasında alınır ve web sayfasında gösterilir.

Flask'ta Veritabanı Etkileşimi:

get_products_from_database, get_product_by_id ve get_viewed_products_from_database gibi fonksiyonlar, veritabanı ile etkileşimde bulunarak ürün bilgilerini çeker.

Kullanıcı Etkileşimi:

Kullanıcılar ana sayfada (index rota) ürünleri görebilir ve ürün detaylarını (product_detail rota) inceleyebilir. Sistem, kullanıcıların gördüğü ürünleri takip eder ve kullanıcılar geçmişlerini görebilir (history rota). Öneriler, kullanıcının gördüğü ürünlere dayanarak ayrı bir sayfada (get_product_recommendations rota) gösterilir.

API Entegrasyonu:

Projeye, Flask-RESTful kullanılarak bir API entegrasyonu eklenmiştir. Özellikle, öneri almak için GetRecommendationsResource adlı bir sınıf eklenmiştir. Önerileri JSON formatında alacak bir API endpoint oluşturulmuştur. Bu endpoint, get_recommendations_json fonksiyonunu kullanarak önerileri alır ve JSON olarak döndürür. Bu entegrasyon, projeye API ile etkileşim imkanı sağlar.
