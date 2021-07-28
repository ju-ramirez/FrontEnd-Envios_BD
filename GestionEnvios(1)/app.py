
from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
from flask import render_template,request,redirect,url_for

app = Flask (__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root' #Indicamos el usuario, por defecto es user
app.config['MYSQL_DATABASE_PASSWORD']='' #Sin contraseña, se puede omitir
app.config['MYSQL_DATABASE_BD']='gestion' #Nombre de nuestra BD
mysql.init_app(app)

@app.route('/')
def index():
    sql="SELECT * FROM `gestion`.`envios` ;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    envios = cursor.fetchall()
    print (envios)
    conn.commit()
    return render_template ('envios/index.html', envios = envios)

@app.route('/create')
def create():
    return render_template('envios/create.html')

@app.route('/update', methods = ['POST'])
def update():
    _cliente=request.form['txtCliente']
    _direccion=request.form['txtDirecc']
    _localidad=request.form['txtLocalid']
    _provincia=request.form['txtProv']
    _contacto=request.form['txtCorreo']
    _paquete=request.form['paquete']
    id=request.form['txtID']

    sql="UPDATE `gestion`.`envios` SET `cliente`= %s,`direccion`= %s, `localidad`= %s,`provincia`= %s , `contacto`= %s, `paquete`= %s WHERE id=%s;"
    datos=(_cliente, _direccion, _localidad, _provincia, _contacto, _paquete, id)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)

    conn.commit()

    return redirect('/')

@app.route('/store', methods = ['POST'])
def storage():
    _cliente=request.form['txtCliente']
    _direccion=request.form['txtDirecc']
    _localidad=request.form['txtLocalid']
    _provincia=request.form['txtProv']
    _contacto=request.form['txtCorreo']
    _paquete=request.form['paquete']

    sql="INSERT INTO `gestion`.`envios` (`cliente`,`direccion`, `localidad`,`provincia` , `contacto`, `paquete`) VALUES (%s, %s, %s, %s, %s, %s);"
    datos=(_cliente, _direccion, _localidad, _provincia, _contacto, _paquete)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    
    return render_template ('envios/index.html')

@app.route('/destroy/<int:id>')
def destroy (id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `gestion`.`envios` WHERE id=%s", (id))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `gestion`.`envios` WHERE id = %s", (id))
    envios = cursor.fetchall()
    conn.commit()
    return render_template('envios/edit.html', envios = envios)

@app.route('/home')
def home():
    return render_template('envios/home.html')

if __name__ == '__main__':
    app.run(debug = True)
    