import random
import heapq
import itertools
import numpy as np
import sys
import copy

class Voter:

    def __init__(self, id, candidates):
        self.id = id
        self.preferences = {x: random.random() for x in candidates}
        # self.preferences = {x: np.random.normal(loc=(float(x)/float(len(candidates))), scale = 2.0*x/float(len(candidates)) + 1.0) for x in candidates}
        self.noisy_preferences = copy.deepcopy(self.preferences)
        for cand in self.noisy_preferences.keys():
            self.noisy_preferences[cand] += np.random.standard_normal()

        # let's choose top 2 noisy_preferred candidates
        self.noisy_preferences[1] = np.random.exponential(scale = 2)
        self.noisy_preferences[2] = np.random.exponential(scale = 2)

        self.preferences[1] = np.random.exponential(scale = 2)
        self.preferences[2] = np.random.exponential(scale = 2)

    def top_vote(self):

        for cand, util in self.noisy_preferences.iteritems():
            if util == max(self.noisy_preferences.values()):
                return cand

    def Borda_vote(self):
        borda_vote = []
        for cand, util in self.noisy_preferences.iteritems():
            borda_vote.append((cand,util))
        votes = sorted(borda_vote,key=lambda x: x[1], reverse = True)
        return votes

    def dem21_vote(self):

        votes = {'pos_vote' : []}

        for cand, util in self.noisy_preferences.iteritems():
            if util == min(self.noisy_preferences.values()):
                votes['neg_vote'] = cand
            elif util == max(self.noisy_preferences.values()):
                votes['pos_vote'].append(cand)
            elif util == heapq.nlargest(2, self.noisy_preferences.values())[1]:
                votes['pos_vote'].append(cand)

        return votes

    def get_util_for_candidate(self, candidate):
        return self.preferences[candidate]

    def get_noisy_util_for_candidate(self, candidate):
        return self.noisy_preferences[candidate]

    def majority_revote(self, candidates):
        """candidates: list of the candidates who can be voted for in the runoff"""
        fav_cand = None
        temp_max_utility = -1*sys.maxint
        for candidate in candidates:
            if self.get_util_for_candidate(candidate) > temp_max_utility:
                temp_max_utility = self.get_noisy_util_for_candidate(candidate)
                fav_cand = candidate
        return fav_cand

class Election:

    def __init__(self, election_type, n_cand, n_voters):
        self.type = election_type
        self.candidates = range(n_cand)
        self.winner = None
        self.vote_record = {x: 0 for x in self.candidates}
        self.voters = {x: None for x in range(n_voters)}
        self.candidate_util = {x: 0 for x in self.candidates}
        self.majority_revote_record = {x: 0 for x in self.candidates}
        self.optimal_cand = None
        self.total_votes = 0

    def create_voters(self):

        i = 0
        for voter_id, voter in self.voters.iteritems():
            self.voters[i] = Voter(i, self.candidates)
            i += 1

    def set_election_type(self, election_type):
        self.type = election_type

    def collect_votes(self):

        if self.type in ['majority', 'plurality']:
            for voter_id, voter in self.voters.iteritems():
                vote = voter.top_vote()
                self.vote_record[vote] += 1

        elif self.type == 'Borda':
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
        
        for voter_id,voter in self.voters.iteritems():
            vote = voter.majority_revote(candidates)
            self.majority_revote_record[vote] +=1

    def determine_runoff_winner(self):
        for cand, votes in self.majority_revote_record.iteritems():
            if votes == max(self.majority_revote_record.values()):
                self.winner = cand

    def determine_winner(self):

        if self.type != 'majority':
            runoff_cand = []
            for cand, votes in self.vote_record.iteritems():
                if votes == max(self.vote_record.values()):
                    runoff_cand.append(cand)
            if len(runoff_cand) == 1:
                self.winner = runoff_cand[0]
            else:
                # We choose to use a majority voting scheme if there are ties
                self.election_majority_revote(runoff_cand)
                self.determine_runoff_winner()
        else:
            runoff_cand = []
            #Either determine a winner or do a re-vote for the 2 highest candidates
            max_votes = max(self.vote_record.values())
            second_max_votes = heapq.nlargest(2, self.vote_record.values())[1]


            n_votes = len(self.voters.keys()) 

            for cand, votes in self.vote_record.iteritems():
                if (votes == max_votes) and (votes >= len(self.voters.keys())):
                    self.winner = candidate

                    return 0
                else:
                    if (votes == max_votes) or (votes == second_max_votes):
                        runoff_cand.append(cand)


            self.election_majority_revote(runoff_cand)
            self.determine_runoff_winner()

    def calc_utilities(self):
        # Fills in a dictionary that maps candidates to how much utility they give to all the voters
        for cand in self.candidates:
            util = 0
            for voter_id, voter in self.voters.iteritems():
                util += voter.get_util_for_candidate(cand)
            self.candidate_util[cand] = util

    def calc_optimal(self):
        # returns the who the winner to maximize social utility would be, and that winner(TBD)
        max_utility = max(self.candidate_util.values())
        for candidate in self.candidates:
            if self.candidate_util[candidate] == max_utility:
                self.optimal_cand = candidate
        # self.optimal_cand = max(self.candidate_util, key=lambda x: self.candidate_util[x])
        return max(self.candidate_util.values())

    def calc_winner_util(self):
        # returns the utility from the winner of the election
        return self.candidate_util[self.winner]

    def calc_total_votes(self):
        self.total_votes = sum(self.vote_record.values())

    def reset_election(self):
        self.vote_record = {x: 0 for x in self.candidates}
        self.winner = None
        self.majority_revote_record = {x: 0 for x in self.candidates}
        self.total_votes = 0
