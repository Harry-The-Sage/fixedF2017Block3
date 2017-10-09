####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

<<<<<<< HEAD
team_name = 'Trump' # Only 10 chars displayed.
strategy_name = 'The Wall'
strategy_description = 'Deportation Station Nation'
    
def move(my_history, their_history, my_score, their_score):
    if their_history[-2:] == 'bb':
        return 'b'
    elif my_history[-1:] == 'b' and their_history[-2:] == 'bb':
        return 'b'
    elif their_history[-1:] == '':
        return 'b'
    elif their_history[-5:] == 'bcbcb':
        return 'b' 
    else:
        return 'c'
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
=======
team_name = 'Tit4Tat-b' # Only 10 chars displayed.
strategy_name = 'Greedy Tit for Tat'
strategy_description = 'Greedy Tit for Tat'
    
def move(my_history, their_history, my_score, their_score):
    #betray on the first turn
    if len(their_history)==0:
      return 'b'
    #betray if opponent betrayed last turn
    elif their_history[-1] == 'b':
      return 'b'
    #collude if opponent colluded last turn
>>>>>>> upstream/master
    else:
      return 'c'