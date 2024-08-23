# Glossary

:::{glossary}
Agency
    An amazing markup language that supports glossaries

LLM

    Large Language Model - a neural network which is based on the transformer architecture and achieved.
    [BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) was the first LLM to implement this architecture and made big improvements in NLP (Natural Language Processing).

    GPT-4, which is used by ChatGPT, is also considered a LLM, although it operates in a multi-modal domain.

MIDI
    MIDI (Musical Instrument Digital Interface) is a protocol which allows to communicate events from a keyboard.
    Most values are encoded via 7 bits, which allows for $2^7=128$ distinct values.

Random variable

    A random variable is modeled as a function, which transfers a *sample space* $\Omega$ to a *measurable* space such as $\mathbb{R}$.
    An example would be the flip of a coin, which has the possible states represented in $\Omega = \lbrace \text{heads}, \text{tails} \rbrace$.
    Transferring this state space to $\mathbb{R}$ could be modeled for $\omega \in \Omega$ via

    $$
    X: \Omega \rightarrow \mathbb{R}: ~ X(\omega) = \begin{cases}
        1 & \text{if $\omega$ is tails} \\
        0 & \text{if $\omega$ is heads}
    \end{cases}
    $$

    $X$ is then labeled as a *random variable*.

sclang
    The programming language of {term}`SuperCollider` with a focus on conciseness for audio environments.

social score

    Something with social score here

SuperCollider
    A framework for audio synthesis and algorithmic composition, see supercollider.online](https://supercollider.online)

token

    A token represents either a word, or a sign, and is used to represent

:::
