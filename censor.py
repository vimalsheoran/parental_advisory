import time
from censor_conf import swear_list, censor_list, LYRICS

swear_count = 0

# Reading the lyrics file
lyrics_file = open(LYRICS, "U")

# for swear in swear_list:
# 	print swear

# Providing swear word analysis
print("Running Analysis.......")
time.sleep(1)
all_words = list(lyrics_file.read().split())
#print all_words
for swear in swear_list:
	for word in all_words:
		if word == swear:
			swear_count += 1
	print swear+" appears "+str(swear_count)+" times in the song."
	swear_count = 0

# Censoring lyrics
print("Censoring Lyrics...........")
time.sleep(1)
raw_lyrics = lyrics_file.read()
for swear in swear_list:
	while swear in raw_lyrics:
		raw_lyrics = raw_lyrics.replace(swear, censor_list[swear])

# Outputing censored lyrics
print("Generating Clean Version.........")
time.sleep(1)
with open("censored_lyrics.txt", "w") as f:
	f.write(raw_lyrics)

print("Done!")

'''
for swear in raw_lyrics:
		swear_count += 1
	print swear+" appears "+str(swear_count)+" times in the song."
	swear_count = 0
'''
