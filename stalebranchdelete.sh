#!/bin/bash
##
# Script to delete remote git branches
##
# Fetch the remote resources
git fetch
# Loop through all remote merged branches
for branch in $(git branch --all | grep '^\s*remotes' | egrep --invert-match '(:?HEAD|master)$'); do
    git branch --track "${branch##*/}" "$branch"
    done	
    		#echo -e `git show --format="%ci %cr %an" ${branch} | head -n 1` \\t$branch
                #remote_branch=$(echo ${branch} | sed 's#origin/##' )
		#echo remote_branch
                # To delete the branches uncomment the bellow git delete command
                # git branch -D ${remote_branch}
        
