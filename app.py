from flask import Flask, request, Response, render_template, redirect, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from create_app import app, db
from flask_migrate import Migrate
from flask_script import Manager
from models import *
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

from flask_admin.form.upload import ImageUploadField
from flask import send_from_directory




app.secret_key="sdfghkjl;"
# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['UPLOAD_FOLDER']='uploads'

admin = Admin(app, name='Admin panel', template_mode='bootstrap3',url='/admin')
# Add administrative views here

@app.route("/uploads/<path:filename>")
def image_handler(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


class CustomView(ModelView):
    form_extra_fields={
        "background_image": ImageUploadField("background_image", base_path=app.config['UPLOAD_FOLDER'])
    }





# class CustomView(ModelView):
#     edit_modal = True
#     create_modal = True

admin.add_view(ModelView(Menu, db.session))
admin.add_view(CustomView(Header, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(ServiceItem, db.session))
admin.add_view(ModelView(Portfolio, db.session))
admin.add_view(ModelView(Contact, db.session))
admin.add_view(ModelView(About, db.session))
admin.add_view(ModelView(Footer, db.session))



@app.route("/", methods=["GET", "POST"])
def main_index():

        header_list=Header.all()
        
        menu_list=Menu.all()
        name=[]
        url=[]
        for obj in menu_list:
                name.append(obj.name)
                url.append(obj.url)

        
        
        for obj in header_list:
                 background_image=obj.background_image
                 title=obj.title
                 sub_title=obj.sub_title
                 button_text=obj.button_text
                 button_url=obj.button_url

        link=["https://images.pexels.com/photos/378570/pexels-photo-378570.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940","https://images.pexels.com/photos/297755/pexels-photo-297755.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940","https://images.pexels.com/photos/2089891/pexels-photo-2089891.jpeg?auto=format%2Ccompress&cs=tinysrgb&dpr=2&h=650&w=940"]
        pro_name=[]
        pro_url=[]
        

       
        context = {
            "background": background_image,
            "title": title,
            "sub_title": sub_title,
            "button_text": button_text,
            "button_url": button_url,
            "name": name,
            "url": url,
            "count": len(url),
            "portfolio_count":len(pro_url),
            "menu_list": Menu.all(),
            "about":About.filter(),
            "service":Service.filter(),
            "header": Header.filter(),
            "service_item":ServiceItem.all(),
            "image_link": link,
            "portfolio": Portfolio.all() 
         }
        
        

        

        if request.method == "GET":
                return render_template("index.html",**context)




app.run(debug=True, host='0.0.0.0', port=8050)