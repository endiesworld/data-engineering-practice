import os
from dotenv import load_dotenv
from typing import Dict, List
from json import loads
from kafka import KafkaConsumer

from ride import Ride
from settings import BOOTSTRAP_SERVERS, KAFKA_TOPIC


class JsonConsumer:
    def __init__(self, props: Dict):
        self.consumer = KafkaConsumer(**props)

    def consume_from_kafka(self, topics: List[str]):
        self.consumer.subscribe(topics)
        print('Consuming from Kafka started')
        print('Available topics to consume: ', self.consumer.subscription())
        while True:
            try:
                # SIGINT can't be handled when polling, limit timeout to 1 second.
                message = self.consumer.poll(1.0)
                if message is None or message == {}:
                    continue
                for message_key, message_value in message.items():
                    for msg_val in message_value:
                        print(msg_val.key, msg_val.value)
            except KeyboardInterrupt:
                break

        self.consumer.close()


if __name__ == '__main__':
    load_dotenv()
    config = {
        'bootstrap_servers': os.getenv("bootstrap.servers"),
        'security_protocol': os.getenv("security.protocol"),
        'sasl_mechanism': os.getenv("sasl.mechanisms"),
        'ssl_check_hostname': False,
        'sasl_plain_username': os.getenv("sasl.username"),
        'sasl_plain_password': os.getenv("sasl.password"),
        'auto_offset_reset': 'earliest',
        'enable_auto_commit': True,
        'key_deserializer': lambda key: int(key.decode('utf-8')),
        'value_deserializer': lambda x: loads(x.decode('utf-8'), object_hook=lambda d: Ride.from_dict(d)),
        'group_id': 'proxy:2551287',
        'api_version':(0, 10, 1)
    }
    # print(config)
    json_consumer = JsonConsumer(props=config)
    json_consumer.consume_from_kafka(topics=[KAFKA_TOPIC])