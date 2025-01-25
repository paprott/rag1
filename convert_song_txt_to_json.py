
import os
import json
import pandas as pd

def read_song_data(file_path):
    song_data = []
    with open(file_path, 'r') as file: 
        lines = file.readlines()
        author = lines[0]
        title = lines[1]
        link = lines[2]
        text = lines[3:]

        song_data.append({
            'Title': title,
            'Author': author,
            'Link to music': link,
            'Text of song': text
        })

    return song_data

def write_json(song_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(song_data, file, indent=4, ensure_ascii=False)

def process_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json")

            song_data = read_song_data(input_file)
            write_json(song_data, output_file)

if __name__ == "__main__":
    # Directory to save text files with songs
    output_dir = './songs'
    os.makedirs(output_dir, exist_ok=True)
    output_dir = './data'
    os.makedirs(output_dir, exist_ok=True)
    
    input_folder = "songs"
    output_folder = "data"

    process_folder(input_folder, output_folder)