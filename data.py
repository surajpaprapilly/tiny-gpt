from numpy import random
import torch
import numpy as np

def read_file(file_path):
    with open (file_path, 'r') as file:
        return file.read()



def create_mappings(text):
    character_set = set(text)
    character_list = list(character_set)
    character_list.sort()
    character_to_id_mapping = {}
    id_to_character_mapping = {}
    for index, char in enumerate(character_list):
        character_to_id_mapping[char] = index
        id_to_character_mapping[index] = char

    return character_to_id_mapping,id_to_character_mapping


def encode(s: str, stoi: dict) -> list[int]:
    
    list_of_index = []
    for char in s:
        list_of_index.append(stoi[char])
    return list_of_index


def decode(ids: list[int], itos: dict) -> str:

    text = ""
    for num in ids:
        text += itos[num]
    return text


def get_batch(encoded_text,block_size=128,batch_size=32):
    max_len = len(encoded_text)
    x_store = []
    y_store = []
    for i in range(0,batch_size):
        starting_index = random.randint(0,max_len-block_size-1)
        x_vector = encoded_text[starting_index:starting_index+block_size]
        y_vector = encoded_text[starting_index+1:starting_index+1+block_size]
        x_store.append(x_vector)
        y_store.append(y_vector)
    
    x_tensor = torch.tensor(x_store)
    y_tensor = torch.tensor(y_store)

    return x_tensor,y_tensor







