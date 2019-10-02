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

### Jupyter notebook

1. Install Jupyter notebook extensions

```
jupyter contrib nbextension install --user
```

2. Go to the Edit menu nbextensions config option to setup plugins

3. Some useful plugins

    * Code prettify
    * Collapsible Headings
    * Comment/Uncomment Hotkey
    * ExecuteTime
    * Select CodeMirror Keymap
    * Table of Contents (2)

4. Start the Jupyter notebook or Jupyterlab environment

```bash
/vagrant/scripts/notebook-jupyter.sh
```

5. Open the notebook in the browser at the URL

### Jupyterlab

1. Enable the server extension

```
jupyter labextension install @jupyterlab/shortcutui
jupyter labextension install @jupyter-widgets/Jupyterlab-manager
jupyter labextension install @Jupyterlab/shortcutui
jupyter labextension install @Jupyterlab/toc
jupyter labextension install jupyterlab-jupytext
jupyter labextension install jupyterlab_vim
jupyter labextension install @krassowski/jupyterlab_go_to_definition

# pip install nbresuse  # displays memory usage on the bottom status bar

# pip install jupyterlab_code_formatter
jupyter labextension install @ryantam626/jupyterlab_code_formatter
# jupyter serverextension enable --py jupyterlab_code_formatter
```

2. Setup the keyboard shortcut in the "Advanced Settings Editor"

```
{
    "shortcuts": [{
            "command": "jupyterlab_code_formatter:yapf",
            "keys": ["Ctrl Shift G"],
            "selector": ".jp-Notebook.jp-mod-editMode"
        }
    ]
}
```

3. Start the Jupyter lab interface
./scripts/lab-jupyter.sh

4. Install these Jupyter extensions

    * @jupyter-widgets/Jupyterlab-manager
    * @Jupyterlab/shortcutui
    * @Jupyterlab/toc
    * jupyterlab-jupytext
    * jupyterlab_vim
    * @ryantam626/jupyterlab_code_formatter

[nbresuse](https://github.com/yuvipanda/nbresuse)

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

### Matplotlib

* [Matplotlib][400]

[400]: http://matplotlib.org/

### Seaborn

* [Seaborn][410]

[410]: http://stanford.edu/~mwaskom/software/seaborn/

### Plotly

[Plotly.js][500] is an open source Javascript plotting library.
[Plotly.py][510] is a Python wrapper over the Plotly javascript plotting
library. [Plotly express][520] is a high-level wrapper around the Plotly Python
library for rapid data exploration and plotting. It uses Pandas dataframes to
transfer data to Plotly.

[500]: https://plot.ly/javascript/
[510]: https://plot.ly/python/
[520]: https://www.plotly.express/

An introduction to plotly express is given in this [article][530]. Alternative
libraries that wrap the low-level Plotly libraries are discussed on this
[page][540].

[530]: https://medium.com/@plotlygraphs/introducing-plotly-express-808df010143d
[540]: https://towardsdatascience.com/its-2019-make-your-data-visualizations-interactive-with-plotly-b361e7d45dc6

https://github.com/jonmmease/plotly_ipywidget_notebooks

### Lolviz

Visualize data structures

https://github.com/parrt/lolviz

### Bokeh

### Dimensionality reduction

Dimensionality reduction similar to t-SNE

[Uniform Manifold Approximation and Projection](https://github.com/lmcinnes/umap)

## Creating dashboards

The dashboards not only display data but also accept simple user inputs.

* [Dash][600]
* [Voila][610]
* [Panel][620]

[600]: https://github.com/plotly/dash
[610]: https://github.com/QuantStack/voila
[620]: https://github.com/pyviz/panel

## Extending pandas

* [Cyberpandas][700] - supports IP addresses
* [GeoPandas][710] - supports geographic data

[700]: https://github.com/ContinuumIO/cyberpandas
[710]: https://github.com/geopandas/geopandas

## Jupyterlab tips

* [Working efficienctly with Jupyterlab](https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/)
* [Upgrading to Jupyterlab](https://hackersandslackers.com/upgrading-to-jupyter-lab-on-ubuntu/)
* [Jupyterlab libraries & resources](https://github.com/markusschanta/awesome-jupyter#jupyterlab-extensions)
* [Convert notebook to Confluence](https://github.com/Valassis-Digital-Media/nbconflux)
* [Python library: Markdown to HTML](https://github.com/Python-Markdown/markdown)
* [Knowledge repo](https://github.com/airbnb/knowledge-repo)

## Knowledge repo

The [Knowledge repo][800] from Airbnb is a curated knowledge sharing platform
for data scientists and other technical professions. 

[800]: https://github.com/airbnb/knowledge-repo/

Detailed instructions for setting up a Knowledge repo are documented [here][810]

[810]: https://daniel.perez.sh/blog/2018/knowledge-repo-setup/

1. Display the knowledge repo version

```
knowledge_repo --version
```

2. Create a knowledge-repo

```
knowledge_repo --repo knowledge-repo init
```

3. Start the knowledge repo

```
knowledge_repo --repo knowledge-repo runserver
```

4. Create a test Jupyter notebook post

```
knowledge_repo --repo knowledge-repo create ipynb test.ipynb
```

5. Start the Jupyter notebook

```
jupyter notebook --no-browser
```

6. Add the post to the repo

```
knowledge_repo --repo knowledge-repo add -p test test.ipynb
```

7. Preview the post by ruuning the server again

```
knowledge_repo --repo knowledge-repo runserver
```

8. Submit the post

```
knowledge_repo --repo knowledge-repo submit test.kp
```

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
pipenv install numpy 
pipenv install scipy
pipenv install sklearn 
pipenv install pandas 
pipenv install watermark 
pipenv install pydot3 
pipenv install matplotlib 
pipenv install statsmodels 
pipenv install seaborn 
pipenv install flake8 
pipenv install yapf 
pipenv install Pillow 
pipenv install plotly 
pipenv install tornado==5.1.1
pipenv install jupyter 
pipenv install jupyter-contrib-nbextensions 
pipenv install jupytext 
pipenv install jupyterlab 
pipenv install nbresuse 
pipenv install "knowledge-repo[all]"
```

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
