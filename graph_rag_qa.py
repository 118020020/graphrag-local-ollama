# this file would be used to run the RAG model on the QA dataset, the default file used is airbnb
# the file name should be consistant with your input data
file_name = 'airbnb' # default
# file_name = None # if you use acquired_transcripts_all.txt, which means all the scripts are included, let file_name = None

import subprocess
import pandas as pd

# read qa questions
qa = pd.read_csv('/home/sedy/Desktop/rag_test_data/acquired-qa-evaluation.csv', encoding='latin1')

#print(qa.file_name.unique())

# keep those only with file_name == airbnb
if file_name:
    qa = qa[qa['file_name'] == file_name]
#print(qa)

# create log file to store results
log_file = open('ragtest/output/transcript_qa_results.txt', 'w')

for i, row in qa.iterrows():
    question = row['question']

    # run graphrag query
    command = [
        'python', '-m', 'graphrag.query',
        '--root', './ragtest_successful',
        '--method', 'global',
        row['question']
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    # print results to console
    # print(f"Question: {question}")
    # print(f"Answer: {result.stdout}")

    # save results to log file
    log_file.write(f"Question: {question}\n")
    log_file.write(f"Answer: {result.stdout}")
    log_file.write('-'*50 + '\n')
