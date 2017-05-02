from utils import DBConnector

def print_oc_wind_vectors():
    with DBConnector(host = "localhost", 
                     user = "admin", 
                     passwd = "password",
                     db="wind") as wind_db:
        for vector in wind_db.vectors("OC_WIND_COMPONENTS"):
            print('u_comp:', vector.u)
            print('v_comp', vector.v)
            print('magnitude:', abs(vector))
            print('angle:', vector.angle)

