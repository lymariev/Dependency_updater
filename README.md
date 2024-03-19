# Dependency updater
### Install and activate venv
```
python3 -m venv ./venv
. venv/bin/activate
```
### Install requirements 
```
pip install -r requirements.txt
```

To use the script you need to have a repository on Bitbucket with `package.json` file in the root directory.  
Also you need to get access token of this repository.  
Receive a token for your repository by the link - `https://bitbucket.org/<workspace>/<repository>/admin/access-tokens`

### Running a script via the console
```
python src/update_dependency.py <dependency-name> <dependency-version> <bitbucket-workspace> <bitbucket-repository> <bitbucket-token>
```
