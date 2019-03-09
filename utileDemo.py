#
from MidiPieces.MidiPiece import MidiPiece
from MidiPieces.MidiPiece import arpeggio

trackNames = ["Treble", "Bass"]
proj = MidiPiece(trackNames)

#Somewhat baroque sounding example which reuses a simple 4 note diatonic descending motif, and a leap of a diatonic 3rd motif, and inversions of it.
key = 69
scale = proj.minorDesc
down = [-1]
mult = 3

duration = 1

proj.addNote(1, proj.channel, key - 24, 1, 4)

times = 2
while times > 0:
    times -= 1
    proj.mainRiff(key, scale, down, mult, 4, 0, duration, proj.track[0])

    proj.mainRiff(key - 24, scale, down, mult, 5, 1, duration, proj.track[1])

    proj.mainRiff(key, scale, down, mult, 5, 0, duration, proj.track[0])

    proj.mainRiff(key - 24, scale, down, mult, 6, 1, duration, proj.track[1])

    intervals = [2, 0]
    diatonic = 2
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, False)
    for pitch in pitches:
        proj.addNote(0, proj.channel, pitch, 0, duration)

    diatonic = 3
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, False)
    for pitch in pitches:
        proj.addNote(0, proj.channel, pitch, 0, duration)

    intervals = [7, 5, 3, 0]
    diatonic = -1
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, False)
    for pitch in pitches:
        proj.addNote(0, proj.channel, pitch, 0, duration)

    proj.addNote(1, proj.channel, key - 24 - 2, 1, duration * 4)

    proj.addNote(1, proj.channel, key - 24 - 4, 1, duration * 2)

    proj.addNote(1, proj.channel, key - 24 - 2, 1, duration * 2)

    diatonic = 4
    proj.mainRiff(key - 24, scale, down, mult, diatonic, 1, duration, proj.track[1])

    intervals = [2, 0]
    diatonic = 0
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, True)
    for pitch in pitches:
        proj.addNote(0, proj.channel, pitch, 0, duration)

    diatonic = 1
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, True)
    for pitch in pitches:
        proj.addNote(0, proj.channel, pitch, 0, duration)

    proj.addNote(0, proj.channel, key + 3, 0, duration * 2, duration * 2)

# write it to disk
with open("output.mid", 'wb') as outf:
    proj.mf.writeFile(outf)





