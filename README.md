*PARENTAL ADVISORY

**WHAT IS IT?
I watched a video online of a kid who was rapping to a track and he was refering to lyrics online to do his karaoke and he was pausing a lot. I realised that he was actually pausing at curses and was not able to say anything. That's when I decided that, this evening I won't be spending my time watching Youtube but, rather write a simple program that can censor lyrics. So here you have it.

**USAGE

1.Before you start cleaning up the lyrics to your favourite track, you will have to setup configurations. To do this you will have to tweak the 'censor_conf.py' file. It has three main controllers. 
    1. 'LYRIC' which is a variable which stores the name of the lyric file, in this case it has been automatically set to 'sample_lyrics.txt'
    2. Next is the 'swear_list' which is the list of all the swear words you want to sensor in a given song. A sample list is already been shipped with the commits.
    3. The last controller is the 'censor_list', which is a dictionary which will map a curse to it's censored version. If you want to censor a particular word in your lyrics, just put in the word as a key and the censored word as the value to the key.
2. 
