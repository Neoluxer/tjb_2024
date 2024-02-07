import psycopg2

from psycopg2 import sql

id = 0


def Counter():
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='IlonMask@Python', host='212.109.199.54')
    cursor = conn.cursor()

    a = 0
    list_sample = []
    for n in range(1, 300, 1):
        cursor.execute('SELECT * FROM contract WHERE customer_id = %s', (int(n),))
        for items in cursor:
            if items not in list_sample:
                list_sample.append (items[4])
    id_set = set(list_sample)
    print(id_set)
    profit_dict={}
    for dataset in id_set:
        sum_profit=0
        cursor.execute('SELECT profit FROM contract WHERE customer_id = %s', (dataset,))
        for items in cursor:
            if (items[0]):
                sum_profit+= (items[0])
        profit_dict[dataset]=int(sum_profit/75.76)
    print (profit_dict)
    for key in profit_dict:
        print (f'{key}--{profit_dict[key]}')
        cursor.execute('UPDATE clients SET value=%s WHERE id=%s', (profit_dict[key], key))
        conn.commit()



# cursor.execute('UPDATE clients SET value=%s WHERE id=%s',(333,40))
#                     conn.commit()

# d = {}
# for a in range(5):
#     k=str(a+1)+' '+'may'
#     d[k] = a
#     print(d)
# print('Ves slovar imeet vid: ',d)


Counter()
