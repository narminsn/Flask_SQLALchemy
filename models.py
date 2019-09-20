

from create_app import db
from sqlalchemy.dialects import postgresql

class BaseModel(db.Model):
    __abstract__=True
    id=db.Column(db.INT, primary_key=True, autoincrement=True)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def filter(cls):
        return cls.query.filter_by().first()

    def save(self):
        db.session.add(self)
        db.session.commit()



class Menu(BaseModel):
    __tablename__="menu"
    name=db.Column(db.VARCHAR(50), nullable=False)
    url=db.Column(db.TEXT, nullable=True)

    def __init__(self, name=None, url=None):
        self.name=name
        self.url=url
    

    




class Header(BaseModel):
    __tablename__="header"
    
    background_image=db.Column(db.TEXT, nullable=True)
    title=db.Column(db.TEXT, nullable=False)
    sub_title=db.Column(db.TEXT, nullable=False)
    button_text=db.Column(db.VARCHAR(50), nullable=False)
    button_url=db.Column(db.TEXT, nullable=True)

    def __init__(self, background_image, title, sub_title, button_text, button_url):
        self.background_image=background_image
        self.title=title
        self.sub_title=sub_title
        self.button_text=button_text
        self.button_url=button_url
    

    
    


class About(BaseModel):
    __tablename__="about"
   
    title=db.Column(db.VARCHAR(250), nullable=False)
    sub_title=db.Column(db.TEXT, nullable=False)
    button_text=db.Column(db.VARCHAR(50), nullable=False)
    button_url=db.Column(db.TEXT, nullable=True)


class ServiceItem(BaseModel):
    __tablename__="serviceitem"
    icon=db.Column(db.TEXT, nullable=True)
    title=db.Column(db.TEXT, nullable=True)
    text=db.Column(db.TEXT, nullable=True)
    service_id=db.Column(db.INT, db.ForeignKey('services.id'))
    service = db.relationship('Service', backref='services', lazy=True)





class Service(BaseModel):
    __tablename__="services"
   
    name=db.Column(db.VARCHAR(50), nullable=False)


class Portfolio(BaseModel):
    __tablename__="portfolio"
    image=db.Column(db.TEXT, nullable=True)
    project_name=db.Column(db.VARCHAR(50), nullable=False)
    
   

   
class Footer(BaseModel):
    __tablename__="footer"
    title=db.Column(db.VARCHAR(50), nullable=False)
    text=db.Column(db.TEXT, nullable=True)
    copyrigh=db.Column(db.TEXT, nullable=True)
    

class Contact(BaseModel):
    __tablename__="Contacs"
    icon=db.Column(db.VARCHAR(50), nullable=True)
    text=db.Column(db.TEXT, nullable=True)
    
    