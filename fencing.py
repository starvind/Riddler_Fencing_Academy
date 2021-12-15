
from math import factorial

r1_target = 15
r2_target = 30
r3_target = 45
prob_seq = [0.25, 0.5, 0.75] 	# chosen sequence of probabilities
#prob_seq = [1, 1, 1]
win_probabilty = 0  			# final win prob initialization
loss_probability = 0 			# final loss prob initialization
round_1_win_prob = 0
round_1_loss_prob = 0
round_2_win_prob = 0
round_2_loss_prob = 0
exp_matches_p1 = 0
exp_matches_p2 = 0
exp_matches_p3 = 0

# function to get probabilties given start (s1, s2) and end states (e1,e2) of your team (1) and opponent (2) and your probability p of winning
def get_prob(s1,e1,s2,e2,p):
	
	d1 = e1 - s1
	d2 = e2 - s2
	n = d1 + d2
	if e1 < e2:
		ld = e1 - s1
	else:
		ld = e2 - s2 
	q = 1 - p 
#	print(s1,e1,s2,e2)	 
	prob = factorial(n-1)*(p**d1)*(q**d2)/(factorial(ld)*factorial(n-1-ld))
	return prob	


def round1():
	global round_1_win_prob
	global round_1_loss_prob
	global exp_matches_p1
	r1_counter = 0
	while r1_counter <=1:
		st1 = 0		
		st2 = 0
		if r1_counter == 0:
			et2 = r1_target
			et1 = 0
			while et1 < r1_target:
				answer_prob = get_prob(st1,et1,st2,et2,prob_seq[0])
				round_1_loss_prob += answer_prob
				exp_matches_p1 += answer_prob*(et1-st1 + et2 - st2)
#				print("from first", st1,st2,et1,et2, answer_prob)
				round2(answer_prob,et1,et2)
				et1 += 1
		else:
			et1 = r1_target
			et2 = 0
			while et2 < r1_target:
				answer_prob = get_prob(st1,et1,st2,et2,prob_seq[0])
				round_1_win_prob += answer_prob
				exp_matches_p1 += answer_prob*(et1-st1 + et2 - st2)
#				print("from second", st1,st2,et1,et2, answer_prob)
				round2(answer_prob,et1,et2)
				et2 += 1				
		r1_counter += 1
	return()



def round2(prob,e1i,e2i):
	global round_2_win_prob
	global round_2_loss_prob
	global exp_matches_p2
	r2_counter = 0
	while r2_counter <=1:
		s1 = e1i
		s2 = e2i
		if r2_counter == 0: 
			e1 = s1  
			e2 = r2_target
			while e1 < r2_target:
				answer_prob = prob*get_prob(s1,e1,s2,e2,prob_seq[1])
				round_2_loss_prob += answer_prob
				exp_matches_p2 += answer_prob*(e1-s1 + e2 - s2)
#				print(e1,e2, answer_prob)
				round3(answer_prob,e1,e2)
				e1 += 1
		else: 
			e1 = r2_target
			e2 = s2
			while e2 < r2_target:
				answer_prob = prob*get_prob(s1,e1,s2,e2,prob_seq[1])
				round_2_win_prob += answer_prob
				exp_matches_p2 += answer_prob*(e1-s1 + e2 - s2)
				round3(answer_prob,e1, e2)
				e2 +=1
		r2_counter +=1


def round3(prob, e1i, e2i):
	global win_probabilty
	global loss_probability
	global exp_matches_p3
	r3_counter = 0
	while r3_counter <=1:
		s1 = e1i
		s2 = e2i
		if r3_counter == 0: 
			e2 = r3_target
			e1 = s1
			while e1 < r3_target:
				loss_probability += prob*get_prob(s1,e1,s2,e2,prob_seq[2])
				exp_matches_p3 += prob*get_prob(s1,e1,s2,e2,prob_seq[2])*(e1-s1+e2-s2)
				e1 += 1
		else:
			e1 = r3_target
			e2 = s2	
			while e2 < r3_target:
				win_probabilty += prob*get_prob(s1,e1,s2,e2,prob_seq[2])
				exp_matches_p3 += prob*get_prob(s1,e1,s2,e2,prob_seq[2])*(e1-s1+e2-s2)
	#			print("final", e1,e2, win_probabilty)
				e2 += 1	
		r3_counter +=1

round1()

print(prob_seq)
print("Round 1 Win Probability:", round_1_win_prob, "Round 1 Loss Probability:", round_1_loss_prob, "Total: ", round_1_win_prob + round_1_loss_prob)
print("Round 2 Win Probability:", round_2_win_prob, "Round 2 Loss Probability:", round_2_loss_prob, "Total: ", round_2_win_prob + round_2_loss_prob)
print("Final Win Probability:", win_probabilty, "Final Loss Probability:", loss_probability, "Total: ", win_probabilty + loss_probability)
print("Expected matches in round 1: ", exp_matches_p1)
print("Expected matches in round 2: ", exp_matches_p2)
print("Expected matches in round 3: ", exp_matches_p3)
print("Expected total matches: ", exp_matches_p3 + exp_matches_p2 + exp_matches_p1)



#-----------
