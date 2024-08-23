# Player Piano limitations

Sound and music have always had some kind of limitations - the most basic being the hearing range of our ears.
But also the limits of a player on an instrument are always tried to be exceeded, something that is often called virtuosity.

Therefore, a player piano seems to be a natural progression in this endeavour, transcending the human barrier by mechanical means.
However, such a player piano is also limited by its construction and physical limitations.

As the *Steinway Spirio r* is a delicate instrument, it is necessary to take precautions in order to avoid going into areas where the piano could be damaged by excessive use.
The results of this limitations are collected here.

## Simultaneous playback

The most obvious limitation of the Steinway: As soon as we tell the piano to play something via MIDI, we will not be able to record any additional input from the keyboard.
After about 5 seconds of not sending any MIDI commands to the piano, the piano will output the input from the keyboard via MIDI again.
Yet it is possible to physically push down additional keys while the MIDI playback is in progress.

One could say: The piano can only *speak* as long as we do not *talk* to it via MIDI.

## MIDI

MIDI also has certain limitations.
It provides $2**7=128$ possible velocity values for 128 keys.
The keys of the Steinway are mapped from $21$ (lowest A) to $108$ (highest C), with $60$ being the middle C.

Although $128$ values may not seem like much, the Steinway already struggles to represent these velocities and also fails to press a key without making a noise.

Velocity | Remark
--- | ---
0 | No action (this should do something as there is a dedicated *note off* event for the release of the note)
1 | The string is hit lightly, but not consistent across the keyboard. This actual likeliness of hitting the keys is also strongly related to the physical surroundings such as temperature, weather and humidity.
2 - 10 | There is no real audible difference between these 9 velocities
10 - 90 | Proper representation, although sometimes a $20$ has no audible difference to a $21$.
100 - 127 | $ffff$ and not suited for continuous playback over a long time, mainly used to represent hitting the keys as strong as possible

The inability to press a key without hitting the string means that spectral changes and modifications of a piano key/string are not really feasible.

:::{note}
Steinway claims that they have an additional. Although this implementation fixes obvious mistakes when using MIDI [^midi_playback], it remains unclear how the claimed higher resolution of their proprietary format would make a difference if the lower resolution of MIDI can not create audible differences in the velocity.
:::

### Delay

There is no significant delay in receiving MIDI events, but the execution of a MIDI event on the actual keyboard has a delay of about 500 ms.
There is also a very slight *pumping* sound when a playback is started via a DAW.

### Pedals

The pedals are send via MIDI CC channels and follow the traditional MIDI CC layout.

Pedal | MIDI CC
--- | ---
Soft (left) | 67
Sustenuto (middle) | 66
Damper | 64

### Tuning

The piano is tuned to $443~\text{Hz}$ like all keyboards at RSH.

### Repetition

A traditional grand piano can reach about 15 hits per second (for an upright about 7 hits per second)[^key_repetition].

The weight of a key also varies along the piano's keyboard, making the lower keys heavier and the higher keys lighter [^weight].

The Steinway is able to play these 15 hits per second, although it depends very much on the velocity used (not too light, but not too hard).
However, some notes "slip" through, which is actually an effect that would also occur if a human were to play too fast.
I've been told that this is not really damaging the piano, but also should not be used excessively as it could be possible to "break a tongue".

## Alternatives

The Yamaha Disklavier is a popular player piano that offers better MIDI capabilities, such as less delay between the send event and the audible event, and also allows simultaneous playback of MIDI events on the keyboard while also outputting what additional keys are pressed on the keyboard.
From a purely MIDI-based perspective, the Disklavier is therefore preferable to a Steinway.
At the same time, there have been reports of motors burning out due to excessive MIDI events being sent.

Conlon Nancarrow used a modified version of a Bösendorfer Ampico that had been prepared in various ways (such as adding metal braids to the hammers or removing the felt entirely to give it a *harder* sound).
To get the high repetition rates necessary for Nancarrow's pieces, the pneumatic-based piano was run at a much higher air pressure and the distance between hammer and string was reduced.

There is also an automaton by Peter Ablinger and Winfried Ritsch in Graz that sits on top of the physical keys of a piano, where motors push down those keys.
It was built to play excessive notes and volumes.

[^key_repetition]: As stated by Yamaha:
    > [...] key repetition (i.e., when a player repeats notes quickly, such as when playing trills) is much smoother and faster in grand pianos than it is in upright pianos — to a maximum of roughly 15 times per second in grands, versus seven times per second in uprights.

    <https://hub.yamaha.com/pianos/p-digital/a-quick-guide-to-weighted-keys/>

[^weight]: As stated by Yamaha:
    > Every single key on a grand piano keyboard is weighted differently. This is because the strings for each note are slightly thinner and shorter in the treble register, becoming thicker and longer towards the bass register. As a result, there is greater resistance when playing low notes than when playing high notes. In other words, a heavier touch is required in the left hand and a lighter touch in the right hand.

    <https://hub.yamaha.com/pianos/p-digital/a-quick-guide-to-weighted-keys/>

[^midi_playback]: When recording a performance on the piano as a MIDI file via the MIDI interface and playing this MIDI file back on the piano results in a much higher velocity of all keys.
