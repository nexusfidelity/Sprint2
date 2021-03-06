import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


#image initializing
banner = Image.open('images/banner.jpg')
image1 = Image.open('images/image1.jpg')
image2 = Image.open('images/image2.jpg')
image3 = Image.open('images/image3.jpg')
image4 = Image.open('images/image4.jpg')
objective = Image.open('images/objective.jpg')
features = Image.open('images/features.jpg')
stream = Image.open('images/based_stream.jpg')
similar = Image.open('images/similarity.jpg')
knn1 = Image.open('images/KNN1.jpg')
knn2 = Image.open('images/KNN2.jpg')
banner2 = Image.open('images/banner2.jpg')

#Streamlit section
my_page = st.sidebar.radio('Sprint Navigation', ['Introduction', 'EDA part1','EDA part2','Recommender Engine','Song','Collaborations','Contributors'])

if my_page == 'Introduction':
    st.title("Introduction")
    
    st.header("Introducing David Guetta to the Philippine Market")
    st.image(banner)
    st.markdown('Pierre David Guetta born in 7 November 1967 is a French DJ, record producer and songwriter. He has racked up over 50 million record sales globally, whereas his total number of streams is over 10 billion. In 2011 and 2020, Guetta was voted as the number one DJ in the DJ Mag Top 100 DJs poll. In 2013, Billboard crowned "When Love Takes Over" as the number one dance-pop collaboration of all time.',unsafe_allow_html=False)
    st.markdown('Born and raised in Paris, he released his first album, Just a Little More Love, in 2002. Later, he released Guetta Blaster (2004), Pop Life (2007), One Love (2009), One More Love (2010), Nothing But The Beat (2011), Listen (2014), Listen Again (2015) and 7 (2018). Guetta achieved mainstream success with his 2009 album One Love which included the hit singles "When Love Takes Over", "Gettin\' Over You", "Sexy Bitch" and "Memories", the first three of which reached number one in the United Kingdom. The 2011 follow-up album, Nothing but the Beat, continued this success, containing the hit singles "Where Them Girls At", "Little Bad Girl", "Without You", "Titanium" and "Turn Me On". In 2018, he released the album "7" featuring J Balvin, Nicki Minaj, Jason Derulo, Sia, G-Eazy and more. The album also featured twelve tracks by his alias Jack Back. In 2019, he started a new movement together with fellow producer MORTEN called "Future Rave". The duo released their "New Rave" EP in July 2020 for the fans to enjoy at home despite clubs being closed.[10] Guetta and Sia reunited to release "Let\'s Love" in 2020, amidst the COVID-19 pandemic.',unsafe_allow_html=False)
    
    st.header("Objectives")
    st.image(objective)
    
elif my_page == 'EDA part1':
    st.title("Exploratory Data Analysis part1")
    
    st.header("Popularity among EDM artist")
    
    st.image(image1)
    
    st.markdown('Among the EDM artists, he has the highest popularity rating globally.',unsafe_allow_html=False)
    
    st.header("Number of Followers among EDM artist")
    
    st.image(image2)
    
    st.markdown('He has the 2nd highest total followers among the global EDM artists.',unsafe_allow_html=False)
    
    
elif my_page == 'EDA part2':
    st.title("Exploratory Data Analysis part2")
    
    st.header("EDM artists track top 200 placement")
    
    st.image(image3)
    
    st.markdown('However, in the Philippine streaming market, only 8 of his songs made it to top 200 from 2017-2021',unsafe_allow_html=False)
    
    st.header("David Guetta\'s Streaming History")
    
    st.image(image4)
    
    st.markdown('The last time that DG???s song made it to top 200 in the Philippines was in Feb 2019. ',unsafe_allow_html=False)
    
elif my_page == 'Recommender Engine':
    st.title("Recommender Engine")
    
    st.header("DataSet")
    st.markdown('We fetched the data from Spotify and cleaned it for it to be processed for ML modeling',unsafe_allow_html=False)
    st.markdown('https://developer.spotify.com/',unsafe_allow_html=False)
    
    st.header("Supervised ML Model")
    st.markdown('We used these features to create the Machine Learning Model to give recommendations on songs and artist collaborations. these features allow us to narrow down what the model woll be looking for in the data set.',unsafe_allow_html=False)
    
    st.image(features)
    
    st.header("KNN (K Nearest Neighbor)")
    st.markdown('We used KNN for the model to search for songs and artists similar to David Guetta. There are many advantages to KNN that is why we used it. its has small training period, new data can be added seamlessly for us to reconfigure the model, and KNN is very easy to implement in Python.',unsafe_allow_html=False)
    
    st.image(knn1)
    
    st.markdown('KNN allows us to find similar songs by tempo and loudness based on its predicted group and being near the selected input song',unsafe_allow_html=False)
    
    st.image(knn2)

