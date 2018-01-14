
class Utils:
    """A class containing some utilities."""    

    #Compare two variables of type int, float or sting
    #return an integer:
      # -ve signifies that the first variable is SMALLER than the second
      # 0 signifies that both the first and second variable are EQUAL
      # +ve signifies that first variable is LARGER than the second
      # -inf signifies, input error
    def compare(self, x, y):
        #We return a -ve float infinity value if there were incompatible variables
        rtn = float("-inf")
        #Comparing the variables if they are of type int or float
        if((type(x) is int or type(x) is float) 
        and (type(y) is int or type(y) is float)):
            rtn = x - y    
        #Comparing the variables if they are of type string
        elif(type(x) is str and type(y) is str):
            x = list(x)
            y = list(y)
            rtn = ord(x[0]) - ord(y[0])
            i = 1
            while(i < len(x) and i < len(y) and rtn == 0):                
                rtn = ord(x[i]) - ord(y[i])
                i += 1
        return rtn
