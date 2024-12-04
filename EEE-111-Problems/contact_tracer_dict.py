if __name__ == "__main__":
    pat_con = {}
    while len(pat_con) != 3:
        patient = int(input())
        contact1 = int(input())
        contact2 = int(input())
        pat_con.update({patient: [contact1, contact2]})
    lookup = int(input())
    lookup_con = pat_con.get(lookup, "No Data")
    print("contacts of {}".format(lookup))    
    print(lookup_con)
    if lookup_con != "No Data":
        for con in lookup_con:
            print('contacts of {}'.format(con))
            print(pat_con.get(con, "No Data"))
                
                