elif my_page == 'Song':
    st.title("Song Recommended")
    
    st.header("Selected Song: Don\'t Leave Me Alone ft Anne Marie")
    
    st.components.v1.iframe("https://www.youtube.com/embed/XeKoCLVXKNo",width=None, height=400)
    
    st.markdown('We selected one of David Guetta\'s song - Don\'t Leave Me Alone ft Anne Marie. The Recommender Engine then searched for songs similar to the Don\'t Leave Me Alone ft Anne Marie by tempo & loudness which is then deployed to a spotify playlist below. The recommended songs are debatable and subject for scrutiny by listeners. Please listen the to playlist below and hear the similarity of these songs with Don\'t Leave Me Alone ft Anne Marie',unsafe_allow_html=False)
    
    st.header("Spotify Playlist")
    st.components.v1.iframe("https://open.spotify.com/embed/playlist/7H9XEQlYxXNTANV75kYhJp", width=None, height=380)
    
elif my_page == 'Collaborations':
    st.title("Collaborations")
    st.header("Why Collaborate?")
    st.markdown('1. Collaboration is the best way to get in front of the audience that is most likely to connect with you.',unsafe_allow_html=False)
    st.markdown('2. Collaboration helps you get the word around.',unsafe_allow_html=False)
    st.markdown('3. Collaboration helps you create a brand image around your name.',unsafe_allow_html=False)
    st.markdown('4. Collaborations lead to exceptional art projects.',unsafe_allow_html=False)
    st.markdown('5. Collaborations promote growth rather than competition.',unsafe_allow_html=False)

    st.markdown('source: https://blog.dextra.art/why-collaboration-is-the-way-to-grow-as-an-artist-58f17bc4e918',unsafe_allow_html=False)
    
    st.header("Collaboration Based On Streams")
    st.image(stream)
    
    st.markdown('Collaborating with artist who has the most streams in the Philippines can boost your brand in the Philippines. Filipinos are very receptive of these artist and will get the word out that you have collaborated with their favorite artist. Collaborating will also increase the streams of both artist making it mutually beneficial for both parties.',unsafe_allow_html=False)
    
    st.header("Collaboration Based On similarity")
    st.image(similar)
    
    st.markdown('Similarly, David Guetta can also boost his brand in the Philippines by collaborating with these artist based on similarity. It can boost his brand not just in the Philippines but also globally',unsafe_allow_html=False)
    
elif my_page == 'Contributors':

    st.header('The Team')
    
    st.markdown('We are proud to present our research and are avid fans of Davide Guetta. We wish for David Guetta, good health and good beats.',unsafe_allow_html=False)

    col1, col2, col3 = st.beta_columns(3)
    
    with col1:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="fidel-ivan-racines-187477167" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/fidel-ivan-racines-187477167?trk=profile-badge">Fidel Ivan Racines</a></div>'''
                              ,height=350)
    
    with col2:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="jon-marco-francisco-77592214a" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/jon-marco-francisco-77592214a?trk=profile-badge%22%3EJon Marco Francisco</a></div>'''
                              ,height=350)
    
    with col3:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="ajloconer" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/ajloconer?trk=profile-badge%22%3EAndrew Justin Oconer</a></div>'''
                              ,height=350)

    col4, col5, col6 = st.beta_columns(3)

    with col4:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="preciouseunicegrullo" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/preciouseunicegrullo?trk=profile-badge%22%3EPrecious Eunice Grullo</a></div>'''
                              ,height=350)
        
    with col5:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="adrianjanairo" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/adrianjanairo?trk=profile-badge%22%3EAdrian Genevie Janairo</a></div>'''
                              ,height=350)
        
    with col6:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="reiniel-dan-pablo-5197641b4" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/reiniel-dan-pablo-5197641b4?trk=profile-badge%22%3EReiniel Dan Pablo</a></div>
                              ''', height=350)
        
    st.header('The Mentor')
    
    st.markdown('Our mentor has helped and guided us through out the process of this study.',unsafe_allow_html=False)
    
    col7, col8, col9 = st.beta_columns(3)
    
    with col7:
        st.components.v1.html('''''', height=350)
        
    with col8:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="patricknuguid" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/patricknuguid?trk=profile-badge%22%3EPatrick Nuguid</a></div>'''
                              ,height=350)
        
    with col9:
        st.components.v1.html('''''', height=350)
        
    st.header('The Organization')
    
    st.image(banner2)
    
    st.markdown('Eskwelabs is an online data upskilling school for people and teams in Southeast Asia. Who gives access opportunities in the future of work through accessible data skills that are high in-demand as the amount of data in the world increases exponentially.',unsafe_allow_html=False)
    
    st.markdown('Our mission is to give access to engaging and future-relevant skills education is then crucial to help people and teams thrive in that future. In Southeast Asia, where more than half of the population is under the age of 30, we believe data education can democratize access to meaningful careers for workers and sustainable competitiveness for companies.',unsafe_allow_html=False)
    
    st.markdown('At the same time, learning happens in all kinds of ways. Many learning environments, both in school and online, rely on lecture formats which are rarely engaging and effective for technical skills. Eskwelabs aims to enable participatory and active learning experiences so beyond acquiring in-demand skills, we can also rediscover the joy of learning and reinventing ourselves.',unsafe_allow_html=False)
