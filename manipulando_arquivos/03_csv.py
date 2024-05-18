import csv

try:
    with open('./example.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["nome", "idade"])
        writer.writerow(["Ana", 30])
        writer.writerow(["João", 25])
except IOError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')

try:
    with open('./example.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]}\t{row[1]}")
                
except IOError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')