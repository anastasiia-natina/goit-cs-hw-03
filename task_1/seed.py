import psycopg2
import faker

conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="localhost"
)

cursor = conn.cursor()
fake = faker.Faker()

for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

statuses = ['new', 'in progress', 'completed']
for status_name in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s)", (status_name,))

for _ in range(20):
    title = fake.sentence(nb_words=5)
    description = fake.paragraph()
    status_id = fake.random_element([1, 2, 3])
    user_id = fake.random_int(min=1, max=10)
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                    (title, description, status_id, user_id))

conn.commit()
cursor.close()
conn.close()