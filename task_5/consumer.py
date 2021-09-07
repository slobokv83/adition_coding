from kafka import KafkaConsumer
import json


if __name__ == '__main__':
  consumer = KafkaConsumer(
    'mysql_records',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='mysql_consumers')
  print('starting the consumer')
  for msg in consumer:
    print(f'Mysql record = {json.loads(msg.value)}')