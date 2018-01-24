import os


giturl="https://github.com/Ticketing/NeConfigurations"
def getGitHubJar(giturl):
	authUrl=giturl[:8]+"vijaymagetone:7cf87497daa4c41b863099af464575059d655e64@"+giturl[8:]
	print authUrl
	os.system("git clone "+authUrl +" ./test")





getGitHubJar(giturl)
