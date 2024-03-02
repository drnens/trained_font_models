import os
import random
import pathlib
import subprocess

training_text_file = '/home/enes/Desktop/tesstrain/tesstrain/langdata_lstm/eng/eng.training_text'

lines = []

with open(training_text_file, 'r') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

output_directory = '/home/enes/Desktop/tesstrain/tesstrain/data/Monospac821BT-ground-truth'

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

random.shuffle(lines)

count = 200 #Define how many examples you want for a specific size, spacing and leading combination.

lines = lines[:count]

font_size = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36]
font_spacing = [-0.3, -0.25, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
font_leading = [0]

line_count = 0

for i in font_size:
    size = i
    for j in font_leading:
        leading = j
        for k in font_spacing:
            spacing = k

            for line in lines:
                training_text_file_name = pathlib.Path(training_text_file).stem
                line_training_text = os.path.join(output_directory,
                                                  f'{training_text_file_name}_{line_count}.gt.txt')
                with open(line_training_text, 'w') as output_file:
                    output_file.writelines([line])

                file_base_name = f'eng_{line_count}'
                # Adjust xsize and ysize as your need. In this case it is set according to A3 size 150 PPI/DP image.
                # https://www.a3-size.com/what-is-a3-size-in-pixels/
                subprocess.run([
                    'text2image',
                    '--font=Monospac821 BT',
                    f'--text={line_training_text}',
                    f'--outputbase={output_directory}/{file_base_name}',
                    '--max_pages=1',
                    '--strip_unrenderable_words',
                    f'--leading={leading}',
                    '--xsize=2480',
                    '--ysize=1754',
                    f'--ptsize={size}',
                    f'--char_spacing={spacing}',
                    '--exposure=0',
                    '--unicharset_file=/home/enes/Desktop/tesstrain/tesstrain/langdata_lstm/eng/eng.unicharset'
                ])
                print(size, leading, spacing)
                line_count += 1



