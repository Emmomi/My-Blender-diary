import sys
markdown=open("Blender-diary.md",mode='a')
text=sys.argv[1]
markdown.write("\n"+str(text))

