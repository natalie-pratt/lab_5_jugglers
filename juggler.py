from peewee import *

db = SqliteDatabase('juggler.sqlite')

class Juggler(Model):
    name = CharField(unique=True) # Name is unique 
    country = CharField()
    num_catches = IntegerField()


    class Meta:
        database = db
        

    def __str__(self): # To string function for all Juggler objects
        return f'\nJuggler name: {self.name}, Juggler country: {self.country}, Juggler catches: {self.num_catches}\n'


db.connect()
db.create_tables([Juggler]) # Create juggler table 

