# my shelfPlayer project


![demo](/images/demo.gif)
Checkout the github: repo
[shelfPlayer](https://www.github.com/rgarcia2304/shelfPlayer)


So I believe it or not I don't remember that much of the analog world. I can vaguely remember the cassette tapes and stereos but I never really used it much. I grew up alongside computers and phones to play my media. 

They say you yearn for what you don't have and in this case its true. Simply put, I don’t want to interface with UI’s or cover art. I just want to put in some tape with the Jams I like and have it play. 

So I built it…. on my computer

## How this came to be 

For much of my undergrad I always tried to better my focus, whether it be studying in specific sports, pomodoro, or being with classmates etc…. But one of my favorite things was going on youtube and watching James Scholz to study with him.. Yes I do have friends btw but with this one I didn’t have to interact with him, and he played nice music with his pomodoro.

But there remained an issue I didn’t want to go on Youtube and be tempted by the latest video or documentary that was curated to me. Plus I didn’t particularly like having to go on youtube  and see James for the 20th session in a row in the same location, studying with me. So I thought, "Wouldn't it be badass if I made some type of player?" 

And then I saw this sony walkman ad. And I knew that's what I needed. 

![walkman](/images/walkman.png)

[walkman video](https://www.youtube.com/watch?v=7lipckhgG5g)

I can’t even state how cool this machinery is to me. 

## The idea 

So I knew I wanted to be able to make tapes from music I had, add a pomodoro timer on it and put some cool UI. 

So I did just that 

At this point in my life I was working a lot with Go and since I’m a nerd I made it a cli tool, so I wouldn’t have to go onto any browser. 

There were a few primary things that needed to be made in order for this to work.

I knew I needed a player inspired by the walkman

Then I was going to need a tape to put into that walkman

I knew I wanted a concept where you would browse off your shelf the tapes you wanted to play. 

## The technical stuff

So as I mentioned this was written in GO. The TUI is built on top of Bubble Tea, which uses an Elm-inspired architecture. Elm just means that we define a model, an update function and a view function. Then Bubble Tea handles the event loop. 

To play audio I used a beep, which decoded mp3 files and streams them to the system audio device. When a track finishes, beep fires a callback from its goroutine (which is like a thread in go, kind’ve not exactly the same thing), and sends a message to the TUI to advance it automatically. 

To make tapes I used yt-dlp. When you look up a track, it uses yt-dlp and parses the results. When you pick one, it downloads it as an mp3 in the background while you keep browsing. Tapes are stored as a folder of MP3s and a tape.json metadata file. You can also put in any tape, or music you own in here too given that it’s an mp3 file. Just read the README if you want to do this. 

Now this was inspired by studying, so I added some pomodoro to it too. It runs on a second goroutine alongside the animations. Whenever we are on break I slow down the spinning reels so you can tell when you are on break. 

The hardest part of the project was creating the design in the terminal. To get the wheels spinning, I had to take 20-30 min breaks, in which stuff still didn’t look right. In the end the way it came to looking at what it does now, having to use math to render the main spectacle. Every single reel was mathematically generated using polar coordinates. So for every character in the grid, compute the distance and angle from the center of the reel. The rim characters are chosen based on the tangent direction at that point on the circle, so they follow the arc. The spokes are rendered by checking if a cell falls within a narrow angular slice of each spokes current rotation angle. 


## A walkthrough the Actual Player

If you want to see how to make Tapes read through the ReadMe
[shelfPlayer](https://www.github.com/rgarcia2304/shelfPlayer)


Thanks for sticking with me through the technical talk here’s the player! 
For this I’m going to walk you 

So when you launch the player you see this

![shelfPlayer1](/images/sp1.png)

Here is your shelf of tapes, that you have made, and you follow the key bindings, to navigate.

I enter my disco track 

![shelfPlayer2](/images/sp2.png)

And then you hit play

![shelfPlayer3](/images/sp3.png)

And boom there you have your own CLI shelf player. 

## Conclusion 

This was a really fun project and I learned a lot about just how hard it is to design a nice CLI application. If you want to try it yourself or see what this is about. 

Now I don’t get baited to watch youtube documentaries or get distracted by my apple music, I just spin this up, in the corner and get to work or don’t … 

-

Cheers

