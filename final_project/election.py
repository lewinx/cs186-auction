from voter import *
import argparse
import pandas as pd

# run the election

# Initialize Parameters



parser = argparse.ArgumentParser(description='Outputs a csv of voting outcomes.')

# command line arguments

parser.add_argument('N_VOTERS', metavar='N_VOTERS', type = int, help = 'number of voters')
parser.add_argument('N_CAND', metavar = 'N_CAND', type = int, help = 'number of candidates')
parser.add_argument('ITER', metavar = 'ITER', type = int, help = 'number of iterations')

args = parser.parse_args()


N_VOTERS = args.N_VOTERS
N_CAND = args.N_CAND
ITER = args.ITER

# save everything to a CSV

plurality_winner = []

df = pd.DataFrame(columns=['plurality_winner','majority_winner','Borda_winner', 'democracy21_winner', 
	'socially_optimal', 'socially_optimal_util', 
	'plurality_loss', 'majority_loss', 'Borda_loss','democracy21_loss'], index=range(ITER))

row = 0

for _ in xrange(ITER):



	election = Election('all', N_CAND, N_VOTERS)
	election.create_voters()

	election.calc_utilities()
	election.calc_optimal()

	print "Total Utility for Each Candidate"
	for cand, util in election.candidate_util.iteritems():
		print "Candidate:", cand, "Total Utility:", util

	print 

	winners = []
	socially_optimal = election.optimal_cand
	socially_optimal_util = 0
	loss = []

	for elec in ['plurality', 'majority', 'Borda', 'democracy21']:

		print elec.upper(), "ELECTION"
		print 

		election.set_election_type(elec)
		election.collect_votes()
		election.determine_winner()

		winners.append(election.winner)

		socially_optimal_util = election.candidate_util[socially_optimal]
		loss.append(socially_optimal_util - election.candidate_util[election.winner])

		print "Winner: Candidate", election.winner

		for cand, vote in election.vote_record.iteritems():
			print "Candidate:", cand, "Total Votes:", vote

		if elec == 'majority':
			print 

			print "REVOTING HAS COMMENCED!"

			print 

			for cand, vote in election.majority_revote_record.iteritems():
				if vote == 0:
					continue
				else:
					print "Candidate:", cand, "Total Votes:", vote	



		print "Winner: Candidate", election.winner
		print 
		print "Socially Optimal: Candidate", election.optimal_cand

		election.calc_total_votes()

		print election.total_votes

		election.reset_election()

	df.loc[row] = pd.Series({'plurality_winner': winners[0], 
		'majority_winner': winners[1], 
		'Borda_winner': winners[2], 
		'democracy21_winner': winners[3], 
		'socially_optimal': socially_optimal,
		'socially_optimal_util': socially_optimal_util, 
		'plurality_loss': loss[0],
		'majority_loss': loss[1],
		'Borda_loss': loss[2],
		'democracy21_loss': loss[3]})

	row += 1

		    
df.to_csv('data_normal1prefs.csv')


