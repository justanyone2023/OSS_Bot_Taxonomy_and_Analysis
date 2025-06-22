import pandas as pd
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

file_name = 'top100_PullRequestEvent'
data = pd.read_csv(f'bot_evluation_process/data/bot/{file_name}.csv')

# Fill missing values w
data['body'] = data['body'].fillna('')

# Load spaCy's model
nlp = spacy.load('en_core_web_md')

# Function: Calculate dissimilar body content
def get_dissimilar_bodies(group, threshold=0.8):
    group = group.copy()
    # Vectorization
    group['body_vector'] = group['body'].apply(lambda x: nlp(x).vector)
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(np.vstack(group['body_vector']))

    # Create a collection to store the index of processed content.
    processed_indices = set()
    # Initialize a list to store the unique bodies.
    unique_bodies_list = []

    for i in range(len(group)):
        if i not in processed_indices:
            # Find all body indexes that are similar to the current body.
            similar_indices = np.where(similarity_matrix[i] >= threshold)[0]
            # Add the first similar body to the unique_bodies_list.
            unique_bodies_list.append(group.iloc[i][['actor_id', 'type', 'body']])
            # Mark these indexes as processed
            processed_indices.update(similar_indices)

    unique_bodies_df = pd.DataFrame(unique_bodies_list)

    return unique_bodies_df

# Function: Process a single actor_id group
def process_actor_id(actor_id, threshold):
    group = data[data['actor_id'] == actor_id]
    return get_dissimilar_bodies(group, threshold=threshold)

# Handling different thresholds
thresholds = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
# thresholds = [0.95]

for threshold in thresholds:
    print(f"Processing for threshold: {threshold}")

    actor_ids = data['actor_id'].unique()
    dissimilar_bodies_list = []

    # Use ThreadPoolExecutor for multithreading processing
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_actor_id, actor_id, threshold): actor_id for actor_id in actor_ids}
        for future in tqdm(as_completed(futures), total=len(actor_ids), desc=f"Processing Groups for threshold {threshold}"):
            dissimilar_bodies_list.append(future.result())

    dissimilar_bodies = pd.concat(dissimilar_bodies_list).reset_index(drop=True)

    output_file = f'bot_evluation_process/data/bot/{file_name}_dissimilar_bodies_threshold_{threshold}.csv'
    dissimilar_bodies.to_csv(output_file, index=False)

    print(f"The dissimilar content has been outputted. {output_file}")
