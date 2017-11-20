# Installation sur conda


    conda install conda-build

aller dans le répertoire `calculator`

    conda skeleton pypi recipes

(crée un répertoire recipes contenant un fichier meta.yaml à modifier)

Copier les fichiers si nécessaire (pas ici)

- build.sh : https://conda.io/docs/_downloads/build1.sh
- build.bat : https://conda.io/docs/_downloads/bld.bat

Normalement il n'est pas nécessaire d'avoir ces fichiers pour une installation de type pypi puisque l'installation est la même commande pour linux et windows

    python setup.py install

Une fois les fichiers du répertoire recipes modifiés, il faut exécuter la commande suivante

    conda build recipes

Pour tester en local

    conda install --use-local calculator

Pour mettre en ligne

    conda install anaconda-client
    anaconda upload /home/loic/miniconda3/conda-bld/linux-64/calculator-0.1.1-py36h585410b_0.tar.bz2

Pour voir le fichier yaml final

    conda render recipes

