# Changelog

## master

* Construction d'un wheel "non-universel" (comprendre : uniquement pour Python 3+).

## v0.5.0

Publiée le 26 juin 2020.

### Changements annexes

* Petites corrections qui évitent l'affichage de messages d'attentions [warning]
* Ajout du support de Python 3.8

## v0.4.0

Publiée le 28 juillet 2018.

### Nouvelle règle

* Ajout de la règle de correction des ligatures en `œ` et `æ` (#2).

## v0.3.0

Publiée le 10 juillet 2018.

### Nouvelles règles

* Correction des doubles, triples, quadruples, nuples points d'exclamation et d'interrogation (#17).
* Un titre ne doit pas se terminer par un point (#19).

### Corrections sur les règles

* Deux points encadrés par des crochets sont des ellipses acceptables et ne doivent pas être remplacés par "…" (#13).
* Les balises autofermées HTML ne comptent pas comme débuts de blocs à ignorer (#15).
* Avant un point-virgule, un point d'interrogation ou un point d'exclamation, on insère une espace fine insécable (#14).

### Autres changements

* **Retrait du support de Markdown** au moins jusqu'à ce qu'on trouve un moyen de parser le fichier simplement. Désolé.
* Ajout d'un "classifier" (Topic :: Text Processing :: Markup :: HTML).
* Instructions d'installation dans le README.
* Correction de l'exemple du README pour l'outil en ligne de commande.
* Correction d'une petite faute de typo dans l'aide de l'outil en ligne de commande et reformulation.
* Ajout de gabarits pour la création de rapports de bogue ou de demandes de fonctionnalités (#18).
* Ajout d'un gabarit pour la création de "pull-requests".

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
