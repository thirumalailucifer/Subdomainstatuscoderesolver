import requests

#Status check function returns the http response code
def checkstatus(requesturl):
    status="Error"  #default value of status is set as Error
    try:
        r=requests.get(requesturl)
        status=r.status_code
    except:
        a=0
    return status

if __name__ == "__main__":

    #1.http_prefix_text to append before the subdomain
    httppretext="http://"
    httpspretextwww="http://www."

    #2.FileInitialization Operations
    inputfile=open('Sublist3r.txt')
    file2=open('Sublist3r.txt')
    outputfile=open("Statusofsubdomains.txt","a")

    #3.count_variable_initialization
    subdomains_count=0
    count1=0

    #4.count the number of subdomains
    for each in inputfile:
        subdomains_count=subdomains_count+1
    inputfile.close()
    inputfile=open('Sublist3r.txt')

    #5.statuscode_list_initialization
    twohundreadstatuslist=[]
    threehundreadstatuslist=[]
    fourhundereadstatuslist=[]
    fivehundereadstatuslist=[]
    otherslist=[]

    #Allocating status to the respected http list
    def statuscodegrouping(chs,requesturl1):
        if(chs.startswith('2')):
            twohundreadstatuslist.append(requesturl1)
        elif(chs.startswith('3')):
            threehundreadstatusstatuslist.append(requesturl1)
        elif(chs.startswith('4')):
            fourhundereadstatuslist.append(requesturl1)
        elif(chs.startswith('5')):
            fivehundereadstatuslist.append(requesturl1)
        else:
            otherslist.append(requesturl1)

    #6.mainprogramstarts
    for eachdomain in inputfile:
        #print(eachdomain)
        wwwcheck=eachdomain.find('www.')
        if(wwwcheck!=-1):  #if the subdomain url does not contain the www.
            requestdomain=httppretext+eachdomain
        else:
            requestdomain=httppretext+eachdomain
        '''Translate is used to not consider the blank space after the subdomain
        in the given input file'''
        requesturl1=(requestdomain.translate({ord('\n'): None}))
        count1=count1+1
        print("*****************")
        chs=checkstatus(requesturl1)
        #200 status code domains
        chs=str(chs)
        statuscodegrouping(chs,requesturl1)
        print(count1,requesturl1,"-->",chs)
        temp=str((count1,requesturl1,"-->",chs))
        outputfile.write("\n")
        outputfile.write(temp)
    outputfile.close()
    statuscodegroupingfile=open('statuscodegroupingfilee.txt','w')
    entirelist=[]
    entirelist.extend((twohundreadstatuslist,threehundreadstatuslist,fourhundereadstatuslist,fivehundereadstatuslist,otherslist))
    print("twohundreadstatus-->",twohundreadstatuslist,"\n",
          "threehundreadstatusstatus-->",threehundreadstatuslist,"\n",
          "fourhundred-->",fourhundereadstatuslist,"\n",
          "fivehundereadstatus-->",fivehundereadstatuslist,"\n",
          "otherslist-->",otherslist)
    if(len(twohundreadstatuslist)!=0):
        statuscodegroupingfile.write("Status code 200 \n")
        for each in twohundreadstatuslist:
            statuscodegroupingfile.write(each)
            statuscodegroupingfile.write("\n")
    if(len(threehundreadstatuslist)!=0):
        statuscodegroupingfile.write("\n\n Status code 300")
        for each in threehundreadstatuslist:
            statuscodegroupingfile.write(each)
            statuscodegroupingfile.write("\n")
    if(len(fourhundereadstatuslist)!=0):
        statuscodegroupingfile.write("\n\n Status code 400")
        for each in fourhundereadstatuslist:
            statuscodegroupingfile.write(each)
            statuscodegroupingfile.write("\n")
    if(len(fivehundereadstatuslist)!=0):
        statuscodegroupingfile.write("\n\n Status code 500")
        for each in fivehundereadstatuslist:
            statuscodegroupingfile.write(each)
            statuscodegroupingfile.write("\n")
    if(len(otherslist)!=0):
        statuscodegroupingfile.write("\n\n Errors and others")
        for each in otherslist:
            statuscodegroupingfile.write(each)
            statuscodegroupingfile.write("\n")
    statuscodegroupingfile.close()
