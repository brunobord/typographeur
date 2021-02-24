# Typographeur

> Faire respecter les règles typographiques françaises en HTML.

Status: Beta

[![Build Status](https://travis-ci.org/brunobord/typographeur.svg?branch=master)](https://travis-ci.org/brunobord/typographeur)
![Python versions: 3.6, 3.7, 3.8 et 3.9](https://img.shields.io/pypi/pyversions/typographeur.svg)

Compatibilité : Python 3.6, 3.7, 3.8 et 3.9.

## Installation

Comme d'autres paquets Python, Typographeur s'installe à l'aide de ``pip``, de préférence dans un ``virtualenv`` :

```sh
pip install typographeur
```

Pour contribuer ou "faire mumuse" avec ce code, [clonez le dépôt Github](https://github.com/brunobord/typographeur) et installez-le en mode "dev" dans l'environnement courant :

```sh
git clone git@github.com:brunobord/typographeur.git
cd typographeur
pip install -e ./
```


## Utilisation

```python
>>> from typographeur import typographeur
>>> typographeur('<p>Exemple : <em>Salut ! ça va ?</em></p>')
'<p>Exemple&nbsp;: <em>Salut&#8239;! ça va&#8239;?</em></p>'
>>> typographeur('<strong>et , entre ( parenthèses  ...) les points sans espace  .</strong>')
'<strong>et, entre (parenthèses…) les points sans espace.</strong>'
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

* les signes `!`, `?` et `;` doivent être précédés d'une (et une seule) espace fine insécable.
* le signe `:` doit être précédé d'une espace insécable.
* pas d'espace après une parenthèse ouvrante, ni avant une parenthèse fermante.
* les points de suspension `...` sont remplacés par le caractère `…` ; de même, on *nettoie* les doubles, triples, quadruples, n-uples points. Le seul cas particulier, c'est celui de deux points encadrés par des crochets, dans le cas de l'ellipse d'une citation : ``[..]``.
* Pour les points d'exclamation ou d'interrogation, la règle c'est d'en afficher un ou trois, mais jamais deux ou "n".
* pas d'espace avant un point (simple `.` ou `…`) ou une virgule (`,`).
* les guillemets doubles classiques ("") sont remplacés par des chevrons («»). À noter l'utilisation d'espaces insécables à l'intérieur des guillemets français.
* les apostrophes `'` sont changées en `’` et ne doivent pas être suivies d'espaces.
* les mots contenant des ligatures seront corrigés (`oe` => `œ` et `ae` => `æ`). Pour ce faire, nous utilisons le dictionnaire fourni par [Dicollecte](https://www.dicollecte.org/).

Pour votre plaisir, un document HTML qui respecte les règles énoncées ci-dessus restera inchangé.

Les blocs encadrés par les balises `pre`, `samp`, `code`, `tt`, `kbd`, `script`, `style`, `math` ne seront pas corrigés, pour que les bouts de code soient affichés sans être déteriorés ; et que les éventuels scripts JS ne présentent pas d'erreur de syntaxe. À noter que les balises autofermantes (exemple : ``<code />``) ne comptent pas comme début de blocs à ignorer.

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
* ``fix_nuples`` : appliquer les règles sur les points d'exclamation et d'interrogation multiples.
* ``fix_title_points`` : appliquer la règle interdisant les points à la fin d'un titre.
* ``fix_oe`` : appliquer la règle des ligatures sur les mots en `œ`.
* ``fix_ae`` : appliquer la règle des ligatures sur les mots en `æ`.
* ``ligature_variant`` : désigne quel variante du dictionnaire utiliser pour la correction des ligatures. Il en existe 4 : 'classique', 'moderne', 'reforme1990' et 'toutesvariantes' (par défaut).

## Outil en ligne de commande

Une fois installé, le paquet propose un outil en ligne de commande. Exemples d'utilisation :

```sh
$ echo '<p>Salut! ça va?</p>' | typographeur
<p>Salut&#8239;! ça va&#8239;?</p>
```

On peut également passer un ou plusieurs fichiers en tant que paramètres :

```sh
$ typographeur input1.html input2.html
```

Toutes les options disponibles et leurs textes d'aide sont visibles via :

```console
$ typographeur --help
```

Par défaut, tous les paramètres booléens de la fonction ``typographeur()`` sont activés. On peut les désactiver via les options suivantes :

* ``--skip-parenthesis``,
* ``--skip-colon``,
* ``--skip-exclamation``,
* ``--skip-interrogation``,
* ``--skip-semicolon``,
* ``--skip-ellipsis``,
* ``--skip-point-space``,
* ``--skip-comma-space``,
* ``--skip-double-quote``,
* ``--skip-apostrophes``,
* ``--skip-nbsp``,
* ``--skip-nuples``,
* ``--skip-title-points``,
* ``--skip-oe``,
* ``--skip-ae``,
* ``--ligature-variant``.

### Ignorer certaines balises

L'option ``--show-default-skip-tags`` affiche la liste des balises HTML qui seront ignorées. Cela signifie qu'à l'intérieur de ces balises, `typographeur` ne cherchera pas à corriger le contenu en utilisant les règles.

Exemple :

```console
$ typographeur --show-default-skip-tags
pre,samp,code,tt,kbd,script,style,math
```

On peut définir soi-même les balises qu'on veut ignorer. Les noms des balises à ignorer sont séparés par des virgules.

*Note :* les noms des balises peuvent aussi être séparés par des espaces, et seront dé-doublonnées.

Voici un premier exemple sans l'option :

```console
$ echo '<pre>Corrigé?</pre> <b>Pas corrigé?</b> <code>Pas Corrigé!</code>' | typographeur
<pre>Corrigé?</pre> <b>Pas corrigé&#8239;?</b> <code>Pas Corrigé!</code>
```

En indiquant qu'on veut ignorer les balises ``<b>`` et ``<code>`` :

```console
$ echo '<pre>Corrigé?</pre> <b>Pas corrigé?</b> <code>Pas Corrigé!</code>' | typographeur --skip-tags="b,code"
<pre>Corrigé&#8239;?</pre> <b>Pas corrigé?</b> <code>Pas Corrigé!</code>
```

Vous aurez constaté que seuls le contenu de la balise ``<pre>`` a été corrigé.

Si vous voulez corriger toutes les balises par défaut + vos balises personnelles, vous pourrez le faire comme suit :

```console
$ echo '<pre>Corrigé?</pre> <b>Pas corrigé?</b> <code>Pas Corrigé!</code>' | typographeur --skip-tags="$(typographeur --show-default-skip-tags),b,em,strong"
<pre>Corrigé?</pre> <b>Pas corrigé?</b> <code>Pas Corrigé!</code>
```

### Limitations

L'objectif de cette bibliothèque reste modeste : il est vraisemblable que certaines règles typographiques ne pourront jamais être implémentées et nous ne cherchons pas ici la perfection. Elle restera une sorte "d'aide à la rédaction", mais rien ne remplacera jamais l'application manuelle des ces règles. Les ouvrages ou les sites de référence sont légions, il est bien vain d'essayer de les lister tous : une simple recherche vous en convaincra. Bon courage !

## Support du texte brut ou Markdown

**Attention :** le support de Markdown est à notre grand regret abandonné. Les tentatives jusqu'ici impliquaient une gestion des blocs simples en parcourant le contenu le plus simplement possible à l'aide d'expressions rationnelles. Mais la muraille infranchissable, c'est le tableau (disponible en *Github Flavored Markdown* et dans d'autres parsers).

**Dans nos projets :** une bibliothèque tierce, qui utilisera un parser Markdown pour faire un rendu Markdown "typographié". Restez à l'écoute !

## Autres implémentations

Des fonctionnalités similaires ont été implémentées dans d'autres langages de programmation. À noter :

* [JoliTypo](https://github.com/jolicode/JoliTypo), en PHP,
* [Cette extension pour Jekyll](https://github.com/borisschapira/jekyll-microtypo/blob/master/lib/jekyll/microtypo.rb), en Ruby.

*Autre ressource :*

[Grammalecte](https://www.dicollecte.org/) est une extension pour LibreOffice, Firefox et Thunderbird pour aider à corriger (entre autres) les fautes de typographie.

## Licence

Ce projet est librement utilisable, publié sous licence MIT.

-----

In *English*, now: this Python (3.6, 3.7, 3.8 & 3.9) library tries to apply basic French typography rules. It's vastly inspired by SmartyPants, and borrows a lot of code from it.

* [Initial SmartyPants project](https://daringfireball.net/projects/smartypants/)
* [Current smartypants.py code](https://pypi.org/project/smartypants/)

MIT License.
