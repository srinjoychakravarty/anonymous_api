from models import Person
import sqlite3

people = [
    (2, 'Brockman', 'Kent', '2018-08-08 21:16:01.888444'),
    (3, 'Easter', 'Bunny', '2018-08-08 21:16:01.889060'),
    (1, 'Farrell', 'Doug', '2018-08-08 21:16:01.886834')
]

lname = 'Farrell'

conn = sqlite3.connect('people.db')

cur = conn.cursor()
cur.execute('SELECT * FROM person ORDER BY lname')
cur.execute('SELECT * FROM person WHERE lname = \'{}\''.format(lname))
people = cur.fetchall()
for person in people:
    print(f'{person[2]} {person[1]}')

people = Person.query.order_by(Person.lname).all()
for person in people:
    print(f'{person.fname} {person.lname}')
