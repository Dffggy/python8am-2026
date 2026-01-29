category=[
    {'cid':1,'name': 'laptop'},
    {'cid':2,'name': 'mobile'},
    {'cid':3,'name': 'tv'},
    {'cid':4,'name': 'books'},
]

products=[
    {'id':1,'cid':1,'name': 'dell', 'quantity':3, 'price':500},
    {'id':2,'cid':1,'name': 'mac', 'quantity':5, 'price':800},
    {'id':3,'cid':1,'name': 'hp','quantity':6, 'price':700},
    {'id':4,'cid':2,'name': 'samsung', 'quantity':7, 'price':600},
    {'id':5,'cid':2,'name': 'apple', 'quantity':4, 'price':900},
    {'id':6,'cid':3,'name': 'sony', 'quantity':2, 'price':200},
    {'id':7,'cid':3,'name': 'lg', 'quantity':1, 'price':300},
]
for cat in category:
    print(f"Category: {cat['name']}")
    for p in products:
        if cat['cid'] == p['cid']:
            print(f"\t \t Product: {p['name']}")


#