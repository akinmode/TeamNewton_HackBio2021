def task1():
    print("Name:Eunice Njuguna")
    print("Email address:eunice2915@gmail.com")
    print("Twitterhandle:@Eunice1420165")
    print("slack username:@Njuguna.E")
    print("my Biostacks:genomics")
task1()

slack_username ="@Njuguna.E"
twitter = "@Eunice1420165"
def HammDist(slack_username,twitter):
    a=slack_username
    b=twitter
    if len(a)>len(b):
        print('Hamming Distance is:', len(a)-len(b))
    elif len(b)>len(a):
        print('Hamming Distance is:', len(b)-len(a))
    else:
        print('Hamming Distance is:',0)
        
HammDist(slack_username,twitter)
