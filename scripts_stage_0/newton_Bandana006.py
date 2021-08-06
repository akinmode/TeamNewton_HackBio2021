def hammingDist(Slack_handle, Twitter_handle):  
    i = 0
    count = 0
 
    while(i < len(Slack_handle)):
        if(Slack_handle[i] != Twitter_handle[i]):
            count += 1
        i += 1
    return count
Name = "Bandana Pahi"
Email = "pahibandana207@gmail.com"
Slack_handle = "@Bandana006"
Biostack = "Transcriptomics"
Twitter_handle = "@bandana998"
Hammdist = hammingDist(Slack_handle, Twitter_handle)
print("Name: {}\nEmail: {}\nSlack_handle: {}\nBiostack: {}\ntwitter handle: {}\nHamming_distance: {}".format(Name, Email, Slack_handle, Biostack, Twitter_handle, Hammdist))
import csv 
    
fields = ['Name', 'Email', 'Slack_handle', 'Biostack', 'Twitter_handle', 'Hamming_distance'] 
    
rows = [ ['Bandana Pahi', 'pahibandana207@gmail.com', '@Bandana006', 'Transcriptomics', '@bandana998', '4']] 
    
filename = "Bandana_Stage1.csv"
     
with open(filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile) 
         
    csvwriter.writerow(fields) 
         
    csvwriter.writerows(rows)
