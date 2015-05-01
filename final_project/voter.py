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
        borda_vote = []
        for cand, util in self.preferences.iteritems():
            borda_vote.append((cand,util))
        votes = sorted(borda_vote,key=itemgetter(1))
        return votes

        #this doesn't look right??
        """cand_util = self.preferences.iteritems()
        return [x[1] for x in cand_util]"""

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

    def get_util_for_candidate(candidate):
        return self.preferences[candidate]


class Election:

    def __init__(self, election_type, n_cand, n_voters):
        self.type = election_type
        self.candidates = range(n_cand)
        self.winner = None
        self.vote_record = {x: None for x in self.candidates}
        self.voters = {x: None for x in range(n_voters)}
        self.candidate_util = {x: 0 for x in self.candidates}

    def create_voters(self):

        for voter_id, voter in self.voters.iteritems():
            self.voters['voter_id'] = Voter()

    def collect_votes(self, votes):

        if self.type in ['majority', 'plurality']:
            for voter_id, voter in self.voters.iteritems():
                vote = voter.top_vote()
                self.vote_record[vote] += 1

        elif self.tpye == 'Borda':
            num_candidates = len(self.candidates)
            for voter in self.voters:
                my_votes = voter.Borda_vote()
                for i in range(len(my_votes)):
                    self.vote_record[my_votes[i][0]] += num_candidates - i
            ####### TBD I don't think the votes itself is right. so I'll do this later

        elif self.type == 'democracy21':
            for voter in self.voters:
                my_vote = voter.dem21_vote()
                for cand in my_vote['pos_vote']:
                    self.vote_record[cand] += 1
                self.vote_record[my_vote['neg_vote']] -=1

    def determine_winner(self):

        if self.type != 'majority':
            for cand, votes in self.vote_record:
                if votes == max(self.vote_record.values):
                    self.winner = cand
        else:
            self.winner = None # TO BE IMPLEMENTED YEAH IDK

    def calc_utilities(self):
        #Fills in a dictionary that maps candidates to how much utility they give to all the voters
        for cand in self.candidates:
            util = 0
            for voter in self.voters:
                util += voter.get_util_for_candidate(cand)
            self.candidate_util[cand] = util

    def calc_optimal(self):
        #returns the who the winner to maximize social utility would be, and that winner(TBD)
        return max(self.candidate_util.values)

    def calc_winner_util(self):
        #returns the utility from the winner of the election
        return self.candidate_util[self.winner]







