#!/bin/bash

## Get the list of all the projects from Bitbucket account across all the pages
get_total_project_list () {
   	start=0
   	total_project_list=()
   	is_last_page=false
	while ! $is_last_page
	do
		response=$(curl -k -u $u -X GET -H "Content-type: application/json" $bitbucket_url/rest/api/1.0/projects?start=$start) 2>&1
		is_last_page=$(echo "${response}" | tr '\r\n' ' ' | jq '.isLastPage')
		partial_project_list=$(echo "${response}" | tr '\r\n' ' ' | jq '.values[].key' | sed -e 's/"//g')
		start=$(echo "${response}" | tr '\r\n' ' ' | jq '.nextPageStart')
		total_project_list=("${total_project_list[@]}" "${partial_project_list[@]}")
	done
}

