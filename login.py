from loanCoin import BlockChain
from loanCoin import Block

class Login:
    def __init__(self, creds):
        self.creds = creds
        self.error = "Enter a valid username and password"
        self.logged_in = False
        self.user_name = None
        self.password = None

    def LogIn(self):
        self.user_name = str(input("Username: "))
        self.password = str(input("Password: "))
        if self.check(self.user_name, self.password):
            print("{} logged in".format(self.user_name))
            self.logged_in = True
        else:
            print("Failed Login")
            self.logged_in = False

    def check(self, username, pwd):
        if username in self.creds and pwd == self.creds[username]:
            print("Login Successful")
            return True
        else:
            print(self.error)
            return False

    def getUsername(self):
        return self.user_name

    def getLoggedIn(self):
        return self.logged_in

    def LogOut(self):
        self.logged_in = False
        self.user_name = None
        self.password = None

    def new_data(self, recipient, description, blockchain, list_of_desc):
        list_of_what_you_own = []
        for key, value in blockchain.whoOwnsWhat(list_of_desc).items():
            if (value == self.getUsername()):
                list_of_what_you_own.append(key)
        if description not in list_of_what_you_own:
            return False

        blockchain.new_data(
            sender=self.getUsername(),
            recipient=recipient,
            description=description
        )

        return True
