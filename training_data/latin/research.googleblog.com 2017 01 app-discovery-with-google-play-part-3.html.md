[App Discovery with Google Play, Part 3: Machine Learning to Fight Spam and Abuse at Scale](https://research.googleblog.com/2017/01/app-discovery-with-google-play-part-3.html)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Monday, January 30, 2017
Posted by Hsu-Chieh Lee, Xing Chen, Software Engineers, and Qian An,
Analyst  
  
  
*In [Part
1](https://research.googleblog.com/2016/11/app-discovery-with-google-play-part-1.html)
and [Part
2](https://research.googleblog.com/2016/12/app-discovery-with-google-play-part-2.html)
of this series on app discovery, we discussed using machine learning to
gain a deeper understanding of the topics associated with an app, and a
deep learning framework to provide personalized recommendations. In this
post, we discuss a machine learning approach to fight spam and abuse on
apps section of the Google Play Store, making it a safe and trusted app
platform for more than a billion Android users.*  
  
With apps becoming an increasingly important part of people’s
professional and personal lives, we realize that it is critical to make
sure that 1) the apps found on Google Play are safe, and 2) the
information presented to you about the apps is both authentic and
unbiased. With more than 1 million apps in our catalog, and a
significant number of new apps introduced everyday, we needed to develop
scalable methods to identify bad actors accurately and swiftly. To
tackle this problem, we take a two-pronged approach, both employing
various machine learning techniques to help fight against spam and abuse
at scale.  
  
**Identifying and blocking ‘bad’ apps from entering Google Play
platform**  
  
As mentioned in [Google Play Developer
Policy](https://play.google.com/about/developer-content-policy/), we
don’t allow listing of malicious, offensive, or illegal apps. Despite
such policy, there are always a small number of bad actors who attempt
to publish apps that prey on users. Finding the apps that violate our
policy among the vast app catalog is not a trivial problem, especially
when there are tens of thousands of apps being submitted each day. This
is why we embraced machine learning techniques in assessing policy
violations and potential risks an app may pose to its potential users.  
  
We use various techniques such as text analysis with word embedding with
large probabilistic networks, image understanding with Google Brain, and
static and dynamic analysis of the APK binary. These individual
techniques are aimed to detect specific violations (e.g., restricted
content, privacy and security, intellectual property, user deception),
in a more systematic and reliable way compared to manual reviews. Apps
that are flagged by our algorithms either gets sent back to the
developers for addressing the detected issues, or are ‘quarantined’
until we can verify its safety and/or clears it of potential violations.
Because of this app review process combining analyses by human experts
and algorithms, developers can take necessary actions (e.g., iterate or
publish) within a few hours of app submission.  
<table>
<tbody>
<tr class="odd">
<td><a href="https://3.bp.blogspot.com/-WpRAutHMDhg/WI-mH5grBUI/AAAAAAAABfw/LMW2Alp9FvENS-9-36yJ3dX7Z29BoybnwCLcB/s1600/image00.png"><img src="https://3.bp.blogspot.com/-WpRAutHMDhg/WI-mH5grBUI/AAAAAAAABfw/LMW2Alp9FvENS-9-36yJ3dX7Z29BoybnwCLcB/s640/image00.png" /></a></td>
</tr>
<tr class="even">
<td>Visualization of word embedding of samples of offensive content policy violating apps (red dots) and policy compliant apps (green dots), visualized with t-SNE (<a href="https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding">t-Distributed Stochastic Neighbor Embedding</a>).</td>
</tr>
</tbody>
</table>

  
**Preventing manipulation of app ratings and rankings**  
  
While an app may itself be legitimate, some bad actors may attempt to
create fake engagements in order to manipulate an app’s ratings and
rankings. In order to provide our users with an accurate reflection of
the app’s perceived quality, we work to nullify these attempts. However,
as we place countermeasures against these efforts, the actors behind the
manipulation attempts change and adapt their behaviors to bypass our
countermeasures thereby presenting us with an [adversarial
problem](https://en.wikipedia.org/wiki/Adversarial_machine_learning).  
  
As such, instead of using a conventional supervised learning approach
(as we did in the ‘[Part
1](https://research.googleblog.com/2016/11/app-discovery-with-google-play-part-1.html)’
or ‘[Part
2](https://research.googleblog.com/2016/12/app-discovery-with-google-play-part-2.html)’
of this series, which are more ‘stationary’ problems), we needed to
develop a repeatable process that allowed us the same (if not more)
agility that bad actors have. We achieved this by using a hybrid
strategy that utilizes [unsupervised
learning](https://en.wikipedia.org/wiki/Unsupervised_learning)
techniques to generate training data which in turn feeds into a model
built on traditional [supervised
learning](https://en.wikipedia.org/wiki/Supervised_learning)
techniques.  
  
Utilizing data on interactions, transactions, and behaviors occurring on
the Google Play platform, we apply anomaly detection techniques to
identify apps that are targeted by fake engagements. For example, a
suspected app may have all its engagement originating from a single data
center, whereas an app with organic engagement will have its engagement
originating from a healthy distribution of sources.  
  
We then use these apps to isolate actors who collude or orchestrate to
manipulate ratings and rankings, who in turn are used as training data
to build a model that identifies similar actors. This model, built using
supervised learning techniques, is then used to expand coverage and
nullify fake engagements across Google Play Apps platform.  
<table>
<tbody>
<tr class="odd">
<td><a href="https://3.bp.blogspot.com/-CgxcDq6mSnM/WI-kOGKaY_I/AAAAAAAABfg/djCvj_DHn3ci4D5QZnTTWvI3zoyxQIsmwCLcB/s1600/image01.png"><img src="https://3.bp.blogspot.com/-CgxcDq6mSnM/WI-kOGKaY_I/AAAAAAAABfg/djCvj_DHn3ci4D5QZnTTWvI3zoyxQIsmwCLcB/s640/image01.png" /></a></td>
</tr>
<tr class="even">
<td>A visualization of how a model trained on known bad actors (red) expands coverage to detect similar bad actors (orange) while ignoring organic users (blue).</td>
</tr>
</tbody>
</table>

  
We strive to make Google Play the best platform for both developers and
users, by enabling fast publication while not compromising user safety.
The machine learning capabilities mentioned above helped us achieve
both, and we’ll continue to innovate on these techniques to ensure we
keep our users safe from spam and abuse.  
  
**Acknowledgements**  
This work was done in close collaboration with Yang Zhang, Zhikun Wang,
Gengxin Miao, Liam MacDermed, Dev Manuel, Daniel Peddity, Yi Li, Kazushi
Nagayama, Sid Chahar, and Xinyu Cheng.

Labels: [Google Play
Apps](https://research.googleblog.com/search/label/Google%20Play%20Apps)
, [Machine
Learning](https://research.googleblog.com/search/label/Machine%20Learning)



