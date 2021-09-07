from kafka import KafkaProducer
import json
from data import dict_mysql
from time import sleep


def json_serializer(data):
  return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)


if __name__ == '__main__':
  for record in dict_mysql:
    print(record)
    producer.send('mysql_records', record)
    sleep(4)