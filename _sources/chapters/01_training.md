# Training and Learning

## Adjusting algorithms

The terms *learning* and *training* are often used interchangeably in the context of machine *learning*, as many people use the term *learning* to refer to the process of adjusting the parameters of an algorithm through data.
This implies a notion of intelligence in a system - is this marketing, or is the term actually justified when we compare this process to how we learn?
In addition, referring to algorithms as *neural* networks implies a similarity to nerons found in a human brain, which is also closely associated with *intelligence*.
Does this association challenge or enhance our perception of what constitutes as intelligent behavior in machines, humans or society?

In machine learning, **training** is often referred to as the process of feeding data into a *model* - an algorithm designed to approximate a *probability distribution* by analyzing multiple juxtapositions of variables - which is *evaluated* based on a given *metric*.
Based on this evaluation, the algorithm can adjust its parameters to improve performance based on the given data.
This is somewhat similar to teaching a piano student by providing examples and correcting mistakes over time through repetition.
Training therefore encapsulates an iterative process of *optimization* where a model tries to *learn* to make predictions or decisions based on input data.

**Learning** is usually referred to the model's internal adjustments and how it updates its understanding of the data through algorithms.
Learning is affected by a *learning rate*, which determines the speed at which a model updates its parameters.
A higher learning rate means the model changes more quickly, potentially missing nuances, while a lower rate means slower but more stable learning.
This distinction is critical because effective training relies on a deep understanding of how the model learns and adapts.

In AI, the means of learning can include processes such as gradient descent, backpropagation, and regularization techniques that are used to shape the model as it attempts to translate an input into an output.
The general goal of these methods is to ensure that it generalizes well to new data and avoids *overfitting* to a training set.

In addition, the language of *training* versus *learning* highlights different aspects of AI development.
Training emphasizes the external process applied by the engineer, while learning focuses on the internal mechanisms of the algorithm itself.

At the same time, parameter adjustments and tuning can also be found in more *basic* algorithms, such as linear regression, which seeks to measure the linear impact of one or more input variables on the output using a scalar.
While obtaining the best possible solution is sometimes not trivial, it is still feasible without the computational power of a computer, though this adaptation step is rarely referred to as *learning*.
Is this because the complexity, in terms of the need for computation, makes this task solvable without a computer, or because there is a definitive answer instead of just an approximation?

```{figure} https://upload.wikimedia.org/wikipedia/commons/3/3a/Linear_regression.svg

A linear regression where the impact of a given $x$ value is measured against its target variable $y$.
Source: <https://commons.wikimedia.org/wiki/File:Linear_regression.svg>
```


## Training piano

This distinction between training and learning in *machine learning* could be analogously applied to training on a piano or for a player piano.
Training a piano could describe the communication between the piano as an object and a person who initiates a communication through an impulse.
This acts as a two-way communication process where the player attempts to direct the piano to produce specific sounds, while simultaneously adjusting techniques in response to the piano's feedback.
The result is that the piano and the player together can create a unique musical expression.
One might assume that a piano is a passive actor, requiring external input to produce sound.
However, the piano possesses its own form of agency, influencing the outcome based on its design and mechanics.
The piano acts therefore also as a translator between an input through the keyboard and the output - and although a piano can be modified or *prepared*, most time of the training is spend on tweaking the input on the piano.

When a person trains on a piano, they engage in repetitive practice, crafting their skills through constant feedback and adjustment — similar to how an machine learning model is trained with data.
The pianist's learning process involves internalizing techniques, developing muscle memory, and understanding musical theory, for which different views and contexts is necessary to develop an understanding.

## The player piano

For a player piano, the training process can have a focus in the programming and input of piano rolls or MIDI files, where specific instructions are fed into the mechanism to produce music.
The learning aspect is reflected in how these instructions are interpreted and executed by the piano, ensuring that the nuances of the music are accurately reproduced.
It allows to mechanical realize an *artifical* performance or *clone* a human performance, which creates in both ways a reflection of how a (player) piano is used.

Just as a machine learning model requires fine-tuning and careful adjustment of its learning rate, a pianist needs to adjust their practice techniques and tempo to master a piece.
Similarly, programming a player piano involves calibration of its input data to achieve the desired musical expression, creating a link between training and learning in using machine learning, practicing a piano or tweaking the input on a player-piano in order to craft a musical performance.

## Player Piano as an abstraction

Acoustic instruments rely on an immediate impulse as a physical action transformed into sound.
This impulse can be the plucking of a string, the blowing of a pipe, or the striking of an object.
Such physical actions produce vibrations that result in an auditory event.

These impulses can be amplified through mechanical means, such as the complex air systems in a church organ, or through electronic means, as seen in electric guitars where pickups convert string vibrations into electrical signals.

The introduction of piano rolls for player pianos created a significant abstraction in the domain of crafting performances.
Piano rolls allow for a separation between the human action of exciting an instrument and the resulting sound.
Unlike traditional musical scores that require a musician's performance, piano rolls encode music in a way that enables the player piano to produce sound quasi autonomously.
This innovation creates an early form of abstraction in music creation, where the physical execution by a musician is no longer directly linked to a sound production.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/PlayerPianoRoll.jpg/1280px-PlayerPianoRoll.jpg

