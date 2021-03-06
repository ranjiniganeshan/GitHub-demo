from github import Github
import csv

# or using an access token
token  = input("Enter the Github token: ")
g = Github(token)
org = input("Enter the name of the Organisation: ")
f = open('names.csv', 'w')



for repo in g.get_organization(org).get_repos():
	print(repo.name)
	if not (repo.has_wiki and repo.has_issues and repo.has_projects and repo.allow_merge_commit and repo.allow_rebase_merge):
		print("Feautures are not set for this repo")
	else:
		print("Feautes are set please remove those")
	# repo1 = org.get_repos(repo.name)
	for team in repo.get_teams():
		print(team.name)
		if team.name in ['cobalt','Cobalt Team']:
			print("Cobalt team is added to repo")
		else:
			print("Cobalt team is not added to repo,please add")
		for branch in repo.get_branches():
			if not branch.name.startswith('CBLT'):
				print(repo.name)
				print("\t", branch.name)
				b = repo.get_branch(branch.name)
				if b.protected:
					print("Repo is --> ",repo.name, "| Branch --> ", b.name, " (protected)")
					x=b.get_required_status_checks()
					print(x.strict)
					y=b.get_required_pull_request_reviews()
					print(y.require_code_owner_reviews)
					print(y.dismiss_stale_reviews)
				    if x.strict and y.require_code_owner_reviews and y.dismiss_stale_reviews
                        print("This branch is as per the guidelines")
with f:
    
    fnames = ["Org Name", "Repo Name", "Wikis", ]
    writer = csv.DictWriter(f, fieldnames=fnames)
writer.writeheader()
writer.writerow({'Org Name' : org, 'Repo Name': repo.name, 'Wikis': repo.has_wiki })
