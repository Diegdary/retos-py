producto ={
    0:{
        'id':123,
        'nombre':'libreta',
        'precio':12.500,
        'id_cat':1
    },
    1:{
        'id':345,
        'nombre':'jabon',
        'precio':10.500,
        'id_cat':2
    },
    2:{
        'id':3888,
        'nombre':'cepillo',
        'precio':35.555,
        'id_cat':2
    }
}


categoria={
    0:{
        'id':1,
        'nombre':'Utiles escolares'
    },
    1:
    {
        'id':2,
        'nombre':'Aseo'
    }
}

diccionarioResultante={}

for i in producto:
    diccionarioResultante[i]={
        'id':producto[i]['id'],
        'nombre':producto[i]['nombre'],
        'categoria':categoria[producto[i]['id_cat']-1]['nombre']
    }

print(diccionarioResultante)