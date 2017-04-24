import pandas as pd
import os
import json


def split_files(path=None):
    aggregate_list = []
    if path is not None:
        with open(path) as f:
            aggregate_list.extend(f.readlines())
        aggregate_list_split = [item.split(
            " +++$+++ ") for item in aggregate_list]
    return aggregate_list_split


def construct_row(schema, record):
    data_point = {}
    for f in schema:
        data_point[f["name"]] = record[f["index"]]
    return data_point

if __name__ == "__main__":
    source_folder = "cornell movie-dialogs corpus"
    dest_folder = "dataset"
    source_ext = ".txt"
    dest_ext = ".json"
    file_names = ["movie_titles_metadata", "movie_lines",
                  "movie_conversations", "movie_characters_metadata"]
    files_schema = {"movie_titles_metadata":
                    [{"index": 0, "name": "movie_id"},
                     {"index": 1, "name": "movie_title"},
                        {"index": 2, "name": "movie_year"},
                        {"index": 3, "name": "imdb_rating"},
                        {"index": 4, "name": "imdb_votes"},
                        {"index": 5, "name": "genres"}],
                    "movie_characters_metadata":
                    [{"index": 0, "name": "character_id"},
                     {"index": 1, "name": "character_name"},
                        {"index": 2, "name": "movie_id"},
                        {"index": 3, "name": "movie_title"},
                        {"index": 4, "name": "gender"},
                        {"index": 5, "name": "position_credits"}],
                    "movie_lines":
                    [{"index": 0, "name": "line_id"},
                        {"index": 1, "name": "character_id"},
                        {"index": 2, "name": "movie_id"},
                        {"index": 3, "name": "character_name"},
                        {"index": 4, "name": "text"}],
                    "movie_conversations":
                    [{"index": 0, "name": "character_id_1"},
                        {"index": 1, "name": "character_id_2"},
                        {"index": 2, "name": "movie_id"},
                        {"index": 3, "name": "line_ids"}]
                    }
    for file in file_names:
        path = source_folder + os.sep + file + source_ext
        split_file = split_files(path)
        schema = files_schema[file]
        split_data = [construct_row(schema, meta)
                      for meta in split_file]
        dest_path = dest_folder + os.sep + file + dest_ext
        pd.DataFrame(split_data).to_json(dest_path)
