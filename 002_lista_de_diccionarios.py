data = {
    'students' : [
        {
            'name': 'Salvador Vizcaino',
            'class': 2015,
            'scores': [10, 9.8, 7, 7.8, 10, 8.9]
        },
        {
            'name': 'Edgar Torres',
            'class': 2015,
            'scores': [10, 8, 8, 6.9, 8.9, 8.9]
        },
        {
            'name': 'Galileo Guzman',
            'class': 2015,
            'scores': [9, 7, 6, 6.9, 8.8, 10]
        },
        {
           'name': 'Liz Rueda',
            'class': 2015,
            'scores': [10, 6, 7, 6.9, 8.5, 8.4] 
        },
        {
           'name': 'Met Vela',
            'class': 2015,
            'scores': [10, 10, 10, 9.9, 9.9, 9] 
        }    
    ]
}

print(type(data))

#students = data['students']
students = data.get('students', [])
print(students)