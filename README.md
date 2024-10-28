# API Performance testing sandbox

My playground for tools to test REST API performance

## Locust

Start the test app:
```
fastapi dev main.py
```

Start the locust app:
```
cd locust
locust
```

Open the locust app at [http://localhost:8089/](http://localhost:8089/), then click *Start*

[Locust Output Example](locust_example.png)

## Postman

Postman requires almost no configuration. You just run a collection and it returns the results.
It's not as pretty as Locust.

[Postman Output Example](postman_example.png)
