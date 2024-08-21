# Measuring

The age of enlightenment in the 17th century marked the beginning of humanity's deep interest in quantification, driven by the influence of geography and the integration of mathematics into the sciences.
Today, measurement is a cornerstone of capitalist society, where the constant question, "What *is* the measure of a product?" drives supply, demand, and inherent tension.
This obsession with measurement extends to organizational structures, where bureaucracy and control seek to objectify issues through impersonal laws, a theme often discussed and explored by philosophers such as Foucault in his analysis of the social frameworks of the 20th century.

Wittgenstein once proposed the mathematization of language, an idea that finds a modern parallel in the development of Large Language Models (LLMs).
However, whereas Wittgenstein envisioned a formal, mathematical structure for natural language, LLMs use mathematics to predict the most likely next {term} {token} using multivariate statistical analysis.
Rather than adhering to a formalistic language structure, LLMs operate within a probabilistic framework that allows them to generate content that sometimes veers off in creative or unexpected directions - what some might call "hallucinations".

## The limits of measurability within mathematics

Measurability is a fundamental concept in mathematics which delves deep into our understanding of numbers and set.
Consider the challenge of calculating the area of a circle — a problem that has engaged mathematicians for centuries.
Even within the realm of real numbers, measurement can quickly become non-trivial.
For instance, the real interval $[0,1] \subset \mathbb{R}$ has an attributed "length" of 1, while the disjoint union $[0, 0.25] \cup [0.75, 1] \subset \mathbb{R}$ has a "length" of 0.5.
But what is the "length" of the set of all rational numbers between 0 and 1, $[0, 1] \cap \mathbb{Q}$?
Despite the density of rational numbers within the real numbers, the [Lebesgue measure](https://en.wikipedia.org/wiki/Lebesgue_measure) suggests that any countable subset of $\mathbb{R}$, including this one, has a "length" of zero.

## Social measuring

Social media operates on the principle of measuring engagement, with algorithms amplifying this engagement through recommendation systems, which are often driven by machine learning algorithms.
These systems often employ [dark patterns](https://www.deceptive.design/) to manipulate user behavior, leading to actions that users may not consciously choose.

While the notion of a {term}`social score` is frequently dismissed in Western societies, similar mechanisms are already in place through ratings and feedback systems.
Questions like "Were you happy with your service?" are used for statistical analyses, and many AI services depend on platforms like [Amazon's Mechanical Turk](https://www.mturk.com/), outsource the task of measurement and evaluation of tasks.

### What are the concerns with this

Data aggregation allows for an enhancement of individual datasets through statistical means — a practice that recommendation algorithms implement routinely.
While recommendations may seem not very problematic, they can lead to significant ethical concerns, especially when applied to sensitive data.

Additionally, much of the data collected online is done so passively, and even anonymized data can yield insights that target vulnerable groups. A notorious example is an [Uber blog post](https://web.archive.org/web/20140827195715/http://blog.uber.com/ridesofglory) that attempts to identify users involved in one-night stands based on their ride patterns.[^uber]

## Practicing piano

The practice of a piano on the other hand can not be easily measured, or can it?
The creation of an image from a given text prompt also seem like a non-trivial task to measure, yet there were measurements which guided the neural network during training to produce a desired output based on the stated input.

Taking a look how Chat-GPT is trained, it is trained on as much data as possible, but still it does not have a sense of how this should work?
After the initial training has been performed, there will be another round to fine tune the existing models through human feedback, which is called [reinforcement learning from human feedback (RLHF)](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback).

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


:::{admonition} Discussion
:class: tip

* What impact do recommendation algorithms have on contemporary piano playing practice?
* Do these algorithms favor streamlined processes which establishes a new normative structure?
* How are utopias, dystopias and norms represented on these platforms and how do they shape them outside of these platforms?
:::


:::{admonition} Further reading
:class: tip

* [Die Logik des Digitalen: Es zählt, was sich zählen lässt!](https://www.deutschlandfunk.de/es-zaehlt-was-sich-zaehlen-laesst-100.html) - a german radio essay about the quantity as central quality criteria in our times.
* [Gilles Deleuze - Postscript on the Societies of Control](https://theanarchistlibrary.org/library/gilles-deleuze-postscript-on-the-societies-of-control)
:::

[^uber]: The blog post in question is remarkable on its own - it is a perfect example of invasion into privacy for the sake of profit, even trying to embedd advertisment onto this story

    > The world has changed, and gone are the days of the Walk of Shame. We live in Uber’s world now.

    Not only shows this study utter insensitivities towards the privacy of their users, but also their sense of *research* seems completely off:

    > It was while playing around with this idea of (blind!) rider segmentation that we came up with the Ride of Glory (RoG). A RoGer is anyone who took a ride between 10pm and 4am on a Friday or Saturday night, and then took a second ride from within 1/10th of a mile of the previous nights’ drop-off point 4-6 hours later (enough for a quick night’s sleep).

    It seems Uber lack of ethics does not only show in the contractor licenses but also in their science department, which also shows in another data-*analysis* related blog post labeled [How prostitution and alcohol make Uber better](https://web.archive.org/web/20110929112743/http://blog.uber.com/2011/09/13/uberdata-how-prostitution-and-alcohol-make-uber-better/).
