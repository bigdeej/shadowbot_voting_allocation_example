import math


SHADOW_DIVIDER = 5
FRACTIONAL_VOTING_THRESHOLD = 1250
FVLSD = FRACTIONAL_VOTING_THRESHOLD / SHADOW_DIVIDER

for shadow_rank in range(101):
	if shadow_rank == 0:
		continue

	print("#################")
	for r in range(21):
		if r == 0:
			continue

    # Hacky just to get a variation of steem power levels
		steem_power = r*r*r*r*5

		vote_curr = math.floor((shadow_rank / SHADOW_DIVIDER))
		if vote_curr < 1:
			vote_curr = 1

		vote_new = round( ( ( ( shadow_rank + (steem_power/ FVLSD) ) / 2 ) / SHADOW_DIVIDER), 1)


		print("SR: {}\t SP: {}\t OLD: {} \t NEW: {}".format(shadow_rank, steem_power, vote_curr, vote_new))
