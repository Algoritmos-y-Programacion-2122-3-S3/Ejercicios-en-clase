name =input("Please enter your name :")
personal_data = {
    'name': name,
    'age': input("Please enter your age")
}
personal_data['name'] = input("Please enter your name :")
personal_data['age'] = input("Please enter your age :")
personal_data['phone'] = input("Please enter your phone :")
personal_data['address'] = input("Please enter your address :")

print(f"{personal_data.get('name')} tiene {personal_data.get('age')} años, vive en {personal_data.get('address')} y su número de teléfono es {personal_data.get('phone')}.")