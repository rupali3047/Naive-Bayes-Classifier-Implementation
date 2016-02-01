from array import *
import Tkinter
import random
files=[]
vocab=[]
liker=[]
final_prob_likes=[]
final_prob_dislikes=[]
disliker=[]
x=0
inserted=0
tmp=0.0
v_likes=0.0
v_dislikes=0.0
num_likes=0.0
num_dislikes=0.0
num_docs=0.0
for y in xrange(3,21):
	
	a=random.randrange(1,2+1)
	if(a==2):
		ins=str(y)+".txt"
		files.insert(x,ins)
		z=str("DISLIKE")
		files.insert(x+1,z)
		num_likes=num_likes+1
		
	elif(a==1):
		ins=str(y)+".txt"
		files.insert(x,ins)
		z=str("LIKE")
		files.insert(x+1,z)
		num_dislikes=num_dislikes+1
		
	x=x+2

print num_likes
print num_dislikes

print len(vocab)
for y in xrange(0,2):
	with open(files[y*2],'r') as f:
		for line in f:
			for word in line.split():
				word1=str(word)
				count=len(vocab)
				for loop in xrange(0,len(vocab)/2):
					if(vocab[loop*2]==word1):
						vocab[(loop*2)+1]=vocab[(loop*2)+1]+1
						inserted=1
				if(inserted==0):
					vocab.insert(len(vocab),word1)
					vocab.insert(len(vocab)+1,1)
				inserted=0
				if(files[(y*2)+1]=="LIKE"):
					for loop in xrange(0,len(liker)/2):
						if(liker[loop*2]==word1):
							liker[(loop*2)+1]=liker[(loop*2)+1]+1
							inserted=1
					if(inserted==0):
						liker.insert(len(liker),word1)
						liker.insert(len(liker)+1,1)
					inserted=0
				elif(files[(y*2)+1]=="DISLIKE"):
					for loop in xrange(0,len(disliker)/2):
						if(disliker[loop*2]==word1):
							disliker[(loop*2)+1]=disliker[(loop*2)+1]+1
							inserted=1
					if(inserted==0):
						disliker.insert(len(disliker),word1)
						disliker.insert(len(disliker)+1,1)
					inserted=0
				
				#print word1
				#print files[y*2]
print files
#print vocab
#print "likers now"
#print liker
#print "dislikers now"
#print disliker
num_vocab=len(vocab)/2
num_docs=num_likes+num_dislikes
prob_likes=float(num_likes/num_docs)
prob_dislikes=float(num_dislikes/num_docs)
print prob_likes
print prob_dislikes

num_elements_likes=len(liker)/2
num_elements_dislikes=len(disliker)/2
print num_elements_likes
print num_elements_dislikes

for y in xrange(0,len(vocab)/2):
	word2=vocab[y*2]
	for x in xrange(0,len(liker)/2):
		if(liker[x*2]==word2):
			final_prob_likes.insert(len(final_prob_likes),word2)
			final_prob_likes.insert(len(final_prob_likes)+1,liker[(x*2)+1])
			tmp=float(float(liker[(x*2)+1]+1)/float(num_elements_likes+num_vocab))
			final_prob_likes.insert(len(final_prob_likes)+2,tmp)
	for x in xrange(0,len(disliker)/2):
		if(disliker[x*2]==word2):
			final_prob_dislikes.insert(len(final_prob_dislikes),word2)
			final_prob_dislikes.insert(len(final_prob_dislikes)+1,disliker[(x*2)+1])
			tmp=float(float(disliker[(x*2)+1]+1)/float(num_elements_dislikes+num_vocab))
			final_prob_dislikes.insert(len(final_prob_dislikes)+2,tmp)
print "Final Prob likes now :-"
print final_prob_likes
print "Final Prob dislikes now :-"
print final_prob_dislikes

# Training Completed




fname=raw_input("Enter The Filename to classify :- ")
v_likes=float(prob_likes)
v_dislikes=float(prob_dislikes)

with open(fname,'r') as f:
		for line in f:
			for word in line.split():
				word3=str(word)
				for x in xrange(0,len(final_prob_likes)):
					if(word3==final_prob_likes[x]):
						tmp=final_prob_likes[x+2]
						v_likes=float(v_likes*tmp)
				for x in xrange(0,len(final_prob_dislikes)):
					if(word3==final_prob_dislikes[x]):
						tmp=final_prob_dislikes[x+2]
						v_dislikes=float(v_dislikes*tmp)

print "v_likes = "
print v_likes
print "v_dislikes = "
print v_dislikes
if(v_likes>=v_dislikes):
	print "This file is classified as LIKE"
elif(v_likes<v_dislikes):
	print "This file is classified as DISLIKE"
