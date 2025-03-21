from faker import Faker
fake = Faker()

name = None
fake.name()


fake.address()


fake.text()


for i in range(1):
  name =fake.name()
  print(name)