from voter import *

# run the election

# Initialize Parameters

N_VOTERS = 100
N_CAND = 5

# plurality_elec = Election('plurality', N_CAND, N_VOTERS)
# plurality_elec.create_voters()
# plurality_elec.collect_votes()
# plurality_elec.determine_winner()

# print "Winner: Candidate", plurality_elec.winner

# plurality_elec.calc_utilities()
# plurality_elec.calc_optimal()

# print "Total Utility for Each Candidate"
# for cand, util in plurality_elec.candidate_util.iteritems():
# 	print "Candidate:", cand, "Total Utility:", util

# print 

# for cand, vote in plurality_elec.vote_record.iteritems():
# 	print "Candidate:", cand, "Total Votes:", vote

# print "Winner: Candidate", plurality_elec.winner
# print "Socially Optimal: Candidate", plurality_elec.optimal_cand


# plurality_elec = Election('majority', N_CAND, N_VOTERS)
# plurality_elec.create_voters()
# plurality_elec.collect_votes()
# plurality_elec.determine_winner()


# plurality_elec.calc_utilities()
# plurality_elec.calc_optimal()

# print "Total Utility for Each Candidate"
# for cand, util in plurality_elec.candidate_util.iteritems():
# 	print "Candidate:", cand, "Total Utility:", util

# print 

# for cand, vote in plurality_elec.vote_record.iteritems():
# 	print "Candidate:", cand, "Total Votes:", vote

# print 

# print "REVOTING HAS COMMENCED!"

# print 

# for cand, vote in plurality_elec.majority_revote_record.iteritems():
# 	if vote == 0:
# 		continue
# 	else:
# 		print "Candidate:", cand, "Total Votes:", vote	

# print "Winner: Candidate", plurality_elec.winner
# print "Socially Optimal: Candidate", plurality_elec.optimal_cand

# plurality_elec = Election('Borda', N_CAND, N_VOTERS)
# plurality_elec.create_voters()
# plurality_elec.collect_votes()
# plurality_elec.determine_winner()


# plurality_elec.calc_utilities()
# plurality_elec.calc_optimal()

# print "Total Utility for Each Candidate"
# for cand, util in plurality_elec.candidate_util.iteritems():
# 	print "Candidate:", cand, "Total Utility:", util

# print 

# for cand, vote in plurality_elec.vote_record.iteritems():
# 	print "Candidate:", cand, "Total Votes:", vote

# print 

# print "Winner: Candidate", plurality_elec.winner
# print "Socially Optimal: Candidate", plurality_elec.optimal_cand


plurality_elec = Election('democracy21', N_CAND, N_VOTERS)
plurality_elec.create_voters()
plurality_elec.collect_votes()
plurality_elec.determine_winner()
plurality_elec.calc_total_votes()


plurality_elec.calc_utilities()
plurality_elec.calc_optimal()

print "Total Utility for Each Candidate"
for cand, util in plurality_elec.candidate_util.iteritems():
	print "Candidate:", cand, "Total Utility:", util

print 

for cand, vote in plurality_elec.vote_record.iteritems():
	print "Candidate:", cand, "Total Votes:", vote



print 

print "Winner: Candidate", plurality_elec.winner
print "Socially Optimal: Candidate", plurality_elec.optimal_cand

print 

print "total votes cast", plurality_elec.total_votes









