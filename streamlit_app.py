
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

if user_input : 
    user_input = int(user_input)
    df = df[df["Reg_no"] == user_input].reset_index()
    def gap_analysis(Aspiration : str , data , required_skills): 
        x , p = [] , 0
        known_skills = known(data,required_skills)
        for i in requried_skills[data["Aspiration"].to_list()[0]] :
            print(i,"\n\n")
            for k,l in requried_skills[data["Aspiration"].to_list()[0][i]]:
                print(k,l)








        
        
        
    def known(data , required_skills) : 
        o = []
        for i,j in requried_skills[data[Aspiration].to_list()[0]].items():
            for k in data[i].to_list():
                if "," in k :
                    o += k.split(",")
                else:
                    o.append(k)
        return o
        








        
