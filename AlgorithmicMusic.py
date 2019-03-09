#This is just a POC of use of python3-midi to generate the same music as
#utileDemo.py, but in an uncompressed/non algorithmic manner. 
#if it doesn't install easily for python 3 try this
#pip install git+https://github.com/vishnubob/python-midi@feature/python3
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

#write a simplistic example 
midi.write_midifile("{}.mid".format(name), pattern)

#write the same example that utileDemo.py writes, but without using pattern repetition
#It was created by copying the output.mid file to the python3-midi folder and cd'ing there
#and using python3-midi for generating the code from an existing binary MIDI file.
#I then pasted the generated code in here
#
#midi.write_midifile("{}.mid".format(name), pattern)
pattern1 = midi.Pattern(format=1, resolution=960, tracks=\
[midi.Track(\
  [midi.SetTempoEvent(tick=0, data=[7, 161, 32]),
   midi.EndOfTrackEvent(tick=0, data=[])]),
 midi.Track(\
  [midi.TrackNameEvent(tick=0, text='Treble', data=[84, 114, 101, 98, 108, 101]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[71, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[69, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[77, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[77, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[71, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[77, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[91, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[91, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[88, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[88, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[79, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[69, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[71, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=1920, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=1920, channel=0, data=[76, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[71, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[69, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[77, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[77, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[71, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[76, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[77, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[91, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[91, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[88, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[88, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[79, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[69, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[72, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[71, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[74, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 100]),
   midi.NoteOffEvent(tick=1920, channel=0, data=[72, 100]),
   midi.EndOfTrackEvent(tick=0, data=[])]),
 midi.Track(\
  [midi.TrackNameEvent(tick=0, text='Bass', data=[66, 97, 115, 115]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 100]),
   midi.NoteOffEvent(tick=3840, channel=0, data=[45, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[53, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[52, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[50, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[48, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[47, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[55, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[55, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[53, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[52, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[50, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[48, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[43, 100]),
   midi.NoteOffEvent(tick=3840, channel=0, data=[43, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[41, 100]),
   midi.NoteOffEvent(tick=1920, channel=0, data=[41, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 100]),
   midi.NoteOffEvent(tick=1920, channel=0, data=[43, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[52, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[50, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[48, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[47, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[45, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[53, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[53, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[52, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[50, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[48, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[47, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[55, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[55, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[53, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[52, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[50, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[48, 100]),
   midi.NoteOnEvent(tick=960, channel=0, data=[43, 100]),
   midi.NoteOffEvent(tick=3840, channel=0, data=[43, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[41, 100]),
   midi.NoteOffEvent(tick=1920, channel=0, data=[41, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 100]),
   midi.NoteOffEvent(tick=1920, channel=0, data=[43, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[52, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[50, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[48, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 100]),
   midi.NoteOffEvent(tick=960, channel=0, data=[47, 100]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 100]),
   midi.NoteOffEvent(tick=2880, channel=0, data=[45, 100]),
   midi.EndOfTrackEvent(tick=0, data=[])])])

midi.write_midifile("{}.mid".format("output1"), pattern1)

