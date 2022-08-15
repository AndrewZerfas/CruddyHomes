from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Home:
    db_name = 'homes'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.price = db_data['price']
        self.location = db_data['location']
        self.rooms = db_data['rooms']
        self.bathrooms = db_data['bathrooms']
        self.squarefootage = db_data['squarefootage']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO homes (price, location, rooms, bathrooms, squarefootage, user_id) VALUES (%(price)s,%(location)s,%(rooms)s,%(bathrooms)s,%(squarefootage)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
#everything above should be good

    @staticmethod
    def validate_home(home):
        is_valid = True
        if int(home['price']) < 1:
            is_valid = False
            flash("home cannot be free","home")
        if len(home['location']) < 3:
            is_valid = False
            flash("location must be at least 3 characters","home")
        if int(home['rooms']) < 1:
            is_valid = False
            flash("what's a house without a room?","home")
        if int(home['bathrooms']) < 1:
            is_valid = False
            flash("house must have atleast 1 bathroom","home")
        if int(home['squarefootage']) < 1:
            is_valid = False
            flash("house must be atleast 1 sqft","home")
        return is_valid

    @classmethod
    def update(cls, data):
        query = "UPDATE homes SET price=%(price)s, location=%(location)s, rooms=%(rooms)s, bathrooms=%(bathrooms)s, squarefootage=%(squarefootage)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)



    #nut so sure about this
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM homes;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_homes = []
        for row in results:
            print(row['price'])
            all_homes.append( cls(row) )
        return all_homes

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM homes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM homes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)