A piano roll on a player piano in which a hole in the roll indicates the pressing of a key.
Source: <https://commons.wikimedia.org/wiki/File:PlayerPianoRoll.jpg>
```

A piano roll on a player piano in which a hole in the roll indicates the pressing of a key.

Piano rolls are akin to punch cards in programming, storing information as a sequence of instructions that control a system with multiple potential outcomes.
Over time, this system of communicating keystrokes evolved into {term}`MIDI`, furthering the abstraction by digitally encoding musical performance data.
This transition from physical rolls to digital MIDI represents a further evolution in the abstraction of musical performance, making it increasingly independent of direct human physical interaction in trade for electro-mechanical interactions.

## Agency of the player piano

The *piano automata* has attracted a multitude of different artists, and this small selection should rather give a small glimpse and taste why it may be interesting to look into player piano as an autonomous instrument.

### Conlon Nancarrow - Studies for player piano

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/LFz2lCEkjFk?si=ZE6HPthjfvwIy-pb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Nancarrow meticulously programmed his player pianos by punching holes in piano rolls, encoding complex rhythms and intricate musical patterns that would be impossible for a human performer to execute.

Nancarrow fed precise data into the player piano, akin to providing training examples for a machine learning algorithm.
The player piano, in turn, "learned" to perform these compositions flawlessly, translating the encoded instructions into sound without requiring human intervention.
This generates an abstraction, where the physical execution of music was separated from human performance and transferred to a mechanical device.
By leveraging the mechanical precision of the player piano, he was able to explore rhythmic complexity and polytempo structures that would be unplayable by even the most skilled pianists.

By empowering the agency of a player piano, Nancarrow's work creates a shift from traditional, human-centric music performance to an abstracted form where the instrument itself becomes an active participant, where his studies push the boundaries of what is musically possible, transforming the player piano from a mere tool into a collaborator capable of executing complex, avant-garde compositions.

For further information on Nancarrow's work, take a look at {cite}`Nancarrow2002`.


### Peter Ablinger & Winfried Ritsch - Speaking piano

Austrian composers Peter Ablinger created an infamous piece entitled [*Deus Cantando*](https://ablinger.mur.at/txt_qu3god.html) which makes use of the [*Speaking Piano*](https://ablinger.mur.at/speaking_piano.html) which was build by Winfried Ritsch.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/muCPjK4nGY4?si=PKeOnLtp85CR9KtY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Ablinger [writes](https://ablinger.mur.at/speaking_piano.html) about the *"speaking piano"*:

> Talking machines have been in conversation since 1748. Leonhard Euler, for example, had the idea of constructing a piano who's individual keys would produce each a speech sound (cf. Mladen Dolar, The Voice of His Master, p. 13ff). In 1780 the Imperial Academy of Sciences in Saint Petersburg announced an award to build a talking machine. Christian Gottlieb Kratzenstein wins the award.
>
> 1748-1780: This is the heyday of the development and emancipation of sonata and instrumental music. And of course, instrumental music is itself a speaking machine. After all, it had to speak to us. It had to tell us something! Only on this condition could the newly emerging instrumental music finally be accepted. And the sonata is nothing more than a speech that tries to convince us, and which we judge according to how convincing we find it.
>
> But the history of instrumental music and speaking machines is also the history of information technology. Because when Graham Bell saw the speaking machine, he wanted to recreate something similar but in the process inadvertently invented the telephone; at the same time Charles Babbage invented the first calculating machine in 1819, also in response to a speaking automaton.
>
> Talking machines, sonatas and computers - or smartphones - are on the same line.

### George Lewis - Voyager

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/o9UsLbsdA6s?si=2TxktWVa8LzmVP71" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Instead of providing a static piece that has a fixed state, George Lewis created a system called *Voyager* that allows for dynamic interaction with a live performer.
*Voyager* is an interactive improvisation system that listens to and analyzes the music played by a human musician in real-time.
It then generates its own musical responses, creating a dialog between the performer and the software.

This innovative system can be seen as an embodiment of the concepts of training, learning, tweaking and tuning algorithms through the means of a musical performance.
The software behind *Voyager* was trained to recognize various musical inputs and respond appropriately, much like how an modern day AI model is trained to understand and generate data.
However, the real-time interaction between the human musician and the system highlights the learning aspect, as *Voyager* continuously adapts to the performer's style and decisions during the performance.

In *Voyager*, the software acts as an autonomous improviser.
This abstraction shifts the role of the musician from solely producing music to interacting with an intelligent system that contributes its own creative input.

The system is not merely executing pre-written instructions: it actively participates in the creation of music, making decisions and contributing to the artistic process.
The instrument itself becomes an active collaborator rather than a passive tool.

## Training a piano to play

Practicing an instrument involves not only the physical mastery of the instrument but also the psychological engagement necessary to develop musicality and expression.
Similarly, having access to a piano means more than just the ability to play notes; it encompasses the intricate interaction between the musician and the instrument.

In the realm of player pianos, the physical training is embedded in the mechanical capabilities and programming of the piano rolls or digital instructions.
However, even when a neural network has been trained and is operational, integrating it with a piano requires thought.
While the physical aspect of training may no longer be necessary to get the machine running, there remains the critical task of determining which musical possibilities should be explored and which should be excluded.

This process involves making artistic and technical decisions to ensure the model's output aligns with a desired musical expression.
Just as a musician refines their performance through practice, a model must be meticulously configured and calibrated to achieve its full potential in musical creation.
This integration of training, learning, and artistic decision-making ultimately expands the boundaries of what can be achieved in both traditional and automated music performance.

:::{admonition} Discussion
:class: tip

* How can the principles of training and learning in machine learning be further applied to enhance the capabilities and expressiveness of automated musical instruments, such as player pianos?
* In what ways can the abstraction of musical performance, as seen in player pianos and autonomous systems like George Lewis's *Voyager*, influence the future of live music and composition?
* How does the process of physical training and learning on a traditional piano compare to the programming and fine-tuning of automated player pianos, and what can musicians and engineers learn from each other in these practices?
:::
