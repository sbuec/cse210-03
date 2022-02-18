class PlayerInput:
    '''Retrieves user input and returns a single character'''

    def retrieve(display_message:str) -> str:
        '''Retrieves user input'''
        return input(display_message)
    
    def isBadInput(user_input:str) -> bool:
        '''Checks for incorrect user input'''
        if len(user_input) > 1 or len(user_input) == 0:
            return True
        else:
            if user_input.isnumeric(): return True
            else: return False