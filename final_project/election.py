from voter import *

# run the election

plurality_elec = Election('plurality', 3, 20)
plurality_elec.create_voters()
plurality_elec.collect_votes()
plurality_elec.determine_winner()

print "Winner: Candidate", plurality_elec.winner

plurality_elec.calc_utilities()
print "Total Utility for Each Candidate"
for cand, util in plurality_elec.candidate_util.iteritems():
	print "Candidate:", cand, "Total Utility:", util

for cand, vote in plurality_elec.vote_record.iteritems():
	print "Candidate:", cand, "Total Votes:", vote

print "Winner: Candidate", plurality_elec.winner
print "Socially Optimal Candidate", "Hi"




