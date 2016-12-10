# Scikit-vm

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[10]: https://github.com/gavinln/scikit-vm.git

## About

This project provides a [Ubuntu (14.04)][20] [Vagrant][30] Virtual Machine (VM) with numerical and scientific libraries for Python. It includes the following libraries.

[20]: http://releases.ubuntu.com/14.04/
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

There are [Ansible][120] scripts that automatically install the software when the VM is started.

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

4. Start the notebook

    ```bash
    /vagrant/scripts/jupyter_notebook.sh
    ```

5. Open the notebook in the browser at the URL.

    ```
    http://localhost:8888/
    ```

6. Open the **Index - Start Here** notebook  first

## Scikit-learn notebooks

### Scipy 2016

To get the Scikit learn [notebooks][130] from [Scipy 2016][140]. The video for
this conference is on [Youtube][150]

[130]: https://github.com/amueller/scipy-2016-sklearn
[140]: http://scipy2016.scipy.org/ehome/index.php?eventid=146062&tabid=332930
[150]: https://www.youtube.com/watch?list=PLYx7XA2nY5Gf37zYZMw6OqGFRPjB1jCy6&v=OB1reY6IX-o

1. Change to the notebooks directory

    ```
    cd /vagrant/notebooks
    ```

2. Get the notebooks into the directory pycon2015

    ```
    svn export http://github.com/amueller/scipy-2016-sklearn/trunk/notebooks scipy2016
    ```

3. In your Jupyter notebook list at http://localhost:8888/ the notebooks
will be in the scipy2016 directory.


### PyCon 2015

To get the Scikit learn [notebooks][170] from [PyCon 2015][180]. The video for
this conference is on [Youtube][190]


[170]: https://github.com/jakevdp/sklearn_pycon2015
[180]: https://us.pycon.org/2015/
[190]: https://www.youtube.com/watch?v=L7R4HUQ-eQ0

1. Change to the notebooks directory

    ```
    cd /vagrant/notebooks
    ```

2. Get the notebooks into the directory pycon2015

    ```
    svn export http://github.com/jakevdp/sklearn_pycon2015/trunk/notebooks pycon2015
    ```

3. In your Jupyter notebook list at http://localhost:8888/ the notebooks will
   be in the pycon2015 directory.

## Requirements

The following software is needed to get the software from github and run
Vagrant to set up the Python development environment. The Git environment
also provides an [SSH  client][200] for Windows.

* [Oracle VM VirtualBox][210]
* [Vagrant][220]
* [Git][230]

[200]: http://en.wikipedia.org/wiki/Secure_Shell
[210]: https://www.virtualbox.org/
[220]: http://vagrantup.com/
[230]: http://git-scm.com/
