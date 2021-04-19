import csv
import mysql.connector
from faker import Faker
import sys
# import mysql.connector.cursor_cext
# create/design normalized database schema; database should consist
# of at least 5 tables in 3NF

db = mysql.connector.connect(
    host="35.236.32.138",
    user="michelle",
    password="chapmanrules",
    database="StudentsMK"
    )

curr = db.cursor()
fake = Faker()

# develop a utility/tool that generates data and exports it to a csv file
# This data that will be used to populate the tables in your normalized database.
# Your data generation tool should take as a command line parameter the file name to
# be created and the number tuples(records)to be generated

#file_name = input("Hello! What is the name of the file you would like to store this generated data in? ")
#number_of_records = int(input("How many records would you like to generate? "))
file_name = sys.argv[1]
number_of_records = sys.argv[2]

def genData(file_name, number_of_records):
#   fake = Faker()
    csv_file = open(file_name, "w")
    writer = csv.writer(csv_file)
    writer.writerow(["FirstName", "LastName", "Major", "County","GPA", "Professor"])
    for x in range(int(number_of_records)):
        writer.writerow([fake.first_name(), fake.last_name(), getMajor(), getCounty(), getGPA(), getProf()])
"""
def getHonorRoll():
    HRs = [0, 1]
    HR = fake.word(ext_word_list=HRs)
    return HR

def getClassSection():
    sections = [1, 2, 3, 4, 5]
    section = fake.word(ext_word_list=sections)
    return section
"""
def getProf():
    profs = ["Rene German", "Erik Linstead", "Michael Fahy", "Tom Springer", "Elizabeth Stevens"]
    prof = fake.word(ext_word_list=profs)
    return prof

def getMajor():
    majors = ["Political Science", "Creative Writing", "Computer Science", "Math", "Business", "Finance", "Acting", "Art", "Photography", "Physics", "Biology", "Chemistry"]
    major = fake.word(ext_word_list=majors)
    return major

def getCounty():
    counties = ["Los Angeles", "Orange", "Ventura", "San Bernardino", "Riverside", "Imperial", "San Diego", "Santa Barbara"]
    county = fake.word(ext_word_list=counties)
    return county

def getGPA():
    gpas = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 2.5, 3.5, 3.8]
    gpa = fake.word(ext_word_list=gpas)
    return gpa
"""
def getZipCode():
    zips = ['90001', '90003', '90620', '90623', '91319', '91320', '91701', '91708', '92232', '92241', '92243', '92251', '92198', '92195', '93120', '93199']
    zip = fake.word(ext_word_list=zips)
    return zip
"""
def importData():
    curr = db.cursor()

    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            print("Importing Member Data")
            #stuId = curr.lastrowid
            #curr.execute("INSERT INTO ClubMember(FirstName, LastName, ClassSection, Major, ZipCode, GPA) "
            #             "VALUES (%s, %s, %s, %s, %s, %s);", (row['FirstName'], row['LastName'], row['ClassSection'], row['Major'], row['ZipCode'], row['GPA']))
            #
            db.commit()
            #stuId = curr.lastrowid

            curr.execute("INSERT INTO WMSTSections(Professor)"
                         "VALUES (%s);", (row['Professor'],))
            ClassSection = curr.lastrowid
            db.commit()

            curr.execute("INSERT INTO StudentInfo(Major)"
                         "VALUES (%s);", (row['Major'],))
            MajorId = curr.lastrowid
            db.commit()

            curr.execute("INSERT INTO PersonalInfo(County)"
                         "VALUES (%s);", (row['County'],))
            CountyId = curr.lastrowid
            db.commit()


            if (float(row["GPA"]) > 3.4):
                curr.execute("INSERT INTO HonorRollInfo(GPA, HonorRoll)"
                             "VALUES (%s, %s);", (row['GPA'], 1),)
                HonorRollId = curr.lastrowid
                db.commit()
            else:
                curr.execute("INSERT INTO HonorRollInfo(GPA, HonorRoll)"
                             "VALUES (%s, %s);", (row['GPA'], 0),)
                HonorRollId = curr.lastrowid
                db.commit()

            curr.execute("INSERT INTO ClubMember(FirstName, LastName, ClassSection, MajorId, CountyId, HonorRollId) "
                            "VALUES (%s, %s, %s, %s, %s, %s);", (row['FirstName'], row['LastName'], ClassSection, MajorId, CountyId, HonorRollId))
            db.commit()
print("Import Successful")

genData(file_name, number_of_records)
importData()