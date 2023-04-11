import psycopg2

def getConnection():
    conn = psycopg2.connect(
        host="localhost",
        database="notebookdb",
        user="postgres",
        password="s"
    )
    return conn

def insertData(notebooks, site):
    conn = getConnection()
    cur = conn.cursor()
    for x in notebooks:
        if site == 'vatan':
            table = 'vatan'
            model_name = x['Model Adı']
            cpu_type = x['İşlemci Teknolojisi']
            cpu_model = x['İşlemci Nesli']
            memory_capacity = x['Ram (Sistem Belleği)']
            dos = x['İşletim Sistemi']
            disc_capacity = x['Disk Kapasitesi']
            disc_type = x['Disk Türü']
            screen_size = x['Ekran Boyutu']
        if site == 'teknosa':
            table = 'teknosa'
            cpu_type = x['İşlemci']
            cpu_model = x['İşlemci Nesli']
            memory_capacity = x['Ram']
            dos = x['İşletim Sistemi Yazılımı']
            disc_capacity = x['SSD Kapasitesi']
            disc_type = x['Disk Türü']
            screen_size = x['Ekran Boyutu']
            try:
                disc_capacity = x['SSD Kapasitesi']
            except:
                disc_capacity = x['HDD Kapasitesi']
            try:
                model_name = x['Model Kodu']
            except:
                model_name = 'null'
        if site == 'n11':
            table = 'n11'
            model_name = x['Model'].rsplit(' ', 1)[1]
            cpu_type = x['İşlemci']
            cpu_model = x['İşlemci Modeli']
            memory_capacity = x['Bellek Kapasitesi']
            dos = x['İşletim Sistemi']
            disc_capacity = x['Disk Kapasitesi']
            disc_type = x['Disk Türü']
            screen_size = x['Ekran Boyutu']

        marka = x['Marka'].strip().upper()
        title = x['Başlık']
        price = x['Fiyat']
        notebook_url = x['Ürün URL']
        image_url = x['Görsel URL']
        
        insertSql = f"""insert into {table}(model_name, marka, title, price, site, notebook_url, image_url, 
        cpu_type, cpu_model, memory_capacity, dos, disc_capacity, disc_type, screen_size) 
        values('{model_name}', '{marka}', '{title}', '{price}', '{site}', '{notebook_url}','{image_url}'
        ,'{cpu_type}','{cpu_model}','{memory_capacity}','{dos}','{disc_capacity}','{disc_type}','{screen_size}')"""
    cur.execute(insertSql)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    insertData()
