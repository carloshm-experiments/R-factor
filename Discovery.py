from sympy import prime

# Definiendo una función para calcular los primeros 20 números del factor x que sean menores a -60%
def get_filtered_table():
    positions = []
    primes_list = []
    mod_values = []
    factor_x_percentage = []
    filtered_table = []
    count = 0

    for i in range(1, 5001):
        prime_number = prime(i)
        mod_value = prime_number % i
        if i > 1:
            prev_value = mod_values[-1]
            percentage_change = (mod_value / prev_value - 1) * 100 if prev_value != 0 else 'Infinity'
            if percentage_change not in ['Infinity', 'N/A'] and float(percentage_change) < -60:
                filtered_table.append((i, prime_number, mod_value, percentage_change))
                count += 1
                if count == 20:
                    break
        positions.append(i)
        primes_list.append(prime_number)
        mod_values.append(mod_value)
        factor_x_percentage.append('N/A' if i == 1 else percentage_change)

    return filtered_table

# Obteniendo la tabla filtrada con los primeros 20 números del factor x menores a -60
filtered_table_5000 = get_filtered_table()

# Creando la tabla en formato legible
filtered_table_5000_formatted = "\n".join([f"Posición: {row[0]}, Primo: {row[1]}, Módulo: {row[2]}, Factor x (%): {row[3]}" for row in filtered_table_5000])

# Mostrando la tabla
filtered_table_5000_formatted
