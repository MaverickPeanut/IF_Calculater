#Tax.py
#社保及个人所得税计算

import math

TAXTHRESHOLD = 3500 #个税起征点（单位: rmb)

ENDOWMENT_RATE_COMPANY = 20 #养老保险(公司部分，%）
ENDOWMENT_RATE_INDIVIDUAL = 8 #养老保险(个人部分，%)

MEDICAL_RATE_COMPANY = 10 #医疗保险(公司部分，%)
MEDICAL_RATE_INDIVIDUAL = 2 #医疗保险(个人部分，%)

UNEMPLOYMENT_RATE_COMPANY = 1.5 #失业保险(公司部分，%)
UNEMPLOYMENT_RATE_INDIVIDUAL = 0.2 #失业保险(个人部分，%)

EMPLOYMENT_INJURY_RATE_COMPANY= 0.5 #工伤保险(公司部分，%)
EMPLOYMENT_INJURY_RATE_INDIVIDUAL = 0 #工伤保险(个人部分，%)

MATERNITY_RATE_COMPANY = 0.8 #生育保险(公司部分，%)
MATERNITY_RATE_INDIVIDUAL = 0 #生育保险(个人部分，%)

HOUSING_RATE_COMPANY = 12 #住房公积金(公司部分，%)
HOUSING_RATE_INDIVIDUAL = 12 #住房公积金(个人部分，%)

wait_option = True






salary = float(input("请输入税前工资: ")) #输入税前工资

while wait_option:
    ensurancebase_is_salary = input("社保计算基数 = 税前工资? (Y/N)")
    if ensurancebase_is_salary == "Y":
        ensurancebase = salary
        wait_option = False
    elif ensurancebase_is_salary == "N":
        ensurancebase = float(input("请输入社保计算基数: ")) #输入社保计算基数
        wait_option = False
    else: 
        print("请输入 Y 或 N ") #如果不是Y/N则重新输入
        wait_option = True

endowment_company = ensurancebase * ENDOWMENT_RATE_COMPANY/100
endowment_individual = ensurancebase * ENDOWMENT_RATE_INDIVIDUAL/100

medical_company = ensurancebase * MEDICAL_RATE_COMPANY/100
medical_individual = ensurancebase * MEDICAL_RATE_INDIVIDUAL/100

unemployment_company = ensurancebase * UNEMPLOYMENT_RATE_COMPANY/100
unemployment_individual = ensurancebase * UNEMPLOYMENT_RATE_INDIVIDUAL/100

employ_injury_company = ensurancebase * EMPLOYMENT_INJURY_RATE_COMPANY/100
employ_injury_individual = ensurancebase * EMPLOYMENT_INJURY_RATE_INDIVIDUAL/100

maternity_company = ensurancebase * MATERNITY_RATE_COMPANY/100
maternity_individual = ensurancebase * MATERNITY_RATE_INDIVIDUAL/100

housing_company = ensurancebase * HOUSING_RATE_COMPANY/100
housing_individual = ensurancebase * HOUSING_RATE_INDIVIDUAL/100

print ("-----------------------------------------------")
print ("社保计算基数: %d" %ensurancebase)
print ("-----------------------------------------------")
print ("养老保险(公司部分): %d" %endowment_company)
print ("养老保险(个人部分): %d" %endowment_individual)
print ("-----------------------------------------------")
print ("医疗保险(公司部分): %d" %medical_company)
print ("医疗保险(个人部分): %d" %medical_individual)
print ("-----------------------------------------------")
print ("失业保险(公司部分): %d" %unemployment_company)
print ("失业保险(个人部分): %d" %unemployment_individual)
print ("-----------------------------------------------")
print ("工伤保险(公司部分): %d" %employ_injury_company)
print ("工伤保险(个人部分): %d" %employ_injury_individual)
print ("-----------------------------------------------")
print ("生育保险(公司部分): %d" %maternity_company)
print ("生育保险(个人部分): %d" %maternity_individual)
print ("-----------------------------------------------")
print ("住房公积金(公司部分): %d" %housing_company)
print ("住房公积金((个人部分): %d" %housing_individual)
insurance_portion = endowment_individual + medical_individual + employ_injury_individual 

taxbase = (salary - insurance_portion - TAXTHRESHOLD) #计税额度

if taxbase <= 0: 
    rate = 0
    deductfactor = 0
elif taxbase <= 1500:
    rate = 3
    deductfactor = 0
elif taxbase <= 4500:
    rate = 10
    deductfactor = 105
elif taxbase <= 9000:
    rate = 20
    deductfactor = 555
elif taxbase <= 35000:
    rate = 25
    deductfactor = 1005
elif taxbase <= 55000:
    rate = 30
    deductfactor = 2755
elif taxbase <= 80000:
    rate = 35
    deductfactor = 5505    
else:
    rate = 45
    deductfactor = 13505
tax = taxbase * rate /100 - deductfactor
print ("-----------------------------------------------")
print ("个人所得税是: %d" %tax)
print ("-----------------------------------------------")
input("按回车健退出...")
