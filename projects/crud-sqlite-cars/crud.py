import db

def insert_data():
	sql = "INSERT INTO cars (brand, model) VALUES(?, ?)"
	cars_data = [
		('Chevrolet', 'Chevrolet Camaro'),
		('Chevrolet', 'Chevrolet Captiva'),
		('Fiat', 'Fiat 125 Mirafiori'),
		('Fiat', 'Fiat 125 Centurion'),
		('Honda', 'Honda CR-V'),
		('Honda', 'Honda CR-X del Sol'),
		('Honda', 'Honda CR-Z')
	]

	result = db.run_query(sql, cars_data, multiple=True)
	print("Record inserted successfully into table", result.rowcount)