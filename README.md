# Typographeur

> Faire respecter les règles typographiques françaises en HTML.

Status: Beta

[![Build Status](https://travis-ci.org/brunobord/typographeur.svg?branch=master)](https://travis-ci.org/brunobord/typographeur)
![Python versions: 3.6, 3.7](https://img.shields.io/pypi/pyversions/typographeur.svg)

Compatibilité : Python 3.6 et 3.7.

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

## Règles implémentées

* les signes `:`, `!`, `?` et `;` doivent être précédés d'une (et une seule) espace insécable.
* pas d'espace après une parenthèse ouvrante, ni avant une parenthèse fermante.
* les points de suspension `...` sont remplacés par le caractère `…` ; de même, on *nettoie* les doubles, triples, quadruples, n-uples points. Ça n'existe pas, c'est tout.
* pas d'espace avant un point (simple `.` ou `…`) ou une virgule (`,`).
* les guillemets doubles classiques ("") sont remplacés par des chevrons («»). À noter l'utilisation d'espaces insécables à l'intérieur des guillemets français.
* les apostrophes `'` sont changées en `’` et ne doivent pas être suivies d'espaces.

Pour votre plaisir, un document HTML qui respecte les règles énoncées ci-dessus restera inchangé.

Les blocs encadrés par les balises `pre`, `samp`, `code`, `tt`, `kbd`, `script`, `style`, `math` ne seront pas corrigés, pour que les bouts de code soient affichés sans être déteriorés ; et que les éventuels scripts JS ne présentent pas d'erreur de syntaxe.

### Paramètres

Chaque règle peut être désactivée via le paramétrage de la fonction ``typographeur()`` :

* ``fix_parenthesis`` : appliquer la règle pour les parenthèse.
* ``fix_colon`` : appliquer la règle pour les deux-points (:).
* ``fix_exclamation`` : appliquer la règle pour les points d'exclamation (!).
* ``fix_interrogation`` : appliquer la règle pour les points d'interrogation (?).
* ``fix_semicolon`` : appliquer la règle pour les points-virgules (;).
* ``fix_ellipsis`` : appliquer la règle pour les points de suspension (... -> …).
* ``fix_point_space`` : supprimer les espaces avant les points (… ou .).
* ``fix_comma_space`` : supprimer les espaces avant les virgules (,).
* ``fix_double_quote`` : transformer les guillemets doubles en chevrons.
* ``fix_apostrophes`` : transformer les apostrophes "dactylographiques" en apostrophes "typographiques",
* ``fix_nbsp`` : les espaces insécables ne seront pas converties en entités HTML, mais laissées telles quelles.

## Outil en ligne de commande

Une fois installé, le paquet propose un outil en ligne de commande. Exemples d'utilisation :

```sh
$ echo "<p>Salut! ça va?</p>" | typographeur
<p>Salut&nbsp; ça va&nbsp;?</p>
```

On peut également passer un ou plusieurs fichiers en tant que paramètres :

```sh
$ typographeur input1.html input2.html
```

Par défaut, tous les paramètres de la fonction ``typographeur()`` sont activés. On peut les désactiver via les options suivantes :

* ``--skip-parenthesis``,
* ``--skip-colon``,
* ``--skip-exclamation``,
* ``--skip-interrogation``,
* ``--skip-semicolon``,
* ``--skip-ellipsis``,
* ``--skip-point-space``,
* ``--skip-comma-space``,
* ``--skip-double-quote``,
* ``--skip-apostrophes``.
* ``--skip-nbsp``.

Toutes les options disponibles sont visibles via :

```sh
$ typographeur --help
```

### Limitations

L'objectif de cette bibliothèque reste modeste : il est vraisemblable que certaines règles typographiques ne pourront jamais être implémentées et nous ne cherchons pas ici la perfection. Elle restera une sorte "d'aide à la rédaction", mais rien ne remplacera jamais l'application manuelle des ces règles. Les ouvrages ou les sites de référence sont légions, il est bien vain d'essayer de les lister tous : une simple recherche vous en convaincra. Bon courage !

#### Support du texte brut ou Markdown

Bien que non-testée, la bibliothèque est supposée corriger les textes « bruts » (markdown, par exemple) aussi bien que le HTML, dans une certaine limite. A priori, il vaut mieux désactiver l'option qui corrige les espaces insécables.

Avec la fonction :

```python
>>> from typographeur import typographeur
>>> typographeur('Il lui *demanda*    : "ça va?" , elle répondit: "oui !"', fix_nbsp=False)
'Il lui *demanda*\xa0: «\xa0ça va\xa0?\xa0», elle répondit\xa0: «\xa0oui\xa0!\xa0»'
```

Avec l'outil en ligne de commande :

```sh
echo 'Il lui *demanda*    : "ça va?" , elle répondit: "oui !"' | typographeur --skip-nbsp
Il lui *demanda* : « ça va ? », elle répondit : « oui ! »
```

Autre limitation : les blocs de code encadrés par des triples-antiquotes ne seront pas proprement échappées.

Des exemples complets se trouvent dans les fichiers en ``.md`` dans le dossier `tests/examples/`.

## Autres implémentations

Des fonctionnalités similaires ont été implémentées dans d'autres langages de programmation. À noter :

* [JoliTypo](https://github.com/jolicode/JoliTypo), en PHP,
* [Cette extension pour Jekyll](https://github.com/borisschapira/jekyll-microtypo/blob/master/lib/jekyll/microtypo.rb), en Ruby.

*Autre ressource :*

[Grammalecte](https://www.dicollecte.org/) est une extension pour LibreOffice, Firefox et Thunderbird pour aider à corriger (entre autres) les fautes de typographie.

## Licence

Ce projet est librement utilisable, publié sous licence MIT.

-----

In *English*, now: this Python (3.6 & 3.7) library tries to apply basic French typography rules. It's vastly inspired by SmartyPants, and borrows a lot of code from it.

* [Initial SmartyPants project](https://daringfireball.net/projects/smartypants/)
* [Current smartypants.py code](https://pypi.org/project/smartypants/)

MIT License.
