print("NAME:Sneha Santhosh")
print("EMAIL:snehainduss@gmail.com")
print("SLACK:@sneha")
print("BIOSTACK:Genomics")
print("TWITTER:@sneht")
def hamDist(slack, twitter):
    i = 0
    count = 0
 
    while(i < len(slack)):
        if(slack[i] != twitter[i]):
            count += 1
        i += 1
    return count
 
# function call
print("HAMMING DISTANCE", hamDist("@sneha", "@sneht"))
