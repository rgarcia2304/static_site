# Using LLM's in education 


[< Back](../)

_"Stuff your eyes with wonder. Live as if you'd drop dead in ten seconds." - Ray Bradbury, Fahrenheit 451._

Here’s a video of me using it in action it’s kind’ve long but I think it’s useful to see what the project actually was 

![intro](/images/intro.jpg)

[video](https://www.youtube.com/watch?v=q85QM74ihVs)


## Why this is important to me 

### Side Note 

Well to be honest to all of you I wrote this a couple of months ago. I was dealing with the internal crossroads of a huge problem. The problem was that I saw people were cheating on everything yet I too fell victim to the convenience. Personally I do wrestle with LLM’s alot, especially if I don’t understand something, but damn there’s something powerful about having a ridiculous problem set question an LLM could one shot. So I built this as a sort of thought experiment to see where I could maybe think up a solution to actually be able to learn with LLMs. I enjoyed every bit of this project and hope you will maybe take a look at some of the work I’ve done, and maybe provide some feedback. This isn’t too technical as in my opinion the product was a much bigger focus. Maybe I could’ve been practicing some leetcode, to do better in my interviews earlier this year but this was way more important and fun to me. 
Enjoy, 
Rodrigo 

### Back to the main story

My father was only able to afford to get a middle school education. It stressed my whole life, the privilege it was to be somewhere where education was widely available. To let you know how serious I took education, my mom has a go to story of me coming home in the fourth grade crying because I got an F, (that would be the last F I got till college, but it was ok in college because of curves.. anyways).  To compound on top of this, over the course of my life the web has made learning more and more accessible. In my eyes education being readily available and free should be how it is. Due to me being curious I always just explored things that interested me which led me down to where I am today for better or worse. The availability of the web and having phenomenal educators have been some of the most important things in my life.

 Yet, just because something is accessible doesn’t make it useful at all. So I think now we may have the problem of too much information and too many shortcuts which are killing curiosity. One of my missions in life is to see how we can address this curiosity pandemic. 

People are completing homeworks that might historically take days in mere hours sometimes minutes. Have people gotten smarter with these new developments in tech? In my opinion no. While the LLM is a huge enabler when used properly, it's also the biggest enabler of cheating ever. The biggest issue is that at the undergrad level with some clever usage you can complete a lot of work rapidly and correctly. As a consequence of this people have stopped struggling, thinking about things deeply and reading, well because technically you don’t have to. As a byproduct of this people are getting fake confidence which only gets checked at exam time. If your class has online material you might never get found out at the undergraduate level, but eventually people will pay the consequences. This article is not here to say don’t use this amazing tool, because in my opinion it can act as an infinitely patient tutor and collaborator. On the contrary, I have been thinking deeply into how to harness this tool to get people thinking. So I made a tutoring agent that I will go into depth into the psychological approach behind the system. 

To understand how I thought about designing this, one has to understand what the point of college was about. Was it about qualifying us for a job, sure. Was it about networking with people, maybe. In my opinion college is all about teaching us how to think critically and gain general domain knowledge that will serve us useful in not only our career but all walks of life. Struggling through things and making us think very hard about problems is how people become interested and curious. Those aha moments produced when solving problems is what motivates you to do more. True reward only comes when solving hard problems. Courses are designed to be given to you in a way to build your fundamentals and enable you. Once you struggle really hard and get something you almost never forget. Thus, I want to get people excited about problem solving and understanding again because it's rewarding. The biggest crux when using an LLM is that it solves that specific problem you are doing with the context it was given, it doesn’t generally know if you understand or what you know. 

Side Note: 
My aha moment, and interest in pursuing computer science came when working for hours to build a calculator in my data structures and algorithms course using a stack. 

## Construction of project:

As a tutor the hardest part of my job is not solving the problems with students because usually I have already solved them countless times. On the contrary, it’s diagnosing what they know. Sometimes I find students themselves don’t know. My tutoring is therefore less meaningful because there’s a disconnect in understanding. To solve this I created a diagnosis agent which probes the students with questions from whatever topic they are struggling on or working on. 

## Implementation

Having thought about the problem for a while I thought about how this could fit into my tutoring center. After much collaboration and testing with fellow peers we settled on some main points into how AI could work alongside us. 

### Diagnosing Agent

![diagnosing](/images/diagnosing.jpg)


So the number 1 pain point I face as a tutor is that I have to sometimes explain foundational material that might take a while to set in for people. In my opinion learning is sometimes slow and takes a while so if I take you from 0 to 100 its A not of much use to you and B it spends precious time trying to figure out what you know and how to go up from there. So I created a diagnosing agent which asks probing questions to see what level you are at. It asks questions and determines a starting point, to start learning from. 

### Teaching Agent 

![teaching](/images/teaching.jpg)

Great, we know where to start now, let's start building you up. 
You learn math and physics by reading the theory or problem type and then actually doing it. This agent designs lessons from the lowest level of understanding you have to the highest level you would need. In terms of content creation, It’s useful to know all the material is rooted in the course syllabus for that semester and former exam materials for context of knowing what to present. We get reports of what they did, after every session so we know where students stand. 

### Quizzing Agent 

![quizzing](/images/quiz.jpg)

So given all that you have learned from the teaching agent we curate about 3-5 questions to validate mastery of the topic. I’ll never give you the direct answer, just guide you with questions about the materials. All our questions are based on the content base we have for materials. If you really don’t get it the session is escalated and a tutor comes to help. 

### Report Generation Agent

![summary](/images/summary.jpg)

We take up all we’ve learned in this session including what you knew when you started what we covered, hints, quiz results and recommendations. This all gets posted in discord for us tutors to see and proceed with. This metadata is all that gets stored in the database. 

From all the context of the lesson 

Exam Creation Agent 

![exam](/images/exam.jpg)

Cool so now students want more material to review so I created an exam review agent that allows people to pick topics they want from the course and get curated problems. To teach them how to generate their own prompts after 1 attempt I gave them the prompt I used to generate material. 

My main critique of LLM usage from what I’ve personally seen and experienced is that students use LLMs to just solve the problem. While yes, it gives very detailed explanations it’s just a snapshot and many students don’t engage with it in a way to check their understanding. 

## The human in the loop


As mentioned previously we read the results of the sessions to see how students are working through the material. From this we can make tweaks to how the LLM behaves to the student input. Also I had the different tutors all play with the system to make tweaks to functionality. Features such as a mathematical toolbox were added before launch because of this. 

Not to say we are subject matter experts on topics taught at the center but most of us have been tutoring those subjects for quite a long time. Given this we know of useful materials and topics hit in the classes. Taking this into account,  we built relevant context for the LLM. Every session the LLM reads context,  having it act as a solid base for what knowledge to pull, when generating practice material for example. 

## Shouldn’t we not trust the LLM

LLMs thrive on content it has a lot of data for. Our current course offerings of calculus 2 and physics 1, have tons of problems and solutions as they have been around for a long long time. From experience I can say with confidence that I trust the creation of content. On top of this we have all the old exams and quizzes and homeworks we pointed to as the base for the material so it should do pretty well. 

## Will this replace tutors and other resources

Well in my opinion I think an LLM can teach a lot given the right context. An LLM truly is a powerful tool in self learning, with many saying why go to class if I have an LLM. Despite this, technically you have not needed the education system or educators to learn anything for a very long time. People have been able to self teach themselves from books for years. But this isn’t a conversation about educators or anything like that. 

My goal here was just to guide the AI, and structure it in a way to be useful for students. What is important here is the idea that true mastery comes in being able to apply these teachings to non straightforward problems and explain what you did. At my tutoring center the students who I collaborate with and explain to me why and how they are doing things, when working on problems are the most successful ones. That teaching and collaboration aspect will never go away in my opinion, thus no we won’t be replaced IMO. At the end of the day we are not there to teach, we are there to reinforce concepts and collaborate. A tutors goal is to get you to be able to solve problems, not do them for you. Beyond this we curate all the material we think is useful for the LLM to know. 

## How it was used at the center


Given that a student has come to the center and does work it's offered to students to supplement their learning. Tutors generate pin codes, using a password protected admin page. Scale issues or security is not that big of an issue, as there are alerts to see who created what when on discord. After this students have a tutor defined access for a certain time frame to the actual agent. 

## Conclusion 

 The project did not get the traction I hoped because I saw that the friction was an issue. Students didn’t want to be led through things, when chatGPT or Claude provided a nicer interface, and could serve them easier. Though I introduced these barriers on purpose there is probably a difference  to put this out in front of students instead of my system, to actually get them to stay on the platform. The most important question I believe we need to answer is how do we create the necessary friction that sparks learning without introducing the frustration that leads to cheating. All these different decisions make me have tremendous respect for product managers, engineers, and all the people in the lifecycle. It's truly hard to get to a product people use and enjoy. 

Also this isn’t some engineering marvel but the problem was used to solve some huge thing I was seeing. Many times the biggest problem is people don’t know what they know. If you don’t know what you know, I have to start making assumptions that may just not work for you because LEARNING IS HARD sometimes. Due to it being hard sometimes it can be slow for people to work with. 

Yes, I know claude or chatGPT can do what I did but that was never the point. I use chatGPT and claude alot actually. I think the big caveat in my usage is I try to not move forward if I don’t understand. This doesn’t give you the lever to do that because the context space we are in is education. If you can master stuff you will be capable of solving harder problems. 



There’s a big talk about who the winners and losers of this AI wave will be. Many say the ones who know how to use it will be the big winners. It’s very true in my opinion too as you can learn things rapidly and build crazy things. The big losers though are those who have taken the shortcuts though. I believe that humans will continue to solve the hardest problems on Earth, but to do that we need to be able to get them thinking again. 

We talked about a lot but I do at once want to bring gravity to the situation. People are graduating by doing almost nothing. I know people with top marks who cheated their way through school. I know almost everybody cheated at some point. We don’t pay the price for this now but we will eventually in my opinion. So how do we work in this new era? Well, I have my opinions but you do need to have really strong fundamentals. We have fancy calculators that crunch crazy numbers but you got to know the purpose behind what you're doing. When I worked on concrete they always said before you touch any machine, you got to know the very most basic thing well which is how to rake :) 

It’s always fun taking a stab at problems in this case designing the site, the approach, the materials, the engineering tradeoffs etc. So while this is sunsetted I am extremely grateful for everyone who used, helped create, and test this idea with me! 

## Technical implementation: 
Granted I don’t know who will read this but if you want to know what I did to build this, reach out to me on linkedIN or email. 

