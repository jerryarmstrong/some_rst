# list all repos in a github user

import github 

g = github.Github()
user = "metaplex-foundation"
for repo in g.get_user(user).get_repos():
    print('git clone https://github.com/' + user + '/' + repo.name + ' --depth 1')
  
user = "coral-labs"
for repo in g.get_user(user).get_repos():
    print('git clone https://github.com/' + user + '/' + repo.name + ' --depth 1')
  