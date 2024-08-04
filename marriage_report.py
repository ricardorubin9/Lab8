"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path, script_dir
import pandas as pd

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)
    all_couples()

def get_married_couples():
    """Queries the Social Network database for all married couples.
    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Get a List of Relationships"
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    all_relationships_query = """
        SELECT person1.name, person2.name, start_date, type FROM relationships
        JOIN people person1 ON person1_id = person1.id
        JOIN people person2 ON person2_id = person2.id
        WHERE type = 'spouse'
"""
    cur.execute(all_relationships_query)
    data = cur.fetchall()
    print (data)
    con.commit()
    con.close()

    return(data)

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  
    
    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    # Hint: We did this in Lab 7.
    df = pd.DataFrame(married_couples)
    df.rename(columns=
              {0:'Person1',1:'Person2', 2:'Anniversary'}, inplace=True)
    df.head()
    df.to_csv(csv_path, index= False)
    print (df)

    return

def all_couples():
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()


    all_relationships_query = """
        SELECT person1.name, person2.name, start_date, type FROM relationships
        JOIN people person1 ON person1_id = person1.id
        JOIN people person2 ON person2_id = person2.id;
    """
     cur.execute(all_relationships_query)
     all_relationships = cur.fetchall()
     
     for person1, person2, start_date, type in all_relationships:
         print(f'{person1} has been a {type} of {person2} since {start_date}') 
     con.close()
     return()
       
       if __name__ == '__main__':
   main()
