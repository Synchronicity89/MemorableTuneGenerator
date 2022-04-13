namespace MidiCsvCompression
{
    public class Compress
    {
        public List<string> ReadMidiCsv(string path)
        {
            var lines = File.ReadAllLines(path);
            return lines.ToList();              
        }

        public List<string> ConvertToRelative(List<string> lines)
        {
            //create list of arrays
            var newLines = lines.Where(l => string.IsNullOrWhiteSpace(l) == false).Select(l => l.Split(',', StringSplitOptions.TrimEntries).ToList()).ToList();
            var tracks = newLines.Where(nl => nl[2] == "Start_track");
            foreach (var track in tracks)
            {
                //Two ways to find the first note, as a runtime test.   TODO: decide which one to keep or rewrite the whole thing to make code cleaner
                var findNoteOn = newLines.Where(l => l.Where(n => n.Contains("Note_on")).Any() && newLines.IndexOf(l) > newLines.IndexOf(track)).FirstOrDefault();
                var firstNote = newLines.TakeLast(newLines.Count - newLines.IndexOf(track)).Where(nl => nl[2].Contains("Note_on")).FirstOrDefault();
                if (findNoteOn != firstNote) throw new Exception("Unsure of next first note");
                if(firstNote != null)
                {
                    //TODO: this assumes that each track corresponds to one and only one MIDI channel, which might always be the case
                    //for now, MIDI should be preprocessed so that is the case
                    if (firstNote[0] != track[0]) { continue; }
                    int indx = 0;
                    foreach (var init in firstNote)
                    {
                        if(init.Any(i => char.IsLetter(i)) == false)
                        {
                            track.AddOrReplace<string>(init, indx);
                        }
                        indx++;
                    }
                    int index = newLines.IndexOf(firstNote);
                    while (tracks.Contains(newLines[index]) == false)
                    {
                        if (newLines[index][2].Contains("Note_o") == true)
                        {
                            for (int i = 1; i < newLines[index].Count; i++)
                            {
                                int num = 0;
                                int numTrack = 0;
                                if (int.TryParse(newLines[index][i], out num))
                                {
                                    if (int.TryParse(track[i], out numTrack))
                                    {
                                        newLines[index][i] = (num - numTrack).ToString();
                                    }
                                }
                            }
                        }
                        index++;
                        if (index == newLines.Count) break;
                    }
                }
            }

            return newLines.Select(nl => String.Join(",", nl)).ToList();
        }

        //Add functions to quantize the relative data, detect timing, remove overlap between melody notes, average the velocity profile of motifs.

        //Add functions to split the notes of chords to separate voices each on their own track.  Have a setting where they can also have their own MIDI channel too

        //Add functions to compress using diatonic pitch patterns.  A key that fits best can be chosen and the patterns represented diatonically, they key choice doesn't have to match the composers intention

        public void WriteMidiRel(string relPath, List<string> newLines)
        {
            File.WriteAllLines(relPath, newLines);  
        }
    }

    public static class List_T_Extensions
    {
        public static void AddOrReplace<T>(this List<T> target, T item, int index)
        {
            while(target.Count <= index)
            {
                target.Add(default(T));
            }
            target[index]=item;
        }
    }
}