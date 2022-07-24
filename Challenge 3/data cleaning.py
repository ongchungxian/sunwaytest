import re 

def checkmailsyntax(email):
    output = re.sub(r"[^a-zA-Z0-9@\.]+", "", email)

    
    print(output)
    


s = checkmailsyntax(".Emil[y_Kli#%ne36@mail.com")
