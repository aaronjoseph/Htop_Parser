import re
import pandas as pd 
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go

# Log File for which the name needs to be edited
FileName = 'top.log'

def Cpu_DF(FileName): 
    match_list = []
    match_list_1 = []
    # Regex to Get the timestamp
    regex = '(?!top - )[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*'
    with open(FileName,"r") as file:
        for line in file:
            for match in re.finditer(regex,line,re.S):
                match_text = match.group()
                match_list.append(match_text)
    # Regex to get the %
    regex_1 = '(Cpu[(]s[)]:)(\s{1,})([0-9]*(?:.)[?:0-9])'
    with open(FileName,"r") as file:
        for line in file:
            for match in re.finditer(regex_1,line,re.S):
                match_text = match.group(3)
                match_list_1.append(match_text)
    # Converting List to Dataframe
    Master_Dict = {'TimeStamp':match_list,'Percentage':match_list_1}
    Final = pd.DataFrame(Master_Dict)
    return(Final)

if __name__ == "__main__":
    DF = Cpu_DF(FileName)
    if st.button("Refresh Plot"):
        DF = Cpu_DF(FileName)
   
    fig = px.line(DF, x='TimeStamp', y='Percentage', title='CPU Utilization over Time')
    fig.update_xaxes(rangeslider_visible=True)
    st.plotly_chart(fig, use_container_width=True)


