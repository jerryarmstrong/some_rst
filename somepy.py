import pandas as pd
import os
from git import Repo
import datetime
import glob
index_rst = """"""
# Path to the local git repository
for repo in glob.glob('/tmp/repos/x/*'):
    repo_path = os.path.join(os.getcwd(), repo)

    # Create a Repo object
    repo = Repo(repo_path)

    # Create an empty DataFrame
    columns = ['file', 'loc', 'ext', 'last_edit_date', 'contents']
    
    # Iterate through all the files in the repository
    for file in repo.tree().traverse():
        df = pd.DataFrame(columns=columns)

        if file.type == 'blob':
            file_path = file.path
            extension = os.path.splitext(file_path)[1]
            print(file_path)
            extensions = ['.py', '.js', '.tsx', '.ts', '.rs', '.md', '.scala', '.java']
            if extension in extensions:
                content = file.data_stream.read().decode('utf-8')
                loc = len(content.splitlines())

                # Get the last commit that modified this file
                commits = list(repo.iter_commits(paths=file_path, max_count=1))
                if commits:
                    last_edit_date = datetime.datetime.utcfromtimestamp(commits[0].committed_date).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    last_edit_date = 'N/A'

                # Add the information to the DataFrame
                df = pd.concat([df,pd.DataFrame({
                    'file': file_path,
                    'loc': loc,
                    'ext': extension,
                    'last_edit_date': last_edit_date,
                    'contents': content
                }, index=[len(df)])], ignore_index=True)
                # link to file_path in rst as :ref: 
                index_rst += f""" `Stack Overflow home <""" + file_path + """>`_ \n\n"""
                
                index_rst += f"""{'=' * len(file_path)} \n\n"""
                index_rst += f"""Last edited: {last_edit_date} \n\n"""
                index_rst += f""".. code-block:: {extension.replace('.', '')} \n\n"""
                

with open('docs/index.rst', 'w') as file:
    file.write(index_rst)