# Songs Recommendation System

>This project use server=Ollama, model="mxbai-embed-large:latest", model="SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M", database=Chroma.  
>Modify the models.py file and adjust the Models class appropriately for the LLM and Embedding models.  
>In the .env file you can add the online API access keys.  


Simpy run your Assistant:
- chat.py

Folders:
- songs: songs texts as '.txt'
- data: songs texts as '.json'
- db: vector database

Files:
- Piosenki.xlsx: songs scrapped from https://www.tekstowo.pl
- Przykladowe pytania do asystenta.txt

Utils:
- convert_song_txt_to_json.py
- convert_song_excel_to_txt.py
- update_vector_database_with_songs.py
- models.py
