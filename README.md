# Peer Review
## Design idea
The goal of this project is to distribute N videos to M people to do the peer review work. But there are two consider points:
1. Make sure people can not review his or her own video.
2. Make sure each video must be reviewed for N times.

Here are what I do to realise the task:
1. Initialize a list called peer_review_scheme to store the result. For each element(index i) of peer_review_scheme list:
        peer_review_scheme[i]= a list of videos people i should review
2. Using get_one_video_randomly function to pick one video randomely everytime from the total M videos of M people.
3. Do the following to the video picked in step 2(generate_scheme method):
Loop through the peer_review_scheme list, if people index is not equal to video index(make sure people can not review his or her own video) and the total number of videos in the video list for this people is less than N, that means we could distribute this video to this people. Stop the Loop through for this video until it has been distributed to N people(make sure each video must be reviewed for N times).
4. Repeat step2 and step3 until all the video is distributed.
5. In order to prevent the dead lock(very rare), I use a function called get_scheme to check the result. If the result list peer_review_scheme is None, that means dead loop happens. Then clean the peer_review_scheme list and try generate_scheme method again until we get the right result.

## How to install and run
1. Clone git repo to local
2. cd local path to the repo on local

Run following command:  
 ```sh
$ pip install -r requirement.txt
$ FLASK_APP=route.py flask run
```
open http://127.0.0.1:5000/homepage in browser.

Also I deployed to heroku: open  https://peer-review-daisy.herokuapp.com/
# Time complexity
For each video, we do at most N+1 search work(if video index equals to people index, we skip this people and keep searching). So the total time complexity is :
      a)Best time(No skip happens, for each video, we do N times search work): O(N*M)
      b)worst time(For each video, we skip once, we do N+1 times search work): O((N+1)*M)
But as mentioned, dead loop may happen. If we consider the dead lock, time complexity is constant times(constant times = times we pepeat in order to get right result) the time complexity in normal condition(No dead loop happens). 

# Space complexity
we use a list[list] to store the result, so the space complexity should be N*M

# How to improve
Owing to time constraints， I only finished the basis part of this project. But there are still a lot to improve:
1. A lot of test work.
2. Add return button to homepage page after each submit. 
3. A more beautiful UI.
4. Allow people to login.

