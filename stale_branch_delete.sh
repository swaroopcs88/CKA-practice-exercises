#!/bin/bash
##
# Script to delete remote git branches
##
# Fetch the remote resources
git fetch
# Loop through all remote merged branches
for branch in $(git branch --merged | grep -v HEAD | grep -v develop | grep -v master | grep -v master | sed /\*/d); do
        if [ -z "$(git log -1 --since='Jun 15, 2022' -s ${branch})" ]; then
                echo -e `git show --format="%ci %cr %an" ${branch} | head -n 1` \\t$branch
                remote_branch=$(echo ${branch} | sed 's#origin/##' )
		git push --set-upstream origin copy_all_branches
		git clone -b ${remote_branch} git@github.com:swaroopcs88/copy_all_branches.git
                # To delete the branches uncomment the bellow git delete command
                # git branch -D ${remote_branch}
        fi
done
