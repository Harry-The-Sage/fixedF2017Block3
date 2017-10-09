#Harrison and Reese

team_name = 'Thunder Chickens' # Only 10 chars displayed.
strategy_name = 'To prevail the rivals'
strategy_description = 'Undisclosed'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)<=2:
        return 'c'
    if their_history[0:3]== 'ccb' and len(my_history)==3:
        return 'b'
    if their_history[0:4]== 'ccbc' and len(my_history)==4:
        return 'c'    
    if their_history[0:5]== 'ccbcb' and len(my_history)==5:
        return 'b'
    if their_history[0:6]== 'ccbcbc':
        return 'c'
    if 'b' in their_history:
        return 'b'
    else:
        return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        # print("move(" +
        #     ", ".join(["'"+my_history+"'", "'"+their_history+"'",
        #                str(my_score), str(their_score)])+
        #     ") returned " + "'" + real_result + "'" +
        #     " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # 1st thing: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
         
     # 2nd thing: Continue betraying despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             