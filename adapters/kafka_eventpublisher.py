from dataclasses import asdict
import json
from confluent_kafka import Producer
from domain.events import Event
import pickle

p=Producer({'bootstrap.servers': 'localhost:9092'})

def publish(topic, event: Event):
    topic = 'event-topic'
    print(f"Publishing: topic:{topic}, Event:{event}")
    b_event = pickle.dumps(event)
    p.poll(1)
    p.produce(topic, b_event)
    p.flush()


