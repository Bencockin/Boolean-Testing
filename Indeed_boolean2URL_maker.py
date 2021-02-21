'''
URL Creator for indeed.
'''

class Indeed:

    start_of_url = "https://de.indeed.com/jobs?q="
    
    #Empty string that will be the recruiter will put a boolean into.
    terms = ""
    
    def __init__(self):
        pass


    def url_maker(self):

    	#Asks the recruiter for their boolean search string
        self.terms = input("Please input your boolean: ")

        #Changes all quotation marks into URL standard
        for letter in self.terms:
            if letter == '"':
                self.terms = self.terms.replace(letter, "%22")
        
        #Changes all Brackets into URL standard        
        for letter in self.terms:
            if letter == '(' or letter == ")":
                self.terms = self.terms.replace(letter, "")
        
        #Changes all spaces into URL standard        
        try:
            self.terms = self.terms.replace(" ", "+")
        
        except:
            pass
    
    # Testing. Python will print out a clickable link. This can be changes to return the URL for later.    
    def start(self):
        
        url = self.start_of_url + self.terms
        
        print(url)