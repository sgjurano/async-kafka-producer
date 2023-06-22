import asyncio
from asyncio import Future
from functools import partial
from threading import Thread

from confluent_kafka import SerializingProducer
from confluent_kafka import Message

CONFIG = {
    'bootstrap.servers': "localhost:9092",  # here you may pass yor own brokers
    'acks': 'all',
}


# https://www.confluent.io/blog/kafka-python-asyncio-integration/
class KafkaProducer:
    POLL_TIMEOUT_SECONDS: float = 0.01

    def __init__(self, config: dict):
        self._producer = SerializingProducer(config)

    async def connect(self):
        # YOUR CODE GOES HERE
        ...

    async def disconnect(self):
        # YOUR CODE GOES HERE
        ...

    async def publish(self, body: dict, topic: str) -> None:
        # YOUR CODE GOES HERE
        ...


async def main():
    p = KafkaProducer(CONFIG)
    await p.connect()
    await p.publish({"test": 42}, "test")
    await p.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
