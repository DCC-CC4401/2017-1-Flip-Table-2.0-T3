from account.models import User, Client, Peddler, Established
from showcase.models import Tag, Dish

# delete previous data base if you want

# User.objects.all().delete()

user1 = User(username='alumno1', first_name='Tibo', last_name='Swy', email='tsy@bla.com', password='12345678abcd')
user2 = User(username='alumno2', first_name='pepe', last_name='pepe2', email='pepe@pepe.com', password='12345678abcd')
user3 = User(username='chino', first_name='diego', last_name='diego2', email='diego@diego.com', password='12345678abcd')
user4 = User(username='lunchbox', first_name='juan', last_name='juan2', email='juan@juan.com', password='12345678abcd')
user5 = User(username='sushi', first_name='lucas', last_name='lucas2', email='lucas@lucas.com', password='12345678abcd')
user6 = User(username='pepe', first_name='pedro', last_name='pedro2', email='pedro@pedro.com', password='12345678abcd')
user7 = User(username='empanada', first_name='carlos', last_name='carlos2', email='carlos@carlos.com',
             password='12345678abcd')

user1.save()
user2.save()
user3.save()
user4.save()
user5.save()
user6.save()
user7.save()

client1 = Client(user=user1)
client2 = Client(user=user2)
peddler1 = Peddler(user=user3)
peddler2 = Peddler(user=user4)
peddler3 = Peddler(user=user5)
established1 = Established(user=user6, start='10:20', end='20:34')
established2 = Established(user=user7, start='10:20', end='20:34')

client1.save()
client2.save()
peddler1.save()
peddler2.save()
peddler3.save()
established1.save()
established2.save()
