import midi

pattern = midi.Pattern()
track = midi.Track()

pattern.append(track)
tickscale = 55
duration = 10
time = 0
note = 64
lastcmdtime = 0
name = "example"
#track.append(midi.NoteOnEvent(tick=(time-lastcmdtime)*tickscale, velocity=40, pitch=note+lowerBound))
#lastcmdtime = time
#track.append(midi.NoteOffEvent(tick=(time-lastcmdtime)*tickscale, pitch=note+lowerBound))
#lastcmdtime = time
#for x in range(0, 3):
for lowerBound in range(1, 10):
    track.append(midi.NoteOnEvent(tick=(0)*tickscale, velocity=40, pitch=note+lowerBound))
    track.append(midi.NoteOffEvent(tick=(duration)*tickscale, pitch=note+lowerBound))


midi.write_midifile("{}.mid".format(name), pattern)

