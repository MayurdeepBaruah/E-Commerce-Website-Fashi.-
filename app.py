from flask import Flask, render_template, url_for, redirect, request, jsonify,session,flash
from flask_session import Session
from werkzeug.utils import secure_filename
import pymysql
import data as d
import secrets
db=pymysql.connect(host="localhost", user="root", password="", database="mayurdeep_ecommerce")
cursor=db.cursor()
app=Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['UPLOAD_FOLDER']='./static/Images/'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home_page'))


#displaying the product category page

@app.route('/category')
def cat_page():
    return render_template('admin_product_category_manage.html')

#displaying data in the product category table

@app.route('/display_category', methods=['GET', 'POST'])
def disp_cat():
    if request.method == 'POST':
        try:
            cursor.execute('SELECT * FROM `product_category`')
            data=cursor.fetchall()
            db.commit()
            return jsonify(data)
        except:
            return('Error')
    
#inserting data in the product category table

@app.route('/insert', methods=['GET','POST'])
def insert_cat_data():
    if request.method=='POST':
        try:
            p_cat_names=request.form['p_cat_name']
            print(p_cat_names)
            p_cat_desps=request.form['p_cat_desp']
            print(p_cat_desps)
            p_cat_imgs=request.files['p_cat_img']  
            filename = secure_filename(p_cat_imgs.filename)
            p_cat_imgs.save(app.config['UPLOAD_FOLDER']+filename)
            print(filename)
            sql=f'INSERT INTO `product_category`(`Category_Name`, `Category_Desp`, `Category_Image`) VALUES ("{p_cat_names}", "{p_cat_desps}", "{filename}")'
            print(sql)
            # val=(p_cat_names, p_cat_desps, filename)
            cursor.execute(sql)
            db.commit()
            return jsonify(1)
        except:
            return jsonify(0)
        
# updating data in the product category table

@app.route('/update_category', methods=['PUT'])
def update_product_category():
    if request.method == 'PUT':
        try:
            p_cat_ids=request.form['cat_id']
            p_cat_names=request.form['p_cat_name']
            p_cat_desps=request.form['p_cat_desp']
            p_cat_imgs=request.files['p_cat_img']
            filename = secure_filename(p_cat_imgs.filename)
            p_cat_imgs.save(app.config['UPLOAD_FOLDER']+filename)
            sql=f"UPDATE `product_category` SET `Category_Name`= '{p_cat_names}',`Category_Desp`= '{p_cat_desps}',`Category_Image`= '{filename}' WHERE `Category_ID`= '{p_cat_ids}'"
            #val=(p_cat_names, p_cat_desps, filename, p_cat_ids)
            cursor.execute(sql)
            db.commit()
            return jsonify('inserted')
        except:
            return jsonify('Error')

#deleting data from the product category table

@app.route('/delete_category', methods=['DELETE'])
def delete_product_category():
    if request.method == 'DELETE':
        try:
            cat_ids=request.form['cat-id']
            sql='DELETE FROM `product_category` WHERE `Category_ID`= %s' 
            val=(cat_ids)
            cursor.execute(sql, val)
            db.commit()
            return jsonify('Deleted')
        except:
            return jsonify('Error')

# displaying the data to updated in the product category form

@app.route('/update1_category', methods=['POST'])
def update1_product_category():
    if request.method == 'POST':
        try:
            cat_ids=request.form['cat-id']
            sql='SELECT * FROM `product_category` WHERE `Category_ID`= %s'
            val=(cat_ids)
            cursor.execute(sql, val)
            p_cat_data=cursor.fetchone()
            db.commit()
            return jsonify(p_cat_data)
        except:
            return jsonify('Error')

# displaying the admin product page

@app.route('/products')
def prod_data():
            cursor.execute('SELECT `Category_ID`, `Category_Name` FROM `product_category`')
            Cat=cursor.fetchall()
            db.commit()
            return render_template('admin_product_manage.html', cat=Cat)

#displaying data in the product table

@app.route('/display_product', methods=['GET', 'POST'])
def display_product():
    if request.method == 'POST':
        try:
            cursor.execute('SELECT * FROM `products`')
            data1=cursor.fetchall()
            db.commit()
            return jsonify(data1)
        except:
            return jsonify('Error')
       
#inserting data in the product form

