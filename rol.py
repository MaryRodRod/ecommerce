import psycopg2


class Rol:
    cant_rols = 0
    
    def __init__(self, cant_roles): # __init__ : así se identifica que es un constructor
        self.cant_roles = cant_roles
        
    def __init__(self): 
        pass   
    
    def list_roles(self):
        
        roles = [] # esta es una variable dentro del metodo list_roles
        
        conn = psycopg2.connect(
            host="ec2-44-198-223-154.compute-1.amazonaws.com",
            database="d6k8pf744iivoh",
            user="glbybbbgetizbw",
            password="4a6d84cd18afa55a53ede162d298b2c6139a0987c0d432558dd91f1d5d5caec6"
        )

        cur = conn.cursor()

        cur.execute('SELECT * FROM rol')

        roles = cur.fetchall()
        self.cant_roles = len(roles)

        cur.close()

        return roles
        