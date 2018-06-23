# Changelog

## master

* Correction de l'exemple du Readme pour l'outil en ligne de commande.

## v0.2.0

Publiée le 23 juin 2018.

* Ajout de dossier ``dist/`` au ``.gitignore``.
* Changement de l'URL du projet (github).
* Ajout d'une option pour désactiver la transformation des espaces insécables en ``&nbsp;`` (#11).
* Ajout du support Python 3.7 (#10).
* État de l'art du support texte brut ou Markdown (#8).
* Correctif : Prise en compte de l'apostrophe précédée d'une majuscule + caractères accentués (même si ça ne devrait jamais arriver en principe).

## v0.1.0

Première release de ``typographeur``, publiée le 21 juin 2018.

Deux utilisations possibles. Via une fonction Python :

```python
>>> from typographeur import typographeur
>>> typographeur('<p>Exemple : <em>Salut ! ça va ?</em></p>')
"<p>Exemple&nbsp;: <em>Salut&nbsp;! ça va&nbsp;?</em></p>"
>>> typographeur('<strong>et , entre ( parenthèses  ...) les points sans espace  .</strong>')
"<strong>et, entre (parenthèses…) les points sans espace.</strong>"
```

ou via un outil en ligne de commande :

```sh
$ echo "<p>Salut! ça va?</p>" | typographeur
$ typographeur input.html
```

### Règles implémentées

* les signes `:`, `!`, `?` et `;` doivent être précédés d'une (et une seule) espace insécable.
* pas d'espace après une parenthèse ouvrante, ni avant une parenthèse fermante.
* les points de suspension `...` sont remplacés par le caractère `…` ; de même, on *nettoie* les doubles, triples, quadruples, n-uples points. Ça n'existe pas, c'est tout.
* pas d'espace avant un point (simple `.` ou `…`) ou une virgule (`,`).
* les guillemets doubles classiques ("") sont remplacés par des chevrons («»). À noter l'utilisation d'espaces insécables à l'intérieur des guillemets français.
* les apostrophes `'` sont changées en `’` et ne doivent pas être suivies d'espaces.

Ces règles sont désactivables via les options de la fonction ``typographeur()`` ou les options de l'outil en lignes de commande.

Les blocs encadrés par les balises `pre`, `samp`, `code`, `tt`, `kbd`, `script`, `style`, `math` ne seront pas corrigés, pour que les bouts de code soient affichés sans être déteriorés ; et que les éventuels scripts JS ne présentent pas d'erreur de syntaxe.
