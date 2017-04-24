# movie_dialogue_analysis

Setup:
1. The starting point for the text analysi pipeline is the "cornell movie-dialogs corpus" folder. This must contain all the files in from the original dataset.
2. The other important thing concerning structures are the folders "model" and "dataset". They are placeholders for the processing.
3. Run the parse_source_data.py and this will parse and create the datasets needed for our analysis.
4. Rest of the analysis are carried out in the 4 notebooks.
	1. EDA - I : Data exploration to learn more about the data;Perform some basic clean up
	2. EDA - 2 : Word Cloud for movie_titles and lines;Basic NLP and phrase modelling;
				Topic Modelling and Visualization (Latent Dirchlet Allocation)
	3. Finding Similar Characters based on dialogues
	4. Finding Similar Conversations
Notes: 
1. Models created during the process are not included, due the large size of the files. 
2. Run sudo python -m spacy.en.download all to download english vocabulary.