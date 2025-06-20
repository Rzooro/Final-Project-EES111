import pandas as pd
import regex as re

class DataManager:
    def __init__(self, txt, inp):
        self.st_name = ""
        self.cr = ""
        self.cr_code = 0
        self.course = False
        self.df = pd.read_csv("data.csv")
        self.txt = txt
        self.inp = inp
        self.results = []
        
    def decode(self):
        
        if self.inp:
            lines = [line.strip() for line in self.txt.splitlines() if line.strip()]
            if len(lines) > 1:
                if lines[0][0].isdigit():
                    try:
                        for i in lines:
                            part = i.split(",")
                            self.cr_code = part[0]
                            self.cr = part[1].replace(" ", "_")
                            self.results.append((self.cr_code, self.cr))
                        course = True
                        return self.results, course
                    except IndexError:
                        raise ValueError("Invalid input format")
                elif lines[0][0].isalpha():
                    try:
                        for i in lines:
                            part = i.partition(",")
                            self.st_name = part[0]
                            self.cr_code = part[2].strip().split(",")
                            self.results.append((self.st_name, self.cr_code))
                        course = False
                        return self.results, course
                    except IndexError:
                        raise ValueError("Invalid input format")                
            else:           
                if lines[0][0].isdigit():
                    try:
                        part = lines[0].split(",")
                        self.cr_code = part[0]
                        self.cr = part[1].replace(" ", "_")
                        course = True
                        return self.cr, self.cr_code, course
                    except IndexError:
                        raise ValueError("Invalid input format")
                elif lines[0][0].isalpha():
                    try:
                        part = lines[0].partition(",")
                        self.st_name = part[0]
                        self.cr_code = part[2].strip().split(",")
                        course = False
                        return self.st_name, self.cr_code, course
                    except IndexError:
                        raise ValueError("Invalid input format")
        else:
            None
            
    def add_course(self):
        if self.course:
            print(self.decode(self.txt, self.inp))