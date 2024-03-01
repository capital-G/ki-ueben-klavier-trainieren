# Realtime Machine Learning

With the help of [FluCoMa](https://www.flucoma.org/) (Fluid Corpus Manipulation) it is possible to execute machine learning algorithms in real time environments such as audio synthesis.

Normally we use piano more in settings which are derived from symbolic notation, but this can also be seen a bit different here.

## Idea

Create a delay line which tries to recreate the sonic identity of the piano again, re-adapting "I a sitting in a room".
This would be also interesting to figure out how the piano would try to reconstruct a non-piano sound.

But in order for this we would either need to reconstruct the synthesis methods of a piano into as a differentiable DSP algorithm (see [DDSP](https://github.com/magenta/ddsp)) which would allow to tweak the parameters of the DSP algorithm with a neural network.

With the help of the realtime environment of FluCoMa it is possible to compare a source signal and a generated signal in realtime, while also adjusting the parameters of the neural network in realtime.
This limits the complexity of the neural network, but the goal for this project is not to have the best performing neural network but instead having a neural network with which we can interact in a real time manner.
