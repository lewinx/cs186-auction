import random
import heapq
import itertools

class Voter():

	def __init__(self, id):
		self.name = name
		self.id = id
		self.preferences = None

	def init_preferences(self, candidates):

		self.preferences = {x: random.randint(0, 100) for x in candidates}

	def top_vote(self):

		for cand, util in self.preferences.iteritems():
    		if util == max(self.preferences.values):
    			return cand

	def Borda_vote(self):

		cand_util = self.preferences.iteritems()
		return [x[1] for x in cand_util]

	def dem21_vote(self):

		votes = {'pos_votes' = []}

		for cand, util in self.preferences.iteritems():
			if util == min(self.preferences.values):
				votes['neg_vote'] = cand
			elif util == max(self.preferences.values):
				votes['pos_vote'].append(cand)
			elif util == heapq.nlargest(2, self.preferences.values):
				votes['pos_vote'].append(cand)

		return votes


class Election:

	def __init__(self, election_type, n_cand, n_voters):
		self.type = election_type
		self.candidates = range(n_cand)
		self.winner = None
		self.vote_record = {x: None for x in self.candidates}
		self.voters = {x: None for x in range(n_voters)}

	def create_voters(self):
		for voter_id, voter in self.voters.iteritems():
			self.voters['voter_id'] = Voter()

	def collect_votes_top(self, votes):

		if self.type in ['majority', 'plurality']:
			for voter_id, voter in self.voters.iteritems():
				vote = voter.top_vote()
				self.vote_record[vote] += 1

		elif self.tpye == 'Borda':
			self.vote_record = None

		elif self.type == 'democracy21':
			self.vote_record = None

	def determine_winner(self):

		if self.type != 'majority':
			for cand, votes in self.vote_record:
				if votes == max(self.vote_record.values):
					self.winner = cand
		else:
			self.winner = None # TO BE IMPLEMENTED

	def calc_utilities(self):

	def calc_optimal(self):







