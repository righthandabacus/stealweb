[Hyperbolicity of the curve graph: the proof from The Book](https://alexsisto.wordpress.com/2013/02/08/hyperbolicity-of-the-curve-graph-the-proof-from-the-book/)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Posted on [February 8,
2013](https://alexsisto.wordpress.com/2013/02/08/hyperbolicity-of-the-curve-graph-the-proof-from-the-book/)
by [Alex Sisto](https://alexsisto.wordpress.com/author/alexsisto/)

In this post I’ll talk about a lovely
[paper](http://arxiv.org/abs/1301.5577) by Sebastian Hensel, Piotr
Przytycki and Richard Webb. They show that all curve graphs are
17-hyperbolic. Hyperbolicity of curve graphs is a very very very
useful\* property because mapping class groups act nicely on them, so
you can prove all sorts of things using this action.  
The proofs available before HPW were quite complicated and relied on
Teichmüller theory, so I was quite amazed to see that this could be
proven in 6 self-contained pages. And, as the authors pointed out to me:
“Well, there’s one page of introduction and one page of references.”

This post is an illustrated guide to the proof. I won’t define arc/curve
complexes here, but I plan to write a BI soon. The more loudly you
complain, the sooner I will actually do.

Ok, let’s start. First of all, as it turns out it’s more convenient to
deal with arc graphs instead of curve graphs.

**Reduction to the arc graph.** (Really, just skip this
![😀](https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f600.svg)
) Here’s a very quick sketch of how to deduce hyperbolicity of curve
graphs once we know it for arc graphs, which for the moment we assume we
do.  
If we are dealing with a (complicated) surface with boundary then the
idea we can use is that one can construct a path in the curve complex
starting from a path
![\\gamma](https://s0.wp.com/latex.php?latex=%5Cgamma&bg=ffffff&fg=333333&s=0 "\gamma")
in the arc complex by considering curves disjoint from the arcs
appearing along
![\\gamma](https://s0.wp.com/latex.php?latex=%5Cgamma&bg=ffffff&fg=333333&s=0 "\gamma")
(it will be clearer later how to exploit this, if you don’t know how to
do it already). I’ll be honest, just this one time: There is a subtle
issue I’m sweeping under the carpet here, but I would like not to make
the post too technical…  
Anyway, suppose instead that your surface,
![S](https://s0.wp.com/latex.php?latex=S&bg=ffffff&fg=333333&s=0 "S"),
is closed. If you call
![S'](https://s0.wp.com/latex.php?latex=S%27&bg=ffffff&fg=333333&s=0 "S'")
the surface obtained by adding a boundary component, then you have a
boundary-forgetting map. This map is Lipschitz, this is immediate, and
has a section, constructed as follows. Choose a hyperbolic metric on
![S](https://s0.wp.com/latex.php?latex=S&bg=ffffff&fg=333333&s=0 "S")
and realise all (homotopy classes of) curves as geodesics. Now you can
take a puncture outside the union of all such (countably many)
geodesics. Using the two properties it’s not hard to see that the curve
graph of
![S](https://s0.wp.com/latex.php?latex=S&bg=ffffff&fg=333333&s=0 "S")
must be hyperbolic as well. The details are in section 5 of the paper.

**Unicorns!** Ok, let’s now take an arc graph. The strategy to show it’s
hyperbolic is to prove that, as David puts it, “it smells
hyperbolic”\*\*, i.e. that there exists a family of preferred paths with
nice properties (you may wish to take a look at [this
pos](https://alexsisto.wordpress.com/2012/07/16/bi-guessing-geodesics-in-hyperbolic-spaces/)t
![🙂](https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f642.svg)
). The most important property that this family should satisfy is that
triangles of preferred paths should be slim. The other properties you
need (in simplified form) are that a preferred path is a geodesic if the
endpoints have distance at most 1 and that a subpath of a preferred path
is a preferred path.  
HPW called the nice paths they constructed unicorn paths (!). They were
initially called one-corner paths, but then Piotr realised that
one-corner and unicorn are almost the same word in Polish, and that
unicorn would be a much more awesome name.  
And now, here are the paths. You have to start with two arcs in minimal
position,
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
and
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b"),
and it’s convenient to fix preferred endpoints,
![\\alpha](https://s0.wp.com/latex.php?latex=%5Calpha&bg=ffffff&fg=333333&s=0 "\alpha")
and
![\\beta](https://s0.wp.com/latex.php?latex=%5Cbeta&bg=ffffff&fg=333333&s=0 "\beta").
We can assume that
![a,b](https://s0.wp.com/latex.php?latex=a%2Cb&bg=ffffff&fg=333333&s=0 "a,b")
intersect minimally. The arcs appearing along the path from
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a") to
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b"),
the unicorn arcs, have a rather simple form: You travel along
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
until you reach some intersection point,
![\\pi](https://s0.wp.com/latex.php?latex=%5Cpi&bg=ffffff&fg=333333&s=0 "\pi"),
and then you go to
![\\beta](https://s0.wp.com/latex.php?latex=%5Cbeta&bg=ffffff&fg=333333&s=0 "\beta").

[![unicorn](https://alexsisto.files.wordpress.com/2013/02/unicorn1.png?w=512&h=288)](https://alexsisto.files.wordpress.com/2013/02/unicorn1.png)

Not all intersection points work, because the procedure described above
might not give an embedded arc (look at
![\\tau](https://s0.wp.com/latex.php?latex=%5Ctau&bg=ffffff&fg=333333&s=0 "\tau"),
for example).  
Let us also include
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
and
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b") in
the collection of unicorn arcs. So, given
![a,b](https://s0.wp.com/latex.php?latex=a%2Cb&bg=ffffff&fg=333333&s=0 "a,b")
you have finitely many arcs, and there is a natural order on them: You
write
![c&lt;c'](https://s0.wp.com/latex.php?latex=c%3Cc%27&bg=ffffff&fg=333333&s=0 "c<c'")
if the common subpath of
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c")
and
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a") is
longer than the common subpath of
![c'](https://s0.wp.com/latex.php?latex=c%27&bg=ffffff&fg=333333&s=0 "c'")
and
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a").
The idea is that you are describing a path from
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a") to
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b"),
so the paths more closely resembling
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
should appear first.  
Now, we have to check that we actually described a path, i.e. that if
![c'](https://s0.wp.com/latex.php?latex=c%27&bg=ffffff&fg=333333&s=0 "c'")
is the successor of
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c")
then
![c,c'](https://s0.wp.com/latex.php?latex=c%2Cc%27&bg=ffffff&fg=333333&s=0 "c,c'")
can be realised disjointly.  
The recipe to construct the successor is simple. Let
![\\pi](https://s0.wp.com/latex.php?latex=%5Cpi&bg=ffffff&fg=333333&s=0 "\pi")
be the intersection point defining
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c"),
and let
![b'](https://s0.wp.com/latex.php?latex=b%27&bg=ffffff&fg=333333&s=0 "b'")
be the subpath of
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c")
from
![\\pi](https://s0.wp.com/latex.php?latex=%5Cpi&bg=ffffff&fg=333333&s=0 "\pi")
to
![\\beta](https://s0.wp.com/latex.php?latex=%5Cbeta&bg=ffffff&fg=333333&s=0 "\beta").
Just travel along
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
after
![\\pi](https://s0.wp.com/latex.php?latex=%5Cpi&bg=ffffff&fg=333333&s=0 "\pi")
until you hit
![b'](https://s0.wp.com/latex.php?latex=b%27&bg=ffffff&fg=333333&s=0 "b'")
in some point
![\\pi'](https://s0.wp.com/latex.php?latex=%5Cpi%27&bg=ffffff&fg=333333&s=0 "\pi'").
Then it’s not hard to convince yourself that
![\\pi'](https://s0.wp.com/latex.php?latex=%5Cpi%27&bg=ffffff&fg=333333&s=0 "\pi'")
defines
![c'](https://s0.wp.com/latex.php?latex=c%27&bg=ffffff&fg=333333&s=0 "c'").

[![unicornsucc](https://alexsisto.files.wordpress.com/2013/02/unicornsucc.png?w=576&h=328)](https://alexsisto.files.wordpress.com/2013/02/unicornsucc.png)

The picture also illustrates how to realise
![c,c'](https://s0.wp.com/latex.php?latex=c%2Cc%27&bg=ffffff&fg=333333&s=0 "c,c'")
disjointly.

**Slim unicorns!** And here is the cool part. Unicorn triangles are
1-slim, i.e. given
![a,b,d](https://s0.wp.com/latex.php?latex=a%2Cb%2Cd&bg=ffffff&fg=333333&s=0 "a,b,d")
and a unicorn arc
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c"),
defined by ![\\pi\\in a\\cap
b](https://s0.wp.com/latex.php?latex=%5Cpi%5Cin+a%5Ccap+b&bg=ffffff&fg=333333&s=0 "\pi\in a\cap b"),
on the unicorn path
![P(a,b)](https://s0.wp.com/latex.php?latex=P%28a%2Cb%29&bg=ffffff&fg=333333&s=0 "P(a,b)")
from
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a") to
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b")
there is a point on ![P(a,d)\\cup
P(b,d)](https://s0.wp.com/latex.php?latex=P%28a%2Cd%29%5Ccup+P%28b%2Cd%29&bg=ffffff&fg=333333&s=0 "P(a,d)\cup P(b,d)")
at distance at most 1 from
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c").
The proof is very easy, just travel along
![d](https://s0.wp.com/latex.php?latex=d&bg=ffffff&fg=333333&s=0 "d")
until you hit
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c"),
then go to
![\\alpha](https://s0.wp.com/latex.php?latex=%5Calpha&bg=ffffff&fg=333333&s=0 "\alpha")
or
![\\beta](https://s0.wp.com/latex.php?latex=%5Cbeta&bg=ffffff&fg=333333&s=0 "\beta"),
whichever you can reach avoiding
![\\pi](https://s0.wp.com/latex.php?latex=%5Cpi&bg=ffffff&fg=333333&s=0 "\pi").

[![unicornslim](https://alexsisto.files.wordpress.com/2013/02/unicornslim1.png?w=512&h=262)](https://alexsisto.files.wordpress.com/2013/02/unicornslim1.png)

The picture hopefully clearly illustrates that the unicorn arc
![c'](https://s0.wp.com/latex.php?latex=c%27&bg=ffffff&fg=333333&s=0 "c'")
we just constructed can be realised disjointly from
![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0 "c").  
The authors told me that the initial argument for 1-slimness of
triangles was based on their dismantlability, you may wish to take a
look at this [paper](http://arxiv.org/abs/1205.0513).

**The technical bit.** You need one more property to show that arc
graphs are hyperbolic and unicorn paths are close to geodesics, that is
to say that a subpath of a unicorn path is a unicorn path. Well, this is
not actually true, sometimes you can have a subpath of a unicorn path of
length 2 connecting points at distance 1 in the arc graph. But that’s
the only bad thing that can happen, and this is good enough for us.  
Stare at the recipe I told you about earlier to construct the successor.
Done? It might now seem to you that if you have two unicorn arcs
![c\_1,c\_2](https://s0.wp.com/latex.php?latex=c_1%2Cc_2&bg=ffffff&fg=333333&s=0 "c_1,c_2")
constructed from
![a,b](https://s0.wp.com/latex.php?latex=a%2Cb&bg=ffffff&fg=333333&s=0 "a,b"),
the recipe will give you exactly the same successor of
![c\_1](https://s0.wp.com/latex.php?latex=c_1&bg=ffffff&fg=333333&s=0 "c_1")
regardless of whether you work “between
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
and
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b")”
or “between
![c\_1](https://s0.wp.com/latex.php?latex=c_1&bg=ffffff&fg=333333&s=0 "c_1")
and
![c\_2](https://s0.wp.com/latex.php?latex=c_2&bg=ffffff&fg=333333&s=0 "c_2").”
So… what’s the problem? The problem is that
![c\_1,c\_2](https://s0.wp.com/latex.php?latex=c_1%2Cc_2&bg=ffffff&fg=333333&s=0 "c_1,c_2")
might not be in minimal position!
![😦](https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f626.svg)  
So you have to understand when they don’t intersect minimally (Sublemma
3.6 in the paper). You can reduce to the case
![a=c\_1](https://s0.wp.com/latex.php?latex=a%3Dc_1&bg=ffffff&fg=333333&s=0 "a=c_1")
and
![c\_2](https://s0.wp.com/latex.php?latex=c_2&bg=ffffff&fg=333333&s=0 "c_2")
the predecessor of
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b"),
once again because of the recipe for the successor. The predecessor of
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b") is
the unicorn arc travelling as little as possible along
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a"),
so you just have to find the first intersection point
![\\pi](https://s0.wp.com/latex.php?latex=%5Cpi&bg=ffffff&fg=333333&s=0 "\pi")
of
![a,b](https://s0.wp.com/latex.php?latex=a%2Cb&bg=ffffff&fg=333333&s=0 "a,b")
along
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a").

[![unicornbigon](https://alexsisto.files.wordpress.com/2013/02/unicornbigon1.png?w=576&h=293)](https://alexsisto.files.wordpress.com/2013/02/unicornbigon1.png)

(Yes, there’s a reason why I’ve drawn the picture in that weird way, see
below
![😉](https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f609.svg)
)  
Let me recall that two arcs are in minimal position if there are no
bigons or half bigons:

[![minimal1](https://alexsisto.files.wordpress.com/2013/02/minimal1.png?w=640&h=116)](https://alexsisto.files.wordpress.com/2013/02/minimal1.png)

Now, there cannot be a bigon between
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
and
![c\_2](https://s0.wp.com/latex.php?latex=c_2&bg=ffffff&fg=333333&s=0 "c_2"),
for otherwise you can easily convince yourself that there would be one
between
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
and
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b").
Similarly, you can only have a half-bigon if
![\\pi](https://s0.wp.com/latex.php?latex=%5Cpi&bg=ffffff&fg=333333&s=0 "\pi")
appears on it:

[![minimal2](https://alexsisto.files.wordpress.com/2013/02/minimal2.png?w=297&h=154)](https://alexsisto.files.wordpress.com/2013/02/minimal2.png)

So, if there is a half-bigon, then it must look like this:

[![unicornbigon2](https://alexsisto.files.wordpress.com/2013/02/unicornbigon21.png?w=576&h=313)](https://alexsisto.files.wordpress.com/2013/02/unicornbigon21.png)

So, you have a very good control on what can go wrong. I won’t go into
details but I hope that you’ll find it reasonable to believe that it’s
possible to deal with this problem.

And that’s the end
![🙂](https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f642.svg)

Let me add the comment that Lemma 3.4, which I didn’t go into, is there
just to get a better constant at the end, but without it you can prove,
say, 19-hyperbolicity.  
The lemma says that given 3 unicorn paths forming a triangle you can
find a triple of points on them at pairwise distance at most 1. If you
allow yourself to substitute 1 with 3, this follows from what we already
know. In fact, suppose you start at
![a](https://s0.wp.com/latex.php?latex=a&bg=ffffff&fg=333333&s=0 "a")
and move towards
![b](https://s0.wp.com/latex.php?latex=b&bg=ffffff&fg=333333&s=0 "b").
At first, you’ll be 1-close to
![P(a,c)](https://s0.wp.com/latex.php?latex=P%28a%2Cc%29&bg=ffffff&fg=333333&s=0 "P(a,c)"),
and at some point you’ll be 1-close to
![P(b,c)](https://s0.wp.com/latex.php?latex=P%28b%2Cc%29&bg=ffffff&fg=333333&s=0 "P(b,c)").
When the switch happens, you have the 3 points you’re looking for. Btw,
analysing this idea gives you a way of finding your candidate points at
pairwise distance 1.

\*David Hume was next to me when I wrote this and said “I have a paper
that relies on that, so I’m not going to argue.”  
\*\* David suggested I add “I would like to thank David for being so
quotable.”



