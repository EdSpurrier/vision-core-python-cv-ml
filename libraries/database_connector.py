#!/usr/bin/env python
import MySQLdb
from os import system
import os
import sys

#   APPLICATION ROOT
sys.path.append(os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/')

#   IMPORT LIBRARIES
import libraries.console as console
from libraries.files_and_folders import folders


console.PrintImport("database_connector.py")


#############################################
#   SQL DATABASE CONNECTION
#############################################

db_setup_local = {
    "db"        :   "loggy",
    "username"  :   "root",
    "password"  :   "idsidsidsids",
    "server"    :   "localhost",
    "port"      :   "3306"
}

""" db_setup_local = {
    "db"        :   "loggy",
    "username"  :   "root",
    "password"  :   "ids2019ids2018ids2017ids2016",
    "server"    :   "203.192.77.12",
    "port"      :   "3306"
} """

db_setup_arvixe = {
    "db"        :   "edspurri_loggy",
    "username"  :   "edspurri_loggy_u",
    "password"  :   "idsidsidsids",
    "server"    :   "edspurrier.com",
    "port"      :   "3306"
}


db_setup = db_setup_local

db = None


def OpenConnection():
    global db
    db = MySQLdb.connect( db_setup["server"] , db_setup["username"] , db_setup["password"], db_setup["db"] )



#############################################
#   CREATE NEW GRAB
#############################################

def CreateNewGrab(grab_timestamp, grab_img_url):
    OpenConnection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    # Prepare SQL query to INSERT a record into the database.
    
    sql = """INSERT INTO `grabs`
            (`grab_unique_id`, `timestamp`, `grab_img_url`)
             VALUES ('""" + grab_timestamp + """', '""" + grab_timestamp + """', '""" + grab_img_url + """')"""

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        console.PrintSuccess("Inserted Grab [" + grab_timestamp + "] Into DB")
        # disconnect from server
        db.close()

        return True

    except (MySQLdb.Error, MySQLdb.Warning) as e:
        console.PrintError("Database Insert Error", e)
        print(e)
        # disconnect from server
        db.close()

        return False

    
    

#############################################
#############################################
#############################################






#############################################
#   CREATE NEW LOG
#############################################

def CreateNewLog(log_line_data):
    OpenConnection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    # Prepare SQL query to INSERT a record into the database.
    
    sql = """INSERT INTO `logs`
            (`log_id`, `log_img_url`, `barcode_img_url`, 
            `grab_unique_id`, `grab_position_x`, 
            `grab_position_y`, `grab_width`, 
            `grab_height`, `actual_diameter`, 
            `jas_diameter`, `jas_cbm`) 
            VALUES ('""" + log_line_data["log_id"] + """', '""" + log_line_data["log_img_url"] + """', '""" + log_line_data["barcode_img_url"] + """', 
            '""" + log_line_data["grab_unique_id"] + """', '""" + log_line_data["grab_position_x"] + """', 
            '""" + log_line_data["grab_position_y"] + """', '""" + log_line_data["grab_width"] + """',
            '""" + log_line_data["grab_height"] + """', '""" + log_line_data["actual_diameter"] + """',
            '""" + log_line_data["jas_diameter"] + """', '""" + log_line_data["jas_cbm"] + """'
            )"""

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        console.PrintSuccess("Inserted Log [" + log_line_data["log_id"] + "][" + log_line_data["grab_unique_id"] + "] Into DB")
        # disconnect from server
        db.close()

        return True

    except (MySQLdb.Error, MySQLdb.Warning) as e:
        console.PrintError("Database Insert Error", e)
        print(e)
        # disconnect from server
        db.close()
        
        return False

    
    

#############################################
#############################################
#############################################





#############################################
#   DUMP & CREATE DATABASE
#############################################

def DumpAndCreateDatabase():
    OpenConnection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    console.PrintAlert("Dumping Old Database")
    console.Print("Dropping Table = GRABS")
    cursor.execute("DROP TABLE IF EXISTS GRABS")

    console.Print("Dropping Table = LOGS")
    cursor.execute("DROP TABLE IF EXISTS LOGS")

    console.Print("Dropping Table = USERS")
    cursor.execute("DROP TABLE IF EXISTS USERS")

    console.Print("Dropping Table = ORDERS")
    cursor.execute("DROP TABLE IF EXISTS ORDERS")

    console.Print("Dropping Table = CONTAINERS")
    cursor.execute("DROP TABLE IF EXISTS CONTAINERS")

    sql = open( folders["assets"] + 'database_structure.sql', 'r' )
    sql = sql.read()
   
    console.PrintStatement(sql)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        console.PrintSuccess("Created New Loggy Core Database")


    except (MySQLdb.Error, MySQLdb.Warning) as e:
        console.PrintError("Unable To Create Database", e)

    # disconnect from server
    #db.close()
    

#############################################
#############################################
#############################################



#############################################
#   DUMP & CREATE ACCOUNTS DATABASE
#############################################

def DumpAndCreateAccountsDatabase():
    OpenConnection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    console.PrintAlert("Dumping Old Database")
    console.Print("Dropping Table = ACCOUNTS")
    cursor.execute("DROP TABLE IF EXISTS ACCOUNTS")

    sql = open( folders["assets"] + 'accounts_database_structure.sql', 'r' )
    sql = sql.read()
   
    console.PrintStatement(sql)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        console.PrintSuccess("Created New Loggy Core Accounts Database")


    except (MySQLdb.Error, MySQLdb.Warning) as e:
        console.PrintError("Unable To Create Accounts Database", e)

    # disconnect from server
    #db.close()
    

#############################################
#############################################
#############################################



#############################################
#   INSERT INTO DATABASE 
#############################################

def InsertIntoDB():
    OpenConnection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        print()

    # disconnect from server
    db.close()
    print("Inserted Into DB")

#############################################
#############################################
#############################################




#############################################
#   TEST DATABASE 
#############################################

def TestDatabase():
    OpenConnection()

    is_database_working = True
    output = 'database is ok'

    try:
        # to check database we will execute raw query
        db.query("""SELECT 1""")
        data = db.use_result()
        console.Print("Database Working", str(data))
    except Exception as e:
        output = str(e)
        is_database_working = False
        console.Print("Database Error ==", output)

    return is_database_working, output


    # disconnect from server
    db.close()


#############################################
#############################################
#############################################




#############################################
#   READ DATABASE 
#############################################

def ReadDB():
    OpenConnection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)

    try:
    # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # Now print fetched result
            print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                    (fname, lname, age, sex, income )
            )
    except:
        print ("Error: unable to fecth data")

    # disconnect from server
    db.close()
    print("Reading DB")

#############################################
#############################################
#############################################






#############################################
#   CREATE TABLE    
#############################################
def CreateTable():
    OpenConnection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Create table as per requirement
    sql = """CREATE TABLE EMPLOYEE (
            FIRST_NAME  CHAR(20) NOT NULL,
            LAST_NAME  CHAR(20),
            AGE INT,  
            SEX CHAR(1),
            INCOME FLOAT )"""

    cursor.execute(sql)

    # disconnect from server
    db.close()

    print("Created Table DB")

#############################################
#############################################
#############################################
