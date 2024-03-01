# Player limitations

Although a player piano is not bound to the human capabilities of human piano playing (already limited by their two hands with each 5 fingers), it still has mechanical limitations as the way the sound is produced (by hitting the hammer on the key) is performed in a electro-mechanical way.

Because a piano is a delicate instrument there need to be made pre-cautions to avoid going into territory where the piano may take damage due to excessive use.

## MIDI

MIDI already has certain limitations - first that it only provides $2**7=128$ possible velocity values - which seems not too much, but when listening to the Steinway it already struggles to represent these velocity values

Velocity | Remark
--- | ---
0 | No action
1 | The string is already hit - a way to press a key down without hitting the string is not possible, which limits makes spectral modifications or enhancements of overtones
2 - 10 | No audible difference
100 | $ffff$
> 100 | Too brutal for human playback

:::{note}
Steinway claims that they have an additional. Although this implementation fixes obvious mistakes when using MIDI [^midi_playback], it remains unclear how the claimed higher resolution of their proprietary format would make a difference if the lower resolution of MIDI can not create audible differences in the velocity.
:::

## Tuning

Although in a digital domain it is possible to change the reference pitch of a sound, this is not possible via.

## Velocity and speed

The calculation of physical force $F$ can be expressed through the formula $F=ma$, where $m$ is the mass and $a$ is the acceleration of the object.

A traditional grand piano can achieve around 15 hits per second (for an upright about 7 hits per second)[^key_repetition].

The values of the weight of a key also differs across the keyboard of the piano, making lower keys heavier and higher keys lighter [^weight].

## Alternatives

### Nancarrow

Nancarrow used a modified version of a Bösendorfer, which was prepared in various ways


:::{note}
> There is some interesting quote in the Nancarrow book I want to quote here
:::

### Ablinger / Ritsch

There is also Peter Ablinger and Winfried Ritsch.

They also visited the Bösendorfer factory, but were not satisfied with the performance of the mechanical player mechanism, so they decided to built one themselves, which has a focus on the aspects that were necessary for their project, which was speed and polyphony.

[^key_repetition]: As stated by Yamaha:
    > [...] key repetition (i.e., when a player repeats notes quickly, such as when playing trills) is much smoother and faster in grand pianos than it is in upright pianos — to a maximum of roughly 15 times per second in grands, versus seven times per second in uprights.

    <https://hub.yamaha.com/pianos/p-digital/a-quick-guide-to-weighted-keys/>

[^weight]: As stated by Yamaha:
    > Every single key on a grand piano keyboard is weighted differently. This is because the strings for each note are slightly thinner and shorter in the treble register, becoming thicker and longer towards the bass register. As a result, there is greater resistance when playing low notes than when playing high notes. In other words, a heavier touch is required in the left hand and a lighter touch in the right hand.

    <https://hub.yamaha.com/pianos/p-digital/a-quick-guide-to-weighted-keys/>

[^midi_playback]: When recording a performance on the piano as a MIDI file via the MIDI interface and playing this MIDI file back on the piano results in a much higher velocity of all keys.
