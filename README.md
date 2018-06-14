# Typographeur

> Faire respecter les règles typographiques françaises en HTML.

Status: Pre-Alpha

## Utilisation

```python
>>> from typographeur import typographeur
>>> typographeur('<p>Exemple : <em>Salut ! ça va ?</em></p>')
"<p>Exemple&nbsp;: <em>Salut&nbsp;! ça va&nbsp;?</em></p>"
>>> typographeur('<strong>et , entre ( parenthèses  ...) les points sans espace  .</strong>')
"<strong>et, entre (parenthèses…) les points sans espace.</strong>"
```

## Origine

Cette bibliothèque a pour but de faire appliquer les règles de base de la typographie française sur des documents au format HTML. Elle s'inspire du projet SmartyPants, et lui emprunte une partie du code.

* [SmartyPants, le projet initial](https://daringfireball.net/projects/smartypants/)
* [smartypants.py, le fork le plus à jour](https://pypi.org/project/smartypants/)

## Tester

Pour tester, lancer (de préférence dans un virtualenv):

```sh
make test
```

Un exemple complet des correctifs que peut produire `typographeur` est disponible dans le dossier `tests/examples/`. On y trouve un fichier `input.html`, qui contient de nombreuses fautes de typographie, et `expected.html`, qui est le résultat attendu après corerection.

## Licence

Ce projet est librement utilisable, publié sous licence MIT.

-----

In *English*, now: this library tries to apply basic French typography rules. It's vastly inspired by SmartyPants, and borrows a lot of code from it.

* [Initial SmartyPants project](https://daringfireball.net/projects/smartypants/)
* [Current smartypants.py code](https://pypi.org/project/smartypants/)

MIT License.
