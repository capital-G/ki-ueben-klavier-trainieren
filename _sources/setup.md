# Setup

Although this course explores the training on a piano, it is not necessary to have one accessible in order to follow along the course, instead there will be also a focus on how, through virtualized environments, the need for a physical thing may be fitted accordingly.

## Python

Although machine learning is an intense resource exhaustive endeavor and Python is not a very performant language, it's adaptability has become the default to setup and control machine learning algorithms.
Although machine learning frameworks such as *Tensorflow* by Google or *torch* by Meta are written in the programming language C++, they offer a Python binding which allows to setup the environment in which we want to transform and evaluate our data.
Once this environment has been setup, Python also takes care of the data- and training-flow and all the calculation, such as on the GPU, happens via the C++ backend.

Python has found high adaptation in multiple areas, especially within research, and follows the, so called, [*Zen of Python*](https://peps.python.org/pep-0020/).

The advised way of setting up Python can be found at <https://realpython.com/installing-python/> - additionally `git` will be necessary to download the course materials.

Afterwards, clone the repository via

```shell
git clone https://github.com/capital-G/ki-ueben-klavier-trainieren
# cd into it
cd ki-ueben-klavier-trainieren
```

and create a new virtual environment and install all dependencies

```shell
virtualenv venv
# this may differ, depeneding on the used OS - take a look at the output of virtualenv if unsure
source venv/bin/activate
# install dependencies
pip install -r requirements.txt
```

### Starting Jupyter

Assuming the current working directory is the repository mentioned above, the following command will spawn the Jupyter server which can be used to edit the course material

```shell
# make sure venv is activated
source venv/bin/activate
venv/bin/jupyter lab
```

## SuperCollider

SuperCollider is an open source audio framework, consisting of a programming language (*sclang*), a synthesis engine (*scsynth*) and many other tools which makes working with audio-synthesis on a computer.
One particular focus of SuperCollider is its reactivity to live events - either from outside, through e.g. MIDI, or through internal procedures.

### Control a piano via MIDI

```{admonition}note
todo
```

### Control a VST via MIDI


```{admonition}note
todo
```
