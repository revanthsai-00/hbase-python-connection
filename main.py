
import happybase

connect=happybase.Connection(host='192.168.56.104',port=9090,autoconnect=False)
connect.open()
print(connect.tables())
#getting tables from hbase
table = connect.table('customer')
print(table)
#perfomed batch operation by inserting and deleting data from table
b = table.batch()
b.put(b'surya', {b'address:city': b'guntur', b'order:amount': b'2000'})
b.put(b'vamsi', {b'address:city': b'vizag', b'order:amount': b'4000'})
b.put(b'ashish', {b'address:city': b'hyderabad', b'order:amount': b'2800',b'order:number':b'ord-035'})
b.delete(b'sunny')
b.send()
#retrieving data from tables
rows = table.rows([b'jahnavi',b'hemanth',b'surya',b'vamsi',b'ashish'])
for key, data in rows:
    print(key, data)