# Typographeur

> Faire respecter les règles typographiques françaises en HTML.

## Utilisation

```python
>>> from typographeur import correcteur
>>> correcteur('<p>Exemple : <em>Salut ! ça va ?</em></p>')
"<p>Exemple&nbsp;: <em>Salut&nbsp;! ça va&nbsp;?</em></p>"
```

-----

In English, now

## Usage

```python
>>> from typographeur import correcteur
>>> correcteur('<p>Exemple : <em>Salut ! ça va ?</em></p>')
"<p>Exemple&nbsp;: <em>Salut&nbsp;! ça va&nbsp;?</em></p>"
```
