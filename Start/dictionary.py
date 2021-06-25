book = {
    'title': 'aditya Book',
    'author': 'Aditya Singh',
    'isbn': '5454-65464-56654',
    'page count': 54

}
book_title = book['title']
book['title'] = 'New book'
print(book['title'])
keys = book.keys()
print(keys)
personality = [{
    'name' : 'Dhoni',
    'age' : 42
},{
    'name': 'Sachin',
    'age' : 53
},{
    'name' : 'virat',
    'age' : 34
}]

print(personality)
bag = {
    'books' : [{
    'title': 'aditya Book',
    'author': 'Aditya Singh',
    'isbn': '5454-65464-56654',
    'page count': 522
    },
    {
    'title': 'ay Book',
    'author': 'Ayushi Singh',
    'isbn': '54-664-564',
    'page count': 5454
    },
    {
    'title': 'ss Book',
    'author': 'narayan Singh',
    'isbn': '54654-65464-654654-564546',
    'page count': 3544
    }],
    'stationary' : [{
        'name' : 'pen',
        'quantity' : 10
    },
    {
        'name' : 'copy',
        'quantity' : 25
    },
    {
        'name' : 'scale',
        'quantity' : 62
    }],
    'size' : 55,
    'color' : 'green'
}
print(bag)