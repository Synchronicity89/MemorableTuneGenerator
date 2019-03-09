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

    def mainRiff(self, key, scale, down, mult, diatonic, timeIndex, duration, track):
        #main riff
        while mult > -1:
            for interval in down:
                pitch = self.Extend(diatonic, key, scale)
                self.mf.addNote(track, self.channel, pitch, self.time[timeIndex], duration, self.volume)
                self.time[timeIndex] += duration
                diatonic = diatonic + interval
            mult = mult - 1
            pitch = self.Extend(diatonic, key, scale)
        self.mf.addNote(track, self.channel, pitch, self.time[timeIndex], duration * 3, self.volume)
        self.time[timeIndex] += duration * 4
        #return time

    def __init__(self, trackNames):
        # create your MIDI object
        self.mf = MIDIFile(len(trackNames))
        self.track = [0] * len(trackNames)
        self.time = [0] * len(trackNames)
        index = 0

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
