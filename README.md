# Scikit-vm

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[10]: https://github.com/gavinln/scikit-vm.git

## About

This project provides a [Ubuntu (16.04)][20] [Vagrant][30] Virtual Machine
(VM) with numerical and scientific libraries for Python. It includes the
following libraries.

[20]: http://releases.ubuntu.com/16.04/
[30]: http://www.vagrantup.com/

* [Numpy][40]
* [Scipy][50]
* [Jupyter notebook][60]
* [Pandas][70]
* [Scikit learn][80]

[40]: http://www.numpy.org/
[50]: http://www.scipy.org/
[60]: http://jupyter.org/
[70]: http://pandas.pydata.org/
[80]: http://scikit-learn.org/stable/

### Visualization libraries

* [Matplotlib][100]
* [Seaborn][110]

[100]: http://matplotlib.org/
[110]: http://stanford.edu/~mwaskom/software/seaborn/

There are [Ansible][120] scripts that automatically install the software when
the VM is started.

[120]: https://www.ansible.com/

## Running

1. Change to the root of the project

    ```
    cd scikit-vm
    ```

2. To start the virtual machine(VM) type

    ```
    vagrant up
    ```

3. Connect to the VM

    ```
    vagrant ssh
    ```

4. Install Jupyter notebook extensions

    ```
    jupyter contrib nbextension install --user
    ```

5. Install vim extension (optional)

    ```
    cd $(jupyter --data-dir)/nbextensions
    git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding
    ```

6. Start the notebook

    ```bash
    /vagrant/scripts/jupyter_notebook.sh
    ```

7. Open the notebook in the browser at the URL

8. Open the **Index - Start Here** notebook  first

## Scikit-learn notebooks

### Scipy 2018

The Scikit-learn tutorial is in two videos

* Machine learning with Scikit-Learn [Part 1][200]
* Machine learning with Scikit-Learn [Part 2][210]

[200]: https://www.youtube.com/watch?v=4PXAztQtoTg
[210]: https://www.youtube.com/watch?v=gK43gtGh49o

The notebooks are in a Github project called [scipy-2018-sklearn][220]

[220]: https://github.com/amueller/scipy-2018-sklearn

To get the notebooks run the following


1. Change to the notebooks directory

    ```
    cd /vagrant/notebooks
    ```

2. Get the notebooks into the directory scipy2018

    ```
    svn export https://github.com/amueller/scipy-2018-sklearn/trunk/notebooks scipy2018
    ```

3. In your Jupyter notebook list at http://192.168.33.10:8888/ the notebooks
will be in the scipy2018 directory.

### Scipy 2017

To get the Scikit learn [notebooks][230] from [Scipy 2017][240]. The video for
this conference is on [Youtube][250]

[230]: https://github.com/amueller/scipy-2017-sklearn
[240]: https://scipy2017.scipy.org/ehome/index.php?eventid=220975&
[250]: https://www.youtube.com/watch?v=2kT6QOVSgSg

1. Change to the notebooks directory

    ```
    cd /vagrant/notebooks
    ```

2. Get the notebooks into the directory scipy2017

    ```
    svn export https://github.com/amueller/scipy-2017-sklearn/trunk/notebooks scipy2017
    ```

3. In your Jupyter notebook list at http://192.168.33.10:8888/ the notebooks
will be in the scipy2017 directory.

### Scipy 2016

To get the Scikit learn [notebooks][260] from [Scipy 2016][270]. The video for
this conference is on [Youtube][280]

[260]: https://github.com/amueller/scipy-2016-sklearn
[270]: http://scipy2016.scipy.org/ehome/index.php?eventid=146062&tabid=332930
[280]: https://www.youtube.com/watch?list=PLYx7XA2nY5Gf37zYZMw6OqGFRPjB1jCy6&v=OB1reY6IX-o

1. Change to the notebooks directory

    ```
    cd /vagrant/notebooks
    ```

2. Get the notebooks into the directory scipy2016

    ```
    svn export http://github.com/amueller/scipy-2016-sklearn/trunk/notebooks scipy2016
    ```

3. In your Jupyter notebook list at http://192.168.33.10:8888/ the notebooks
will be in the scipy2016 directory.


### PyCon 2015

To get the Scikit learn [notebooks][290] from [PyCon 2015][300]. The video for
this conference is on [Youtube][310]


[290]: https://github.com/jakevdp/sklearn_pycon2015
[300]: https://us.pycon.org/2015/
[310]: https://www.youtube.com/watch?v=L7R4HUQ-eQ0

1. Change to the notebooks directory

    ```
    cd /vagrant/notebooks
    ```

2. Get the notebooks into the directory pycon2015

    ```
    svn export http://github.com/jakevdp/sklearn_pycon2015/trunk/notebooks pycon2015
    ```

3. In your Jupyter notebook list at http://192.168.33.10:8888/ the notebooks will
   be in the pycon2015 directory.

## Miscellaneous topics

### Statistical distances

* https://www.youtube.com/watch?v=U7xdiGc7IRU&list=PLYx7XA2nY5Gd-tNhm79CNMe_qvi35PgUR

#### Kolmogorov–Smirnov test

* https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test

#### Earth Mover's distance

* https://en.wikipedia.org/wiki/Earth_mover%27s_distance

#### Kullback–Leibler divergence

* https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

## Requirements

The following software is needed to get the software from github and run
Vagrant to set up the Python development environment. The Git environment
also provides an [SSH  client][400] for Windows.

* [Oracle VM VirtualBox][410]
* [Vagrant][420] version 1.9.1 or higher
* [Git][430]

[400]: http://en.wikipedia.org/wiki/Secure_Shell
[410]: https://www.virtualbox.org/
[420]: http://vagrantup.com/
[430]: http://git-scm.com/