@app.route('/insert_product', methods=['GET','POST'])
def insert_product():
    if request.method == 'POST':
        try:
            p_names=request.form['p_name']
            p_prices=request.form['p_price']
            p_cats=request.form['p_cat']
            p_srt_desps=request.form['p_srt_desp']
            p_lng_desps=request.form['p_lng_desp']
            p_imgs=request.files['p_img']
            filename = secure_filename(p_imgs.filename)
            p_imgs.save(app.config['UPLOAD_FOLDER']+filename)
            sql=f"""INSERT INTO `products`(`Product_Name`, `Product_Price`, `Category_ID`, `Product_Short_Desp`, `Product_Long_Desp`, `Product_Images`) VALUES ("{p_names}", "{p_prices}","{p_cats}", "{p_srt_desps}", "{p_lng_desps}", '{filename}')"""
            #val=(p_names, p_prices, p_srt_desps, p_lng_desps, filename)
            print(sql)
            print(filename)
            cursor.execute(sql)
            db.commit()
            return jsonify(1)
        except:
            return jsonify(0)
        
# updating data in the product table

@app.route('/update_product', methods=['PUT'])
def update_product():
    if request.method == 'PUT':
        try:
            p_ids=request.form['p-id']
            p_names=request.form['p_name']
            p_prices=request.form['p_price']
            p_srt_desps=request.form['p_srt_desp']
            p_lng_desps=request.form['p_lng_desp']
            p_imgs=request.files['p_img']
            filename = secure_filename(p_imgs.filename)
            p_imgs.save(app.config['UPLOAD_FOLDER']+filename)
            sql=f'UPDATE `products` SET `Product_Name`= "{p_names}",`Product_Price`= "{p_prices}",`Product_Short_Desp`= "{p_srt_desps}",`Product_Long_Desp`= "{p_lng_desps}", `Product_Images`= "{filename}" WHERE `Product_ID`= "{p_ids}"'
            #val=(p_names, p_prices, p_srt_desps,  p_lng_desps, filename, p_ids)
            print(sql)
            cursor.execute(sql)
            db.commit()
            return jsonify('inserted')
        except:
            return jsonify('Error')
        
#deleting data from the product table

@app.route('/delete_product', methods=['DELETE'])
def delete_product():
    if request.method == 'DELETE':
        try:
            p_ids=request.form['p-id']
            sql=f"DELETE FROM `products` WHERE `Product_ID`= '{p_ids}'" 
            #val=(p_ids)
            print(sql)
            cursor.execute(sql)
            db.commit()
            return jsonify('Deleted')
        except:
            return jsonify('Error') 

# displaying the data to updated in the product category form

@app.route('/update1_product', methods=['POST'])
def update1_product():
    if request.method == 'POST':
        try:
            p_ids=request.form['p-id']
            sql='SELECT * FROM `products` WHERE `Product_ID`= %s'
            val=(p_ids)
            cursor.execute(sql, val)
            p_data=cursor.fetchone()
            db.commit()
            return jsonify(p_data)
        except:
            return jsonify('Error')

# displaying the admin product user page

@app.route('/user')
def prod_user_data():
    return render_template('admin_product_user_data.html')

#displaying data in the product user table

@app.route('/display_product_user', methods=['GET','POST'])
def display_product_user():
    if request.method=='POST':
        try: 
            cursor.execute('SELECT * FROM `product_user`')
            data2=cursor.fetchall()
            db.commit()
            return jsonify(data2)
        except:
            return jsonify('error')
            
# displaying the admin product user page

@app.route('/order')
def prod_order_data():
    cursor.execute('SELECT `User_ID` FROM `product_user`')
    order_data=cursor.fetchall()
    db.commit()
    return render_template('admin_product_order_data.html', Order_data=order_data)

#displaying data in the product order table

@app.route('/display_product_order', methods=['GET','POST'])
def display_product_order():
    if request.method=='POST':
        try:
            cursor.execute('SELECT * FROM `product_order`')
            data3=cursor.fetchall()
            db.commit()
            return jsonify(data3)
        except:
            return jsonify('error')
        
# displaying admin manage blog page       

@app.route('/admin_blog')
def blg_page():
    return render_template('admin_manage_blog.html')

# displaying data in the admin blog page

@app.route('/display_blog', methods=['GET','POST'])
def display_blog():
    if request.method=='POST':
        try: 
            cursor.execute('SELECT * FROM `product_blog`')
            blog_data=cursor.fetchall()
            db.commit()
            return jsonify(blog_data)
        except:
            return jsonify('Error')

# inserting data in the admin blog page

