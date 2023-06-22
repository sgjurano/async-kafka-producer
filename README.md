Нужно дописать недостающий код в файле producer.py таким образом, чтобы класс обеспечивал
асинхронный интерфейс для записи json-сообщений в кафку.

Инструкция по интеграции от confluent:\
https://www.confluent.io/blog/kafka-python-asyncio-integration/

Поднять кафку локально можно вот так:\
`docker-compose up -d`

Создать топик для записи в него (запускать надо из контейнера с кафкой):\
`kafka-topics.sh --create --topic test --bootstrap-server localhost:9092`

Подписаться на топик (предварительно kafkacat надо установить):\
`kafkacat -b localhost -C -t test`

Если возникает проблема с резолвингом id контейнера при вызове kafkacat, то его можно
закинуть в `/etc/hosts` как `127.0.0.1`.

Чтобы запустить программу достаточно сделать следующее:
```bash
python producer.py
```

При успешном выполнении программы, она корректно завершится, а в терминале будет видно сообщение:\
```bash
kafkacat -b localhost -C -t test                 
% Reached end of topic test [0] at offset 0
{"test": 42}
```