from playwright.sync_api import Page
class enteraddress:
    def __init__(self,page):
        self.fristname=page.locator("#first-name")
        self.lastname=page.get_by_placeholder("Last Name")
        self.postalcode=page.locator('[name="postalCode"]')
        
    def enter_firstname(self,fname):
        self.fristname.fill(fname)
    def enter_lastname(self,lname):
        self.lastname.fill(lname)
    def enter_postalcode(self,pcode):
        self.postalcode.fill(pcode)
        