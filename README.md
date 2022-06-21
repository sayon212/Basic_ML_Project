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
git add.
```
Check version:
```
git log
```
Commit:
```
git commit -m "any_message_here"
```