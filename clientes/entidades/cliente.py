class Cliente():
    def __init__(self, nome, sexo, date, email, profissao):
        print(nome)
        self.__nome = nome
        self.__sexo = sexo
        self.__date = date
        self.__email = email
        self.__profissao = profissao
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__datw = date
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao