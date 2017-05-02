import MySQLdb
import logging
import math


def print_oc_wind_vectors():
    try:
        conn = MySQLdb.connect(host="localhost",    
                            user="admin",         
                            passwd="password",  
                            db="wind") 
    except MySQLdb.Error:
        logging.error('Unable to connect to mysql database')
        return None

    try:
        cur = conn.cursor()
    except MySQLdb.Error:
        logging.error('Unable to get database cursor')
        conn.close()
        return None

    try:
        cur.execute("SELECT * FROM OC_WIND_COMPONENTS")
        num_rows = cur.rowcount
        for i in range(num_rows):
            row = cur.fetchone()
            u_comp = row[0]
            v_comp = row[1]
            print('u_comp:', u_comp)
            print('v_comp', v_comp)
            print('magnitude:', math.sqrt(u_comp * u_comp, v_comp * v_comp))
            print('angle:', math.atan2(v_comp, u_comp))
    except MySQLdb.Error:
        logging.error('Unable to get wind component rows')
    finally:
        cur.close()
        conn.close()
