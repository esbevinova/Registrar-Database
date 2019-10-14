import datetime
from prettytable import PrettyTable
import os

def dates():
    """A function that calculates various given dates."""

    date1 = "27 FEB 2000"
    date2 = "27 FEB 2017"
    date3 = "1 JAN 2017"
    date4 = "31 OCT 2017"
    dt1 = datetime.datetime.strptime(date1, '%d %b %Y')
    dt2 = datetime.datetime.strptime(date2, '%d %b %Y')
    dt3 = datetime.datetime.strptime(date3, '%d %b %Y')
    dt4 = datetime.datetime.strptime(date4, '%d %b %Y')
    dt1_str = dt1.strftime('%m/%d/%Y')
    dt2_str = dt2.strftime('%m/%d/%Y')
    dt3_str = dt3.strftime('%m/%d/%Y')
    dt4_str = dt4.strftime('%m/%d/%Y')
   
    num_days = 3
    dt5 = dt1 + datetime.timedelta(days=num_days)
    print('{} days after {} is {}.'.format(num_days, dt1_str, dt5.strftime('%m/%d/%Y')))

    num_days = 3
    dt6 = dt2 + datetime.timedelta(days=num_days)
    print('{} days after {} is {}.'.format(num_days, dt2_str, dt6.strftime('%m/%d/%Y')))

    delta = dt4 - dt3
    print('{} days passed between {} and {}.'.format(delta.days, dt3_str, dt4_str))


def read_file(file_name, fields, sep=',', header=False):
    """A function that reads through the file splitting it at a given separator and returns all the values."""
    try:
        fp = open(file_name, 'r')
    except FileNotFoundError:
        print("Can't open ", file_name)
    else:
        with fp:
            for num, line in enumerate(fp, 1):
                line = line.strip('\n')
                values = line.split(sep)
                if len(values) == fields:
                    if header==True and num==1:
                        continue
                    yield values
                else:
                    raise ValueError(file_name + " has " + str(fields) + "fields on line " + str(num) + " but expected " + str(fields))
            
def summarize(path):
    """A function that returns a list of python files along with the summary of its contents: classes, functions, lines, characters in a table."""

    pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print("Can't find the directory", path)
    else:
        for file in files:
            if file.endswith('.py'):
                filename, classes, functions, lines, characters = scan(os.path.join(path, file))
                pt.add_row([filename, classes, functions, lines, characters])
        print (pt)
    
def scan(path):
    """A function that scans through the python file returning a summary of filename, classes, functions, lines, characters."""
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print("Can't find the file", fp)
    else:
        with fp:
            classes = 0
            functions = 0
            lines = 0
            characters = 0
            for line in fp:
                if line.lstrip().startswith('class '):
                    classes += 1
                elif line.lstrip().startswith('def '):
                    functions += 1

                lines += 1
                characters += len(line)
            return path, classes, functions, lines, characters
           
def main():
    dates()
    print(list(read_file(r'C:\Users\Kat\Documents\VSC-Python\.vscode\810\.vscode\students.txt', 4, ',', True)))
    summarize(r'C:\Users\Kat\Documents\VSC-Python\.vscode\810\files for hw8')
    
 
if __name__ == '__main__':
    main()