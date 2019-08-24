# Scikit-vm

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[10]: https://github.com/gavinln/scikit-vm.git

## About

This project provides a [Ubuntu (18.04)][20] [Vagrant][30] Virtual Machine
(VM) with numerical and scientific libraries for Python. It includes the
following libraries.

[20]: http://releases.ubuntu.com/18.04/
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
5. Go to the Edit menu nbextensions config option to setup plugins

6. Some useful plugins

    * Code prettify
    * Collapsible Headings
    * Comment/Uncomment Hotkey
    * ExecuteTime
    * Select CodeMirror Keymap
    * Table of Contents (2)

7. Start the Jupyter notebook or Jupyterlab environment

```bash
/vagrant/scripts/jupyter_notebook.sh
```

8. Open the notebook in the browser at the URL

### Jupyterlab

1. Install Jupyterlab vim extension (optional)

```
sudo jupyter labextension install jupyterlab_vim
```
2. Start the Jupyterlab environment

```bash
/vagrant/scripts/lab_notebook.sh
```

## Scikit-learn notebooks

### Scipy 2018

The [SciPy 2018][200] conference has two tutorials on using the Scikit-learn
library. There are two videos: [Video 1][210] and [Video 2][220]

[200]: https://scipy2018.scipy.org/ehome/index.php?eventid=299527
[210]: https://www.youtube.com/watch?v=4PXAztQtoTg
[220]: https://www.youtube.com/watch?v=gK43gtGh49o

The notebooks are in a Github project called [scipy-2018-sklearn][230]

[230]: https://github.com/amueller/scipy-2018-sklearn

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

To get the Scikit learn [notebooks][240] from [Scipy 2017][250]. The video for
this conference is on [Youtube][260]

[240]: https://github.com/amueller/scipy-2017-sklearn
[250]: https://scipy2017.scipy.org/ehome/index.php?eventid=220975&
[260]: https://www.youtube.com/watch?v=2kT6QOVSgSg

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

To get the Scikit learn [notebooks][360] from [Scipy 2016][370]. The video for
this conference is on [Youtube][380]

[360]: https://github.com/amueller/scipy-2016-sklearn
[370]: http://scipy2016.scipy.org/ehome/index.php?eventid=146062&tabid=332930
[380]: https://www.youtube.com/watch?list=PLYx7XA2nY5Gf37zYZMw6OqGFRPjB1jCy6&v=OB1reY6IX-o

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

### Text tutorial

1. Change to the text notebooks directory

```
cd /vagrant/notebooks/text_processing
```

2. Get the text examples code and data

```
svn export https://github.com/scikit-learn/scikit-learn/trunk/doc/tutorial/text_analytics/skeletons skeletons
svn export https://github.com/scikit-learn/scikit-learn/trunk/doc/tutorial/text_analytics/data data
```

## Plotting

### Interactive charts with Plotly

[Plotly.js][500] is an open source Javascript plotting library.
[Plotly.py][510] is a Python wrapper over the Plotly javascript plotting
library. [Plotly express][520] is a high-level wrapper around the Plotly Python
library for rapid data exploration and plotting. It uses Pandas dataframes to
transfer data to Plotly.

[500]: https://plot.ly/javascript/
[510]: https://plot.ly/python/
[520]: https://www.plotly.express/

1. Change to the notebooks directory

```
cd /vagrant/notebooks
```

2. Get the notebooks into the directory px-plot directory

```
svn export https://github.com/plotly/plotly_express/branches/gh-pages px-plot
rm -rf px-plot/plotly_express
```

3. In your Jupyter notebook list at http://192.168.33.10:8888/ the notebooks
   will be in the px-plot directory.

An introduction to plotly express is given in this [article][530]. Alternative
libraries that wrap the low-level Plotly libraries are discussed on this
[page][540].

[530]: https://medium.com/@plotlygraphs/introducing-plotly-express-808df010143d
[540]: https://towardsdatascience.com/its-2019-make-your-data-visualizations-interactive-with-plotly-b361e7d45dc6

https://github.com/jonmmease/plotly_ipywidget_notebooks

### Seaborn

## Miscellaneous

To generate a requirements.txt file run the following

```
python ansible\convert-ansible-to-requirements.py  > requirements.txt
```

To create a Pipfile on the Windows subsystem for Linux and choose the correct
Python

```
pipenv --python $(which python3)
pipenv install --python /usr/bin/python3
```

To install the libraries manually type:

```
pipenv install sklearn pandas jupyter
```

ls

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
