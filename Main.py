from Social_Media_Username_Finder.Roblox import Roblox
from Social_Media_Username_Finder.Instagram import Instagram
from Social_Media_Username_Finder.X import X
from Social_Media_Username_Finder.Facebook import Facebook


username = str(input("Enter a username: "))
Roblox.get_Roblox_Username(username)
Instagram.get_Instagram_Username(username)
X.get_X_Username(username)
Facebook.get_Facebook_Username(username)


# ToDo
# - Add option to choose whice category to search in
# - Make better folder structure