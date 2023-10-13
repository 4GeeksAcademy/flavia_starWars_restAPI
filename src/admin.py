import os
from flask_admin import Admin
from models import db, Favorite_Species, Species, Favorite_Characters, Characters, Favorite_Films, Films_Species, Films_Characters, Films, Favorite_Planets, Planets_Films, Planets, Favorite_Starships, Starships_Characters, Starships_Films, Starships, User
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class ChildView(ModelView):
        column_display_pk = True # optional, but I like to see the IDs in the list
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(ModelView(Starships_Films, db.session))
    admin.add_view(ModelView(Starships_Characters, db.session))
    admin.add_view(ModelView(Favorite_Starships, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Planets_Films, db.session))
    admin.add_view(ModelView(Favorite_Planets, db.session))
    admin.add_view(ModelView(Films, db.session))
    admin.add_view(ModelView(Films_Characters, db.session))
    admin.add_view(ModelView(Films_Species, db.session))
    admin.add_view(ModelView(Favorite_Films, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Favorite_Characters, db.session))
    admin.add_view(ChildView(Species, db.session))
    admin.add_view(ModelView(Favorite_Species, db.session))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))