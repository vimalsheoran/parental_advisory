from censor_conf import swear_list, censor_list, LYRICS

swear_count = 0

# Reading the lyrics file
lyrics_file = open(LYRICS, "U")

# Censoring lyrics
raw_lyrics = lyrics_file.read()
for swear in swear_list:
	while swear in raw_lyrics:
		raw_lyrics = raw_lyrics.replace(swear, censor_list[swear])
		swear_count += 1
	print swear+" appears "+str(swear_count)+" in the song."
	swear_count = 0
	
# Outputing censored lyrics
with open("censored_lyrics.txt", "w") as f:
	f.write(raw_lyrics)

