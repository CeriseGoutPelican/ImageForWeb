Ce petit script python vous permet de réduire vos images et/ou d'ajouter une watermark dessus afin de pouvoir les publier en ligne sans souci !
Ce script, encore basic, sera sans doute mis à jour au fur et à mesure selon vos besoins. N'hésitez pas à proposer des mises à jour sur Github.

## Installation
Premièrement il vous faudra installer Python 2.7.x, ce que vous pouvez faire directement sur le site officiel python.org (rien de plus simple) : https://www.python.org/

Ensuite il fadra installer la dépendance Image du module PILLOW à l'aide de pip. Faites Windows+R puis tapez `cmd` pour ouvrir l'invité de commande. Insérez ensuite les lignes suivantes (sans le $) :
```shell
$ pip install Image
```
## Utilisation
L'utilisation est très simple :
1. Faites glisser-déposer le fichier ImageForWeb.py dans le dossier où se trouve vos photos
2. Faites MAJ+clique droit quelque part dans le dossier puis "Ouvrir l'invité de commande"
3. Ecrivez les lignes suivantes dans le cmd :
```shell
$ python ImpageForWeb.py
```
4. Puis suivez les instructions ! Vos images éditées seront mises dans un nouveau sous-dossier nommé "web"
