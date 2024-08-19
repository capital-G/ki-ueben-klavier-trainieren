# Measuring

With the age of enlightenment in the 17th century, people start to quantify everything which is reflected by the motivation of geography and the introduction of mathematics into science.
Nowadays measuring is the crucial aspect of the capitalist society, where the constant question "What *is* the measure of a product" creates demand, supply and therefore tension.
Within organization structures this is also reflected by the implication of bureaucracy and controlling, which tries to separate the issue from the person through objective laws, and these organizational structures shaped the humankind of the 20th century as discussed by Foucault?

Wittgenstein already once proposed the mathematization of language, and with the advent of LLMs this proposal seems to be implemented, although in a different manner than thought by Wittgenstein.
Where Wittgenstein wanted to make use of the formal power and correctness of mathematics within natural language, LLMs use mathematics to calculate the most likely next {term}`token` based on multivariate statistical analysis, therefore LLMs do not follow a formalistic construction of language, but instead the formal programming language creates a room of possibilities in which the LLM can hallucinate.

## The limits of measurability within mathematics

Measurability within mathematics is a fundamental aspect in mathematics as already the measurement of the area of a circle is an old and non-trivial question.
Also, the measurement within the real numbers can quickly become non-trivial: For example the given subset $[0,1] \subset \mathbb{R}$ has the attributed *length* of $1$, and $[0, 0.25] \cup [0.75, 1] \subset \mathbb{R}$ has a length of $0.5$.
But what is the length of all rational numbers between $0$ and $1$, so $[0, 1] \cap \mathbb{Q}$?
As the rational numbers are [dense](https://en.wikipedia.org/wiki/Diophantine_approximation) within the real numbers, this value could be anything between $0$ and $1$. (Through lesbuege measures it is possible to show that every countable subset within $\mathbb{R}$ has a length/mass of 0).

This shows that mathematics itself is not limited to research objects that are quantifiable, often enough mathematics is more about the classification of objects, and that even within mathematics there is a limit to what can be measured.

## Social measuring

Social media is also driven by an measuring engagement - its measuring and amplification through recommendation algorithms, it contains [dark patterns](https://www.deceptive.design/) to trick people into doing actions they do not want to perform.

Although something like a {term}`social score`` is often disregarded within western societies, the very same is already in place through ratings: "Where you happy with your service?" will be used within a statistical analysis, and many AI services are relying on services such as Mechanical Turk by AWS, which is also based upon measuring the success of people, which gets evaluated onto.

### What are the concerns with this

Individuality freedom vs. collective knowledge shows as a perfect example of controversial opinions in the covid 19 pandemic.

Additionally, derived from the data points of the many, the dataset of a single person can be enhanced quite impressive through statistical calculations (this is basically what a recommendation algorithm implements).
While recommendations itself may seem not problematic, they sure create a lot of tensions when used for estimation about sensitive data such as.

Additionally, many data is just collected on the fly and even anonymous data can give insights which can be used to target marginal groups.
Uber once posted an infamous blog post which tries to [estimate potential one night stand users based on their booked routes](https://web.archive.org/web/20140827195715/http://blog.uber.com/ridesofglory).[^uber]

## Practicing piano

The practice of a piano on the other hand can not be easily measured, or can it?
The creation of an image from a given text prompt also seem like a non-trivial task to measure, yet there were measurements which guided the neural network during training to produce a desired output based on the stated input.

Taking a look how Chat-GPT is trained, it is trained on as much data as possible, but still it does not have a sense of how this should work?
After the initial training has been performed, there will be another round to fine tune the existing models through human feedback, which is called [reinforcement learning from human feedback (RLHF)](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback).

Therefore

## Tuning and learning

On a violin it is essential to train ones pitch sensitivity in order to have a stable intonation, especially in the more sensitive, higher frequency domains.

When tuning a piano, it is necessary to tune them in relation to each other, so they sound in a harmonious way together.
After a reference point has been established, it can be used to tune all other.
It is important to note that the overtones of a piano string have a vast impact on the tuning of a piano: Because the upper strings are too stiff on their ends, the overtones tend to sound sharper than they should, creating *inharmonicities*.

Tunings such as *just intonation* are often tied to their reference point (see [Pythagorean comma](https://en.wikipedia.org/wiki/Pythagorean_comma)), which makes modulation (which is the change of reference point) possible, but imposes an additional, strong coloring of the relations.
In an effort to minimize the coloring of the relations the *equal temperament* tuning has been developed which suggest an approximation of absolute pitches such that the relations should stay consistent in every tuning.
This imbalance can be heard as *beating*, which becomes audible as the difference between tones or overtones within one keyboard.

Comparing this to the *training* of neural networks, it is possible to associate the singular preciseness of a relative just intonation with neural networks which work within a single domain to the ones which work in a multi-modal domain.
Afterwards the tuner adjusts the system, which tries to balance, tweak and *tune* the output of the default setting.

Of course, there are different kind of tuning which have been established, the pure tonal.
Yet the preciseness and sureness of tactility can only be given when the tuning foundation has been made properly.

## Tuning as a performance

Although tuning is essential to any kind of music, this tuning is rarely tweaked within performances (other than to get the instrument back into tune).

:::{tip}
What could be the whammy bar on a guitar on a neural network? Maybe how loose let it be?
Maybe this could be an interesting lead.
:::

:::{admonition} Discussion
:class: tip

* What impact do recommendation algorithms have on contemporary piano playing practice?
* Do these algorithms favor streamlined processes which establishes a new normative structure?
* How are utopias represented on these platforms?
:::

## Reading assignments

* <https://www.deutschlandfunk.de/es-zaehlt-was-sich-zaehlen-laesst-100.html>
* Deleuze - Postscript on the Societies of Control

[^uber]: The blog post in question is remarkable on its own - it is a perfect example of invasion into privacy for the sake of profit, even trying to embedd advertisment onto this story

    > The world has changed, and gone are the days of the Walk of Shame. We live in Uber’s world now.

    Not only shows this study utter insensitivities towards the privacy of their users, but also their sense of *research* seems completely off:

    > It was while playing around with this idea of (blind!) rider segmentation that we came up with the Ride of Glory (RoG). A RoGer is anyone who took a ride between 10pm and 4am on a Friday or Saturday night, and then took a second ride from within 1/10th of a mile of the previous nights’ drop-off point 4-6 hours later (enough for a quick night’s sleep).

    It seems Uber lack of ethics does not only show in the contractor licenses but also in their science department, which also shows in another data-*analysis* related blog post labeled [How prostitution and alcohol make Uber better](https://web.archive.org/web/20110929112743/http://blog.uber.com/2011/09/13/uberdata-how-prostitution-and-alcohol-make-uber-better/).
