import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import mysql.connector as conn
import time
global df
df=pd.read_csv("literacy_rate.csv")
#---------------------------------------------
#Function to display the main menu.
#---------------------------------------------
def MainMenu():
    ans='y'
    while ans=='y' or ans=='y':
        opt=""
        print()
        print("===============================================")
        print(" Literacy Rate Of India ")
        print("***********************************************")
        print("1-Data Visualisation\n")
        print("2-Analysis\n")
        print("3-Manipulation\n")
        print("4-Exit")
        print("===============================================")
        opt=input("Enter your choice:")
        if opt==&#39;1&#39;:
            visuals()
        elif opt==&#39;2&#39;:
            analysis()
        elif opt==&#39;3&#39;:
            manipulation()
        elif opt==&#39;4&#39;:
            my_chance=input(&quot;Do you really want to exit?(y/n)&quot;)

            if my_chance==&quot;y&quot; or my_chance==&quot;Y&quot;:
                print(&quot;Thank you. Exiting now......&quot;)
                sys.exit()
            else:
                print(&quot;\nInvlaid choice. Try again&quot;)
                continue
        else:
            ans=input(&quot;Do you want to continue(y/n)&quot;)

#------------------------------------------------
#Function for Data Visualization.
#------------------------------------------------
def visuals():
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
while True:
print(&quot;V I S U A L M E N U&quot;)
print(&quot;=====================&quot;)
print(&quot;1-Line Chart of a Particular Year&quot;)
print(&quot;2-Bar Chart for different Years&quot;)
print(&quot;3-Histogram for a Year&quot;)
print(&quot;4-Line Chart Average Literacy Year wise&quot;)
print(&quot;5-Back to Main Menu&quot;)
print(&quot;==================================&quot;)
choice=int(input(&quot;Enter your choice: &quot;))
if choice==1:
year=input(&quot;Enter Year of Literacy : &quot;)
df1=df.sort_values(by=[year],ascending=False)
n=int(input(&quot;Enter number of states (1-34) : &quot;))
print(df1.head(n))
df1.plot(x =&#39;State/ UTs&#39;, y=year, kind = &#39;line&#39;,rot=75)
plt.xlabel(&quot;State/UT Name--&gt;&quot;, color=&#39;b&#39;,fontsize=12)
plt.ylabel(&quot;Literacy Rate (%)-&gt;&quot;, color=&#39;b&#39;,fontsize=12)
plt.title(&quot;Top &quot;+str(n)+&quot; Indian State(s) Literacy Analysis&quot;,color=&#39;r&#39;,fontsize=16)
plt.show()
elif choice==2:
year=eval(input(&quot;Enter Year of Literacy as list like[&#39;1951&#39;,&#39;2011&#39;]: &quot;))
n=int(input(&quot;Enter number of states (1-34) : &quot;))
print(df.head(n))
df1=df.head(n)
df1.plot(x=&#39;State/ UTs&#39;,y=year,kind=&#39;bar&#39;,rot=75)
plt.xlabel(&quot;State/UT Name--&gt;&quot;, color=&#39;r&#39;,fontsize=12)

plt.ylabel(&quot;Literacy Rate (%)-&gt;&quot;, color=&#39;r&#39;,fontsize=12)
plt.title(&quot;Top &quot;+str(n)+&quot; Indian State(s) Literacy Analysis&quot;,color=&#39;g&#39;,fontsize=16)
plt.show()
elif choice==3:
year=input(&quot;Enter Year of Literacy : &quot;)
df.hist(column=year,color=&#39;r&#39;,edgecolor=&#39;black&#39;)
plt.xlabel(&quot;Literacy Rate (%)-&gt;&quot;, color=&#39;r&#39;,fontsize=12)
plt.ylabel(&quot;No. of States&quot;, color=&#39;r&#39;,fontsize=12)
plt.title(&quot;All Indian State(s) Literacy Analysis of \nYear-&quot;+year,color=&#39;g&#39;,fontsize=16)
plt.show()
elif choice==4:
s1=df.mean()
mylabel=s1.index
plt.plot(mylabel,s1.values,linestyle=&#39;dashed&#39;,linewidth=3,\
color=&#39;r&#39;,marker=&#39;o&#39;,mfc=&#39;b&#39;,ms=10)
plt.xlabel(&quot;Year--&gt;&quot;, color=&#39;b&#39;,fontsize=12)
plt.ylabel(&quot;Literacy Rate (%) of India -&gt;&quot;, color=&#39;b&#39;,fontsize=12)
plt.title(&quot;Indian Literacy Rate Analysis 1951 to 2011&quot;, color=&#39;r&#39;,fontsize=16)
plt.grid()
plt.show()
else:
break
#------------------------------------------------
#Function to analyse data from a dataframe.
#------------------------------------------------
def analysis():
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
while True:
print(&quot;Data Frame Analysis&quot;)
print(&quot;*******************&quot;)
menu=&#39;&#39;&#39;\n 1.Top record
\n 2.Bottom records
\n 3.To Display Literacy of a particular year
\n 4.To Display States with Literacy rate is &gt;= n% in a year
\n 5.To Display States with Maximun Literacy rate
\n 6.To display Average Literacy of India
\n 7.To display Complete DataFrame
\n 8.To Minimum, Maximum and Average Literacy in a year&quot;
\n 9.Back to Main Menu&#39;&#39;&#39;
print(menu)
print(&quot;==========================================&quot;)

ch_an=int(input(&quot;Enter your choice: &quot;))
if ch_an==1:
n=int(input(&quot;Enter the number of records to be displayed: &quot;))
print(&quot;Top&quot;,n,&quot;records from the dtaframe&quot;)
print(df.head(n))
elif ch_an==2:
n=int(input(&quot;Enter the number of records to be displayed: &quot;))
print(&quot;Bottom&quot;,n,&quot;records from the dtaframe&quot;)
print(df.tail(n))
elif ch_an==3:
print(&quot;Name of the columns\n&quot;,df.columns)
col=eval(input(&quot;Enter the year of Literacy like [&#39;State/ UTs&#39;,&#39;1951&#39;]: &quot;))
print(df.loc[:,col])
elif ch_an==4:
yr=input(&quot;Enter Year : &quot;)
n=float(input(&quot;Enter percentage :&quot;))
df1=df.loc[(df[yr]&gt;n),[&#39;State/ UTs&#39;,yr]]
df1=df1.sort_values(by=yr,ascending=False)
print(df1)
elif ch_an==5:
yr=input(&quot;Enter Year : &quot;)
print()
print(&quot;State with Maximum Literacy in the year-&quot;+yr)
print(&quot;----------------------------------------------&quot;)
x=df[yr].max()
print(df.loc[(df[yr]==x),[&#39;State/ UTs&#39;,yr]])
print(&quot;----------------------------------------------\n&quot;)
elif ch_an==6:
print(&quot;Average Literacy of India&quot;)
print(&quot;-------------------------&quot;)
print(df.mean())
print(&quot;-------------------------&quot;)
elif ch_an==7:
print(&quot;Displaying Complete DataFrame&quot;)
print(&quot;-------------------------&quot;)
print(df)
print(&quot;-------------------------&quot;)
elif ch_an==8:
yr=input(&quot;Enter Year : &quot;)
print(&quot;\nMaximum Literacy:&quot;)
print(&quot;-------------------------&quot;)
x=df[yr].max()

print(df.loc[(df[yr]==x),[&#39;State/ UTs&#39;,yr]])
print(&quot;-------------------------&quot;)
print(&quot;Minimum Literacy:&quot;)
print(&quot;-------------------------&quot;)
y=df[yr].min()
print(df.loc[(df[yr]==y),[&#39;State/ UTs&#39;,yr]])
avg=df[yr].mean()
print(&quot;------------------------------------------------------------&quot;)
print(&quot;Average Literacy in the Year-&quot;+yr+&quot; in India =&quot;,avg)
print(&quot;------------------------------------------------------------&quot;)
else:
break

#------------------------------------------------
#Function to manipulate data in a dataframe.
#------------------------------------------------
def manipulation():
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
while True:
print(&quot;\n\nManipulation Menu&quot;)
print(&quot;*********************&quot;)
print(&#39;&#39;&#39;\n1. Insert a row\n
2. Insert a Column\n
3. Delete a Row\n
4. Delete a column\n
5. Update a cell value\n
6. Back to Main Menu&#39;&#39;&#39;)
print(&quot;=====================&quot;)
mch=int(input(&quot;Ente your choice: &quot;))
if mch==1:
df1=pd.DataFrame()
col=df.columns
print(col)
print(df.head(1))
j=0
lst=[]
lst1=eval(input(&quot;Enter a list of values in the sequence of columns: &quot;))
print(lst1)
s1=pd.Series(lst1,index=df.columns)
df1=df.append(s1,ignore_index=True)
print(&quot;New row inserted&quot;)

print(df1)
df1.to_csv(&quot;literacy_rate.csv&quot;,index=False)
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
elif mch==2:
n=int(input(&quot;How Many States? &quot;))
yr=input(&quot;Enter Year of Literacy : &quot;)
lst_literacy=[]
for i in range(n):
lrate=float(input(&quot;Enter literacy rate of &quot;+df.loc[i,[&#39;State/ UTs&#39;]]+&quot;: &quot;))
lst_literacy.append(lrate)
df[yr]=lst_literacy
print(df)
df.to_csv(&quot;literacy_rate.csv&quot;,index=False)
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
elif mch==3:
print(&quot;List of States-\n&quot;,df[&#39;State/ UTs&#39;])
n=int(input(&quot;Enter the index number of the State for row deletion :&quot;))
ch=input(&quot;Do you really want to delete row of-\n&quot;+str(df[(df.index==n)])+&quot;(y/n)?&quot;)
if ch==&#39;y&#39; or ch==&#39;Y&#39;:
df.drop(index=n,inplace=True)
print(df)
print(&quot;Row of index no- &quot;,n,&quot;deleted successfully!!!&quot;)
df.to_csv(&quot;literacy_rate.csv&quot;,index=False)
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
elif mch==4:
print(df.columns)
col=input(&quot;Enter column name to be deleted from the above&quot;)
ch=input(&quot;Do you really want to delete column(y/n)?&quot;)
if ch==&#39;y&#39; or ch==&#39;Y&#39;:
del df[col]
print(&quot;Column- &quot;,col,&quot;deleted successfully!!!&quot;)
print(df)
df.to_csv(&quot;literacy_rate.csv&quot;,index=False)
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
elif mch==5:
print(df)
row_idx=int(input(&quot;Enter row index/label for edit : &quot;))
col_idx=input(&quot;Enter column index/label for edit : &quot;)
x=df.loc[row_idx,col_idx]
ch=input(&quot;Do you really want to overwrite the value&quot;+str(x)+&quot; column(y/n)? &quot;)
if ch==&#39;y&#39; or ch==&#39;Y&#39;:
val=eval(input(&quot;Enter new value : &quot;))

df.loc[row_idx,col_idx]=val
print(&quot;Value overwritten Successfully!!!&quot;)
print(df)
df.to_csv(&quot;literacy_rate.csv&quot;,index=False)
df=pd.read_csv(&quot;literacy_rate.csv&quot;)
else:
break

#***************************************************
# Calling main program
#***************************************************
MainMenu()
