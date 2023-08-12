import pandas as pd
import os
from git import Repo
import datetime
import glob
index_rst = """"""
# Path to the local git repository
for repo in glob.glob('/tmp/repos/*'):
    repo_path = os.path.join(os.getcwd(), repo)
    
    # Create a Repo object
    repo = Repo(repo_path)

    # Create an empty DataFrame
    columns = ['file', 'loc', 'ext', 'last_edit_date', 'contents']
    try:
        # Iterate through all the files in the repository
        for file in repo.tree().traverse():
            df = pd.DataFrame(columns=columns)

            if file.type == 'blob':
                file_path = file.path
                extension = os.path.splitext(file_path)[1]
                
                extensions = ['.py', '.js', '.tsx', '.ts', '.rs', '.md', '.scala', '.java']
                if extension in extensions:
                    print(file_path)
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

                    # Write the contents to an RST file
                    rst_path = 'docs/'+repo_path.split('/')[-1]+'/'+os.path.splitext(file_path)[0] + '.rst'
                    # Get the directory name
                    dir_path = os.path.dirname(rst_path)

                    # Create the directory if it doesn't exist
                    if not os.path.exists(dir_path) and len(dir_path) > 0:
                        print(dir_path)
                        os.makedirs(dir_path)
                    try:
                        with open(rst_path, 'w') as rst_file:
                            rst_file.write(f"{file_path}\n{'='*len(file_path)}\n\n")
                            rst_file.write(f"Last edited: {last_edit_date}\n\n")
                            rst_file.write(f"Contents:\n\n")
                            rst_file.write(f".. code-block:: {extension[1:]}\n\n")
                            rst_file.write(f"    {content}\n\n")
                    except:
                        abc=123
                    index_rst += f""" `{file_path} <""" + rst_path + """.html>`_ \n\n"""
    except Exception as e:
        print(e)            
                

with open('docs/index.rst', 'w') as file:
    file.write(index_rst)