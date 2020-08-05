import matplotlib.pyplot as plt
# print(plt.style.available)

# print("""['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 
# 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
# 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid',
#  'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 
#  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']""")
# input_numbers = range(1,5001)
# output_numbers = [x**3 for x in input_numbers]
# plt.style.use('bmh')
# fig,ax =plt.subplots()

# ax.scatter(input_numbers,output_numbers,c=output_numbers ,cmap =plt.cm.Blues,s=50)
# ax.set_title("CubeNumbers ",fontsize = 24)
# ax.set_xlabel("Numbers",fontsize = 15)
# ax.set_ylabel("CubicNumbers",fontsize = 18)
# ax.tick_params(axis="both",labelsize = 14)

# plt.show()
# import smtplib

    


# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# print(smtpObj.ehlo())
# print(smtpObj.starttls())
# pop =smtpObj.login('jawwadahmed747@gmail.com','nqibwaygbkrhveam')
# print(pop)
    
# lol =smtpObj.sendmail('jawwadahmed747@gmail.com','jawwadahmed747@gmail.com', 'Subject: Python .\nDear , This is an auto generated eamil using python. Sincerely, Bob')
# print(lol)

# smtpObj.quit()


import csv, smtplib

message = """Subject: Your grade

Hi {name}, your grade is {grade} , this is an email from pyhton smtplib library good for sending emails!"""

 

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

print(smtpObj.ehlo())
print(smtpObj.starttls())
pop =smtpObj.login('jawwadahmed747@gmail.com','nqibwaygbkrhveam')
print(pop)
with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email, grade in reader:
        lol =smtpObj.sendmail(
            'jawwadahmed747@gmail.com',
            email,
            message.format(name=name,grade=grade),
            )
print(lol)
smtpObj.quit()