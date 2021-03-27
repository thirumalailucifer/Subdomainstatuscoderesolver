import requests

#Http_StatusCheck_Function
def checkstatus(requesturl):
    status="Error"
    try:
     r=requests.get(requesturl)
     status=r.status_code
    except:
        a=0
    return status


if __name__ == "__main__":
    #1.httpretext
    httpspretext="http://"
    httpspretextwww="http://www."

    #2.FileInitialization Operations
    file=open('Sublist3r.txt')  #Input file with list of subdomains
    file2=open('Sublist3r.txt') #Input file with list of subdomains
    file3=open("Statusofsubdomains.txt","a") #Output file with list of subdomains and corresponding http code

    #3.count_variable_initialization
    count=0
    count1=0

    #4.countvariable
    for each in file:
        count=count+1

    #5.statuscodelistinitialization
    twohundreadlist=[]
    fourhundereadlist=[]
    otherslist=[]

    #6.Printing the executed Output in Terminal/Console
    for eachurl in file2:
           #print("inside second loop")
           #print(count1,"Existing url",eachurl)
           wwwcheck=eachurl.find('www.')
           if(wwwcheck!=-1):
             requesturl=httpspretext+eachurl
             #print("Modified url",requesturl)
           else:
               requesturl=httpspretext+eachurl
               #print("Modified url",requesturl)
           requesturl1=(requesturl.translate({ord('\n'): None}))
           count1=count1+1
           print("*****************")
           #function_variable=checkstatus(requesturl1)
           print(count1,requesturl1,"-->",checkstatus(requesturl1))
           temp=str((count1,requesturl1,"-->",checkstatus(requesturl1)))
           file3.write("\n")
           file3.write(temp)
    file3.close()
