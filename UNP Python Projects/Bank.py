def import_and_create_bank(filename):
    #create an empty dictionary 
    bank = {}
    #open the file in read mode
    f = open(filename, 'r')
    #get all lines as a list
    lines = f.readlines()
    #iterate over each line in lines
    for line in lines:
    
        #strip whitespace from beginning and end of line
        #split the line into a list based on ':' separator
        lst = line.strip().split(":")
        #skip line if it does not have a name or deposit amount
        if len(lst) <= 1:
            continue
        
        #get key(name) or the value (deposit amount) from line 
        #strip whitespace from beginning of key(name) and value(deposit amount)
        key = lst[0].strip()
        value = lst[1].strip()

        try:
            #try to cast value(deposit amount) to numeric value
            value = float(value)
            #add new deposit amount to current total balance 
            #associated with key (name), or 0
            bank[key] = bank.get(key, 0) + value
        
        except:
           #otherwise, skip this line
            continue
    f.close()

def signup(user_accounts, log_in, username, password):
    