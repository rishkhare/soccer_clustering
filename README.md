

# Soccer players similiarity clustering


The data was taken from the whoscored website. It contains the details of around 17000+ soccer players all around the world. 


## Aim

The aim of this project was to find similar players on the basis of goals, assists, chance creation, tackles, etc. This idea stemmed from a reddit post that mentioned that Oliver Kahn (Soccer head for the German team Bayern Munich) has an analytics software that recommends like-for-like players in the case they want to go into the market for buying a new player.


## Machine Learning 

After cleaning the dataset (since a lot of the small leagues do not have all the stats available for the players), we used K-means unsupervised algorithm to find similar player clusters.


The interactive bokeh plot was deployed via Streamlit and can be viewed here: https://rishkhare-soccer-clustering-visual-mzvy84.streamlitapp.com/
