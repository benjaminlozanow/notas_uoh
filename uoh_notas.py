import pandas as pd 
import sys

MASTER_FILE = "master_notas.xlsx"
TEMPLATE_FILE = "notas.xlsx"
SECOND_ARG = sys.argv[1]
COLUMN_NUMBER = 3

def grade_calculator(score, max_score, percentage):
    min_grade = 1.0
    max_grade = 7.0
    approval_grade = 4.0
    e = percentage/100
    if score < e * max_score:
        grade = (approval_grade - min_grade) * (score / (e * max_score)) + min_grade
    elif score >= e * max_score:
        grade = (max_grade - approval_grade) * ((score - e * max_score) / (max_score * (1 - e))) + approval_grade
    else:
        raise Exception("Something went wrong, try again")
    return (round(grade,2))

class Notas:
    def __init__(self):
        self.score_file = SECOND_ARG
        self.master_file = MASTER_FILE
        self.template_file = TEMPLATE_FILE
        self.max_score = 0
        self.percentage = 0

    def load_df(self):
        self.score_df = pd.read_excel(self.score_file)
        self.master_df = pd.read_excel(self.master_file)
        self.column_name = self.score_df.columns[COLUMN_NUMBER]
        self.template_df = pd.read_excel(self.template_file)

    def user_input(self):
        # Grade calculation parameters
        column_use = input("Do you want to calculate grades for " + self.column_name + "? (y/n)")
        if column_use.lower() == 'y' or column_use.lower() == 'yes':
            self.max_score = int(input("What is the maximum score for this test?"))
            self.percentage = int(input("What is the minimum score percentage (just the number) for approval? (60% or 50% are commonly used)"))
        else:
            print("Let's skip the column then")
    
    def calculate_grades(self):
        self.score_df.fillna(0, inplace=True)
        if not (self.max_score == 0) and not (self.percentage == 0):
            self.score_df['nota_' + self.column_name] = self.score_df[self.column_name].apply(grade_calculator, args = (self.max_score, self.percentage))

    def grade_export(self):
        self.score_df.to_excel(self.column_name + ".xlsx", index = False)
        print("Done")
    
    def template_export(self):
        self.template_df["Nota"] = self.score_df['nota_' + self.column_name]
        self.template_df.to_excel(f'uoh_{self.column_name}.xlsx', index = False)

    def merge_master(self):
        if 'nota_' + self.column_name in self.master_df.columns or self.column_name in self.master_df.columns:
            self.master_df.drop(columns = ['nota_' + self.column_name, self.column_name], inplace=True)
        self.merged_df = pd.merge(self.master_df, self.score_df, how = "left", on = ["Nº", "Persona", "RUT"])
        self.merged_df.to_excel(MASTER_FILE, index = False)


evaluacion = Notas()
evaluacion.load_df()
evaluacion.user_input()
evaluacion.calculate_grades()
evaluacion.grade_export()
evaluacion.template_export()     
evaluacion.merge_master() 

    