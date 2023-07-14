
import pandas as pd
import streamlit as st
import plotly.express as px

required_skills = {"Cloud Computing":{
    "Cloud_Platforms":{"AWS":1,"AZURE": 2,"GCP": 1},
    "Networking fundamentals":{"TCP/IP":1,"DNS": 2,"Load balancing":5,"VPN":5 },
    "OS":{"Linux":4, "Windows":5}, 
    "Automation & Scripting":{"Python":2,"Powershell":3,"Bash":4},
    "IAC":{"Terraform":1 ,"AWS cloud formation":2},
    "Containerization":{"Docker":1,"Kubernetes":2},
    "Monitoring & Troubleshooting":{"AWS cloudwatch":1,"Azure monitor":2},
    "Softskills":{"Effective communication":1,"Teamwork":1,"Collaboration skills":1}
}}


st.sidebar.header('Input here')
user_input = st.sidebar.text_input("Enter Register NO : ")
df = pd.read_excel("intern21.xlsx")


user_input = int(user_input)
df = df[df["Reg_no"] == user_input].reset_index()
def gap_analysis( data , required_skills): 
    x , p = [] , 0
    known_skills = known(data,required_skills)
    for i in required_skills[data["Aspiration"].to_list()[0]] :
        for k,l in required_skills[data["Aspiration"].to_list()[0]][i].items():
            if k not in known_skills:
                x.append(x)
                p = p + required_skills[data["Aspiration"].to_list()[0]][i][k]
    return  p , x            
    
    
def known(data , required_skills) : 
    o = []
    for i,j in required_skills[data["Aspiration"].to_list()[0]].items():
        for k in data[i].to_list():
            if "," in k :
                o = o + k.split(",")
            else:
                o.append(k)
    return o

weight , unknown  = gap_analysis(df,required_skills)
weight1  = weight
weight  = abs(100-weight)/10
st.mardown("###Report")



        







        
