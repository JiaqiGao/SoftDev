import random

def RandomStudent(period):
    if period == 4:
        ary = [ 'Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson',
         'Brian', 'Farhan', 'Janet', 'Harry', 'Kevin',
         'Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth',
         'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhriaj',
         'Amy', 'Arvind', 'Nobel', 'Angela', 'Edward',
         'Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina']
        return(ary[random.randint(0,len(ary))])
    elif period == 8:
        ary = ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki',
        'Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda',
        'Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vncent',
        'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel',
        'Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio',
        'Kelly', 'William', 'Jordan', 'Haley', 'Henry']
        return(ary[random.randint(0,len(ary))])
    elif period == 9:
        ary = ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C',
        'Joel', 'Steph', 'Xinhui', 'Richard', 'Misha',
        'Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry',
        'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine',
        'Jessica', 'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L',
        'Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']
        return(ary[random.randint(0,len(ary))])
    return("Period input is invalid")
    
