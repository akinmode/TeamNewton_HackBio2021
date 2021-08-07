
name = "NAME:Modupe Ariyo"
email = "EMAIL:ariyocedar@gmail.com"
slackUsername = "SLACK:@Modupe"
biostack = "BIOSTACK:Genomics"
twitter_handle = "TWITTER:@modeee"
def hammingDistance(str1,str2):
     count = 0  #this is the incremented variable for loop
     ham = 0 #incremented variable for hammD
     while (count < len(str1)):
          if str1[count] == str2[count]:
             ham+=1
          return ham
     count+=1
    
hamming_distance = "HAMMING:"+str(hammingDistance(slackUsername, twitter_handle))



print(name,email,slackUsername,biostack,twitter_handle,hamming_distance, sep="\n")
