"""
Author: Edison Kaulfuss, Corey Bock, Brian Mellino

This file is for the list object that will handle each login instance
"""

class LoginInfo:
    # Attributes
    login_site = ""
    username = ""
    password = ""

    # TODO: add comments as 4th variable if deemed valuable
    # comments = ""

    def __init__(self, _login_site="!", _username="!", _password="!"):
        """
        This is the constructor method
        """
        self.login_site = self.encrypt(_login_site)
        self.username = self.encrypt(_username)
        self.password = self.encrypt(_password)

    def getLoginSite(self):
        """
        Retrieves the decrypted login site.

        :returns: Decrypted login site string.
        """
        # TODO: Add decryption, return decrypted info
        return self.decrypt(self.login_site)

    def getUsername(self):
        """
        Retrieves the decrypted username.

        :returns: Decrypted username string.
        """
        # TODO: Add decryption, return decrypted info
        return self.decrypt(self.username)

    def getPassword(self):
        """
        Retrieves the decrypted password.

        :returns: Decrypted password string.
        """
        # TODO: Add decryption, return decrypted info
        return self.decrypt(self.password)

    def dumpForSave(self):
        """
        Prepares data for saving without decryption.

        :returns: Concatenated string of login_site, username, and password.
        """
        # Do not decrypt
        return str(self.login_site) + "|" + str(self.username) + "|" + str(self.password)

    def setLoginSite(self, _login_site, encrypt=True):
        """
        Sets the login site.

        :param _login_site: New login site string.
        :param encrypt: Boolean to determine if encryption is applied.
        """
        # TODO: Add encryption
        if encrypt:
            self.login_site = self.encrypt(_login_site)
        else:
            self.login_site = _login_site

    def setUsername(self, _username, encrypt=True):
        """
        Sets the username.

        :param _username: New username string.
        :param encrypt: Boolean to determine if encryption is applied.
        """
        # TODO: Add encryption
        if encrypt:
            self.username = self.encrypt(_username)
        else:
            self.username = _username

    def setPassword(self, _password, encrypt=True):
        """
        Sets the password.

        :param _password: New password string.
        :param encrypt: Boolean to determine if encryption is applied.
        """
        # TODO: Add encryption
        if encrypt:
            self.password = self.encrypt(_password)
        else:
            self.password = _password

    def encrypt(self, incoming):
        """
        Encrypts a string.

        :param incoming: String to be encrypted.
        :returns: Encrypted string.
        """
        # TODO add encryption function
        holderStr = ""
        for cha in incoming:
            charHolder = str(ord(cha))
            if len(charHolder) < 3:
                charHolder = "0" + charHolder
            holderStr += charHolder
        convertedChar = int(holderStr)
        doMathHere = pow(10, len(holderStr)) + convertedChar
        encrypted = doMathHere * 42  # or w/e
        return encrypted

    def decrypt(self, incoming):
        """
        Decrypts an encrypted string.

        :param incoming: Encrypted string to be decrypted.
        :returns: Decrypted string.
        """
        # TODO add decryption function
        incoming = int(incoming) // 42  # or w/e algorithm
        returner = ""
        preReturner = str(incoming)
        preReturner = preReturner.removeprefix("1")
        while len(preReturner) > 0:
            returner += chr(int(preReturner[:3]))
            preReturner = preReturner[3:]
        return returner
