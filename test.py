import os
import pandas as pd

path = 'stimuli'
num_of_images = len(os.listdir(path))

body_image = [f'stimuli/{p}' for p in os.listdir(path)] * 20
body_condition = [x[:-4] for x in os.listdir(path)] * 20

arrow_key_correct = []
trial_response_correct = []
for item in body_condition:
    if item == 'Forwards-R' or item == "Backwards-L":
        arrow_key_correct.append('c')
        trial_response_correct.append('l')
    else:
        arrow_key_correct.append('n')
        trial_response_correct.append('r')

df = pd.DataFrame(list(zip(body_image, body_condition, arrow_key_correct, trial_response_correct)),
                  columns=['body_image', 'body_condition', 'arrow_key_correct',
                           'trial_response_correct'])

df.to_csv('spatial.csv')
