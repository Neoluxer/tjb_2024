import psycopg2


class PsycopgDatabase:

    def create(self):
        conn = psycopg2.connect(dbname='postgres', user='postgres',
                                password='IlonMask@Python', host='localhost')
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS superheroes ")
        cur.execute("DROP TABLE IF EXISTS traffic_light ")

        cur.commit()
        cur.execute("CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, strengh int); ")
        cur.execute("INSERT INTO superheroes (hero_name,strenth) VALUES (%s,%s)",("Superman",100))
