#My first Assignment

##Print Name,Email,Slack,Biostack and Twitter
print("NAME:Nelson Mokaya Nyakundi")
print("EMAIL:mokayanelson@yahoo.com")
print("SLACK USERNAME:@NNyakundi")
print("BIOSTACK:Genomics")
print("TWITTER HANDLE:@Nel_Nielsen")

## hamming distance between twitter handle and slack username

Twitter_handle= "@Nel_nielsen"
Stack_username= "@NNyakundi"
def h_d_loop(str_1, str_2):
    h_distance = 0
    if len(str_1) != len(str_2):
     print("Whoops! Strings must be the same length.")
     return
    for position in range(len(str_1)):
        if str_1[position] != str_2[position]:
            h_distance += 1
    return h_distance
print("HAMING DISTANCE:",end = "")
print(h_d_loop(Twitter_handle,Stack_username))

##importing to csv
import csv
fields = ['NAME', 'EMAIL', 'SLACK USERNAME', 'BIOSTACK', 'TWITTER HANDLE', 'HAMING DISTANCE'] 

rows = [ ['Nelson Mokaya Nyakundi', 'mokayanelson@yahoo.com', '@NNyakundi', 'Genomics', '@Nel_Nielsen', 'None']] 
filename = "@NNyakundi_Ass1.csv"
csv_file = open('filename', 'w') 
writer = csv.writer(csv_file) 
writer.writerow(fields) 
writer.writerows(rows)
csv_file.close()
