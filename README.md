# deepl-translator
Easily use the deepl translator from python

## Install requirements
```
  pip install requests
```

## Use
Import and instance:
```python
from deepl_translator import DeeplTranslator

translator = DeeplTranslator(api_key="YOUR_API_KEY_HERE")
```

Get account info:
```python
result = translator.get_info()
```

Simple sentence translation:
```python
result = translator.translate(
    text="Happy Coding", source_lang=translator.EN, target_lang=translator.IT)
```

Auto detect source language:
```python
result = translator.translate(
    text="Happy Coding", target_lang=translator.IT)
```

Translate many sentences:
```python

result = translator.translate(
    text=["Hi guys", "Happy Coding", "Bye Bye"], target_lang=translator.IT)
```
