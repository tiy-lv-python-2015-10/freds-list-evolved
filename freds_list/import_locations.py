import csv
from fredslist.models import State, City

with open('states.csv', 'r') as f:
     reader = csv.reader(f, delimiter=',')
     for row in reader:
         input_state = row[0]
         State.objects.create(state=input_state)
         for input_city in range(1, len(reader)):
                 City.objects.create(city=input_city, state = input_state)