@app.route('/Insert_Blog', methods=['GET','POST'])
def insert_blog():
    if request.method=='POST':
        try:
            blog_imgs=request.files['blog_img']
            filename = secure_filename(blog_imgs.filename)
            blog_imgs.save(app.config['UPLOAD_FOLDER']+filename)
            blog_titles=request.form['blog_title']
            blog_cats=request.form['blog_cat']
            blog_desps=request.form['blog_desp']
            blog_desps1=request.form['blog_desp1']
            sql=f'INSERT INTO `product_blog`(`Blog_Image`, `Blog_Title`, `Blog_Category`, `Blog_Desp`, `Blog_Desp1`) VALUES ("{filename}","{blog_titles}","{blog_cats}", "{blog_desps}", "{blog_desps1}")'
            print(sql)
            cursor.execute(sql)
            db.commit()
            return jsonify(1)
        except:
            return jsonify(0)
        
# deleting data from the admin blog page        
        
@app.route('/delete_blog', methods=['DELETE'])
def delete_blog():
    if request.method=='DELETE':
        try:
            blog_ids=request.form['blog-id']
            sql="DELETE FROM `product_blog` WHERE `Blog_ID` = %s"
            val=(blog_ids)
            cursor.execute(sql, val)
            db.commit()
            return jsonify(1)
        except:
            return jsonify(0) 
        
# updating data in the admin blog page        

@app.route('/update_blog', methods=['POST'])
def update_blog():
    if request.method=='POST':
        try:
            upd_blogs=request.form['blog-id']
            sql="SELECT * FROM `product_blog` WHERE `Blog_ID`= %s"
            val=(upd_blogs)
            cursor.execute(sql, val)
            upd_blog1=cursor.fetchone()
            db.commit()
            return jsonify(upd_blog1)
        except:
            return jsonify('Error')
        
# adding updated data in the admin blog page        

@app.route('/update1_blog', methods=['PUT'])
def update1_blog():
    if request.method== 'PUT':
        try:
            blog_ids=request.form['blog-id']
            blogs_imgs=request.files['blog_img']
            filename = secure_filename(blogs_imgs.filename)
            blogs_imgs.save(app.config['UPLOAD_FOLDER']+filename)
            blog_titles=request.form['blog_title']
            blog_cats=request.form['blog_cat']
            blog_desps=request.form['blog_desp']
            blog_desps1=request.form['blog_desp1']
            sql=f'UPDATE `product_blog` SET `Blog_Image`="{filename}",`Blog_Title`="{blog_titles}",`Blog_Category`="{blog_cats}",`Blog_Desp`="{blog_desps}",`Blog_Desp1`="{blog_desps1}" WHERE `Blog_ID`="{blog_ids}"'
            print(sql)
            cursor.execute(sql)
            db.commit()
            return jsonify(1)
        except:
            return jsonify(0)
                   
###################################################################################################################################################################################

# displaying home page of user site

@app.route('/')
def home_page():
        cursor.execute('SELECT * FROM `products`')
        prod_cat=cursor.fetchall()
        print(prod_cat)
        db.commit()
        cursor.execute('SELECT * FROM `product_blog`')
        blog_data=cursor.fetchall()
        db.commit()

        data=d.data
        data1=d.data1
        data2=d.data2
        data4=d.data4
        return render_template("retailer_home.html", prod_cat=prod_cat, data=data, data1=data1, data2=data2, data4=data4, blog_data=blog_data)

# displaying shop page of user site using filters and checkboxes

@app.route('/Shopprod',methods=['GET','POST'])
def shop_prod():
    if request.method=='POST':
        cats=request.form.getlist('pcat')
        cats=','.join(cats)
        print(cats)
        sql=f'SELECT p.*,c.Category_Name FROM `products` p , `product_category` c WHERE p.Category_ID=c.Category_ID and p.Category_ID in("{cats}");'
    else:
        sql="SELECT p.*,c.Category_Name FROM `products` p , `product_category` c WHERE p.Category_ID=c.Category_ID"
    cursor.execute(sql)
    prod=cursor.fetchall()
    return jsonify(prod)
    
    
@app.route('/Shop', methods=['GET','POST'])
def shop_page():
    
    cursor.execute("SELECT * FROM `product_category`")
    cat=cursor.fetchall()
    db.commit()
    return render_template('retailer_shop.html', cat=cat)

# displaying blog page of the user site

@app.route('/Blog')
def blog_page():
    cursor.execute('SELECT * FROM `product_blog`')
    blog_data=cursor.fetchall()
    db.commit()
    data7=d.data7
    data8=d.data8
    return render_template('retailer_blog.html', data7=data7, data8=data8, blog_data=blog_data)

