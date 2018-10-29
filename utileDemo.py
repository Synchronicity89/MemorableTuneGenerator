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
            
        

class baroque:

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
        time = time + duration * 4
        return time

    def __init__(self):
        # create your MIDI object
        self.mf = MIDIFile(2)     # only 1 track
        self.track0 = 0   # the only track
        self.track1 = 1

        timeT = 0    # start at the beginning
        timeB = 0    # start at the beginning
        self.mf.addTrackName(self.track0, timeT, "Treble")
        self.mf.addTempo(self.track0, timeT, 120)
        self.mf.addTrackName(self.track1, timeB, "Bass")
        self.mf.addTempo(self.track1, timeB, 120)

        # add some notes
        self.channel = 0
        self.volume = 100 

        #The most common scales, by relative number semi-tones from root 
        self.major = [0, 2, 4, 5, 7, 9, 11]
        self.minorAsc = [0, 2, 3, 5, 7, 9, 11]
        self.minorDesc = [0, 2, 3, 5, 7, 8, 10]
        self.minorHarm = [0, 2, 3, 5, 7, 8, 11]

        #baroque example
        key = 69
        scale = self.minorDesc
        down = [-1]
        mult = 3

        duration = 1

        self.mf.addNote(self.track1, self.channel, key - 24, timeB, 4, self.volume)
        timeB = timeB + 4
        times = 2
        while times > 0:
            diatonic = 4
            times = times - 1
            timeT = self.mainRiff(key, scale, down, mult, diatonic, timeT, duration, self.track0)

            diatonic = 5
            timeB = self.mainRiff(key - 24, scale, down, mult, diatonic, timeB, duration, self.track1)

            timeT = self.mainRiff(key, scale, down, mult, diatonic, timeT, duration, self.track0)

            diatonic = 6
            timeB = self.mainRiff(key - 24, scale, down, mult, diatonic, timeB, duration, self.track1)

            intervals = [2, 0]
            diatonic = 2
            arp = arpeggio(intervals)
            pitches = arp.Render(diatonic, key, scale, duration, False)
            for pitch in pitches:
                self.mf.addNote(self.track0, self.channel, pitch, timeT, duration, self.volume)
                timeT = timeT + duration

            diatonic = 3
            arp = arpeggio(intervals)
            pitches = arp.Render(diatonic, key, scale, duration, False)
            for pitch in pitches:
                self.mf.addNote(self.track0, self.channel, pitch, timeT, duration, self.volume)
                timeT = timeT + duration

            intervals = [7, 5, 3, 0]
            diatonic = -1
            arp = arpeggio(intervals)
            pitches = arp.Render(diatonic, key, scale, duration, False)
            for pitch in pitches:
                self.mf.addNote(self.track0, self.channel, pitch, timeT, duration, self.volume)
                timeT = timeT + duration

            self.mf.addNote(self.track1, self.channel, key - 24 - 2, timeB, duration * 4, self.volume)
            timeB = timeB + duration * 4

            self.mf.addNote(self.track1, self.channel, key - 24 - 4, timeB, duration * 2, self.volume)
            timeB = timeB + duration * 2
            self.mf.addNote(self.track1, self.channel, key - 24 - 2, timeB, duration * 2, self.volume)
            timeB = timeB + duration * 2

            diatonic = 4
            timeB = self.mainRiff(key - 24, scale, down, mult, diatonic, timeB, duration, self.track1)

            intervals = [2, 0]
            diatonic = 0
            arp = arpeggio(intervals)
            pitches = arp.Render(diatonic, key, scale, duration, True)
            for pitch in pitches:
                self.mf.addNote(self.track0, self.channel, pitch, timeT, duration, self.volume)
                timeT = timeT + duration

            #intervals = [2, 0]
            diatonic = 1
            arp = arpeggio(intervals)
            pitches = arp.Render(diatonic, key, scale, duration, True)
            for pitch in pitches:
                self.mf.addNote(self.track0, self.channel, pitch, timeT, duration, self.volume)
                timeT = timeT + duration

            self.mf.addNote(self.track0, self.channel, key + 3, timeT, duration * 2, self.volume)
            timeT = timeT + duration * 4


        # write it to disk
        with open("output.mid", 'wb') as outf:
            self.mf.writeFile(outf)
 
proj = baroque()



