import random
import heapq
import itertools

class Voter:

    def __init__(self, id, candidates):
        self.id = id
        self.preferences = {x: random.randint(0, 100) for x in candidates}

    def top_vote(self):

        for cand, util in self.preferences.iteritems():
            if util == max(self.preferences.values()):
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

        votes = {'pos_votes' : []}

        for cand, util in self.preferences.iteritems():
            if util == min(self.preferences.values):
                votes['neg_vote'] = cand
            elif util == max(self.preferences.values):
                votes['pos_vote'].append(cand)
            elif util == heapq.nlargest(2, self.preferences.values):
                votes['pos_vote'].append(cand)

        return votes

    def get_util_for_candidate(self, candidate):
        return self.preferences[candidate]

    def majority_revote(self, candidates):
        """candidates: list of the two candidates who can be voted for in the runoff"""
        if self.preferences(candidates[0]) > self.preferences(candidates[1]):
            return candidates[0]
        else:
            return candidate[1]



class Election:

    def __init__(self, election_type, n_cand, n_voters):
        self.type = election_type
        self.candidates = range(n_cand)
        self.winner = None
        self.vote_record = {x: 0 for x in self.candidates}
        self.voters = {x: None for x in range(n_voters)}
        self.candidate_util = {x: 0 for x in self.candidates}
        self.majority_revote_record = {x: None for x in self.candidates}

    def create_voters(self):

        i = 0
        for voter_id, voter in self.voters.iteritems():
            self.voters[i] = Voter(i, self.candidates)
            i += 1

    def collect_votes(self):

        if self.type in ['majority', 'plurality']:
            for voter_id, voter in self.voters.iteritems():
                vote = voter.top_vote()
                self.vote_record[vote] += 1

        elif self.tpye == 'Borda':
            num_candidates = len(self.candidates)
            for voter_id, voter in self.voters.iteritems():
                my_votes = voter.Borda_vote()
                for i in range(len(my_votes)):
                    self.vote_record[my_votes[i][0]] += num_candidates - i

        elif self.type == 'democracy21':
            for voter_id, voter in self.voters.iteritems():
                my_vote = voter.dem21_vote()
                for cand in my_vote['pos_vote']:
                    self.vote_record[cand] += 1
                self.vote_record[my_vote['neg_vote']] -=1

    def election_majority_revote(self, candidates):
        """Performs revote for a limited set of candidates
            candidates: the list of candidates that are allowed to be voted for
        """
        if len(candidates) != 2:
            print("majority_revote failed")
            return 1
        for voter_id,voter in self.voters.iteritems():
            vote = voter.majority_revote(candidates)
            self.majority_revote_record[vote] +=1

    def determine_runoff_winner(self):
        for cand, votes in self.vote_record:
            if votes = max(self.majority_revote_record)
                return cand

    def determine_winner(self):

        if self.type != 'majority':
            for cand, votes in self.vote_record.iteritems():
                if votes == max(self.vote_record.values()):
                    self.winner = cand
        else:
            runoff_cand = []
            #Either determine a winner or do a re-vote for the 2 highest candidates
            for cand, votes in self.vote_record:
                if votes == max(self.vote_record.values) and votes >= len(self.voters):
                    self.winner = candidate
                    return 0
                else:
                    if votes == max(self.vote_record.values) or heapq.nlargest(2, self.vote_record.values):
                        runoff_cand.append(cand)

            election_majority_revote(runoff_cand)
            self.winner = determine_runoff_winner()

    def calc_utilities(self):
        #Fills in a dictionary that maps candidates to how much utility they give to all the voters
        for cand in self.candidates:
            util = 0
            for voter_id, voter in self.voters.iteritems():
                util += voter.get_util_for_candidate(cand)
            self.candidate_util[cand] = util

    def calc_optimal(self):
        #returns the who the winner to maximize social utility would be, and that winner(TBD)
        return max(self.candidate_util.values)

    def calc_winner_util(self):
        #returns the utility from the winner of the election
        return self.candidate_util[self.winner]







