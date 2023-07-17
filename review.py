def create_youtube_video(title,description):
	new_youtube_video = {"title": "animals","description": "scary","likes": 0,"dislikes" :0,"comments" : {}}
	return new_youtube_video 

def like(new_youtube_video):
	if "likes" in new_youtube_video:
		new_youtube_video["likes"]+=1
	return new_youtube_video

def dislike():
	if "dislikes" in new_youtube_video:
		new_youtube_video["dislikes"]+=1
	return new_youtube_video

def add_comment(new_youtube_video,username,commentText):
	new_youtube_video["comments"][username]==commentText
	return new_youtube_vide

y = create_youtube_video("baby","baby go to school")
y =like(y)  
y =dislike(y) 
y =add_comment(y,"celine","unbelieveable")

for i in range(495):
   y=like(y)	