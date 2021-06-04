import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
#from PIL import Image

#image initializing
#banner = Image.open('images/banner.jpg')
#image1 = Image.open('images/image1.jpg')
#image2 = Image.open('images/image2.jpg')
#image3 = Image.open('images/image3.jpg')
#image4 = Image.open('images/image4.jpg')
#objective = Image.open('images/objective.jpg')
#features = Image.open('images/features.jpg')
#stream = Image.open('images/based_stream.jpg')
#similar = Image.open('images/similarity.jpg')

#Streamlit section
my_page = st.sidebar.radio('Sprint Navigation', ['Introduction', 'EDA part1','EDA part2','Recommender Engine','Collaborations'])

if my_page == 'Introduction':
    st.title("Introduction")
    
    st.header("Introducing David Guetta to the Philippine Market")
    #st.image(banner)
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    st.header("Objectives")
    #st.image(objective)
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
elif my_page == 'EDA part1':
    st.title("Exploratory Data Analysis part1")
    
    st.header("Popularity among EDM artist")
    
    #st.image(image1)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    st.header("Number of Followers among EDM artist")
    
    #st.image(image2)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
elif my_page == 'EDA part2':
    st.title("Exploratory Data Analysis part2")
    
    st.header("EDM artists track top 200 placement")
    
    #st.image(image3)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    st.header("David Guetta\'s Streaming History")
    
    #st.image(image4)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
elif my_page == 'Recommender Engine':
    st.title("Recommender Engine")
    
    st.header("Supervised ML Model")
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    #st.image(features)
    
    st.header("Resulting Output")
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)

elif my_page == 'Collaborations':
    st.title("Collaborations")
    st.header("Why Collaborate?")
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    st.header("Collaboration Based On Streams")
    #st.image(stream)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
    
    st.header("Collaboration Based On Streams")
    #st.image(similar)
    
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vehicula ac tellus eu hendrerit. Sed in diam scelerisque, ullamcorper justo ut, pharetra ex. Aenean vel sagittis odio, sed elementum arcu. Mauris ac enim ac tortor dictum molestie. Ut efficitur tempor odio sit amet hendrerit. Cras ut leo dignissim, efficitur justo in, varius risus. Praesent convallis rutrum leo vel egestas. Etiam malesuada a lacus at volutpat. Cras sed convallis neque, eget aliquam nulla.',unsafe_allow_html=False)