# displaying blog details page of the user site

@app.route('/Blog/Blog_Details/<int:id>')
def blog_detail_page(id):
     cursor.execute(f'SELECT * FROM `product_blog` WHERE `Blog_ID`={id};')
     blog_data1=cursor.fetchone()
     db.commit()
     cursor.execute('SELECT * FROM `product_blog`')
     blog_data2=cursor.fetchall()
     db.commit()
     data12=d.data12
     return render_template('retailer_blog_details.html', data12=data12, blog_data1=blog_data1, blog_data2=blog_data2)

# displaying contact page of the user site

@app.route('/Contact')
def contact_page():
    return render_template('retailer_contact.html')

# displaying the FAQ page of the user site

@app.route('/FAQ')
def FAQ_page():
    return render_template('retailer_FAQ.html')

# displaying the register page of the user site

@app.route('/Register')
def register_page():
    return render_template('retailer_register.html')

# inserting the data from the register page of the user site

@app.route('/Insert_User', methods=['GET','POST'])
def insert_user():
    if request.method=='POST':
        try:
            user_names=request.form['user_name']
            user_emails=request.form['user_email']
            user_passwords=request.form['user_password'] 
            user_ages=request.form['user_age']
            user_genders=request.form['user_gender'] 
            user_addresses=request.form['user_address']   
            user_mobiles=request.form['user_mobile'] 
            sql=f'INSERT INTO `product_user`(`User_Name`, `User_Email`, `User_Password`, `User_Age`, `User_Gender`, `User_Address`, `User_Mobile`) VALUES ("{user_names}","{user_emails}","{user_passwords}","{user_ages}","{user_genders}","{user_addresses}","{user_mobiles}")'
            print(sql)
            cursor.execute(sql)
            db.commit()
            
            return jsonify(1)
        except:
            return jsonify(0)

#displaying login page of the user site and user logging in to access pages

@app.route('/Login',methods=['POST','GET'])
def login_page():
    if request.method=='POST':
        login_users=request.form['login_user']
        login_passwords=request.form['login_password']
        sql=f'SELECT * FROM `product_user` WHERE (`User_Email`="{login_users}" OR `User_Name`="{login_users}") AND `User_Password`="{login_passwords}"'
        cursor.execute(sql)
        user=cursor.fetchone()
        if(user!=None):
            print(user)
            session['uid']=user[0]
            print(session.get('uid'))
            return redirect(url_for('home_page'))
        else:
            return redirect(url_for('login_page'))
    else:    
        return render_template('retailer_login.html')

# displaying product details of the user site

@app.route('/Shop/product_detail/<int:id>')
def prod_detail(id):
    cursor.execute(f'SELECT p.*,c.Category_Name FROM `products` p , `product_category` c WHERE p.Category_ID=c.Category_ID and Product_ID={id};')
    prod=cursor.fetchone()
    db.commit()
    cursor.execute(f'SELECT * FROM `products` WHERE `Category_ID`={prod[3]}')
    cats=cursor.fetchall()
    db.commit()
    return render_template('retailer_product_details.html', i=prod, cats=cats)

# adding products in the cart of the user site

@app.route('/insert_cart', methods=['GET','POST'])
def insert_cart():
    if request.method=='POST':
        if(session.get('uid')):
            try:
                cart_ids=request.form['cart-id']
                cursor.execute(f"SELECT * FROM `product_cart` WHERE `User_ID`='{session['uid']}' AND `Product_ID`='{cart_ids}'")
                check_cart=cursor.fetchone()
                db.commit()
                if(check_cart==None):    
                    sql=f"INSERT INTO `product_cart`(`User_ID`, `Product_ID`) VALUES ('{session['uid']}','{cart_ids}')"
                    cursor.execute(sql)
                    db.commit()
                    return jsonify(1)
                else: 
                    return jsonify(-1)
            except:
                return jsonify(0)
        else:
            return jsonify(2)
        
#deleting products from cart page of user site
    
@app.route('/del_cart', methods=['DELETE'])
def del_cart():
        if request.method == 'DELETE':
            cart_ids=request.form['cart-id']
            sql=f'DELETE FROM `product_cart` WHERE `Product_ID`="{cart_ids}"'
            print(sql)
            cursor.execute(sql)
            db.commit()
            return jsonify(1)
        else:
            return jsonify(0)
        
#updating quantity of products from cart page of user site
    
