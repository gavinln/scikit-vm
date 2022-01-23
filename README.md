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

### Jupyterlab extensions

Jupyterlab 3.x supports installing extensions directory using pip without
building the extensions using node.

The following extensions are useful

```
pipenv install jupyterlab-git
pipenv install jupyterlab_vim
pipenv install jupyterlab_lsp
pipenv install aquirdturtle_collapsible_headings  # less useful
```

### Jupyterlab extensions old

1. Enable the server extension

```
jupyter labextension install @jupyterlab/shortcutui
jupyter labextension install @jupyter-widgets/Jupyterlab-manager
jupyter labextension install @Jupyterlab/shortcutui
jupyter labextension install @Jupyterlab/toc
jupyter labextension install jupyterlab-jupytext
jupyter labextension install jupyterlab_vim
jupyter labextension install @krassowski/jupyterlab_go_to_definition
jupyter labextension install @aquirdturtle/collapsible_headings

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

4. Install the [Jupyter language server](https://github.com/krassowski/jupyterlab-lsp)

5. Start the Jupyter lab interface
./scripts/lab-jupyter.sh

6. Install these Jupyter extensions

* @jupyter-widgets/Jupyterlab-manager
* @Jupyterlab/shortcutui
* @Jupyterlab/toc
* jupyterlab-jupytext
* jupyterlab_vim
* @ryantam626/jupyterlab_code_formatter

[nbresuse](https://github.com/yuvipanda/nbresuse)

#### Other extensions

From the PyData [presentation](https://www.youtube.com/watch?v=3pdrzhny9Lc)

* jupyterlab-git
* nbdime
* jupyterlab_code_formatter
* jupyterlab-toc
* jupyterlab-quickopen
* jupyterlab-sidecar
* jupyterlab-drawio
* jupyterlab-topbar
* jupyterlab-sql
* jupyterlab-celltags
* jupyterlab-go-to-definition
* jupyterlab-lsp
* voila
* jupyterlab-matplotlib
* jupyterlab-variableinspector
* jupyterlab-templates

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

[Visualize data][550] structures

[550]: https://github.com/parrt/lolviz

### Bokeh

Python [visualization library][560]

[560]: https://bokeh.org/

### Plotnine

[Grammar of graphics][570] for Python

[570]: https://github.com/has2k1/plotnine


### Dexplot

A [plotting library][580] like Seaborn that wraps matplotlib and data frames.

[580]: https://github.com/dexplo/dexplot

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

## Additional Jupyter libraries

[Qgrid][https://github.com/quantopian/qgrid]

## Serving machine learning models

[Scikit-learn model with ONNX and FastAPI](https://medium.com/@nico.axtmann95/deploying-a-scikit-learn-model-with-onnx-und-fastapi-1af398268915)

[Porting Flask to FastAPI](https://www.pluralsight.com/tech-blog/porting-flask-to-fastapi-for-ml-model-serving/)

## Pandas

### Extending pandas

* [Cyberpandas][700] - supports IP addresses
* [GeoPandas][710] - supports geographic data

[700]: https://github.com/ContinuumIO/cyberpandas
[710]: https://github.com/geopandas/geopandas

### Learning pandas

* [100 numpy puzzles][720]
* [100 Pandas puzzles][730]

[720]: https://github.com/rougier/numpy-100
[730]: https://github.com/ajcr/100-pandas-puzzles

## Jupyterlab tips

* [Working efficienctly with Jupyterlab](https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/)
* [Upgrading to Jupyterlab](https://hackersandslackers.com/upgrading-to-jupyter-lab-on-ubuntu/)
* [Jupyterlab libraries & resources](https://github.com/markusschanta/awesome-jupyter#jupyterlab-extensions)
* [Convert notebook to Confluence](https://github.com/Valassis-Digital-Media/nbconflux)
* [Python library: Markdown to HTML](https://github.com/Python-Markdown/markdown)
* [Best practices with notebooks](https://cloud.google.com/blog/products/ai-machine-learning/best-practices-that-can-improve-the-life-of-any-developer-using-jupyter-notebooks)

## Miscellaneous

### Machine learning operational details

1. [Feature store](https://github.com/gojek/feast/) from Google and GoJEK

2. Machine learning [formats](https://towardsdatascience.com/guide-to-file-formats-for-machine-learning-columnar-training-inferencing-and-the-feature-store-2e0c3d18d4f9)

3. Managing [ML experiements](https://medium.com/@hadyelsahar/how-do-you-manage-your-machine-learning-experiments-ab87508348ac)

### Generate requirements.txt file

```
python ansible\convert-ansible-to-requirements.py  > requirements.txt
```

### Choose the correct Python version

To create a Pipfile on the Windows subsystem for Linux and choose the correct
Python

```
pipenv --python $(which python3)
pipenv install --python /usr/bin/python3
```

### Install libraries manually

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
```

### Clean Jupyter notebooks

1. Convert notebook to python file

```
jupytext --to py 19_jupyter-widgets.ipynb
```

2. Run flake8 to check coding conventions

```
flake8 19_jupyter-widgets.ipynb
```

3. Automatically fix code style

```
autopep8 -i -a 19_jupyter-widgets.ipynb
```

5. Setup flake8 in vim

```
:set makeprg=flake8\ %
:make
:clast
:cprevious
```
4. Convert back to notebook

