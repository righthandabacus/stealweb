[Open sourcing the Embedding Projector: a tool for visualizing high dimensional data](https://research.googleblog.com/2016/12/open-sourcing-embedding-projector-tool.html)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Wednesday, December 07, 2016
Posted by Daniel Smilkov and the Big Picture group  
  
Recent advances in Machine Learning (ML) have shown impressive results,
with applications ranging from [image
recognition](https://research.googleblog.com/2016/08/improving-inception-and-image.html),
[language
translation](https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html),
[medical
diagnosis](https://research.googleblog.com/2016/11/deep-learning-for-detection-of-diabetic.html)
and more. With the widespread adoption of ML systems, it is increasingly
important for research scientists to be able to explore how the data is
being interpreted by the models. However, one of the main challenges in
exploring this data is that it often has hundreds or even thousands of
dimensions, requiring special tools to investigate the space.  
  
To enable a more intuitive exploration process, we are [open-sourcing
the Embedding
Projector](https://www.tensorflow.org/versions/master/how_tos/embedding_viz/index.html),
a web application for interactive visualization and analysis of
high-dimensional data recently shown as an [A.I.
Experiment](https://aiexperiments.withgoogle.com/visualizing-high-dimensional-space),
as part of [TensorFlow](https://www.tensorflow.org/). We are also
releasing a standalone version at
[projector.tensorflow.org](http://projector.tensorflow.org/), where
users can visualize their high-dimensional data without the need to
install and run TensorFlow.  
  
[![](https://2.bp.blogspot.com/-yL_425HS2ck/WEDZLk5cq0I/AAAAAAAABcI/kwy4F4Cmfi4jyG_InIiYu6F7y2-BKTXWQCLcB/s640/embedding-mnist.gif)](https://2.bp.blogspot.com/-yL_425HS2ck/WEDZLk5cq0I/AAAAAAAABcI/kwy4F4Cmfi4jyG_InIiYu6F7y2-BKTXWQCLcB/s1600/embedding-mnist.gif)  
**Exploring Embeddings**  
  
The data needed to train machine learning systems comes in a form that
computers don't immediately understand. To translate the things we
understand naturally (e.g. words, sounds, or videos) to a form that the
algorithms can process, we use
*[embeddings](https://en.wikipedia.org/wiki/Embedding)*, a mathematical
vector representation that captures different facets (dimensions) of the
data. For example, in [this language
embedding](https://opensource.googleblog.com/2013/08/learning-meaning-behind-words.html),
similar words are mapped to points that are close to each other.  
  
With the Embedding Projector, you can navigate through views of data in
either a 2D or a 3D mode, zooming, rotating, and panning using natural
click-and-drag gestures. Below is a figure showing the nearest points to
the embedding for the word “important” after training a TensorFlow model
using the [word2vec
tutorial](https://www.tensorflow.org/versions/r0.12/tutorials/word2vec/index.html).
Clicking on any point (which represents the learned embedding for a
given word) in this visualization, brings up a list of nearest points
and distances, which shows which words the algorithm has learned to be
semantically related. This type of interaction represents an important
way in which one can explore how an algorithm is performing.  
**  
**  
[![](https://2.bp.blogspot.com/-Uql7bl2KEYM/WEfQ4Kl_0YI/AAAAAAAABck/GkktuPM8KoMcMl2Tot6GzH3-NgwPNETMgCLcB/s640/image03.png)](https://2.bp.blogspot.com/-Uql7bl2KEYM/WEfQ4Kl_0YI/AAAAAAAABck/GkktuPM8KoMcMl2Tot6GzH3-NgwPNETMgCLcB/s1600/image03.png)
**Methods of Dimensionality Reduction**  
  
The Embedding Projector offers three commonly used methods of data
dimensionality reduction, which allow easier visualization of complex
data: [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis),
[t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding)
and custom linear projections.
[PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) is
often effective at exploring the internal structure of the embeddings,
revealing the most influential dimensions in the data.
[t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding),
on the other hand, is useful for exploring local neighborhoods and
finding clusters, allowing developers to make sure that an embedding
preserves the meaning in the data (e.g. in the [MNIST
dataset](https://en.wikipedia.org/wiki/MNIST_database), seeing that the
same digits are clustered together). Finally, custom linear projections
can help discover meaningful "directions" in data sets - such as the
distinction between a formal and casual tone in a language generation
model - which would allow the design of more adaptable ML systems.  
<table>
<tbody>
<tr class="odd">
<td><a href="https://1.bp.blogspot.com/-5vEgY1mh1cA/WEfRAmER3iI/AAAAAAAABco/beMK-6LNq2M37QOUGQVwXMT1B6FIMLAxgCLcB/s1600/image00.png"><img src="https://1.bp.blogspot.com/-5vEgY1mh1cA/WEfRAmER3iI/AAAAAAAABco/beMK-6LNq2M37QOUGQVwXMT1B6FIMLAxgCLcB/s640/image00.png" /></a></td>
</tr>
<tr class="even">
<td>A custom linear projection of the 100 nearest points of &quot;See attachments.&quot; onto the &quot;yes&quot; - &quot;yeah&quot; vector (“yes” is right, “yeah” is left) of a corpus of <a href="https://research.googleblog.com/2015/11/computer-respond-to-this-email.html">35k frequently used phrases in emails</a></td>
</tr>
</tbody>
</table>

The Embedding Projector [website](http://projector.tensorflow.org/)
includes a few datasets to play with. We’ve also made it easy for users
to publish and share their embeddings with others (just click on the
“Publish” button on the left pane). It is our hope that the [Embedding
Projector](https://www.tensorflow.org/versions/master/how_tos/embedding_viz/index.html)
will be a useful tool to help the research community explore and refine
their ML applications, as well as enable anyone to better understand how
ML algorithms interpret data. If you'd like to get the full details on
the Embedding Projector, you can read the paper
[here](https://arxiv.org/pdf/1611.05469v1.pdf). Have fun exploring the
world of embeddings!  
  
  

Labels: [Google
Brain](https://research.googleblog.com/search/label/Google%20Brain) ,
[Machine
Learning](https://research.googleblog.com/search/label/Machine%20Learning)
, [open
source](https://research.googleblog.com/search/label/open%20source) ,
[TensorFlow](https://research.googleblog.com/search/label/TensorFlow) ,
[Visualization](https://research.googleblog.com/search/label/Visualization)



