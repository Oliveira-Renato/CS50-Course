people = [
    {'name':'Aragorn','race':'Dúnedain'},
    {'name':'Legolas','race':'Elf'},
    {'name':'Gimli','race':'Dwarf'}
]


#def f(person):
    #return person['name']

people.sort(key=lambda person: person['name'])

print(people)