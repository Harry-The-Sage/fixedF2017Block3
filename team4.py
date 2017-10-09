####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

<<<<<<< HEAD
team_name = 'T-Bones' # Only 10 chars displayed.
strategy_name = 'T-Bone Master Race'
strategy_description = 'Better than the Trumpets'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)<=2:
        return 'b'
    if their_history[0:3]== 'ccb' and len(my_history)==3:
        return 'b'
    if their_history[0:4]== 'ccbc' and len(my_history)==4:
        return 'c'    
    if their_history[0:5]== 'ccbcb':
        return 'b'
    if their_history[0:6]== 'ccbcbc':
        return 'c'
    if 'b' in their_history:
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
team_name = 'Vindict-c' # Only 10 chars displayed.
strategy_name = 'Benevolent Vindictive'
strategy_description = 'Benevolent Vindictive'
    
def move(my_history, their_history, my_score, their_score):
    #collude on the first turn
    if len(their_history)==0:
      return 'c'
    #betray if opponent has ever betrayed previously
    elif 'b' in their_history[-1]:
      return 'b'
    #collude if opponent has never betrayed
>>>>>>> upstream/master
    else:
      return 'c'