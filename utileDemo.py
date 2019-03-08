#

from midiutil.MidiFile import MIDIFile

class arpeggio:
    def __init__(self, intervals, diatonicMath = True):
        self.intervals = list(intervals)
        self.diatonicMath = diatonicMath
    
    def Render(self, diatonic, key, scale, noteDuration, reverseDirection = False):
        if reverseDirection == True:
            self.intervals.reverse()
        toReturn = []
        for interval in self.intervals:
            pitch = key + scale[(diatonic + interval) % 7]
            if (diatonic > 6) or (diatonic < 0):
                pitch = pitch + 12 * (round((diatonic + interval) /7))
            toReturn.append(pitch)
        return toReturn
            
        

class MidiPiece:

    def Extend(self, diatonic, key, scale):
        pitch = key + scale[diatonic % 7]
        if (diatonic > 6) or (diatonic < 0):
            return pitch + 12 * (round(diatonic /7))
        return pitch

    def mainRiff(self, key, scale, down, mult, diatonic, time, duration, track):
        #main riff
        while mult > -1:
            for interval in down:
                pitch = self.Extend(diatonic, key, scale)
                self.mf.addNote(track, self.channel, pitch, time, duration, self.volume)
                time = time + duration
                diatonic = diatonic + interval
            mult = mult - 1
            pitch = self.Extend(diatonic, key, scale)
        self.mf.addNote(track, self.channel, pitch, time, duration * 3, self.volume)
       # self.time = self.time + duration * 4
        return time

    def __init__(self, trackNames):
        # create your MIDI object
        self.mf = MIDIFile(len(trackNames))
        self.track = [0] * len(trackNames)
        self.time = [1] * len(trackNames)
        index = 0

        #proj.time[0] = 0    # start at the beginning
        #proj.time[1] = 0    # start at the beginning
        #self.mf.addTrackName(self.track[1], proj.time[1], "Bass")
        #self.mf.addTempo(self.track[1], proj.time[1], 120)
        for name in trackNames:
            #self.track.append(index)
            self.mf.addTrackName(self.track[index], self.time[index], trackNames[index])
            self.mf.addTempo(self.track[index], self.time[index], 120)
            index = index + 1


        # add some notes
        self.channel = 0
        self.volume = 100 

        #The most common scales, by relative number semi-tones from root 
        self.major = [0, 2, 4, 5, 7, 9, 11]
        self.minorAsc = [0, 2, 3, 5, 7, 9, 11]
        self.minorDesc = [0, 2, 3, 5, 7, 8, 10]
        self.minorHarm = [0, 2, 3, 5, 7, 8, 11]

trackNames = ["Treble", "Bass"]
proj = MidiPiece(trackNames)

#baroque example
key = 69
scale = proj.minorDesc
down = [-1]
mult = 3

duration = 1

proj.mf.addNote(proj.track[1], proj.channel, key - 24, proj.time[1], 4, proj.volume)
proj.time[1] += 4
times = 2
while times > 0:
    diatonic = 4
    times = times - 1
    proj.time[0] = proj.mainRiff(key, scale, down, mult, diatonic, proj.time[0], duration, proj.track[0])

    diatonic = 5
    proj.time[1] = proj.mainRiff(key - 24, scale, down, mult, diatonic, proj.time[1], duration, proj.track[1])

    proj.time[0] = proj.mainRiff(key, scale, down, mult, diatonic, proj.time[0], duration, proj.track[0])

    diatonic = 6
    proj.time[1] = proj.mainRiff(key - 24, scale, down, mult, diatonic, proj.time[1], duration, proj.track[1])

    intervals = [2, 0]
    diatonic = 2
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, False)
    for pitch in pitches:
        proj.mf.addNote(proj.track[0], proj.channel, pitch, proj.time[0], duration, proj.volume)
        proj.time[0] = proj.time[0] + duration

    diatonic = 3
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, False)
    for pitch in pitches:
        proj.mf.addNote(proj.track[0], proj.channel, pitch, proj.time[0], duration, proj.volume)
        proj.time[0] = proj.time[0] + duration

    intervals = [7, 5, 3, 0]
    diatonic = -1
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, False)
    for pitch in pitches:
        proj.mf.addNote(proj.track[0], proj.channel, pitch, proj.time[0], duration, proj.volume)
        proj.time[0] = proj.time[0] + duration

    proj.mf.addNote(proj.track[1], proj.channel, key - 24 - 2, proj.time[1], duration * 4, proj.volume)
    proj.time[1] = proj.time[1] + duration * 4

    proj.mf.addNote(proj.track[1], proj.channel, key - 24 - 4, proj.time[1], duration * 2, proj.volume)
    proj.time[1] = proj.time[1] + duration * 2
    proj.mf.addNote(proj.track[1], proj.channel, key - 24 - 2, proj.time[1], duration * 2, proj.volume)
    proj.time[1] = proj.time[1] + duration * 2

    diatonic = 4
    proj.time[1] = proj.mainRiff(key - 24, scale, down, mult, diatonic, proj.time[1], duration, proj.track[1])

    intervals = [2, 0]
    diatonic = 0
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, True)
    for pitch in pitches:
        proj.mf.addNote(proj.track[0], proj.channel, pitch, proj.time[0], duration, proj.volume)
        proj.time[0] = proj.time[0] + duration

    #intervals = [2, 0]
    diatonic = 1
    arp = arpeggio(intervals)
    pitches = arp.Render(diatonic, key, scale, duration, True)
    for pitch in pitches:
        proj.mf.addNote(proj.track[0], proj.channel, pitch, proj.time[0], duration, proj.volume)
        proj.time[0] = proj.time[0] + duration

    proj.mf.addNote(proj.track[0], proj.channel, key + 3, proj.time[0], duration * 2, proj.volume)
    proj.time[0] = proj.time[0] + duration * 4

    # write it to disk
    with open("output.mid", 'wb') as outf:
        proj.mf.writeFile(outf)





