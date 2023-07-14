
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
st.markdown("###Report")
col1,col2 = st.columns(2)
col1.metric('Name' , df['Name'][0])
col2.metric("Roll NO" , df["Reg_no"][0])

col3,col4 = st.columns(2)
col3.metric("Persentage", abs(weight1 - 100))
col4.metric("Gender" , df["Gender"][0])


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig , ax = plt.subplots(figsize = (16,10))
st.write(fig)

x_line = [0 , weight]
y_line = [0,0]

ax.plot(
    x_line,y_line,
    color = "blue" ,
    linewidth = 1 ,
    linestyle = '-' ,
    marker = "*" ,  
    markersize = 6,
    markeredgecolor = "black",
    markeredgewidth = 1,
    label = "Line"
)
ax.set_yticks([])
ax.set_ylabel("")

# Remove the outline box (spines) around the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Set the x-axis limits
ax.set_xlim(0,10)

# Set labels and title
ax.set_xlabel('Where you Stand')

# Load the Mario block image
mario_block_img = plt.imread('mario_block.png')  # Replace 'mario_block.png' with the actual path to the Mario block image

# Plot the Mario block image at the desired position
mario_position = x_line[1]  # The position along the x-axis where the Mario block image will be placed
ax.imshow(mario_block_img, extent=[mario_position-0.40, mario_position + 0.90, -0.110, 0.99])

# Add a legend
ax.legend()

st.markdown('### Where I Stand')

st.pyplot(fig)

if(weight1==0):
    st.write('Congralutions you have achieved your goal')
else:
    weight2=abs(weight1-100)
    st.write(f'You have completed {weight2} foot steps more {weight1} foot steps to reach goal')





        







        
