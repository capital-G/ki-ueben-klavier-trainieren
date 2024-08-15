# Setup

Although this course explores the training on a piano, it is not necessary to have one accessible in order to follow along the course, instead there will be also a focus on how, through virtualized environments, the need for a physical thing may be fitted accordingly.

## SuperCollider

SuperCollider is an open source audio framework, consisting of a programming language (*sclang*), a synthesis engine (*scsynth*) and many other tools which makes working with audio-synthesis on a computer.
One particular focus of SuperCollider is its reactivity to live events - either from outside, through e.g. MIDI, or through internal procedures.

### Control a piano via MIDI


### Control a VST via MIDI

```supercollider
Ndef(\foo, {SinOsc.ar(freq: 200.0)}).play;
```

## Python

Although machine learning is an intense resource exhaustive endeavor and Python is not a very performant language, it's adaptability has become the default to setup and control machine learning algorithms.
Although machine learning frameworks such as *Tensorflow* by Google or *torch* by Meta are written in the programming language C++, they offer a Python binding which allows to setup the environment in which we want to transform and evaluate our data.
Once this environment has been setup, Python also takes care of the data- and training-flow and all the calculation, such as on the GPU, happens via the C++ backend.

Python has found high adaptation in multiple areas, especially within research, and follows the, so called, [*Zen of Python*](https://peps.python.org/pep-0020/).
