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

text = read_file("shakespeare.txt")
stoi, itos = create_mappings(text)


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
