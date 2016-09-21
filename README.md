##Install Flask

```pip install Flask```

##Run 

```python MosesWS.py```

##Test

```curl  http://127.0.0.1:5000/translate?text=je%20suis%20un%20homme```

```
  {
    "text": "I am a man ",
    "word-align": [
      {
        "source-word": 0,
        "target-word": 0
      },
      {
        "source-word": 1,
        "target-word": 1
      },
      {
        "source-word": 2,
        "target-word": 2
      },
      {
        "source-word": 3,
        "target-word": 3
      }
    ]
  }
```
