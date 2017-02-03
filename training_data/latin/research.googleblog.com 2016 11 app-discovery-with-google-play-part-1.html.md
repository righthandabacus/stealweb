[App Discovery with Google Play, Part 1: Understanding Topics](https://research.googleblog.com/2016/11/app-discovery-with-google-play-part-1.html)
--------------------------------------------------------------------------------------------------------------------------------------------------

Tuesday, November 08, 2016
Posted by Malay Haldar, Matt MacMahon, Neha Jha and Raj Arasu, Software
Engineers  
  
Every month, more than a billion users come to Google Play to download
apps for their mobile devices. While some are looking for specific apps,
like Snapchat, others come with only a broad notion of what they are
interested in, like “*horror games*” or “*selfie apps*”. These broad
searches by topic represent nearly half of the queries in Play Store, so
it’s critical to find the most relevant apps.  
  
Searches by topic require more than simply indexing apps by query terms;
they require an *understanding* of the topics associated with an app.
Machine learning approaches have been applied to similar problems, but
success heavily depends on the number of training examples to learn
about a topic. While for some popular topics such as “*social
networking*” we had many labeled apps to learn from, the majority of
topics had only a handful of examples. Our challenge was to learn from a
very limited number of training examples and scale to millions of apps
across thousands of topics, forcing us to adapt our machine learning
techniques.  
  
Our initial attempt was to build a [deep neural
network](https://en.wikipedia.org/wiki/Deep_learning) (DNN) trained to
predict topics for an app based on words and phrases from the app title
and description. For example, if the app description mentioned
“*frightening*”, “*very scary*”, and “*fear*” then associate the
“*horror game*” topic with it. However, given the learning capacity of
DNNs, it completely “memorized” the topics for the apps in our small
training data and failed to generalize to new apps it hadn’t seen
before.  
  
To generalize effectively, we needed a much larger dataset to train on,
so we turned to how people learn as inspiration. In contrast to DNNs,
human beings need much less training data. For example, you would likely
need to see very few “*horror game*” app descriptions before learning
how to generalize and associate new apps to that genre. Just by knowing
the language describing the apps, people can correctly infer topics from
even a few examples.  
  
To emulate this, we tried a very rough approximation of this
language-centric learning. We trained a neural network to learn how
language was used to describe apps. We built a [Skip-gram
model](https://www.tensorflow.org/versions/r0.8/tutorials/word2vec/index.html#the-skip-gram-model),
where the neural network attempts to predict the words around a given
word, for example “*share*” given “*photo*”. The neural network encodes
its knowledge as vectors of floating point numbers, referred to as
*embeddings*. These embeddings were used to train another model called a
*classifier*, capable of distinguishing which topics applied to an app.
We now needed much less training data to learn about app topics, due to
the large amount of learning already done with Skip-gram.  
  
While this architecture generalized well for popular topics like
“*social networking*”, we ran into a new problem for more niche topics
like “*selfie*”. The single classifier built to predict all the topics
together focused most of its learning on the popular topics, ignoring
the errors it made on the less common ones. To solve this problem we
built a separate classifier for each topic and tuned them in
isolation.  
  
This architecture produced reasonable results, but would still sometimes
overgeneralize. For instance, it might associate *Facebook* with
“*dating*” or *Plants vs Zombies* with “*educational games*”. To produce
more precise classifiers, we needed higher volume and quality of
training data. We treated the system described above as a coarse
classifier that pruned down every possible {app, topic} pair, numbering
in billions, to a more manageable list of {app, topic} pairs of
interest. We built a pipeline to have human raters evaluate the
classifier output and fed consensus results back as training data. This
process allowed us to bootstrap from our existing system, giving us a
path to steadily improve classifier performance.  
  
[![](https://4.bp.blogspot.com/-ysKil48TeE8/WCIPiiLzrzI/AAAAAAAABX8/uYqpeRJ-4fMV40A29eQ-lKdpGlOU1EQgQCLcB/s640/image00.png)](https://4.bp.blogspot.com/-ysKil48TeE8/WCIPiiLzrzI/AAAAAAAABX8/uYqpeRJ-4fMV40A29eQ-lKdpGlOU1EQgQCLcB/s1600/image00.png)  
To evaluate {app, topic} pairs by human raters, we asked them questions
of the form, “*To what extent is topic X related to app Y?*” Multiple
raters received the same question and independently selected answers on
a rating scale to indicate if the topic was “important” for the app,
“somewhat related”, or completely “off-topic”. Our initial evaluations
showed a high level of disagreement amongst the raters. Diving deeper,
we identified several causes of disagreement: vague guidelines for
answer selection, insufficient rater training, evaluating broad topics
like “*computer files*” and “*game physics*” that applied to most apps
or games. Tackling these issues led to significant gains in rater
agreement. Asking raters to choose an explicit reason for their answer
from a curated list further improved reliability. Despite the
improvements, we sometimes still have to “agree to disagree” and
currently discard answers where raters fail to reach consensus.  
  
These app topic classifiers enable search and discovery features in the
[Google Play Apps store](https://play.google.com/store/apps?hl=en). The
current system helps provide relevant results to our users, but we are
constantly exploring new ways to improve the system, through additional
signals, architectural improvements and new algorithms. In Part 2 of
this series, we will discuss how to personalize the app discovery
experience for users.  
  
**Acknowledgments**  
This work was done within the Google Play team in close collaboration
with Liadan O'Callaghan, Yuhua Zhu, Mark Taylor and Michael Watson.  
  
  

Labels: [Google Play
Apps](https://research.googleblog.com/search/label/Google%20Play%20Apps)
, [Machine
Learning](https://research.googleblog.com/search/label/Machine%20Learning)
, [Neural
Networks](https://research.googleblog.com/search/label/Neural%20Networks)



