"""
This is what is referred to as a "batch test harness". Essentially, that 
means that many test cases may be run in a single execution of the code.

This method of testing is incredibly valuable when we must run many dozens
(or hundreds or thousands) of test cases in order to validate code.

"""
from user import User                 # We must import the class definition

#=============================================================================
def main( ):
    """
    The main function will essentially call other functions to do all the
    "heavy lifting". As usual, this funciton is the "traffic cop" directing
    the action rather than the one taking action.
    """
    # Call a function to collect the test case and instantiate User objects
    testCases = getTestCases( )
    
    # Use a for loop to check the User objects - Are they what we expect?
    print( "%50s" % "Testing String Method" )
    for case in testCases:
        print( case )
    # end for loop
   

# end main Function 
    
#=============================================================================    
def getTestCases( ):
    """
    This function will prompt for an input file name. (You are MORE THAN
    WELCOME TO CREATE YOUR OWN TEST CASES!) The file containing the test
    cases will be opened for reading. Each line represents a test case. 
    The individual lines will be broken into their constituent pieces and
    those pieces will then be used to INSTANTIATE User objects for testing.
    """
    caseFile = input( "Which file do you want to use for testing? " )
    inputFile = open( caseFile, 'r' ) # Open the file for reading/input

    caseList = [ ]                    # Declare an empty List structure
    
    for line in inputFile:            # Each line in the file = 1 test case
        
        line = line.strip( )          # Strip the newline character from input
        items = line.split( "," )     # Split into "parts" based on comma 
        
        # Instantiate a User object for testing
        testCase = User( items[ 0 ],  # userId
                         items[ 1 ],  # name
                         items[ 2 ],  # employeeNbr
                         items[ 3 ],  # role
                         items[ 4 ] ) # password
         
        # Add the new User object to the List structure
        caseList.append( testCase )
    # end for loop
    
    # Return the completed List structure to caller
    return caseList
# end getTestCases Function


#============================================================================
if __name__ == "__main__":
    main( )

