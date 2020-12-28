windows_path = 'C:\\Users\\rob\\Documents\\Python Scripts\\CIS325Py\\loan-data-v1.csv'
path = windows_path

openfile = open(path, 'r',  encoding='utf-8', errors='ignore')
next(openfile)
customer_list = []

for line in openfile:
    ls = line.split(',')
    int(ls[7])
    ls[10].strip()
    customer_list.append(ls)
openfile.close()

from operator import itemgetter
customer_list.sort(key=itemgetter(7), reverse=True)
print(customer_list)

write_path='C:\\Users\\rob\\Documents\\Python Scripts\\CIS325Py\\loan-data-v1.csv'

writefile=open(write_path, 'w', encoding='utf-8', errors='ignore')
writefile.write('Name,State,Age,Annual Income,Loan Type,Loan Amount,Length of Loan in Years,Days Delinquent,Interest Rate,Number of Loans Prior,Years as Customer\n')
for x in customer_list:
    if int(x[7]) >= 90:
        name=x[0].strip()
        state=x[1].strip()
        age=x[2].strip()
        income=x[3].strip()
        loantype=x[4].strip()
        loanamt=x[5].strip()
        length=x[6].strip()
        daysdel=x[7].strip()
        interestrate=x[8].strip()
        numofloans=x[9].strip()
        years=x[10].strip()
        writefile.write(name + ',' + state + ',' + age + ',' + income + ',' +
                        loantype + ',' + loanamt + ',' + length + ',' + daysdel + ',' + 
                        interestrate + ',' + numofloans + ',' + years + '\n')
        
writefile.close()