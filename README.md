# Setup
### 1. Check if conda is present in VSCode terminal by rinning the following in vscode terminal

```
conda --version
```
If not present then add path of conda to windows environment variables

### 2. Create conda environment named venv_basic_ml
```
conda create -p <env_name> python==<version> -y
```
If there is proxy or firewall error then from anaconda3\Library\bin copy below files and paste them in anaconda3/DLLs:
-   libcrypto-1_1-x64.dll
-   libssl-1_1-x64.dll

### 3. Activate the environment
```
conda activate <env_name>\
```
### 4. Create requirements.txt file and write required libraries and install it
```
pip -r install requirements.txt
```
### 5. Create Python app
### 6. To ignore file or folder in Git add the file or foldername in gitignore
### 7. Git useful commands
Check status:
```
git status
```
Add files:
```
git add .
```
Check version:
```
git log
```
Commit:
```
git commit -m "any_message_here"
```
Check remote url:
```
git remote -v
```
Push latest commit to Git: 
```
git push origin main
```
origin is variable that stores repo url link
### 8. Steps for Git:
- Git add
- Git commit
- This commit happend in local git repo
- Send latest commit to Git

### 9. CI/CD
- Heroku Account Name
- Heroku API Key
- Heroku app

### 10. Create Docker File
- Install python 3.8
- Specify files and folders we dont want in .dockerignore
- Copy required files from current folder "." to app folder which will be present
by default in docker
- Change current drectory to app folder
- Install libraries using pip install -r requirements.txt
- Expose a port
- Form IP address and run the app using gunicorn

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

CMD = to execute the gunicorn command.

guicorn = to run the command.

bind = 0.0.0.0:PORT = ip address with port.

first app = python file name.

second app = application name.

### 11. Create Docker Image
```
docker build -t <image_name>:<tag_name> <location_of_docker_file>
```
Use . as location for current directory

To list docker images:
```
docker images
```
### 12. Run Docker Image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```
Check running container
```
docker ps
```
Stop Docker Image:
```
docker stop <container_id>
```
### 13. Local Testing done
### 14. Create folder structure .github\workflows\main.yaml
### 15. Add yaml template which is a standard file
### 16. Push Latest Code to Git
### 17. Create 3 secrets - Email, API Key and App name in Github with exact same names as in yaml
### 18. At runtime the yaml file will take these secrets and create the release to Heroku