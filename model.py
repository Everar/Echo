import web, datetime

db_host='am1shyeyqbxzy8gc.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name='azrd3bql1guetrj0'
db_user='r6dakcllmlu9yrvx'
db_pw='kv4j39xhign75jre'

db=web.database(
  dbn='mysql',
  host=db_host,
  db=db_name,
  user=db_user,
  pw=db_pw
	)

def get_posts():
    return db.select('productos', order='id_producto ASC')

def get_post(id_producto):
    try:
        return db.select('productos', where='id_producto=$id_producto', vars=locals())[0]
    except:
        return None

def new_post(producto, varchar, existencias, precio_compra, precio_venta, imagen_producto):
    db.insert('productos', producto=producto, descripcion=varchar, existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto, posted_on=datetime.datetime.utcnow())

def del_post(id_producto):
    db.delete('productos', where="id_producto=$id_producto", vars=locals())

def update_post(id_producto, producto, varchar, existencias, precio_compra, precio_venta, imagen_producto):
    db.update('productos', where="id_producto=$id_producto", vars=locals(),
        producto=producto, descripcion=varchar,  existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto, posted_on=datetime.datetime.utcnow())