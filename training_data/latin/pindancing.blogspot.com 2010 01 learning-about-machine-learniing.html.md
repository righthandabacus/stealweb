### Learning about Machine Learning

Bradford Cross has posted an awesome blog post (edit: removed link,
since Bradford took down the post) titled "Learning about Statistical
Learning". If you plan to work in ML, read the post, buy some of the
books and work through them.  
  
Could save you years of work if you are systematic from the beginning (I
wasn't), especially if you are self taught (I am).  
  
  
I work on different domains (Robotics/Computer Vision/Simulation) from
Bradford and so have a different list of books. Please read Bradford's
lists first. This is a supplement to his awesome post rather than a
replacement.  
  
I assume you are a good developer and you have a solid grip on algorithm
analysis etc.(though, that said, see reccomendations for Discrete Math
books below)  
  
The first step..  
  
Learn proof techniques \*first\*. You'll make no serious progress till
you do. The best book is  
  
Velleman's ["How to Prove
It"](http://www.amazon.com/How-Prove-Structured-Daniel-Velleman/dp/0521675995/)
- reccomended by Bradford but I am repeating it here because this is
***critical***.  
  
Mathematics  
  
In my experience you need to be somewhat comfortable with 6 branches of
Mathematics before you can tackle ML. Imo, best to take a year and get
these right before venturing into ML proper. (I know, it sounds awfully
boring. I wasted a lot of time trying to shorten this step. In this
case, the long way is the real shortcut)  
  
(1) Calculus - best "lite" book -
[Calculus](http://ocw.mit.edu/ans7870/resources/Strang/strangtext.htm)
by Strang (free download) ,  
  
best "heavy" books -
[Calculus](http://www.amazon.com/Calculus-Michael-Spivak/dp/0914098918/)
by Spivak,[Principles of Mathematical
Analysis](http://www.amazon.com/Principles-Mathematical-Analysis-Third-Walter/dp/007054235X)
a.k.a "Baby Rudin"  
  
  
(2) Some book on Discrete Math (don't know what to recommend here - I
don't like Rosen's book) + a good book on say Introduction to Algorithms
by Cormen et al will do \[\*\]  
  
(3) Linear Algebra (First work through [Strang's
book](http://www.amazon.com/Introduction-Linear-Algebra-Fourth-Gilbert/dp/0980232716),
then
[Axler's](http://www.amazon.com/Linear-Algebra-Right-Sheldon-Axler/dp/0387982582))  
  
(4) Probability (Bertsekas is a good book for those with no prior exp)
and  
  
(5) Statistics (I would recommend [Devore and
Peck](http://www.amazon.com/Introduction-Statistics-Data-Analysis-Roxy/dp/0495557838/)
for the total beginner but it is a damn expensive book. So hit a library
or get a bootlegged copy to see if it suits you before buying a copy,
see brad's list for advanced stuff.)  
  
(6) Information Theory ([MacKay's
book](http://www.inference.phy.cam.ac.uk/mackay/itila/) is freely
available online)  
  
Basic AI.  
  
Brad suggests [Mitchell's
book](http://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077).  
  
I think [AIMA (3d
Edition)](http://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597)
is much better. ( I am biased. I wrote and maintained the Java code for
a long while -- children, don't do this. Java is an terrible language to
develop AI algorithms in. If you need the JVM use Scala or Clojure --
and I think it covers a lot more than Mitchell does. Take a look at
both. Pick one).  
  
  
Machine Learning.  
  
NB: you need all the linear algebra, calculus etc worked through before
you hit this point  
  
In order,  
  
["Pattern Recognition and Machine
Learning"](http://www.amazon.com/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738)
by Christopher Bishop,  
  
  
\*then\* ["Elements of Statistical
Learning"](http://www-stat.stanford.edu/~tibs/ElemStatLearn/) (free
download).  
  
Neural Networks:  
  
In order,  
  
[Neural Network
Design](http://www.amazon.com/Neural-Network-Design-Martin-Hagan/dp/0971732108/)Hagan
Demuth and Beale,  
  
[Neural Networks, A Comprehensive Foundation (2nd
edition)](http://www.amazon.com/Neural-Networks-Comprehensive-Foundation-2nd/dp/0132733501)
- By Haykin (there is a newer edition out but I don't know anything
about that, this is the one I used)  
  
and [Neural Networks for Pattern
Recognition](http://www.amazon.com/Neural-Networks-Pattern-Recognition-Christopher/dp/0198538642/)
( Bishop).  
  
At this point you are in good shape to read any papers in NN. My
reccomendations - anything by [Yann LeCun](http://yann.lecun.com/) and
[Geoffrey Hinton](http://www.cs.toronto.edu/~hinton/). Both do amazing
research.  
  
Reinforcement Learning (again this is just stuff \*I\* happened to
specialize in for various projects, so feel free to ignore)  
  
[Reinforcement Learning - An Introduction by Barto and
Sutton](http://www.amazon.com/Reinforcement-Learning-Introduction-Adaptive-Computation/dp/0262193981/)
(follow up with ["Recent Advances In reinforcement Learning"
(](http://rlai.cs.ualberta.ca/papers/barto03recent.pdf)PDF) which is an
old paper but a GREAT introduction to \*Hierarchical\* Reinforcement
learning  
  
  
[Neuro Dynamic
Programming](http://www.amazon.com/Neuro-Dynamic-Programming-Optimization-Neural-Computation/dp/1886529108/ref=sr_1_2?ie=UTF8&s=books&qid=1263575843)
by Bertsekas  
  
  
Computer Vision  
  
[Introductory Techniques for 3-D Computer
Vision](http://www.amazon.com/Introductory-Techniques-3-D-Computer-Vision/dp/0132611082/),
by Emanuele Trucco and Alessandro Verri.  
  
[An Invitation to 3-D
Vision](http://www.amazon.com/Invitation-3-D-Vision-Yi-Ma/dp/0387008934/)
by Y. Ma, S. Soatto, J. Kosecka, S.S. Sastry. (warning TOUGH!!)  
  
Robotics.  
  
I know only about the software/algorithms side of Robotics and that too
only Probabilistic Robotics. I don't know anything about hardware,
electronics or Physics.  
  
[Probabilistic Graphical Models: Principles and Techniques (Adaptive
Computation and Machine
Learning)](http://www.amazon.com/Probabilistic-Graphical-Models-Principles-Computation/dp/0262013193/)
(strictly speaking not a robotics book, but a lot of the theory in this
book is behind the algorithms in the next book  
  
[Probabilistic Robotics (Intelligent Robotics and Autonomous
Agents)](http://www.amazon.com/Probabilistic-Robotics-Intelligent-Autonomous-Agents/dp/0262201623/)by
Thrun, Burgard and Fox (trivia Thrun also wrote the Robotics chapter in
AIMA - did I tell you AIMA rocks as a first introduction to AI?)  
  
And that's all folks. Happy hacking!  
  
  
\[\*\] working though Cormen et al is a humungous task and can easily
consume a year or more of work. Something like Sally Goldman's new
Algorithm book maybe more suited to programmers.  
  
  
PS: I have been getting a lot of email asking \*how\* one should learn X
or Y. I have no idea really. The above is a list of books that worked
for me and is provided only in the spirit of "these are good books that
worked for me I don't know if they'll work for you."  
  
As to how I learned, I just read books and papers, try to understand, (a
lot of banging head against wall at this point) and try to solve
problems and code stuff. Beyond that I have no advice on how to learn
effectively etc. I am entirely self taught and have no idea how to teach
this stuff. You probably need to talk to a good prof.



