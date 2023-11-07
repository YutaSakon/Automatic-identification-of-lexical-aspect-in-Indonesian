#Identify the position of the verb in each sentence in the txt file, counting from the beginning.

import pandas as pd

def find_position(sentence, target_word):
    words = str(sentence).split(' ')
    try:
        position = words.index(target_word)
    except ValueError:
        position = -1
    return position

if __name__ == "__main__":
    # Select a file
    df_input = pd.read_csv("/content/drive/MyDrive/Colab_Notebooks/find_position.txt", encoding="shift_jis", sep='\t', header=None, names=['Sentence', 'Target Word'])

    output_data = []

    for index, row in df_input.iterrows():
        input_sentence, target_word = row['Sentence'], row['Target Word']
        position = find_position(input_sentence, target_word)
        output_data.append([input_sentence, target_word, position])

    # Create a new DataFrame with the output data and write it to an Excel file
    df_output = pd.DataFrame(output_data, columns=["Sentence", "Target Word", "Position"])
    df_output.to_excel("output.xlsx", index=False)
