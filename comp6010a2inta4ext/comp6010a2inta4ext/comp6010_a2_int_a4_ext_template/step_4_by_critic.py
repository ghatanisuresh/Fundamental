'''
DO NOT REMOVE THIS COMMENT
STUDENT ID: 46864512
STUDENT NAME: Suresh Ghatani
[]: add an 'x' inside the square brackets to declare that 
you haven't seen any other person's code
and you haven't shared your code with, or shown your code to, anyone
'''
# only for internal students
 
import step_1_data_reader
import unittest

def get_toughest_critic(dict):       	   		   		 	  		 	
    '''       	   		   		 	  		 	
    Return the index of the toughest critic.
    That is, the critic who gave the minimum
    total core across all the characters.
    '''       	   		   		 	  		 	
    None

class Tester(unittest.TestCase):
    def test_get_toughest_critic(self):       	   		   		 	  		 	
        avatar = step_1_data_reader.read_data("avatar.csv")
        avatar_toughest_critic = get_toughest_critic(avatar)
        self.assertEqual(avatar_toughest_critic, 7)

        harryPotter = step_1_data_reader.read_data("harryPotter.csv")
        harryPotter_toughest_critic = get_toughest_critic(harryPotter)
        self.assertEqual(harryPotter_toughest_critic, 2)
if __name__ == '__main__':
    unittest.main()


