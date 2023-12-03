#taking a email as input
email=input("enter your Emailid:")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]==".") or (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong Email ---space should not present:")
                else:
                    print("correct Emailid:")
            else:
                print("wrong Email--please check the . is present in Your mail or not")
        else:
            print("wrong Email---@should be present and it should not repeat more than 1")
    
    else:
        print("wrong Email--firts letter should be charecter not number:")
else:
    print("wrong Emailid--please enter mail length more than 6 charecters:")


