# PARENTAL ADVISORY

## WHAT IS IT?
I watched a video online of a kid who was rapping to a track and he was refering to lyrics online to do his karaoke and he was pausing a lot. I realised that he was actually pausing at curses and was not able to say anything. That`s when I decided that, this evening I won`t be spending my time watching Youtube but, rather write a simple program that can censor lyrics. So here you have it.

## USAGE

1. Before you start cleaning up the lyrics to your favourite track, you will have to setup configurations. To do this you will have to tweak the `censor_conf.py` file. It has three main controllers. 
    1.1. `LYRIC` which is a variable which stores the name of the lyric file, in this case it has been automatically set to `sample_lyrics.txt`
    1.2. Next is the `swear_list` which is the list of all the swear words you want to sensor in a given song. A sample list is already been shipped with the commits.
    1.3. The last controller is the `censor_list`, which is a dictionary which will map a curse to it's censored version. If you want to censor a particular word in your lyrics, just put in the word as a key and the censored word as the value to the key.
2. Now you can run the `censor.py` file to generate an analysis of swear words in your lyrics and create a censored lyric file by the name `censored_lyrics.txt`

## Important Notice

I do not own the song 'Nikki' by Logic. The lyrics are provided only to demonstrate the working of the program. I do not aim to commercialise or sell the copyrighted work of Logic and Visionary Music Group. 
