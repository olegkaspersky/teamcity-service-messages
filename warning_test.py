print("##teamcity[compilationStarted compiler='<compiler name>']")
print("##teamcity[message text='compiler output']")
print("##teamcity[message text='compiler output']")
print("##teamcity[message text='warning message' status='WARNING']")
print("##teamcity[inspectionType id='test' name='test inspection' description='reports inspection warnings' category='test']")
print("##teamcity[inspection typeId='test' message='inspection instance description' file='warning filename' line='111' additional attribute='additional attribute']")
print("##teamcity[compilationFinished compiler='<compiler name>']")
