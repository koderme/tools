#!/usr/bin/bash
show_github_repo()
{
		echo "# tools" >> README.md
		echo git init
		echo git add README.md
		echo git commit -m "first commit"
		echo git remote add origin https://github.com/koderme/tools.git
		echo git push -u origin master
}

show_github_repo