@app.route('/upd_cart', methods=['POST'])
def upd_cart():
    if(session.get('uid')):
        id=session.get('uid')

        if request.method== 'POST':
            p_ids=request.form.get('id')
            p_qtys=request.form.get('q')
            sql=f'UPDATE `product_cart` SET `Product_Quantity`="{p_qtys}" WHERE `Product_ID`="{p_ids}"'
            cursor.execute(sql)
            db.commit()

            sql1=f'SELECT sum(p.Product_Price*c.Product_Quantity) as "Total Price" FROM `products` p, `product_cart` c WHERE p.Product_ID=c.Product_ID AND `User_ID`="{id}"'
            cursor.execute(sql1)
            cart_sum=cursor.fetchone()
            db.commit()
            print(sql1)

            return jsonify(cart_sum)
        else:
            return jsonify(0)
        
#displaying cart page of the user site

@app.route('/cart')
def disp_cart():
    if(session.get('uid')):
        id=session.get('uid')
        cursor.execute(f'SELECT p.*, c.* FROM `products` p, `product_cart` c WHERE p.Product_ID=c.Product_ID AND `User_ID`="{id}"')
        cart_data=cursor.fetchall()
        db.commit()
        
        cursor.execute(f'SELECT c.Product_Quantity, sum(p.Product_Price*c.Product_Quantity) as "Total Price" FROM `products` p, `product_cart` c WHERE p.Product_ID=c.Product_ID AND `User_ID`="{id}"')
        cart_sum=cursor.fetchall()
        db.commit()

        cursor.execute(f'SELECT * FROM `product_user` WHERE `User_ID`="{id}"')
        user=cursor.fetchall()
        print(user)
        db.commit()
        return render_template('retailer_shopping_cart.html', cart_data=cart_data, cart_sum=cart_sum, qty=[i for i in range(1,10+1)], user=user)
    else:
        return redirect(url_for('login_page'))
    
# displaying total price API of the products 

@app.route('/totals', methods=['GET'])
def totals():
    if request.method == 'GET':
            try:
                cursor.execute(f'SELECT c.Product_Quantity, sum(p.Product_Price*c.Product_Quantity) as "Total Price" FROM `products` p, `product_cart` c WHERE p.Product_ID=c.Product_ID')
                cart_sum=cursor.fetchall()
                print(cart_sum)
                db.commit()
                return jsonify(cart_sum)
            except:
                return jsonify(0)
    else:
        return jsonify('Error')
    
#displaying checkout page of the user site

@app.route('/checkout/<int:id>', methods=['GET'])

def checkout(id):
    if request.method=='GET':
        oid=secrets.token_hex(5)
        cursor.execute(f'SELECT * FROM `product_user` WHERE `User_ID`="{id}"')
        user=cursor.fetchall()
        db.commit()
        cursor.execute(f'SELECT p.*, c.* FROM `products` p, `product_cart` c WHERE p.Product_ID=c.Product_ID AND `User_ID`="{id}"')
        prod=cursor.fetchall()
        db.commit()
        cursor.execute(f'SELECT c.Product_Quantity, sum(p.Product_Price*c.Product_Quantity) as "Total Price" FROM `products` p, `product_cart` c WHERE p.Product_ID=c.Product_ID AND `User_ID`="{id}"')
        sum=cursor.fetchall()
        db.commit() 
        for i in prod:
            sql=f'INSERT INTO `product_order`(`Order_ID`, `User_ID`, `Product_Quantity`, `Product_ID`) VALUES ("{oid}","{id}","{i[10]}","{i[9]}")'
            print(sql)
            cursor.execute(sql)
        db.commit()
        return render_template('retailer_checkout.html', user=user, prod=prod, sum=sum)
    


'''@app.route('/insert_ord_detail', methods=['POST'])

def insert_ord_detail():
    if request.method=='POST':
        id=session.get('uid')
        prd_qty=request.form.get("prd_qty")
        print(prd_qty)
        sql=f'INSERT INTO `product_order`(`User_ID`, `Product_Quantity`) VALUES ("{id}","{prd_qty}")'
        print(sql)
        cursor.execute(sql)
        db.commit()
    else:
        return jsonify("error")

@app.route("/disp_ord_detail", methods=['GET', 'POST'])

def disp_ord_detail():
    if request.method=='POST':
        cursor.execute("SELECT * FROM `product_order`")
        ord=cursor.fetchall()
        db.commit()
        return jsonify(ord)
    else:
        return jsonify("error")    
'''
        



if __name__ == '__main__':
    app.run(debug=True)


