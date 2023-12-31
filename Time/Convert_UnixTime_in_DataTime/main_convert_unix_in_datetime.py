import datetime

# Unix-метка времени
timestamp = 1703109896

# Преобразование в datetime
dt_object = datetime.datetime.utcfromtimestamp(timestamp)

print("Дата и время в UTC:", dt_object)