```
jupytext --to ipynb 19_jupyter-widgets.ipynb
```

### Vifm filtering files

1. Add a filter to hide files

```
:filter {*.py}
```

2. Toggle filter to only show files ending in py

```
:filter!
```

3. Show the value of the filter

```
:filter?
```

### AI tools

Articles

* [AI developer stack](https://blog.fiddler.ai/2019/06/ai-needs-a-new-developer-stack)

Tools

* [mlflow](https://github.com/mlflow/mlflow) - manage machine learning models - 4761 stars
* [DVC](https://github.com/iterative/dvc) - data version control  - 3662 stars
* [Pachyderm](https://github.com/pachyderm/pachyderm) - reproducible data science using Docker - 3965 stars
* [streamlit](https://github.com/streamlit/streamlit) - tools for machine learning - 1389 stars
* [scikit libraries](https://towardsdatascience.com/5-obscure-python-libraries-every-data-scientist-should-know-3651bf5d3be3)

### Python libraries to try

* logguru - more convenient logging
* pyupgrade - upgrade Python code from 3.6 to 3.7/3.8/3.9
* ntfy - cross-platform notifications

## Other machine learning libraries

* [Feature engine][400] - feature transformers for scikit-learn

[400]: https://github.com/solegalli/feature_engine

* [Shap][410] - explain the output of machine learning models

[410]: https://github.com/slundberg/shap

* [Shap video][420] - background behind approach

[420]: https://www.youtube.com/watch?v=B-c8tIgchu0

* [yellowbrick][430] - visualize machine learning models

[430]: https://github.com/DistrictDataLabs/yellowbrick

### PyCaret

[PyCaret][440] is a low-code machine learning library that supports multiple
machine learning libraries including sklearn on the CPU and other libraries
such as XGBoost, LightGBM and Catboost on the GPU. It also supports integration
with MLFlow.

PyCaret depends on an older version of scikit-learn (0.23.2) and cannot be used
with scikit-learn (1.0.2) as of 2022-01-15.

This happens even when running `poetry add pycaret --allow-prereleases`

[440]: https://github.com/pycaret

### TPOT

[TPOT][450] is an automated Python machine learning tool that optimizes machine
learning pipelines using genetic programming. Other than sklearn it supports
libraries such as XgBoost and PyTorch on the GPU. It does not support lightgbm.

[450]: https://github.com/EpistasisLab/tpot/

1. Install pre-requisite libraries

```
pip install deap update_checker tqdm stopit 
```

2. Install tpot

```
pip install tpot
```

### Auto-sklearn

[Auto-sklearn][460] is an automated machine learning toolkit and a drop-in
replacement for Sklearn estimators. It does not support other libraries such as
XGBoost nor LightGBM. This [tutorial][470] explains how to use Auto-sklearn.

[460]: https://github.com/automl/auto-sklearn

[470]: https://machinelearningmastery.com/auto-sklearn-for-automated-machine-learning-in-python/

### Hyper-parameter optimization libraries

- https://github.com/optuna/optuna
- https://github.com/scikit-optimize/scikit-optimize
- https://github.com/fmfn/BayesianOptimization
- https://github.com/hyperopt/hyperopt

### Feature engineering

#### Videos

https://www.youtube.com/watch?v=tfWzbhKX294

https://www.youtube.com/watch?v=vsKNxbP8R_8

#### Feature engineering books

http://www.feat.engineering/

#### Machine learning videos including feature engineering

https://www.youtube.com/c/HeatonResearch/search

### Statsmodels

Videos

1. [Introduction to statsmodels][900]
2. [Introduction to patsy][910]
3. [Patsy design matrices][910]

[900]: https://www.youtube.com/watch?v=V86gTgL1FRw
[910]: https://www.youtube.com/watch?v=8eeRNiVmo2U
[920]: https://www.youtube.com/watch?v=3DLrznP4pOM


## Setup pre-commit

https://pre-commit.com/

1. Install pre-commit pip install pre-commit

```
2. Check version
pre-commit --version
```

3. Generate a sample .pre-commit-config.yaml file

```
pre-commit sample-config
```

4. Save and overwrite the existing .pre-commit-config.yaml

```
pre-commit sample-config > .pre-commit-config.yaml
```

5. Run the pre-commit checks manuall

```
pre-commit run --all-files
```

6. Install the pre-commit hooks

```
pre-commit install
```

7. Uninstall the pre-commit hooks

```
pre-commit uninstall
```

## Prediction intervals

* https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html

* https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html

* https://machinelearningmastery.com/prediction-intervals-for-machine-learning/

* https://towardsdatascience.com/how-to-generate-prediction-intervals-with-scikit-learn-and-python-ab3899f992ed

* https://medium.com/@qucit/a-simple-technique-to-estimate-prediction-intervals-for-any-regression-model-2dd73f630bcb

* http://www.xavierdupre.fr/app/mlinsights/helpsphinx/index.html

## Interpretable machine learning

* https://christophm.github.io/interpretable-ml-book/counterfactual.html

## Requirements

The following software is needed to get the software from github and run
Vagrant to set up the Python development environment.

* [Oracle VM VirtualBox][1000]
* [Vagrant][1010] version 1.9.1 or higher

[1000]: https://www.virtualbox.org/
[1010]: http://vagrantup.com/
