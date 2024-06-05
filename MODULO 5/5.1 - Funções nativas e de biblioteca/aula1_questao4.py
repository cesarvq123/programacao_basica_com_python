from datetime import datetime

now = datetime.now()

data_formatada = f"Data: {now.day:02}/{now.month:02}/{now.year}"
hora_formatada = f"Hora: {now.hour:02}:{now.minute:02}"

print(data_formatada)
print(hora_formatada)
