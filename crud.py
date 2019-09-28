from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template('index.html');  
 
@app.route("/add")  
def add():  
    return render_template("add_book.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "failed"  
    if request.method == "POST":  
        try:  
            id_buku = request.form["Id"]  
            kategori = request.form["Kategori"]  
            nama_buku = request.form["Jd"]
            pengarang_buku = request.form["Pb"]
            harga_buku = request.form["Price"]
            stock_buku = request.form["Stock"]
            penerbit_buku = request.form["Penerbit"]
            print(id_buku, kategori, nama_buku, pengarang_buku, harga_buku, stock_buku, penerbit_buku)

            # conn = sqlite3.connect("D:\Project\Serifikasi\dbtoko.sqlite")
            with sqlite3.connect("D:\Project\Serifikasi\dbtoko.sqlite") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO TOKOBUKU1 (ID, KATEGORI, JD, PB, PRICE, STOCK, PENERBIT)   \
                    VALUES (?,?,?,?,?,?,?)", (id_buku, kategori, nama_buku, pengarang_buku, harga_buku, stock_buku, penerbit_buku) )

                con.commit()
                msg = "Book successfully Added"
          
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("D:\Project\Serifikasi\dbtoko.sqlite")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from TOKOBUKU1")  
    rows = cur.fetchall()  
    return render_template("view_book.html",rows = rows)  
 
 
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():                 
    try:
        idd = request.form["IDD"]
        statment = ("DELETE from Orders where Order_Status = %s" %id)
        print('id: ', id)
        with sqlite3.connect("D:\Project\Serifikasi\dbtoko.sqlite") as con: 
            cur = con.cursor()  
            cur.execute(("DELETE from TOKOBUKU1 where ID = ?", str(idd) ))
                # VALUES (?,?,?,?,?,?,?)", (id_buku, kategori, nama_buku, pengarang_buku, harga_buku, stock_buku, penerbit_buku) )  
            msg = "record successfully deleted"  
    except:  
        msg = "data can't be deleted"  
    finally:  
        return render_template("delete_record.html",msg = msg)
        con.commit()

if __name__ == "__main__":  
    app.run(debug = True)  