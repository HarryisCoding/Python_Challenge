import csv
from datetime import datetime
from itertools import zip_longest

employee = []
total_emp_id1 = []
total_full_name = []
total_dob = []
total_ssn = []
total_state = []

total_emp_id2 = []
total_full_name2 = []
total_dob2 = []
total_ssn2 = []
total_state2 = []

total_emp_id = []
total_first_name = []
total_last_name = []
new_total_dob = []
new_total_ssn = []
new_total_state = []

with open ("data/employee_data1.csv", newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader, 0)
    for x in reader:
        emp_id = x[0]
        name = x[1]
        dob = x[2]
        ssn = x[3]
        state = x[4]
        total_emp_id1.append(emp_id)
        total_full_name.append(name)
        total_dob.append(dob)
        total_ssn.append(ssn)
        total_state.append(state)
    #print(total_emp_id)
    #print(total_full_name)
    #print(total_dob)
    #print(total_ssn)
    #print(total_state)
    for x in range(len(total_full_name)):
        firstname = total_full_name[x].split()[0]
        lastname = total_full_name[x].split()[1]
        total_first_name.append(firstname)
        total_last_name.append(lastname)
    #print(total_first_name)
    #print(total_last_name)
    #print(total_full_name[0])
    #for x in reader:
    #    employee.append(x)
    ## what is reader??? list???
    #employee = list(reader)
    #print(employee)
    #print(reader)

    for x in range(len(total_dob)):
        dates = datetime.strptime(total_dob[x], '%Y-%m-%d').strftime('%m/%d/%Y')
        new_total_dob.append(dates)
    #print(new_total_dob)
    #print(total_ssn[1])
    for x in range(len(total_ssn)):
        t = list(total_ssn[x])
        t[0] = '*'
        t[1] = '*'
        t[2] = '*'
        t[4] = '*'
        t[5] = '*'
        new_t = ''.join(t)
        new_total_ssn.append(new_t)
    #print(t)
    #print(total_ssn[0])
    #print(new_total_ssn)
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    for x in total_state:
        state_abb = us_state_abbrev[x]
        new_total_state.append(state_abb)
    #print(new_total_state)
    #print(total_state)

with open ("data/employee_data2.csv", newline = '') as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter = ",")
    next(reader2, 0)
    for x in reader2:
        emp_id2 = x[0]
        name2 = x[1]
        dob2 = x[2]
        ssn2 = x[3]
        state2 = x[4]
        total_emp_id2.append(emp_id2)
        total_full_name2.append(name2)
        total_dob2.append(dob2)
        total_ssn2.append(ssn2)
        total_state2.append(state2)

    for x in range(len(total_full_name2)):
        firstname2 = total_full_name2[x].split()[0]
        lastname2 = total_full_name2[x].split()[1]
        total_first_name.append(firstname2)
        total_last_name.append(lastname2)

    for x in range(len(total_dob2)):
        dates2 = datetime.strptime(total_dob2[x], '%Y-%m-%d').strftime('%m/%d/%Y')
        new_total_dob.append(dates2)

    for x in range(len(total_ssn2)):
        t2 = list(total_ssn2[x])
        t2[0] = '*'
        t2[1] = '*'
        t2[2] = '*'
        t2[4] = '*'
        t2[5] = '*'
        new_t2 = ''.join(t)
        new_total_ssn.append(new_t2)

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    for x in total_state2:
        state_abb2 = us_state_abbrev[x]
        new_total_state.append(state_abb2)
    #print(new_total_state)
    #print(total_state)

total_emp_id = total_emp_id1 + total_emp_id2
d = [total_emp_id, total_first_name, total_last_name, new_total_dob, new_total_ssn, new_total_state]
export_data = zip_longest(*d, fillvalue = '')
with open('data/Result_new_employee_data.csv', 'w', newline='') as csvfile3:
    header = ['Emp ID', 'First Name','Last Name', 'DOB', 'SSN', 'State']
    filewriter = csv.writer(csvfile3, delimiter=',')
    filewriter.writerow(header)
    filewriter.writerows(export_data)

with open ("data/Result_new_employee_data.csv", newline = '') as csvfile4:
    for line in csvfile4:
        print(line)

