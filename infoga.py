git config --global user.name "YourGitHubUsername"
git config --global user.email "YourGitHubEmail"

git clone https://github.com/atalshah/NumberInfo.git
cd NumberInfo
mv ../number_info.py .
git add .
git commit -m "First commit - Number Info Tool"
git push origin main