name1=input("Enter Boy Name:")
name2=input("Enter Girl Name:")
combine_name=name1+name2
lower_case_string=combine_name.lower()
t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t+r+u+e
l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f"Love Score is{love_score} and your together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f"Love Score is {love_score} and your good together")
else:
    print(f"Your Love Score {love_score}")