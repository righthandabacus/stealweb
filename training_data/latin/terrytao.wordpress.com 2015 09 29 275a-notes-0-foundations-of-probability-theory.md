275A, Notes 0: Foundations of probability theory
================================================

29 September, 2015 in [275A - probability
theory](https://terrytao.wordpress.com/category/teaching/275a-probability-theory/),
[math.CA](https://terrytao.wordpress.com/category/mathematics/mathca/),
[math.PR](https://terrytao.wordpress.com/category/mathematics/mathpr/) |
Tags: [foundations](https://terrytao.wordpress.com/tag/foundations/)

Starting this week, I will be teaching an [introductory graduate course
(Math 275A)](https://ccle.ucla.edu/mod/page/view.php?id=834267) on
probability theory here at UCLA. While I find myself *using*
probabilistic methods routinely nowadays in my research (for instance,
the probabilistic concept of [Shannon
entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))
played a crucial role in my [recent paper on the Chowla and Elliott
conjectures](https://terrytao.wordpress.com/2015/09/18/the-logarithmically-averaged-chowla-and-elliott-conjectures-for-two-point-correlations-the-erdos-discrepancy-problem/),
and random multiplicative functions similarly played a central role in
the [paper on the Erdos discrepancy
problem](https://terrytao.wordpress.com/2015/09/11/the-erdos-discrepancy-problem-via-the-elliott-conjecture/)),
this will actually be the first time I will be *teaching* a course on
probability itself (although I did give a [course on random matrix
theory](https://terrytao.wordpress.com/category/teaching/254a-random-matrices/)
some years ago that presumed familiarity with graduate-level probability
theory). As such, I will be relying primarily on an existing textbook,
in this case Durrett’s [Probability: Theory and
Examples](http://www.math.duke.edu/~rtd/PTE/PTE4_1.pdf). I still need to
prepare lecture notes, though, and so I thought I would continue my
practice of putting my notes online, although in this particular case
they will be less detailed or complete than with other courses, as they
will mostly be focusing on those topics that are not already
comprehensively covered in the text of Durrett. Below the fold are my
first such set of notes, concerning the classical measure-theoretic
foundations of probability. (I wrote on these foundations also in [this
previous blog
post](https://terrytao.wordpress.com/2010/01/01/254a-notes-0-a-review-of-probability-theory/),
but in that post I already assumed that the reader was familiar with
measure theory and basic probability, whereas in this course not every
student will have a strong background in these areas.)

Note: as this set of notes is primarily concerned with foundational
issues, it will contain a large number of pedantic (and nearly trivial)
formalities and philosophical points. We dwell on these technicalities
in this set of notes primarily so that they are out of the way in later
notes, when we work with the actual mathematics of probability, rather
than on the supporting foundations of that mathematics. In particular,
the excessively formal and philosophical language in this set of notes
will not be replicated in later notes.

**— 1. Some philosophical generalities —**

By default, mathematical reasoning is understood to take place in a
*deterministic* mathematical universe. In such a universe, any given
mathematical statement
![{S}](https://s0.wp.com/latex.php?latex=%7BS%7D&bg=ffffff&fg=000000&s=0 "{S}")
(that is to say, a sentence with no free variables) is either true or
false, with no intermediate truth value available. Similarly, any
deterministic variable
![{x}](https://s0.wp.com/latex.php?latex=%7Bx%7D&bg=ffffff&fg=000000&s=0 "{x}")
can take on only one specific value at a time.

However, for a variety of reasons, both within pure mathematics and in
the applications of mathematics to other disciplines, it is often
desirable to have a rigorous mathematical framework in which one can
discuss *non-deterministic* statements and variables – that is to say,
statements which are not always true or always false, but in some
intermediate state, or variables that do not take one particular value
or another with definite certainty, but are again in some intermediate
state. In probability theory, which is by far the most widely adopted
mathematical framework to formally capture the concept of
non-determinism, non-deterministic statements are referred to as
*events*, and non-deterministic variables are referred to as *random
variables*. In the standard foundations of probability theory, as laid
out by Kolmogorov, we can then *model* these events and random variables
by introducing a [sample
space](https://en.wikipedia.org/wiki/Sample_space) (which will be given
the structure of a [probability
space](https://en.wikipedia.org/wiki/Probability_space)) to capture all
the ambient sources of randomness; events are then modeled as measurable
subsets of this sample space, and random variables are modeled as
measurable functions on this sample space. (We will briefly discuss a
more abstract way to set up probability theory, as well as other
frameworks to capture non-determinism than classical probability theory,
at the end of this set of notes; however, the rest of the course will be
concerned exclusively with classical probability theory using the
orthodox Kolmogorov models.)

Note carefully that sample spaces (and their attendant structures) will
be used to *model* probabilistic concepts, rather than to actually *be*
the concepts themselves. This distinction (a mathematical analogue of
the
[map-territory](https://en.wikipedia.org/wiki/Map%E2%80%93territory_relation)
distinction in philosophy) actually is implicit in much of modern
mathematics, when we make a distinction between an abstract version of a
mathematical object, and a concrete representation (or *model*) of that
object. For instance:

-   In linear algebra, we distinguish between an [abstract vector
    space](https://en.wikipedia.org/wiki/Vector_space)
    ![{V}](https://s0.wp.com/latex.php?latex=%7BV%7D&bg=ffffff&fg=000000&s=0 "{V}"),
    and a concrete system of coordinates ![{\\phi: V \\rightarrow {\\bf
    R}^n}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%3A+V+%5Crightarrow+%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{\phi: V \rightarrow {\bf R}^n}")
    given by some
    [basis](https://en.wikipedia.org/wiki/Basis_(linear_algebra)) of
    ![{V}](https://s0.wp.com/latex.php?latex=%7BV%7D&bg=ffffff&fg=000000&s=0 "{V}").
-   In group theory, we distinguish between an [abstract
    group](https://en.wikipedia.org/wiki/Group_(mathematics))
    ![{G}](https://s0.wp.com/latex.php?latex=%7BG%7D&bg=ffffff&fg=000000&s=0 "{G}"),
    and a concrete [representation of that
    group](https://en.wikipedia.org/wiki/Group_representation) ![{\\phi:
    G \\rightarrow
    \\hbox{Aut}(X)}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%3A+G+%5Crightarrow+%5Chbox%7BAut%7D%28X%29%7D&bg=ffffff&fg=000000&s=0 "{\phi: G \rightarrow \hbox{Aut}(X)}")
    as isomorphisms on some space
    ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}").
-   In differential geometry, we distinguish between an [abstract
    manifold](https://en.wikipedia.org/wiki/Manifold)
    ![{M}](https://s0.wp.com/latex.php?latex=%7BM%7D&bg=ffffff&fg=000000&s=0 "{M}"),
    and a concrete [atlas of coordinate
    systems](https://en.wikipedia.org/wiki/Atlas_(topology)) that
    coordinatises that manifold.
-   Though it is rarely mentioned explicitly, the abstract [number
    systems](https://en.wikipedia.org/wiki/Number#Classification) such
    as ![{{\\bf N}, {\\bf Z}, {\\bf Q}, {\\bf R}, {\\bf
    C}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+N%7D%2C+%7B%5Cbf+Z%7D%2C+%7B%5Cbf+Q%7D%2C+%7B%5Cbf+R%7D%2C+%7B%5Cbf+C%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf N}, {\bf Z}, {\bf Q}, {\bf R}, {\bf C}}")
    are distinguished from the concrete [numeral
    systems](https://en.wikipedia.org/wiki/Numeral_system) (e.g. the
    decimal or binary systems) that are used to represent them (this
    distinction is particularly useful to keep in mind when faced with
    the [infamous identity](https://en.wikipedia.org/wiki/0.999...)
    ![{0.999\\dots =
    1}](https://s0.wp.com/latex.php?latex=%7B0.999%5Cdots+%3D+1%7D&bg=ffffff&fg=000000&s=0 "{0.999\dots = 1}"),
    or when switching from one numeral representation system
    to another).

The distinction between abstract objects and concrete models can be
fairly safely discarded if one is only going to use a single model for
each abstract object, particularly if that model is “canonical” in some
sense. However, one needs to keep the distinction in mind if one plans
to switch between different models of a single object (e.g. to perform
change of basis in linear algebra, change of coordinates in differential
geometry, or [base change](https://en.wikipedia.org/wiki/Base_change) in
algebraic geometry). As it turns out, in probability theory it is often
desirable to change the sample space model (for instance, one could
*extend* the sample space by adding in new sources of randomness, or one
could couple together two systems of random variables by *joining* their
sample space models together). Because of this, we will take some care
in this foundational set of notes to distinguish probabilistic concepts
(such as events and random variables) from their sample space models.
(But we may be more willing to conflate the two in later notes, once the
foundational issues are out of the way.)

From a foundational point of view, it is often logical to begin with
some axiomatic description of the abstract version of a mathematical
object, and discuss the concrete representations of that object later;
for instance, one could start with the axioms of an abstract group, and
then later consider concrete representations of such a group by
permutations, invertible linear transformations, and so forth. This
approach is often employed in the more algebraic areas of mathematics.
However, there are at least two other ways to present these concepts
which can be preferable from a pedagogical point of view. One way is to
start with the concrete representations as motivating examples, and only
later give the abstract object that these representations are modeling;
this is how linear algebra, for instance, is often taught at the
undergraduate level, by starting first with ![{{\\bf
R}^2}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5E2%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^2}"),
![{{\\bf
R}^3}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5E3%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^3}"),
and ![{{\\bf
R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}"),
and only later introducing the abstract vector spaces. Another way is to
avoid the abstract objects altogether, and focus exclusively on concrete
representations, but taking care to emphasise how these representations
transform when one switches from one representation to another. For
instance, in general relativity courses in undergraduate physics, it is
not uncommon to see tensors presented purely through the concrete
representation of coordinates indexed by multiple indices, with the
transformation of such tensors under changes of variable carefully
described; the abstract constructions of tensors and tensor spaces using
operations such as tensor product and duality of vector spaces or vector
bundles are often left to an advanced differential geometry class to set
up properly.

The foundations of probability theory are usually presented (almost by
default) using the last of the above three approaches; namely, one talks
almost exclusively about sample space models for probabilistic concepts
such as events and random variables, and only occasionally dwells on the
need to extend or otherwise modify the sample space when one needs to
introduce new sources of randomness (or to forget about some existing
sources of randomness). However, much as in differential geometry one
tends to work with manifolds without specifying any given atlas of
coordinate charts, in probability one usually manipulates events and
random variables without explicitly specifying any given sample space.
For a student raised exclusively on concrete sample space foundations of
probability, this can be a bit confusing, for instance it can give the
misconception that any given random variable is somehow associated to
its own unique sample space, with different random variables possibly
living on different sample spaces, which often leads to nonsense when
one then tries to combine those random variables together. Because of
such confusions, we will try to take particular care in these notes to
separate probabilistic concepts from their sample space models.

**— 2. A simple class of models: discrete probability spaces —**

The simplest models of probability theory are those generated by
*discrete probability spaces*, which are adequate models for many
applications (particularly in combinatorics and other areas of discrete
mathematics), and which already capture much of the essence of
probability theory while avoiding some of the finer measure-theoretic
subtleties. We thus begin by considering discrete sample space models.

> **Definition 1 (Discrete probability theory)** A *discrete probability
> space* ![{\\Omega = (\\Omega, (p\_\\omega)\_{\\omega \\in
> \\Omega})}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%28%5COmega%2C+%28p_%5Comega%29_%7B%5Comega+%5Cin+%5COmega%7D%29%7D&bg=ffffff&fg=000000&s=0 "{\Omega = (\Omega, (p_\omega)_{\omega \in \Omega})}")
> is an at most countable set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> (whose elements ![{\\omega \\in
> \\Omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega+%5Cin+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\omega \in \Omega}")
> will be referred to as *outcomes*), together with a non-negative real
> number
> ![{p\_\\omega}](https://s0.wp.com/latex.php?latex=%7Bp_%5Comega%7D&bg=ffffff&fg=000000&s=0 "{p_\omega}")
> assigned to each outcome
> ![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}")
> such that ![{\\sum\_{\\omega \\in \\Omega} p\_\\omega =
> 1}](https://s0.wp.com/latex.php?latex=%7B%5Csum_%7B%5Comega+%5Cin+%5COmega%7D+p_%5Comega+%3D+1%7D&bg=ffffff&fg=000000&s=0 "{\sum_{\omega \in \Omega} p_\omega = 1}");
> we refer to
> ![{p\_\\omega}](https://s0.wp.com/latex.php?latex=%7Bp_%5Comega%7D&bg=ffffff&fg=000000&s=0 "{p_\omega}")
> as the *probability* of the outcome
> ![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}").
> The set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> itself, without the structure ![{(p\_\\omega)\_{\\omega \\in
> \\Omega}}](https://s0.wp.com/latex.php?latex=%7B%28p_%5Comega%29_%7B%5Comega+%5Cin+%5COmega%7D%7D&bg=ffffff&fg=000000&s=0 "{(p_\omega)_{\omega \in \Omega}}"),
> is often referred to as the *sample space*, though we will often abuse
> notation by using the sample space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> to refer to the entire discrete probability space ![{(\\Omega,
> (p\_\\omega)\_{\\omega \\in
> \\Omega})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%28p_%5Comega%29_%7B%5Comega+%5Cin+%5COmega%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, (p_\omega)_{\omega \in \Omega})}").
>
> In discrete probability theory, we choose an ambient discrete
> probability space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> as the randomness model. We then model *events*
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> by subsets
> ![{E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega}")
> of the sample space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}").
> The *probability* ![{{\\bf
> P}(E)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28E%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(E)}")
> of an event
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> is defined to be the quantity
>
> ![\\displaystyle {\\bf P}(E) := \\sum\_{\\omega \\in E\_\\Omega}
> p\_\\omega;](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28E%29+%3A%3D+%5Csum_%7B%5Comega+%5Cin+E_%5COmega%7D+p_%5Comega%3B&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(E) := \sum_{\omega \in E_\Omega} p_\omega;")
>
> note that this is a real number in the interval
> ![{\[0,1\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,1]}").
> An event
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> is *surely true* or is the *sure event* if ![{E\_\\Omega =
> \\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega+%3D+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega = \Omega}"),
> and is *surely false* or is the *empty event* if ![{E\_\\Omega
> =\\emptyset}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega+%3D%5Cemptyset%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega =\emptyset}").
>
> We model random variables
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> taking values in the range
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
> by functions ![{X\_\\Omega: \\Omega \\rightarrow
> R}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%3A+%5COmega+%5Crightarrow+R%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega: \Omega \rightarrow R}")
> from the sample space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> to the range
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}").
> Random variables taking values in ![{{\\bf
> R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}")
> will be called *real random variables* or *random real numbers*.
> Similarly for random variables taking values in ![{{\\bf
> C}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+C%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf C}}").
> We refer to real and complex random variables collectively as *scalar
> random variables*.
>
> We consider two events
> ![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
> to be equal if they are modeled by the same set: ![{E=F \\iff
> E\_\\Omega =
> F\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE%3DF+%5Ciff+E_%5COmega+%3D+F_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E=F \iff E_\Omega = F_\Omega}").
> Similarly, two random variables
> ![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}")
> taking values in a common range
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
> are considered to be equal if they are modeled by the same function:
> ![{X=Y \\iff X\_\\Omega =
> Y\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BX%3DY+%5Ciff+X_%5COmega+%3D+Y_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{X=Y \iff X_\Omega = Y_\Omega}").
> In particular, if the discrete sample space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is understood from context, we will usually abuse notation by
> identifying an event
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> with its model
> ![{E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega}"),
> and similarly identify a random variable
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> with its model
> ![{X\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega}").

> **Remark 2** One can view classical (deterministic) mathematics as the
> special case of discrete probability theory in which
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is a singleton set (there is only one outcome
> ![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}")),
> and the probability assigned to the single outcome
> ![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}")
> in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is
> ![{1}](https://s0.wp.com/latex.php?latex=%7B1%7D&bg=ffffff&fg=000000&s=0 "{1}"):
> ![{p\_\\omega =
> 1}](https://s0.wp.com/latex.php?latex=%7Bp_%5Comega+%3D+1%7D&bg=ffffff&fg=000000&s=0 "{p_\omega = 1}").
> Then there are only two events (the surely true and surely false
> events), and a random variable in
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
> can be identified with a deterministic element of
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}").
> Thus we can view probability theory as a generalisation of
> deterministic mathematics.

As discussed in the preceding section, the distinction between a
collection of events and random variable and its models becomes
important if one ever wishes to modify the sample space, and in
particular to *extend* the sample space to a larger space that can
accommodate new sources of randomness (an operation which we will define
formally later, but which for now can be thought of as an analogue to
change of basis in linear algebra, coordinate change in differential
geometry, or [base change](https://en.wikipedia.org/wiki/Base_change) in
algebraic geometry). This is best illustrated with a simple example.

> **Example 3 (Extending the sample space)** Suppose one wishes to model
> the outcome
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> of rolling a single, unbiased six-sided die using discrete probability
> theory. One can do this by choosing the discrete proability space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> to be the six-element set
> ![{\\{1,2,3,4,5,6\\}}](https://s0.wp.com/latex.php?latex=%7B%5C%7B1%2C2%2C3%2C4%2C5%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\{1,2,3,4,5,6\}}"),
> with each outcome ![{i \\in
> \\{1,2,3,4,5,6\\}}](https://s0.wp.com/latex.php?latex=%7Bi+%5Cin+%5C%7B1%2C2%2C3%2C4%2C5%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{i \in \{1,2,3,4,5,6\}}")
> given an equal probability of ![{p\_i :=
> 1/6}](https://s0.wp.com/latex.php?latex=%7Bp_i+%3A%3D+1%2F6%7D&bg=ffffff&fg=000000&s=0 "{p_i := 1/6}")
> of occurring; this outcome
> ![{i}](https://s0.wp.com/latex.php?latex=%7Bi%7D&bg=ffffff&fg=000000&s=0 "{i}")
> may be interpreted as the state in which the die roll
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> ended up being equal to
> ![{i}](https://s0.wp.com/latex.php?latex=%7Bi%7D&bg=ffffff&fg=000000&s=0 "{i}").
> The outcome
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> of rolling a die may then be identified with the identity function
> ![{X\_\\Omega: \\Omega \\rightarrow
> \\{1,\\dots,6\\}}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%3A+%5COmega+%5Crightarrow+%5C%7B1%2C%5Cdots%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega: \Omega \rightarrow \{1,\dots,6\}}"),
> defined by ![{X\_\\Omega(i) :=
> i}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%28i%29+%3A%3D+i%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega(i) := i}")
> for ![{i \\in
> \\Omega}](https://s0.wp.com/latex.php?latex=%7Bi+%5Cin+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{i \in \Omega}").
> If we let
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> be the event that the outcome
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> of rolling the die is an even number, then with this model
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> we have ![{E\_\\Omega =
> \\{2,4,6\\}}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega+%3D+%5C%7B2%2C4%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega = \{2,4,6\}}"),
> and
>
> ![\\displaystyle {\\bf P}(E) = \\sum\_{\\omega \\in E\_\\Omega}
> p\_\\omega = 3 \\times \\frac{1}{6} =
> \\frac{1}{2}.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28E%29+%3D+%5Csum_%7B%5Comega+%5Cin+E_%5COmega%7D+p_%5Comega+%3D+3+%5Ctimes+%5Cfrac%7B1%7D%7B6%7D+%3D+%5Cfrac%7B1%7D%7B2%7D.&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(E) = \sum_{\omega \in E_\Omega} p_\omega = 3 \times \frac{1}{6} = \frac{1}{2}.")
>
> Now suppose that we wish to roll the die again to obtain a second
> random variable
> ![{Y}](https://s0.wp.com/latex.php?latex=%7BY%7D&bg=ffffff&fg=000000&s=0 "{Y}").
> The sample space ![{\\Omega =
> \\{1,2,3,4,5,6\\}}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%5C%7B1%2C2%2C3%2C4%2C5%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\Omega = \{1,2,3,4,5,6\}}")
> is inadequate for modeling both the original die roll
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> and the second die roll
> ![{Y}](https://s0.wp.com/latex.php?latex=%7BY%7D&bg=ffffff&fg=000000&s=0 "{Y}").
> To accommodate this new source of randomness, we can then move to the
> larger discrete probability space ![{\\Omega' := \\{1,\\dots,6\\}
> \\times
> \\{1,\\dots,6\\}}](https://s0.wp.com/latex.php?latex=%7B%5COmega%27+%3A%3D+%5C%7B1%2C%5Cdots%2C6%5C%7D+%5Ctimes+%5C%7B1%2C%5Cdots%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\Omega' := \{1,\dots,6\} \times \{1,\dots,6\}}"),
> where each outcome ![{(i,j) \\in
> \\Omega'}](https://s0.wp.com/latex.php?latex=%7B%28i%2Cj%29+%5Cin+%5COmega%27%7D&bg=ffffff&fg=000000&s=0 "{(i,j) \in \Omega'}")
> now having probability ![{p'\_{(i,j)} :=
> \\frac{1}{36}}](https://s0.wp.com/latex.php?latex=%7Bp%27_%7B%28i%2Cj%29%7D+%3A%3D+%5Cfrac%7B1%7D%7B36%7D%7D&bg=ffffff&fg=000000&s=0 "{p'_{(i,j)} := \frac{1}{36}}");
> this outcome
> ![{(i,j)}](https://s0.wp.com/latex.php?latex=%7B%28i%2Cj%29%7D&bg=ffffff&fg=000000&s=0 "{(i,j)}")
> can be interpreted as the state in which the die roll
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> ended up being
> ![{i}](https://s0.wp.com/latex.php?latex=%7Bi%7D&bg=ffffff&fg=000000&s=0 "{i}"),
> and the die roll
> ![{Y}](https://s0.wp.com/latex.php?latex=%7BY%7D&bg=ffffff&fg=000000&s=0 "{Y}")
> ended up being
> ![{j}](https://s0.wp.com/latex.php?latex=%7Bj%7D&bg=ffffff&fg=000000&s=0 "{j}").
> The random variable
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> is now modeled by a new function ![{X\_{\\Omega'}: \\Omega'
> \\rightarrow
> \\{1,\\dots,6\\}}](https://s0.wp.com/latex.php?latex=%7BX_%7B%5COmega%27%7D%3A+%5COmega%27+%5Crightarrow+%5C%7B1%2C%5Cdots%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{X_{\Omega'}: \Omega' \rightarrow \{1,\dots,6\}}")
> defined by ![{X\_{\\Omega'}(i,j) :=
> i}](https://s0.wp.com/latex.php?latex=%7BX_%7B%5COmega%27%7D%28i%2Cj%29+%3A%3D+i%7D&bg=ffffff&fg=000000&s=0 "{X_{\Omega'}(i,j) := i}")
> for ![{(i,j) \\in
> \\Omega'}](https://s0.wp.com/latex.php?latex=%7B%28i%2Cj%29+%5Cin+%5COmega%27%7D&bg=ffffff&fg=000000&s=0 "{(i,j) \in \Omega'}");
> the random variable
> ![{Y}](https://s0.wp.com/latex.php?latex=%7BY%7D&bg=ffffff&fg=000000&s=0 "{Y}")
> is similarly modeled by the function ![{Y\_{\\Omega'}: \\Omega'
> \\rightarrow
> \\{1,\\dots,6\\}}](https://s0.wp.com/latex.php?latex=%7BY_%7B%5COmega%27%7D%3A+%5COmega%27+%5Crightarrow+%5C%7B1%2C%5Cdots%2C6%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{Y_{\Omega'}: \Omega' \rightarrow \{1,\dots,6\}}")
> defined by ![{Y\_{\\Omega'}(i,j) :=
> j}](https://s0.wp.com/latex.php?latex=%7BY_%7B%5COmega%27%7D%28i%2Cj%29+%3A%3D+j%7D&bg=ffffff&fg=000000&s=0 "{Y_{\Omega'}(i,j) := j}")
> for ![{(i,j) \\in
> \\Omega'}](https://s0.wp.com/latex.php?latex=%7B%28i%2Cj%29+%5Cin+%5COmega%27%7D&bg=ffffff&fg=000000&s=0 "{(i,j) \in \Omega'}").
> The event
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> that
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> is even is now modeled by the set
>
> ![\\displaystyle E\_{\\Omega'} = \\{2,4,6\\} \\times
> \\{1,2,3,4,5,6\\}.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++E_%7B%5COmega%27%7D+%3D+%5C%7B2%2C4%2C6%5C%7D+%5Ctimes+%5C%7B1%2C2%2C3%2C4%2C5%2C6%5C%7D.&bg=ffffff&fg=000000&s=0 "\displaystyle  E_{\Omega'} = \{2,4,6\} \times \{1,2,3,4,5,6\}.")
>
> This set is distinct from the previous model
> ![{E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega}")
> of
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> (for instance,
> ![{E\_{\\Omega'}}](https://s0.wp.com/latex.php?latex=%7BE_%7B%5COmega%27%7D%7D&bg=ffffff&fg=000000&s=0 "{E_{\Omega'}}")
> has eighteen elements, whereas
> ![{E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega}")
> has just three), but the probability of
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> is unchanged:
>
> ![\\displaystyle {\\bf P}(E) = \\sum\_{\\omega' \\in E\_{\\Omega'}}
> p'\_{\\omega'} = 18 \\times\\frac{1}{36} =
> \\frac{1}{2}.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28E%29+%3D+%5Csum_%7B%5Comega%27+%5Cin+E_%7B%5COmega%27%7D%7D+p%27_%7B%5Comega%27%7D+%3D+18+%5Ctimes%5Cfrac%7B1%7D%7B36%7D+%3D+%5Cfrac%7B1%7D%7B2%7D.&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(E) = \sum_{\omega' \in E_{\Omega'}} p'_{\omega'} = 18 \times\frac{1}{36} = \frac{1}{2}.")
>
> One can of course also combine together the random variables
> ![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}")
> in various ways. For instance, the sum
> ![{X+Y}](https://s0.wp.com/latex.php?latex=%7BX%2BY%7D&bg=ffffff&fg=000000&s=0 "{X+Y}")
> of the two die rolls is a random variable taking values in
> ![{\\{2,\\dots,12\\}}](https://s0.wp.com/latex.php?latex=%7B%5C%7B2%2C%5Cdots%2C12%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\{2,\dots,12\}}");
> it cannot be modeled by the sample space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> but in
> ![{\\Omega'}](https://s0.wp.com/latex.php?latex=%7B%5COmega%27%7D&bg=ffffff&fg=000000&s=0 "{\Omega'}")
> it is modeled by the function
>
> ![\\displaystyle (X+Y)\_{\\Omega'}: (i,j) \\mapsto
> i+j.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%28X%2BY%29_%7B%5COmega%27%7D%3A+%28i%2Cj%29+%5Cmapsto+i%2Bj.&bg=ffffff&fg=000000&s=0 "\displaystyle  (X+Y)_{\Omega'}: (i,j) \mapsto i+j.")
>
> Similarly, the event
> ![{X=Y}](https://s0.wp.com/latex.php?latex=%7BX%3DY%7D&bg=ffffff&fg=000000&s=0 "{X=Y}")
> that the two die rolls are equal cannot be modeled by
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> but is modeled in
> ![{\\Omega'}](https://s0.wp.com/latex.php?latex=%7B%5COmega%27%7D&bg=ffffff&fg=000000&s=0 "{\Omega'}")
> by the set
>
> ![\\displaystyle (X=Y)\_{\\Omega'} = \\{ (i,i):
> i=1,\\dots,6\\}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%28X%3DY%29_%7B%5COmega%27%7D+%3D+%5C%7B+%28i%2Ci%29%3A+i%3D1%2C%5Cdots%2C6%5C%7D&bg=ffffff&fg=000000&s=0 "\displaystyle  (X=Y)_{\Omega'} = \{ (i,i): i=1,\dots,6\}")
>
> and the probability ![{{\\bf
> P}(X=Y)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28X%3DY%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(X=Y)}")
> of this event is
>
> ![\\displaystyle {\\bf P}(X=Y) = \\sum\_{\\omega' \\in
> (X=Y)\_{\\Omega'}} p'\_{\\omega'} = 6 \\times \\frac{1}{36} =
> \\frac{1}{6}.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28X%3DY%29+%3D+%5Csum_%7B%5Comega%27+%5Cin+%28X%3DY%29_%7B%5COmega%27%7D%7D+p%27_%7B%5Comega%27%7D+%3D+6+%5Ctimes+%5Cfrac%7B1%7D%7B36%7D+%3D+%5Cfrac%7B1%7D%7B6%7D.&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(X=Y) = \sum_{\omega' \in (X=Y)_{\Omega'}} p'_{\omega'} = 6 \times \frac{1}{36} = \frac{1}{6}.")
>
> We thus see that extending the probability space has also enlarged the
> space of events one can consider, as well as the random variables one
> can define, but that existing events and random variables continue to
> be interpretable in the extended model, and that probabilistic
> concepts such as the probability of an event remain unchanged by the
> extension of the model.

The set-theoretic operations on the sample space
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
induce similar boolean operations on events:

-   The *conjunction* ![{E \\wedge
    F}](https://s0.wp.com/latex.php?latex=%7BE+%5Cwedge+F%7D&bg=ffffff&fg=000000&s=0 "{E \wedge F}")
    of two events
    ![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
    is defined through the intersection of their models: ![{(E \\wedge
    F)\_\\Omega := E\_\\Omega \\cap
    F\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%28E+%5Cwedge+F%29_%5COmega+%3A%3D+E_%5COmega+%5Ccap+F_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{(E \wedge F)_\Omega := E_\Omega \cap F_\Omega}").
-   The *disjunction* ![{E \\vee
    F}](https://s0.wp.com/latex.php?latex=%7BE+%5Cvee+F%7D&bg=ffffff&fg=000000&s=0 "{E \vee F}")
    of two events
    ![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
    is defined through the the union of their models: ![{(E \\vee
    F)\_\\Omega := E\_\\Omega \\cup
    F\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%28E+%5Cvee+F%29_%5COmega+%3A%3D+E_%5COmega+%5Ccup+F_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{(E \vee F)_\Omega := E_\Omega \cup F_\Omega}").
-   The *symmetric difference* ![{E \\Delta
    F}](https://s0.wp.com/latex.php?latex=%7BE+%5CDelta+F%7D&bg=ffffff&fg=000000&s=0 "{E \Delta F}")
    of two events
    ![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
    is defined through the symmetric difference of their models: ![{(E
    \\Delta F)\_\\Omega := E\_\\Omega \\Delta
    F\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%28E+%5CDelta+F%29_%5COmega+%3A%3D+E_%5COmega+%5CDelta+F_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{(E \Delta F)_\Omega := E_\Omega \Delta F_\Omega}").
-   The *complement*
    ![{\\overline{E}}](https://s0.wp.com/latex.php?latex=%7B%5Coverline%7BE%7D%7D&bg=ffffff&fg=000000&s=0 "{\overline{E}}")
    of an event
    ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
    is defined through the complement of their models:
    ![{\\overline{E}\_\\Omega := \\Omega \\backslash
    E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5Coverline%7BE%7D_%5COmega+%3A%3D+%5COmega+%5Cbackslash+E_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\overline{E}_\Omega := \Omega \backslash E_\Omega}").
-   We say that one event
    ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
    is *contained in* or *implies* another event
    ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}"),
    and write ![{E \\subset
    F}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+F%7D&bg=ffffff&fg=000000&s=0 "{E \subset F}"),
    if we have containment of their models: ![{E \\subset F \\iff
    E\_\\Omega \\subset
    F\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+F+%5Ciff+E_%5COmega+%5Csubset+F_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E \subset F \iff E_\Omega \subset F_\Omega}").
    We also write
    “![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
    is true on
    ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")”
    synonymously with ![{E \\subset
    F}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+F%7D&bg=ffffff&fg=000000&s=0 "{E \subset F}").
-   Two events
    ![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
    are *disjoint* if their conjunction is the empty event, or
    equivalently if their models ![{E\_\\Omega,
    F\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega%2C+F_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega, F_\Omega}")
    are disjoint.

Thus, for instance, the conjunction of the event that a die roll
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
is even, and that it is less than
![{3}](https://s0.wp.com/latex.php?latex=%7B3%7D&bg=ffffff&fg=000000&s=0 "{3}"),
is the event that the die roll is exactly
![{2}](https://s0.wp.com/latex.php?latex=%7B2%7D&bg=ffffff&fg=000000&s=0 "{2}").
As before, we will usually be in a situation in which the sample space
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
is clear from context, and in that case one can safely identify events
with their models, and view the symbols
![{\\vee}](https://s0.wp.com/latex.php?latex=%7B%5Cvee%7D&bg=ffffff&fg=000000&s=0 "{\vee}")
and
![{\\wedge}](https://s0.wp.com/latex.php?latex=%7B%5Cwedge%7D&bg=ffffff&fg=000000&s=0 "{\wedge}")
as being synonymous with their set-theoretic counterparts
![{\\cup}](https://s0.wp.com/latex.php?latex=%7B%5Ccup%7D&bg=ffffff&fg=000000&s=0 "{\cup}")
and
![{\\cap}](https://s0.wp.com/latex.php?latex=%7B%5Ccap%7D&bg=ffffff&fg=000000&s=0 "{\cap}")
(this is for instance what is done in Durrett).

With these operations, the space of all events (known as the *event
space*) thus has the structure of a [boolean
algebra](https://en.wikipedia.org/wiki/Boolean_algebra) (defined below
in Definition [4](#mesalg)). We observe that the probability ![{{\\bf
P}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}}")
is *finitely additive* in the sense that

![\\displaystyle {\\bf P}( E \\vee F ) = {\\bf P}(E) + {\\bf
P}(F)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28+E+%5Cvee+F+%29+%3D+%7B%5Cbf+P%7D%28E%29+%2B+%7B%5Cbf+P%7D%28F%29&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}( E \vee F ) = {\bf P}(E) + {\bf P}(F)")

whenever
![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
are disjoint events; by induction this implies that

![\\displaystyle {\\bf P}(E\_1 \\vee \\dots \\vee E\_n) = {\\bf P}(E\_1)
+ \\dots + {\\bf
P}(E\_n)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28E_1+%5Cvee+%5Cdots+%5Cvee+E_n%29+%3D+%7B%5Cbf+P%7D%28E_1%29+%2B+%5Cdots+%2B+%7B%5Cbf+P%7D%28E_n%29&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(E_1 \vee \dots \vee E_n) = {\bf P}(E_1) + \dots + {\bf P}(E_n)")

whenever
![{E\_1,\\dots,E\_n}](https://s0.wp.com/latex.php?latex=%7BE_1%2C%5Cdots%2CE_n%7D&bg=ffffff&fg=000000&s=0 "{E_1,\dots,E_n}")
are pairwise disjoint events. We have ![{{\\bf
P}(\\emptyset)=0}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28%5Cemptyset%29%3D0%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(\emptyset)=0}")
and ![{{\\bf
P}(\\overline{\\emptyset})=1}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28%5Coverline%7B%5Cemptyset%7D%29%3D1%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(\overline{\emptyset})=1}"),
and more generally

![\\displaystyle {\\bf P}(\\overline{E}) = 1 - {\\bf
P}(E)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28%5Coverline%7BE%7D%29+%3D+1+-+%7B%5Cbf+P%7D%28E%29&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(\overline{E}) = 1 - {\bf P}(E)")

for any event
![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}").
We also have monotonicity: if ![{E \\subset
F}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+F%7D&bg=ffffff&fg=000000&s=0 "{E \subset F}"),
then ![{{\\bf P}(E) \\leq {\\bf
P}(F)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28E%29+%5Cleq+%7B%5Cbf+P%7D%28F%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(E) \leq {\bf P}(F)}").

Now we define operations on random variables. Whenever one has a
function ![{f: R \\rightarrow
S}](https://s0.wp.com/latex.php?latex=%7Bf%3A+R+%5Crightarrow+S%7D&bg=ffffff&fg=000000&s=0 "{f: R \rightarrow S}")
from one range
![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
to another
![{S}](https://s0.wp.com/latex.php?latex=%7BS%7D&bg=ffffff&fg=000000&s=0 "{S}"),
and a random variable
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
taking values in
![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}"),
one can define a random variable
![{f(X)}](https://s0.wp.com/latex.php?latex=%7Bf%28X%29%7D&bg=ffffff&fg=000000&s=0 "{f(X)}")
taking values in
![{S}](https://s0.wp.com/latex.php?latex=%7BS%7D&bg=ffffff&fg=000000&s=0 "{S}")
by composing the relevant models:

![\\displaystyle f(X)\_\\Omega := f \\circ
X\_\\Omega,](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++f%28X%29_%5COmega+%3A%3D+f+%5Ccirc+X_%5COmega%2C&bg=ffffff&fg=000000&s=0 "\displaystyle  f(X)_\Omega := f \circ X_\Omega,")

thus
![{f(X)\_\\Omega}](https://s0.wp.com/latex.php?latex=%7Bf%28X%29_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{f(X)_\Omega}")
maps
![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}")
to
![{f(X\_\\Omega(\\omega))}](https://s0.wp.com/latex.php?latex=%7Bf%28X_%5COmega%28%5Comega%29%29%7D&bg=ffffff&fg=000000&s=0 "{f(X_\Omega(\omega))}")
for any outcome ![{\\omega \\in
\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega+%5Cin+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\omega \in \Omega}").
Given a finite number
![{X\_1,\\dots,X\_n}](https://s0.wp.com/latex.php?latex=%7BX_1%2C%5Cdots%2CX_n%7D&bg=ffffff&fg=000000&s=0 "{X_1,\dots,X_n}")
of random variables taking values in ranges
![{R\_1,\\dots,R\_n}](https://s0.wp.com/latex.php?latex=%7BR_1%2C%5Cdots%2CR_n%7D&bg=ffffff&fg=000000&s=0 "{R_1,\dots,R_n}"),
we can form the joint random variable
![{(X\_1,\\dots,X\_n)}](https://s0.wp.com/latex.php?latex=%7B%28X_1%2C%5Cdots%2CX_n%29%7D&bg=ffffff&fg=000000&s=0 "{(X_1,\dots,X_n)}")
taking values in the Cartesian product ![{R\_1 \\times \\dots \\times
R\_n}](https://s0.wp.com/latex.php?latex=%7BR_1+%5Ctimes+%5Cdots+%5Ctimes+R_n%7D&bg=ffffff&fg=000000&s=0 "{R_1 \times \dots \times R_n}")
by concatenation of the models, thus

![\\displaystyle (X\_1,\\dots,X\_n)\_\\Omega: \\omega \\mapsto
((X\_1)\_\\Omega(\\omega),\\dots,
(X\_n)\_{\\Omega}(\\omega)).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%28X_1%2C%5Cdots%2CX_n%29_%5COmega%3A+%5Comega+%5Cmapsto+%28%28X_1%29_%5COmega%28%5Comega%29%2C%5Cdots%2C+%28X_n%29_%7B%5COmega%7D%28%5Comega%29%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  (X_1,\dots,X_n)_\Omega: \omega \mapsto ((X_1)_\Omega(\omega),\dots, (X_n)_{\Omega}(\omega)).")

Combining these two operations, given any function ![{f: R\_1 \\times
\\dots \\times R\_n \\rightarrow
S}](https://s0.wp.com/latex.php?latex=%7Bf%3A+R_1+%5Ctimes+%5Cdots+%5Ctimes+R_n+%5Crightarrow+S%7D&bg=ffffff&fg=000000&s=0 "{f: R_1 \times \dots \times R_n \rightarrow S}")
of
![{n}](https://s0.wp.com/latex.php?latex=%7Bn%7D&bg=ffffff&fg=000000&s=0 "{n}")
variables in ranges
![{R\_1,\\dots,R\_n}](https://s0.wp.com/latex.php?latex=%7BR_1%2C%5Cdots%2CR_n%7D&bg=ffffff&fg=000000&s=0 "{R_1,\dots,R_n}"),
and random variables
![{X\_1,\\dots,X\_n}](https://s0.wp.com/latex.php?latex=%7BX_1%2C%5Cdots%2CX_n%7D&bg=ffffff&fg=000000&s=0 "{X_1,\dots,X_n}")
taking values in
![{R\_1,\\dots,R\_n}](https://s0.wp.com/latex.php?latex=%7BR_1%2C%5Cdots%2CR_n%7D&bg=ffffff&fg=000000&s=0 "{R_1,\dots,R_n}")
respectively, we can form a random variable
![{f(X\_1,\\dots,X\_n)}](https://s0.wp.com/latex.php?latex=%7Bf%28X_1%2C%5Cdots%2CX_n%29%7D&bg=ffffff&fg=000000&s=0 "{f(X_1,\dots,X_n)}")
taking values in
![{S}](https://s0.wp.com/latex.php?latex=%7BS%7D&bg=ffffff&fg=000000&s=0 "{S}")
by the formula

![\\displaystyle f(X\_1,\\dots,X\_n)\_\\Omega: \\omega \\mapsto
f((X\_1)\_\\Omega(\\omega),\\dots,
(X\_n)\_{\\Omega}(\\omega)).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++f%28X_1%2C%5Cdots%2CX_n%29_%5COmega%3A+%5Comega+%5Cmapsto+f%28%28X_1%29_%5COmega%28%5Comega%29%2C%5Cdots%2C+%28X_n%29_%7B%5COmega%7D%28%5Comega%29%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  f(X_1,\dots,X_n)_\Omega: \omega \mapsto f((X_1)_\Omega(\omega),\dots, (X_n)_{\Omega}(\omega)).")

Thus for instance we can add, subtract, or multiply two scalar random
variables to obtain another scalar random variable.

A deterministic element
![{x}](https://s0.wp.com/latex.php?latex=%7Bx%7D&bg=ffffff&fg=000000&s=0 "{x}")
of a range
![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
will (by abuse of notation) be identified with a random variable
![{x}](https://s0.wp.com/latex.php?latex=%7Bx%7D&bg=ffffff&fg=000000&s=0 "{x}")
taking values in
![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}"),
whose model in
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
is constant: ![{x\_\\Omega(\\omega) =
x}](https://s0.wp.com/latex.php?latex=%7Bx_%5COmega%28%5Comega%29+%3D+x%7D&bg=ffffff&fg=000000&s=0 "{x_\Omega(\omega) = x}")
for all ![{\\omega \\in
\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega+%5Cin+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\omega \in \Omega}").
Thus for instance
![{37}](https://s0.wp.com/latex.php?latex=%7B37%7D&bg=ffffff&fg=000000&s=0 "{37}")
is a scalar random variable.

Given a relation ![{F: R\_1 \\times \\dots \\times R\_n \\rightarrow \\{
\\hbox{ true}, \\hbox{
false}\\}}](https://s0.wp.com/latex.php?latex=%7BF%3A+R_1+%5Ctimes+%5Cdots+%5Ctimes+R_n+%5Crightarrow+%5C%7B+%5Chbox%7B+true%7D%2C+%5Chbox%7B+false%7D%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{F: R_1 \times \dots \times R_n \rightarrow \{ \hbox{ true}, \hbox{ false}\}}")
on
![{n}](https://s0.wp.com/latex.php?latex=%7Bn%7D&bg=ffffff&fg=000000&s=0 "{n}")
ranges
![{R\_1,\\dots,R\_n}](https://s0.wp.com/latex.php?latex=%7BR_1%2C%5Cdots%2CR_n%7D&bg=ffffff&fg=000000&s=0 "{R_1,\dots,R_n}"),
and random variables
![{X\_1,\\dots,X\_n}](https://s0.wp.com/latex.php?latex=%7BX_1%2C%5Cdots%2CX_n%7D&bg=ffffff&fg=000000&s=0 "{X_1,\dots,X_n}"),
we can define the event
![{F(X\_1,\\dots,X\_n)}](https://s0.wp.com/latex.php?latex=%7BF%28X_1%2C%5Cdots%2CX_n%29%7D&bg=ffffff&fg=000000&s=0 "{F(X_1,\dots,X_n)}")
by setting

![\\displaystyle F(X\_1,\\dots,X\_n) :=\\{ \\omega \\in \\Omega:
F((X\_1)\_\\Omega(\\omega),\\dots,(X\_n)\_\\Omega(\\omega)) \\hbox{
true}\\}.
](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28X_1%2C%5Cdots%2CX_n%29+%3A%3D%5C%7B+%5Comega+%5Cin+%5COmega%3A+F%28%28X_1%29_%5COmega%28%5Comega%29%2C%5Cdots%2C%28X_n%29_%5COmega%28%5Comega%29%29+%5Chbox%7B+true%7D%5C%7D.+&bg=ffffff&fg=000000&s=0 "\displaystyle  F(X_1,\dots,X_n) :=\{ \omega \in \Omega: F((X_1)_\Omega(\omega),\dots,(X_n)_\Omega(\omega)) \hbox{ true}\}. ")

Thus for instance, for two real random variables
![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}"),
the event ![{X &gt;
Y}](https://s0.wp.com/latex.php?latex=%7BX+%3E+Y%7D&bg=ffffff&fg=000000&s=0 "{X > Y}")
is modeled as

![\\displaystyle (X&gt;Y)\_\\Omega := \\{ \\omega \\in \\Omega:
X\_\\Omega(\\omega) &gt; Y\_\\Omega(\\omega)
\\}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%28X%3EY%29_%5COmega+%3A%3D+%5C%7B+%5Comega+%5Cin+%5COmega%3A+X_%5COmega%28%5Comega%29+%3E+Y_%5COmega%28%5Comega%29+%5C%7D&bg=ffffff&fg=000000&s=0 "\displaystyle  (X>Y)_\Omega := \{ \omega \in \Omega: X_\Omega(\omega) > Y_\Omega(\omega) \}")

and the event
![{X=Y}](https://s0.wp.com/latex.php?latex=%7BX%3DY%7D&bg=ffffff&fg=000000&s=0 "{X=Y}")
is modeled as

![\\displaystyle (X=Y)\_\\Omega := \\{ \\omega \\in \\Omega:
X\_\\Omega(\\omega) = Y\_\\Omega(\\omega)
\\}.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%28X%3DY%29_%5COmega+%3A%3D+%5C%7B+%5Comega+%5Cin+%5COmega%3A+X_%5COmega%28%5Comega%29+%3D+Y_%5COmega%28%5Comega%29+%5C%7D.&bg=ffffff&fg=000000&s=0 "\displaystyle  (X=Y)_\Omega := \{ \omega \in \Omega: X_\Omega(\omega) = Y_\Omega(\omega) \}.")

At this point we encounter a slight notational conflict between the dual
role of the equality symbol
![{=}](https://s0.wp.com/latex.php?latex=%7B%3D%7D&bg=ffffff&fg=000000&s=0 "{=}")
as a logical symbol and as a binary relation: we are interpreting
![{X=Y}](https://s0.wp.com/latex.php?latex=%7BX%3DY%7D&bg=ffffff&fg=000000&s=0 "{X=Y}")
both as an external equality relation between the two random variables
(which is true iff the functions
![{X\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega}"),
![{Y\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BY_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{Y_\Omega}")
are identical), and as an internal event (modeled by
![{(X=Y)\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%28X%3DY%29_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{(X=Y)_\Omega}")).
However, it is clear that
![{X=Y}](https://s0.wp.com/latex.php?latex=%7BX%3DY%7D&bg=ffffff&fg=000000&s=0 "{X=Y}")
is true in the external sense if and only if the internal event
![{X=Y}](https://s0.wp.com/latex.php?latex=%7BX%3DY%7D&bg=ffffff&fg=000000&s=0 "{X=Y}")
is surely true. As such, we shall abuse notation and continue to use the
equality symbol for both the internal and external concepts of equality
(and use the modifier “surely” for emphasis when referring to the
external usage).

It is clear that any equational identity concerning functions or
operations on deterministic variables implies the same identity (in the
external, or surely true, sense) for random variables. For instance, the
commutativity of addition
![{x+y=y+x}](https://s0.wp.com/latex.php?latex=%7Bx%2By%3Dy%2Bx%7D&bg=ffffff&fg=000000&s=0 "{x+y=y+x}")
for deterministic real numbers
![{x,y}](https://s0.wp.com/latex.php?latex=%7Bx%2Cy%7D&bg=ffffff&fg=000000&s=0 "{x,y}")
immediately implies the commutativity of addition:
![{X+Y=Y+X}](https://s0.wp.com/latex.php?latex=%7BX%2BY%3DY%2BX%7D&bg=ffffff&fg=000000&s=0 "{X+Y=Y+X}")
is surely true for real random variables
![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}");
similarly
![{X+0=X}](https://s0.wp.com/latex.php?latex=%7BX%2B0%3DX%7D&bg=ffffff&fg=000000&s=0 "{X+0=X}")
is surely true for all scalar random variables
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}"),
etc.. We will freely apply the usual laws of algebra for scalar random
variables without further comment.

Given an event
![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}"),
we can associate the [indicator random
variable](https://en.wikipedia.org/wiki/Indicator_function)
![{1\_E}](https://s0.wp.com/latex.php?latex=%7B1_E%7D&bg=ffffff&fg=000000&s=0 "{1_E}")
(also written as ![{{\\bf
I}(E)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+I%7D%28E%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf I}(E)}")
in some texts) to be the unique real random variable such that
![{1\_E=1}](https://s0.wp.com/latex.php?latex=%7B1_E%3D1%7D&bg=ffffff&fg=000000&s=0 "{1_E=1}")
when
![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
is true and
![{1\_E=0}](https://s0.wp.com/latex.php?latex=%7B1_E%3D0%7D&bg=ffffff&fg=000000&s=0 "{1_E=0}")
when
![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
is false, thus
![{(1\_E)\_\\Omega(\\omega)}](https://s0.wp.com/latex.php?latex=%7B%281_E%29_%5COmega%28%5Comega%29%7D&bg=ffffff&fg=000000&s=0 "{(1_E)_\Omega(\omega)}")
is equal to
![{1}](https://s0.wp.com/latex.php?latex=%7B1%7D&bg=ffffff&fg=000000&s=0 "{1}")
when ![{\\omega \\in
E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega+%5Cin+E_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\omega \in E_\Omega}")
and
![{0}](https://s0.wp.com/latex.php?latex=%7B0%7D&bg=ffffff&fg=000000&s=0 "{0}")
otherwise. (The indicator random variable is sometimes called the
*characteristic function* in analysis, and sometimes denoted
![{\\chi\_E}](https://s0.wp.com/latex.php?latex=%7B%5Cchi_E%7D&bg=ffffff&fg=000000&s=0 "{\chi_E}")
instead of
![{1\_E}](https://s0.wp.com/latex.php?latex=%7B1_E%7D&bg=ffffff&fg=000000&s=0 "{1_E}"),
but we avoid using the term “characteristic function” here, as it will
have an [unrelated but important
meaning](https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory))
in probability theory.) We record the trivial but useful fact that
Boolean operations on events correspond to arithmetic manipulations on
their indicators. For instance, if
![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
are events, we have

![\\displaystyle 1\_{E \\wedge F} = 1\_E
1\_F](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++1_%7BE+%5Cwedge+F%7D+%3D+1_E+1_F&bg=ffffff&fg=000000&s=0 "\displaystyle  1_{E \wedge F} = 1_E 1_F")

![\\displaystyle 1\_{\\overline{E}} = 1 -
1\_E](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++1_%7B%5Coverline%7BE%7D%7D+%3D+1+-+1_E&bg=ffffff&fg=000000&s=0 "\displaystyle  1_{\overline{E}} = 1 - 1_E")

and the inclusion-exclusion principle

[![\\displaystyle 1\_{E \\vee F} = 1\_E + 1\_F - 1\_{E \\wedge F}. \\ \\
\\ \\ \\
(1)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++1_%7BE+%5Cvee+F%7D+%3D+1_E+%2B+1_F+-+1_%7BE+%5Cwedge+F%7D.+%5C+%5C+%5C+%5C+%5C+%281%29&bg=ffffff&fg=000000&s=0 "\displaystyle  1_{E \vee F} = 1_E + 1_F - 1_{E \wedge F}. \ \ \ \ \ (1)")]()

In particular, if the events
![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
are disjoint, then

![\\displaystyle 1\_{E \\vee F} = 1\_E +
1\_F.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++1_%7BE+%5Cvee+F%7D+%3D+1_E+%2B+1_F.&bg=ffffff&fg=000000&s=0 "\displaystyle  1_{E \vee F} = 1_E + 1_F.")

Also note that ![{E \\subset
F}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+F%7D&bg=ffffff&fg=000000&s=0 "{E \subset F}")
if and only if the assertion ![{1\_E \\leq
1\_F}](https://s0.wp.com/latex.php?latex=%7B1_E+%5Cleq+1_F%7D&bg=ffffff&fg=000000&s=0 "{1_E \leq 1_F}")
is surely true. We will use these identities and equivalences throughout
the course without further comment.

Given a scalar random variable
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}"),
we can attempt to define the
[expectation](https://en.wikipedia.org/wiki/Expected_value) ![{{\\bf
E}(X)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+E%7D%28X%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf E}(X)}")
through the model
![{X\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega}")
by the formula

![\\displaystyle {\\bf E}(X) := \\sum\_{\\omega \\in \\Omega}
X\_\\Omega(\\omega)
p\_\\omega.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+E%7D%28X%29+%3A%3D+%5Csum_%7B%5Comega+%5Cin+%5COmega%7D+X_%5COmega%28%5Comega%29+p_%5Comega.&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf E}(X) := \sum_{\omega \in \Omega} X_\Omega(\omega) p_\omega.")

If the discrete sample space
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
is finite, then this sum is always well-defined and so every scalar
random variable has an expectation. If however the discrete sample space
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
is infinite, the expectation may not be well defined. There are however
two key cases in which one has a meaningful expectation. The first is if
the random variable
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
is *unsigned*, that is to say it takes values in the non-negative reals
![{\[0,+\\infty)}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C%2B%5Cinfty%29%7D&bg=ffffff&fg=000000&s=0 "{[0,+\infty)}"),
or more generally in the extended non-negative real line
![{\[0,+\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C%2B%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,+\infty]}").
In that case, one can interpret the expectation ![{{\\bf
E}(X)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+E%7D%28X%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf E}(X)}")
as an element of
![{\[0,+\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C%2B%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,+\infty]}").
The other case is when the random variable
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
is *absolutely integrable*, which means that the absolute value
![{|X|}](https://s0.wp.com/latex.php?latex=%7B%7CX%7C%7D&bg=ffffff&fg=000000&s=0 "{|X|}")
(which is an unsigned random variable) has finite expectation: ![{{\\bf
E} |X| &lt;
\\infty}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+E%7D+%7CX%7C+%3C+%5Cinfty%7D&bg=ffffff&fg=000000&s=0 "{{\bf E} |X| < \infty}").
In that case, the series defining ![{{\\bf
E}(X)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+E%7D%28X%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf E}(X)}")
is absolutely convergent to a real or complex number (depending on
whether
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
was a real or complex random variable.)

We have the basic link

![\\displaystyle {\\bf P}(E) = {\\bf
E}(1\_E)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28E%29+%3D+%7B%5Cbf+E%7D%281_E%29&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(E) = {\bf E}(1_E)")

between probability and expectation, valid for any event
![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}").
We also have the obvious, but fundamentally important, property of
*linearity of expectation*: we have

![\\displaystyle {\\bf E}(cX) = c {\\bf
E}(X)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+E%7D%28cX%29+%3D+c+%7B%5Cbf+E%7D%28X%29&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf E}(cX) = c {\bf E}(X)")

and

![\\displaystyle {\\bf E}(X+Y) = {\\bf E}(X) + {\\bf
E}(Y)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+E%7D%28X%2BY%29+%3D+%7B%5Cbf+E%7D%28X%29+%2B+%7B%5Cbf+E%7D%28Y%29&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf E}(X+Y) = {\bf E}(X) + {\bf E}(Y)")

whenever
![{c}](https://s0.wp.com/latex.php?latex=%7Bc%7D&bg=ffffff&fg=000000&s=0 "{c}")
is a scalar and
![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}")
are scalar random variables, either under the assumption that
![{c,X,Y}](https://s0.wp.com/latex.php?latex=%7Bc%2CX%2CY%7D&bg=ffffff&fg=000000&s=0 "{c,X,Y}")
are all unsigned, or that
![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}")
are absolutely integrable. Thus for instance by applying expectations to
[(1)](#iep) we obtain the identity

![\\displaystyle {\\bf P}(E \\vee F) = {\\bf P}(E) + {\\bf P}(F) - {\\bf
P}(E \\wedge
F).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28E+%5Cvee+F%29+%3D+%7B%5Cbf+P%7D%28E%29+%2B+%7B%5Cbf+P%7D%28F%29+-+%7B%5Cbf+P%7D%28E+%5Cwedge+F%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(E \vee F) = {\bf P}(E) + {\bf P}(F) - {\bf P}(E \wedge F).")

We close this section by noting that discrete probabilistic models
stumble when trying to model *continuous* random variables, which take
on an uncountable number of values. Suppose for instance one wants to
model a random real number
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
drawn uniformly at random from the unit interval
![{\[0,1\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,1]}"),
which is an uncountable set. One would then expect, for any subinterval
![{\[a,b\]}](https://s0.wp.com/latex.php?latex=%7B%5Ba%2Cb%5D%7D&bg=ffffff&fg=000000&s=0 "{[a,b]}")
of
![{\[0,1\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,1]}"),
that
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
will fall into this interval with probability
![{b-a}](https://s0.wp.com/latex.php?latex=%7Bb-a%7D&bg=ffffff&fg=000000&s=0 "{b-a}").
Setting
![{a=b}](https://s0.wp.com/latex.php?latex=%7Ba%3Db%7D&bg=ffffff&fg=000000&s=0 "{a=b}")
(or, if one wishes instead, taking a limit such as ![{b \\rightarrow
a^+}](https://s0.wp.com/latex.php?latex=%7Bb+%5Crightarrow+a%5E%2B%7D&bg=ffffff&fg=000000&s=0 "{b \rightarrow a^+}")),
we conclude in particular that for any real number
![{a}](https://s0.wp.com/latex.php?latex=%7Ba%7D&bg=ffffff&fg=000000&s=0 "{a}")
in
![{\[0,1\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,1]}"),
that
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
will equal
![{a}](https://s0.wp.com/latex.php?latex=%7Ba%7D&bg=ffffff&fg=000000&s=0 "{a}")
with probability
![{0}](https://s0.wp.com/latex.php?latex=%7B0%7D&bg=ffffff&fg=000000&s=0 "{0}").
If one attempted to model this situation by a discrete probability
model, we would find that each outcome
![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}")
of the discrete sample space
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
has to occur with probability ![{p\_\\omega =
0}](https://s0.wp.com/latex.php?latex=%7Bp_%5Comega+%3D+0%7D&bg=ffffff&fg=000000&s=0 "{p_\omega = 0}")
(since for each
![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}"),
the random variable
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
has only a single value
![{X\_\\Omega(\\omega)}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%28%5Comega%29%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega(\omega)}")).
But we are also requiring that the sum ![{\\sum\_{\\omega \\in \\Omega}
p\_\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Csum_%7B%5Comega+%5Cin+%5COmega%7D+p_%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\sum_{\omega \in \Omega} p_\omega}")
is equal to
![{1}](https://s0.wp.com/latex.php?latex=%7B1%7D&bg=ffffff&fg=000000&s=0 "{1}"),
a contradiction. In order to address this defect we must generalise from
discrete models to more general probabilistic models, to which we now
turn.

**— 3. The Kolmogorov foundations of probability theory —**

We now present the more general measure-theoretic foundation of
Kolmogorov which subsumes the discrete theory, while also allowing one
to model continuous random variables. It turns out that in order to
perform sums, limits and integrals properly, the finite additivity
property of probability needs to be amplified to *countable* additivity
(but, as we shall see, *uncountable* additivity is too strong of a
property to ask for).

We begin with the notion of a measurable space. (See also this [previous
blog
post](https://terrytao.wordpress.com/2010/09/25/245a-notes-3-integration-on-abstract-measure-spaces-and-the-convergence-theorems/),
which covers similar material from the perspective of a real analysis
graduate class rather than a probability class.)

> **Definition 4 (Measurable space)** Let
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> be a set. A [Boolean
> algebra](https://en.wikipedia.org/wiki/Boolean_algebra) in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is a collection ![{{\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}")
> of subsets of
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> which
>
> -   contains
>     ![{\\emptyset}](https://s0.wp.com/latex.php?latex=%7B%5Cemptyset%7D&bg=ffffff&fg=000000&s=0 "{\emptyset}")
>     and
>     ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}");
> -   is closed under pairwise unions and intersections (thus if ![{E,F
>     \\in {\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7BE%2CF+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{E,F \in {\mathcal F}}"),
>     then ![{E \\cup
>     F}](https://s0.wp.com/latex.php?latex=%7BE+%5Ccup+F%7D&bg=ffffff&fg=000000&s=0 "{E \cup F}")
>     and ![{E \\cap
>     F}](https://s0.wp.com/latex.php?latex=%7BE+%5Ccap+F%7D&bg=ffffff&fg=000000&s=0 "{E \cap F}")
>     also lie in ![{{\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}"));
>     and
> -   is closed under complements (thus if ![{E \\in {\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7BE+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{E \in {\mathcal F}}"),
>     then ![{\\Omega \\backslash
>     E}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%5Cbackslash+E%7D&bg=ffffff&fg=000000&s=0 "{\Omega \backslash E}")
>     also lies in ![{{\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}").
>
> (Note that some of these assumptions are redundant and can be dropped,
> thanks to [de Morgan’s
> laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws).) A
> [![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra](https://en.wikipedia.org/wiki/Sigma-algebra)
> in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> (also known as a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-field)
> is a Boolean algebra ![{{\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}")
> in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> which is also
>
> -   closed under countable unions and countable intersections (thus if
>     ![{E\_1,E\_2,E\_3,\\dots \\in {\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7BE_1%2CE_2%2CE_3%2C%5Cdots+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{E_1,E_2,E_3,\dots \in {\mathcal F}}"),
>     then ![{\\bigcup\_{n=1}^\\infty E\_n \\in {\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7B%5Cbigcup_%7Bn%3D1%7D%5E%5Cinfty+E_n+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{\bigcup_{n=1}^\infty E_n \in {\mathcal F}}")
>     and ![{\\bigcap\_{n=1}^\\infty E\_n \\in {\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7B%5Cbigcap_%7Bn%3D1%7D%5E%5Cinfty+E_n+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{\bigcap_{n=1}^\infty E_n \in {\mathcal F}}")).
>
> Again, thanks to de Morgan’s laws, one only needs to verify closure
> under just countable union (or just countable intersection) in order
> to verify that a Boolean algebra is a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra.
> A *measurable space* is a pair ![{(\\Omega, {\\mathcal
> F})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%7B%5Cmathcal+F%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, {\mathcal F})}"),
> where
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is a set and ![{{\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}")
> is a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}").
> Elements of ![{{\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}")
> are referred to as *measurable sets* in this measurable space.
>
> If ![{{\\mathcal F}, {\\mathcal
> F}'}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%2C+%7B%5Cmathcal+F%7D%27%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}, {\mathcal F}'}")
> are two
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebras
> in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> we say that ![{{\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}")
> is *coarser than* ![{{\\mathcal
> F}'}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%27%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}'}")
> (or ![{{\\mathcal
> F}'}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%27%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}'}")
> is *finer than* ![{{\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}"))
> if ![{{\\mathcal F} \\subset {\\mathcal
> F}'}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D+%5Csubset+%7B%5Cmathcal+F%7D%27%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F} \subset {\mathcal F}'}"),
> thus every set that is measurable in ![{(\\Omega,{\\mathcal
> F})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C%7B%5Cmathcal+F%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega,{\mathcal F})}")
> is also measurable in ![{(\\Omega,{\\mathcal
> F}')}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C%7B%5Cmathcal+F%7D%27%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega,{\mathcal F}')}").

> **Example 5 (Trivial measurable space)** Given any set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> the collection ![{\\{\\emptyset,
> \\Omega\\}}](https://s0.wp.com/latex.php?latex=%7B%5C%7B%5Cemptyset%2C+%5COmega%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\{\emptyset, \Omega\}}")
> is a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra;
> in fact it is the coarsest
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> one can place on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}").
> We refer to ![{(\\Omega,
> \\{\\emptyset,\\Omega\\})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%5C%7B%5Cemptyset%2C%5COmega%5C%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, \{\emptyset,\Omega\})}")
> as the *trivial* measurable space on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}").

> **Example 6 (Discrete measurable space)** At the other extreme, given
> any set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> the power set ![{2^\\Omega := \\{ E: E \\subset
> \\Omega\\}}](https://s0.wp.com/latex.php?latex=%7B2%5E%5COmega+%3A%3D+%5C%7B+E%3A+E+%5Csubset+%5COmega%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{2^\Omega := \{ E: E \subset \Omega\}}")
> is a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> (and is the finest
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> one can place on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")).
> We refer to ![{(\\Omega,
> 2^\\Omega)}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+2%5E%5COmega%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, 2^\Omega)}")
> as the *discrete* measurable space on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}").

> **Example 7 (Atomic measurable spaces)** Suppose we have a partition
> ![{\\Omega = \\biguplus\_{\\alpha \\in A}
> E\_\\alpha}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%5Cbiguplus_%7B%5Calpha+%5Cin+A%7D+E_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{\Omega = \biguplus_{\alpha \in A} E_\alpha}")
> of a set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> into disjoint subsets
> ![{E\_\\alpha}](https://s0.wp.com/latex.php?latex=%7BE_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{E_\alpha}")
> (which we will call *atoms*), indexed by some label set
> ![{A}](https://s0.wp.com/latex.php?latex=%7BA%7D&bg=ffffff&fg=000000&s=0 "{A}")
> (which may be finite, countable, or uncountable). Such a partition
> defines a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> consisting of all sets of the form ![{\\bigcup\_{\\alpha \\in B}
> E\_\\alpha}](https://s0.wp.com/latex.php?latex=%7B%5Cbigcup_%7B%5Calpha+%5Cin+B%7D+E_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{\bigcup_{\alpha \in B} E_\alpha}")
> for subsets
> ![{B}](https://s0.wp.com/latex.php?latex=%7BB%7D&bg=ffffff&fg=000000&s=0 "{B}")
> of
> ![{A}](https://s0.wp.com/latex.php?latex=%7BA%7D&bg=ffffff&fg=000000&s=0 "{A}")
> (we allow
> ![{B}](https://s0.wp.com/latex.php?latex=%7BB%7D&bg=ffffff&fg=000000&s=0 "{B}")
> to be empty); thus a set is measurable here if and only if it can be
> described as a union of atoms. One can easily verify that this is
> indeed a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra.
> The trivial and discrete measurable spaces in the preceding two
> examples are special cases of this atomic construction, corresponding
> to the trivial partition ![{\\Omega =
> \\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega = \Omega}")
> (in which there is just one atom
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"))
> and the discrete partition ![{\\Omega = \\biguplus\_{x \\in \\Omega}
> \\{x\\}}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%5Cbiguplus_%7Bx+%5Cin+%5COmega%7D+%5C%7Bx%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\Omega = \biguplus_{x \in \Omega} \{x\}}")
> (in which the atoms are individual points in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")).

> **Example 8** Let
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> be an uncountable set, and let ![{{\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}}")
> be the collection of sets in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> which are either at most countable, or are cocountable (their
> complement is at most countable). Show that this is a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> which is non-atomic (i.e. it is not of the form of the preceding
> example).

> **Example 9 (Generated measurable spaces)** It is easy to see that if
> one has a non-empty family ![{({\\mathcal F}\_\\alpha)\_{\\alpha \\in
> A}}](https://s0.wp.com/latex.php?latex=%7B%28%7B%5Cmathcal+F%7D_%5Calpha%29_%7B%5Calpha+%5Cin+A%7D%7D&bg=ffffff&fg=000000&s=0 "{({\mathcal F}_\alpha)_{\alpha \in A}}")
> of
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebras
> on a set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> then their intersection ![{\\bigcap\_{\\alpha \\in A} {\\mathcal
> F}\_\\alpha}](https://s0.wp.com/latex.php?latex=%7B%5Cbigcap_%7B%5Calpha+%5Cin+A%7D+%7B%5Cmathcal+F%7D_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{\bigcap_{\alpha \in A} {\mathcal F}_\alpha}")
> is also a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra,
> even if
> ![{A}](https://s0.wp.com/latex.php?latex=%7BA%7D&bg=ffffff&fg=000000&s=0 "{A}")
> is uncountably infinite. Because of this, whenever one has an
> arbitrary collection ![{{\\mathcal
> A}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+A%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal A}}")
> of subsets in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> one can define the
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> ![{\\langle {\\mathcal A}
> \\rangle}](https://s0.wp.com/latex.php?latex=%7B%5Clangle+%7B%5Cmathcal+A%7D+%5Crangle%7D&bg=ffffff&fg=000000&s=0 "{\langle {\mathcal A} \rangle}")*generated*
> by ![{{\\mathcal
> A}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+A%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal A}}")
> to be the intersection of all the
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebras
> that contain ![{{\\mathcal
> A}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+A%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal A}}")
> (note that there is always at least one
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> participating in this intersection, namely the discrete
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra).
> Equivalently, ![{\\langle {\\mathcal A}
> \\rangle}](https://s0.wp.com/latex.php?latex=%7B%5Clangle+%7B%5Cmathcal+A%7D+%5Crangle%7D&bg=ffffff&fg=000000&s=0 "{\langle {\mathcal A} \rangle}")
> is the coarsest
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> that views every set in ![{{\\mathcal
> A}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+A%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal A}}")
> as being measurable. (This is a rather indirect way to describe
> ![{\\langle {\\mathcal A}
> \\rangle}](https://s0.wp.com/latex.php?latex=%7B%5Clangle+%7B%5Cmathcal+A%7D+%5Crangle%7D&bg=ffffff&fg=000000&s=0 "{\langle {\mathcal A} \rangle}"),
> as it does not make it easy to figure out exactly what sets lie in
> ![{\\langle {\\mathcal A}
> \\rangle}](https://s0.wp.com/latex.php?latex=%7B%5Clangle+%7B%5Cmathcal+A%7D+%5Crangle%7D&bg=ffffff&fg=000000&s=0 "{\langle {\mathcal A} \rangle}").
> There is a more direct description of this
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra,
> but it requires the use of the [first uncountable
> ordinal](https://en.wikipedia.org/wiki/First_uncountable_ordinal); see
> Exercise 15 of [these
> notes](https://terrytao.wordpress.com/2010/09/25/245a-notes-3-integration-on-abstract-measure-spaces-and-the-convergence-theorems/).)
> In Durrett, the notation ![{\\sigma({\\mathcal
> A})}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%28%7B%5Cmathcal+A%7D%29%7D&bg=ffffff&fg=000000&s=0 "{\sigma({\mathcal A})}")
> is used in place of ![{\\langle {\\mathcal
> A}\\rangle}](https://s0.wp.com/latex.php?latex=%7B%5Clangle+%7B%5Cmathcal+A%7D%5Crangle%7D&bg=ffffff&fg=000000&s=0 "{\langle {\mathcal A}\rangle}").

> **Example 10 (Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra)**
> Let
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> be a topological space; to avoid pathologies let us assume that
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is locally compact Hausdorff and
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-compact,
> though the definition below also can be made for more general spaces.
> For instance, one could take ![{\\Omega = {\\bf
> R}^n}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{\Omega = {\bf R}^n}")
> or ![{\\Omega = {\\bf
> C}^n}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%7B%5Cbf+C%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{\Omega = {\bf C}^n}")
> for some finite
> ![{n}](https://s0.wp.com/latex.php?latex=%7Bn%7D&bg=ffffff&fg=000000&s=0 "{n}").
> We define the [Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra](https://en.wikipedia.org/wiki/Borel_set)
> on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> to be the
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> generated by the open sets of
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}").
> (Due to our topological hypotheses on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> is also generated by the compact sets of
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}").)
> Measurable subsets in the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> are known as *Borel sets*. Thus for instance open and closed sets are
> Borel, and countable unions and countable intersections of Borel sets
> are Borel. In fact, as a rule of thumb, any subset of ![{{\\bf
> R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}")
> or ![{{\\bf
> C}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+C%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf C}^n}")
> that arises from a “non-pathological” construction (not using the
> axiom of choice, or from a deliberate attempt to build a non-Borel
> set) can be expected to be a Borel set. Nevertheless, non-Borel sets
> exist in abundance if one looks hard enough for them, even without the
> axiom of choice; see for instance Exercise 16 of [this previous blog
> post](https://terrytao.wordpress.com/2010/09/25/245a-notes-3-integration-on-abstract-measure-spaces-and-the-convergence-theorems/).

The following exercise gives a useful tool (somewhat analogous to
mathematical induction) to verify properties regarding measurable sets
in generated
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebras,
such as Borel
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebras.

> **Exercise 11** Let ![{{\\mathcal
> A}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+A%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal A}}")
> be a collection of subsets of a set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
> and let
> ![{P(E)}](https://s0.wp.com/latex.php?latex=%7BP%28E%29%7D&bg=ffffff&fg=000000&s=0 "{P(E)}")
> be a property of subsets
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> of
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> (thus
> ![{P(E)}](https://s0.wp.com/latex.php?latex=%7BP%28E%29%7D&bg=ffffff&fg=000000&s=0 "{P(E)}")
> is true or false for each
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")).
> Assume the following axioms:
>
> -   ![{P(\\emptyset)}](https://s0.wp.com/latex.php?latex=%7BP%28%5Cemptyset%29%7D&bg=ffffff&fg=000000&s=0 "{P(\emptyset)}")
>     is true.
> -   ![{P(E)}](https://s0.wp.com/latex.php?latex=%7BP%28E%29%7D&bg=ffffff&fg=000000&s=0 "{P(E)}")
>     is true for all ![{E \\in {\\mathcal
>     A}}](https://s0.wp.com/latex.php?latex=%7BE+%5Cin+%7B%5Cmathcal+A%7D%7D&bg=ffffff&fg=000000&s=0 "{E \in {\mathcal A}}").
> -   If ![{E \\subset
>     \\Omega}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E \subset \Omega}")
>     is such that
>     ![{P(E)}](https://s0.wp.com/latex.php?latex=%7BP%28E%29%7D&bg=ffffff&fg=000000&s=0 "{P(E)}")
>     is true, then ![{P(\\Omega \\backslash
>     E)}](https://s0.wp.com/latex.php?latex=%7BP%28%5COmega+%5Cbackslash+E%29%7D&bg=ffffff&fg=000000&s=0 "{P(\Omega \backslash E)}")
>     is also true.
> -   If ![{E\_1, E\_2, \\dots \\subset
>     \\Omega}](https://s0.wp.com/latex.php?latex=%7BE_1%2C+E_2%2C+%5Cdots+%5Csubset+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_1, E_2, \dots \subset \Omega}")
>     are such that
>     ![{P(E\_n)}](https://s0.wp.com/latex.php?latex=%7BP%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{P(E_n)}")
>     is true for all
>     ![{n}](https://s0.wp.com/latex.php?latex=%7Bn%7D&bg=ffffff&fg=000000&s=0 "{n}"),
>     then ![{P(\\bigcup\_n
>     E\_n)}](https://s0.wp.com/latex.php?latex=%7BP%28%5Cbigcup_n+E_n%29%7D&bg=ffffff&fg=000000&s=0 "{P(\bigcup_n E_n)}")
>     is true.
>
> Show that
> ![{P(E)}](https://s0.wp.com/latex.php?latex=%7BP%28E%29%7D&bg=ffffff&fg=000000&s=0 "{P(E)}")
> is true for all ![{E \\in \\langle {\\mathcal A}
> \\rangle}](https://s0.wp.com/latex.php?latex=%7BE+%5Cin+%5Clangle+%7B%5Cmathcal+A%7D+%5Crangle%7D&bg=ffffff&fg=000000&s=0 "{E \in \langle {\mathcal A} \rangle}").
> (*Hint:* what can one say about ![{\\{ E \\subset \\Omega: P(E)
> \\hbox{
> true}\\}}](https://s0.wp.com/latex.php?latex=%7B%5C%7B+E+%5Csubset+%5COmega%3A+P%28E%29+%5Chbox%7B+true%7D%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\{ E \subset \Omega: P(E) \hbox{ true}\}}")?)

Thus, for instance, if a property of subsets of ![{{\\bf
R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}")
is true for all open sets, and is closed under countable unions and
complements, then it is automatically true for all Borel sets.

> **Example 12 (Pullback)** Let ![{(R, {\\mathcal
> B})}](https://s0.wp.com/latex.php?latex=%7B%28R%2C+%7B%5Cmathcal+B%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(R, {\mathcal B})}")
> be a measurable space, and let ![{\\phi: \\Omega \\rightarrow
> R}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%3A+%5COmega+%5Crightarrow+R%7D&bg=ffffff&fg=000000&s=0 "{\phi: \Omega \rightarrow R}")
> be any function from another set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> to
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}").
> Then we can define the *pullback* ![{\\phi^\*({\\mathcal
> B})}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%5E%2A%28%7B%5Cmathcal+B%7D%29%7D&bg=ffffff&fg=000000&s=0 "{\phi^*({\mathcal B})}")
> of the
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> ![{{\\mathcal
> B}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+B%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal B}}")
> to be the collection of all subsets in
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> that are of the form
> ![{\\phi^{-1}(S)}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%5E%7B-1%7D%28S%29%7D&bg=ffffff&fg=000000&s=0 "{\phi^{-1}(S)}")
> for some ![{S \\in {\\mathcal
> B}}](https://s0.wp.com/latex.php?latex=%7BS+%5Cin+%7B%5Cmathcal+B%7D%7D&bg=ffffff&fg=000000&s=0 "{S \in {\mathcal B}}").
> This is easily verified to be a
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra.
> We refer to the measurable space ![{(\\Omega, \\phi^\*({\\mathcal
> B}))}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%5Cphi%5E%2A%28%7B%5Cmathcal+B%7D%29%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, \phi^*({\mathcal B}))}")
> as the pullback of the measurable space ![{(R, {\\mathcal
> B})}](https://s0.wp.com/latex.php?latex=%7B%28R%2C+%7B%5Cmathcal+B%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(R, {\mathcal B})}")
> by
> ![{\\phi}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%7D&bg=ffffff&fg=000000&s=0 "{\phi}").
> Thus for instance an atomic measurable space on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> generated by a partition ![{\\Omega = \\biguplus\_{\\alpha \\in A}
> E\_\\alpha}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%5Cbiguplus_%7B%5Calpha+%5Cin+A%7D+E_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{\Omega = \biguplus_{\alpha \in A} E_\alpha}")
> is the pullback of
> ![{A}](https://s0.wp.com/latex.php?latex=%7BA%7D&bg=ffffff&fg=000000&s=0 "{A}")
> (viewed as a discrete measurable space) by the “colouring” map from
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> to
> ![{A}](https://s0.wp.com/latex.php?latex=%7BA%7D&bg=ffffff&fg=000000&s=0 "{A}")
> that sends each element of
> ![{E\_\\alpha}](https://s0.wp.com/latex.php?latex=%7BE_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{E_\alpha}")
> to
> ![{\\alpha}](https://s0.wp.com/latex.php?latex=%7B%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{\alpha}")
> for all ![{\\alpha \\in
> A}](https://s0.wp.com/latex.php?latex=%7B%5Calpha+%5Cin+A%7D&bg=ffffff&fg=000000&s=0 "{\alpha \in A}").

> **Remark 13** In probabilistic terms, one can interpret the space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> in the above construction as a sample space, and the function
> ![{\\phi}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%7D&bg=ffffff&fg=000000&s=0 "{\phi}")
> as some collection of “random variables” or “measurements” on that
> space, with
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
> being all the possible outcomes of these measurements. The pullback
> then represents all the “information” one can extract from that given
> set of measurements.

> **Example 14 (Product space)** Let ![{(R\_\\alpha, {\\mathcal
> B}\_\\alpha)\_{\\alpha \\in
> A}}](https://s0.wp.com/latex.php?latex=%7B%28R_%5Calpha%2C+%7B%5Cmathcal+B%7D_%5Calpha%29_%7B%5Calpha+%5Cin+A%7D%7D&bg=ffffff&fg=000000&s=0 "{(R_\alpha, {\mathcal B}_\alpha)_{\alpha \in A}}")
> be a family of measurable spaces indexed by a (possibly infinite or
> uncountable) set
> ![{A}](https://s0.wp.com/latex.php?latex=%7BA%7D&bg=ffffff&fg=000000&s=0 "{A}").
> We define the product ![{(\\prod\_{\\alpha \\in A} R\_\\alpha,
> \\prod\_{\\alpha \\in A} {\\mathcal
> B}\_\\alpha)}](https://s0.wp.com/latex.php?latex=%7B%28%5Cprod_%7B%5Calpha+%5Cin+A%7D+R_%5Calpha%2C+%5Cprod_%7B%5Calpha+%5Cin+A%7D+%7B%5Cmathcal+B%7D_%5Calpha%29%7D&bg=ffffff&fg=000000&s=0 "{(\prod_{\alpha \in A} R_\alpha, \prod_{\alpha \in A} {\mathcal B}_\alpha)}")
> on the Cartesian product space ![{\\prod\_{\\alpha \\in A}
> R\_\\alpha}](https://s0.wp.com/latex.php?latex=%7B%5Cprod_%7B%5Calpha+%5Cin+A%7D+R_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{\prod_{\alpha \in A} R_\alpha}")
> by defining ![{\\prod\_{\\alpha \\in A} {\\mathcal
> B}\_\\alpha}](https://s0.wp.com/latex.php?latex=%7B%5Cprod_%7B%5Calpha+%5Cin+A%7D+%7B%5Cmathcal+B%7D_%5Calpha%7D&bg=ffffff&fg=000000&s=0 "{\prod_{\alpha \in A} {\mathcal B}_\alpha}")
> to be the
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> generated by the [basic cylinder
> sets](https://en.wikipedia.org/wiki/Cylinder_set) of the form
>
> ![\\displaystyle \\{ (x\_\\alpha)\_{\\alpha \\in A} \\in
> \\prod\_{\\alpha \\in A} R\_\\alpha: x\_\\beta \\in E\_\\beta
> \\}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5C%7B+%28x_%5Calpha%29_%7B%5Calpha+%5Cin+A%7D+%5Cin+%5Cprod_%7B%5Calpha+%5Cin+A%7D+R_%5Calpha%3A+x_%5Cbeta+%5Cin+E_%5Cbeta+%5C%7D&bg=ffffff&fg=000000&s=0 "\displaystyle  \{ (x_\alpha)_{\alpha \in A} \in \prod_{\alpha \in A} R_\alpha: x_\beta \in E_\beta \}")
>
> for ![{\\beta \\in
> A}](https://s0.wp.com/latex.php?latex=%7B%5Cbeta+%5Cin+A%7D&bg=ffffff&fg=000000&s=0 "{\beta \in A}")
> and ![{E\_\\beta \\in {\\mathcal
> B}\_\\beta}](https://s0.wp.com/latex.php?latex=%7BE_%5Cbeta+%5Cin+%7B%5Cmathcal+B%7D_%5Cbeta%7D&bg=ffffff&fg=000000&s=0 "{E_\beta \in {\mathcal B}_\beta}").
> For instance, given two measurable spaces ![{(R\_1, {\\mathcal
> B}\_1)}](https://s0.wp.com/latex.php?latex=%7B%28R_1%2C+%7B%5Cmathcal+B%7D_1%29%7D&bg=ffffff&fg=000000&s=0 "{(R_1, {\mathcal B}_1)}")
> and ![{(R\_2, {\\mathcal
> B}\_2)}](https://s0.wp.com/latex.php?latex=%7B%28R_2%2C+%7B%5Cmathcal+B%7D_2%29%7D&bg=ffffff&fg=000000&s=0 "{(R_2, {\mathcal B}_2)}"),
> the product
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> ![{{\\mathcal B}\_1 \\times {\\mathcal
> B}\_2}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+B%7D_1+%5Ctimes+%7B%5Cmathcal+B%7D_2%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal B}_1 \times {\mathcal B}_2}")
> is generated by the sets ![{E\_1 \\times
> R\_2}](https://s0.wp.com/latex.php?latex=%7BE_1+%5Ctimes+R_2%7D&bg=ffffff&fg=000000&s=0 "{E_1 \times R_2}")
> and ![{R\_1 \\times
> E\_2}](https://s0.wp.com/latex.php?latex=%7BR_1+%5Ctimes+E_2%7D&bg=ffffff&fg=000000&s=0 "{R_1 \times E_2}")
> for ![{E\_1 \\in {\\mathcal B}\_1, E\_2 \\in {\\mathcal
> B}\_2}](https://s0.wp.com/latex.php?latex=%7BE_1+%5Cin+%7B%5Cmathcal+B%7D_1%2C+E_2+%5Cin+%7B%5Cmathcal+B%7D_2%7D&bg=ffffff&fg=000000&s=0 "{E_1 \in {\mathcal B}_1, E_2 \in {\mathcal B}_2}").
> (One can also show that ![{{\\mathcal B}\_1 \\times {\\mathcal
> B}\_2}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+B%7D_1+%5Ctimes+%7B%5Cmathcal+B%7D_2%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal B}_1 \times {\mathcal B}_2}")
> is the
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> generated by the products ![{E\_1 \\times
> E\_2}](https://s0.wp.com/latex.php?latex=%7BE_1+%5Ctimes+E_2%7D&bg=ffffff&fg=000000&s=0 "{E_1 \times E_2}")
> for ![{E\_1 \\in {\\mathcal B}\_1, E\_2 \\in {\\mathcal
> B}\_2}](https://s0.wp.com/latex.php?latex=%7BE_1+%5Cin+%7B%5Cmathcal+B%7D_1%2C+E_2+%5Cin+%7B%5Cmathcal+B%7D_2%7D&bg=ffffff&fg=000000&s=0 "{E_1 \in {\mathcal B}_1, E_2 \in {\mathcal B}_2}"),
> but this observation does not extend to uncountable products of
> measurable spaces.)

> **Exercise 15** Show that ![{{\\bf
> R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}")
> with the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> is the product of
> ![{n}](https://s0.wp.com/latex.php?latex=%7Bn%7D&bg=ffffff&fg=000000&s=0 "{n}")
> copies of ![{{\\bf
> R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}")
> with the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra.

As with almost any other notion of space in mathematics, there is a
natural notion of a map (or *morphism*) between measurable spaces.

> **Definition 16** A function ![{\\phi: \\Omega \\rightarrow
> R}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%3A+%5COmega+%5Crightarrow+R%7D&bg=ffffff&fg=000000&s=0 "{\phi: \Omega \rightarrow R}")
> between two measurable spaces ![{(\\Omega, {\\mathcal
> F})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%7B%5Cmathcal+F%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, {\mathcal F})}"),
> ![{(R,{\\mathcal
> B})}](https://s0.wp.com/latex.php?latex=%7B%28R%2C%7B%5Cmathcal+B%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(R,{\mathcal B})}")
> is said to be *measurable* if one has ![{\\phi^{-1}(S) \\in {\\mathcal
> F}}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%5E%7B-1%7D%28S%29+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{\phi^{-1}(S) \in {\mathcal F}}")
> for all ![{S \\in {\\mathcal
> B}}](https://s0.wp.com/latex.php?latex=%7BS+%5Cin+%7B%5Cmathcal+B%7D%7D&bg=ffffff&fg=000000&s=0 "{S \in {\mathcal B}}").

Thus for instance the pullback of a measurable space
![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
by a map ![{\\phi: \\Omega \\rightarrow
R}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%3A+%5COmega+%5Crightarrow+R%7D&bg=ffffff&fg=000000&s=0 "{\phi: \Omega \rightarrow R}")
could alternatively be defined as the coarsest measurable space
structure on
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
for which
![{\\phi}](https://s0.wp.com/latex.php?latex=%7B%5Cphi%7D&bg=ffffff&fg=000000&s=0 "{\phi}")
is still measurable. It is clear that the composition of measurable
functions is also measurable.

> **Exercise 17** Show that any continuous map from one topological
> space
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> to another
> ![{Y}](https://s0.wp.com/latex.php?latex=%7BY%7D&bg=ffffff&fg=000000&s=0 "{Y}")
> is necessarily measurable (when one gives
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> and
> ![{Y}](https://s0.wp.com/latex.php?latex=%7BY%7D&bg=ffffff&fg=000000&s=0 "{Y}")
> the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebras).

> **Exercise 18** If ![{X\_1: \\Omega \\rightarrow R\_1, \\dots, X\_n:
> \\Omega \\rightarrow
> R\_n}](https://s0.wp.com/latex.php?latex=%7BX_1%3A+%5COmega+%5Crightarrow+R_1%2C+%5Cdots%2C+X_n%3A+%5COmega+%5Crightarrow+R_n%7D&bg=ffffff&fg=000000&s=0 "{X_1: \Omega \rightarrow R_1, \dots, X_n: \Omega \rightarrow R_n}")
> are measurable functions into measurable spaces
> ![{R\_1,\\dots,R\_m}](https://s0.wp.com/latex.php?latex=%7BR_1%2C%5Cdots%2CR_m%7D&bg=ffffff&fg=000000&s=0 "{R_1,\dots,R_m}"),
> show that the joint function ![{(X\_1,\\dots,X\_n): \\Omega
> \\rightarrow R\_1 \\times \\dots \\times
> R\_n}](https://s0.wp.com/latex.php?latex=%7B%28X_1%2C%5Cdots%2CX_n%29%3A+%5COmega+%5Crightarrow+R_1+%5Ctimes+%5Cdots+%5Ctimes+R_n%7D&bg=ffffff&fg=000000&s=0 "{(X_1,\dots,X_n): \Omega \rightarrow R_1 \times \dots \times R_n}")
> into the product space ![{R\_1 \\times \\dots \\times
> R\_n}](https://s0.wp.com/latex.php?latex=%7BR_1+%5Ctimes+%5Cdots+%5Ctimes+R_n%7D&bg=ffffff&fg=000000&s=0 "{R_1 \times \dots \times R_n}")
> defined by ![{(X\_1,\\dots,X\_n): \\omega \\mapsto
> (X\_1(\\omega),\\dots,X\_n(\\omega))}](https://s0.wp.com/latex.php?latex=%7B%28X_1%2C%5Cdots%2CX_n%29%3A+%5Comega+%5Cmapsto+%28X_1%28%5Comega%29%2C%5Cdots%2CX_n%28%5Comega%29%29%7D&bg=ffffff&fg=000000&s=0 "{(X_1,\dots,X_n): \omega \mapsto (X_1(\omega),\dots,X_n(\omega))}")
> is also measurable.

As a corollary of the above exercise, we see that if ![{X\_1: \\Omega
\\rightarrow R\_1, \\dots, X\_n: \\Omega \\rightarrow
R\_n}](https://s0.wp.com/latex.php?latex=%7BX_1%3A+%5COmega+%5Crightarrow+R_1%2C+%5Cdots%2C+X_n%3A+%5COmega+%5Crightarrow+R_n%7D&bg=ffffff&fg=000000&s=0 "{X_1: \Omega \rightarrow R_1, \dots, X_n: \Omega \rightarrow R_n}")
are measurable, and ![{F: R\_1 \\times \\dots \\times R\_n \\rightarrow
S}](https://s0.wp.com/latex.php?latex=%7BF%3A+R_1+%5Ctimes+%5Cdots+%5Ctimes+R_n+%5Crightarrow+S%7D&bg=ffffff&fg=000000&s=0 "{F: R_1 \times \dots \times R_n \rightarrow S}")
is measurable, then ![{F(X\_1,\\dots,X\_n): \\Omega \\rightarrow
S}](https://s0.wp.com/latex.php?latex=%7BF%28X_1%2C%5Cdots%2CX_n%29%3A+%5COmega+%5Crightarrow+S%7D&bg=ffffff&fg=000000&s=0 "{F(X_1,\dots,X_n): \Omega \rightarrow S}")
is also measurable. In particular, if ![{X\_1, X\_2: \\Omega
\\rightarrow {\\bf
R}}](https://s0.wp.com/latex.php?latex=%7BX_1%2C+X_2%3A+%5COmega+%5Crightarrow+%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{X_1, X_2: \Omega \rightarrow {\bf R}}")
or ![{X\_1,X\_2: \\Omega \\rightarrow {\\bf
C}}](https://s0.wp.com/latex.php?latex=%7BX_1%2CX_2%3A+%5COmega+%5Crightarrow+%7B%5Cbf+C%7D%7D&bg=ffffff&fg=000000&s=0 "{X_1,X_2: \Omega \rightarrow {\bf C}}")
are scalar measurable functions, then so are ![{X\_1
+X\_2}](https://s0.wp.com/latex.php?latex=%7BX_1+%2BX_2%7D&bg=ffffff&fg=000000&s=0 "{X_1 +X_2}"),
![{X\_1 -
X\_2}](https://s0.wp.com/latex.php?latex=%7BX_1+-+X_2%7D&bg=ffffff&fg=000000&s=0 "{X_1 - X_2}"),
![{X\_1 \\cdot
X\_2}](https://s0.wp.com/latex.php?latex=%7BX_1+%5Ccdot+X_2%7D&bg=ffffff&fg=000000&s=0 "{X_1 \cdot X_2}"),
etc..

Next, we turn measurable spaces into measure spaces by adding a measure.

> **Definition 19 (Measure spaces)** Let ![{(\\Omega, {\\mathcal
> F})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%7B%5Cmathcal+F%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, {\mathcal F})}")
> be a measurable space. A *finitely additive measure* on this space is
> a map ![{\\mu: {\\mathcal F} \\rightarrow
> \[0,+\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%3A+%7B%5Cmathcal+F%7D+%5Crightarrow+%5B0%2C%2B%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{\mu: {\mathcal F} \rightarrow [0,+\infty]}")
> obeying the following axioms:
>
> -   (Empty set)
>     ![{\\mu(\\emptyset)=0}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28%5Cemptyset%29%3D0%7D&bg=ffffff&fg=000000&s=0 "{\mu(\emptyset)=0}").
> -   (Finite additivity) If ![{E, F \\in {\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7BE%2C+F+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{E, F \in {\mathcal F}}")
>     are disjoint, then ![{\\mu(E \\cup F) = \\mu(E) +
>     \\mu(F)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28E+%5Ccup+F%29+%3D+%5Cmu%28E%29+%2B+%5Cmu%28F%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(E \cup F) = \mu(E) + \mu(F)}").
>
> A [countably additive
> measure](https://en.wikipedia.org/wiki/Measure_(mathematics)) is a
> finitely additive measure ![{\\mu: {\\mathcal F} \\rightarrow
> \[0,+\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%3A+%7B%5Cmathcal+F%7D+%5Crightarrow+%5B0%2C%2B%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{\mu: {\mathcal F} \rightarrow [0,+\infty]}")
> obeying the following additional axiom:
>
> -   (Countable additivity) If ![{E\_1, E\_2, E\_3, \\dots \\in
>     {\\mathcal
>     F}}](https://s0.wp.com/latex.php?latex=%7BE_1%2C+E_2%2C+E_3%2C+%5Cdots+%5Cin+%7B%5Cmathcal+F%7D%7D&bg=ffffff&fg=000000&s=0 "{E_1, E_2, E_3, \dots \in {\mathcal F}}")
>     are disjoint, then ![{\\mu(\\bigcup\_{n=1}^\\infty E\_n) =
>     \\sum\_{n=1}^\\infty
>     \\mu(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28%5Cbigcup_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%3D+%5Csum_%7Bn%3D1%7D%5E%5Cinfty+%5Cmu%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(\bigcup_{n=1}^\infty E_n) = \sum_{n=1}^\infty \mu(E_n)}").
>
> A [probability
> measure](https://en.wikipedia.org/wiki/Probability_measure) on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is a countably additive measure ![{\\mu: {\\mathcal F} \\rightarrow
> \[0,+\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%3A+%7B%5Cmathcal+F%7D+%5Crightarrow+%5B0%2C%2B%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{\mu: {\mathcal F} \rightarrow [0,+\infty]}")
> obeying the following additional axiom:
>
> -   (Unit total probability)
>     ![{\\mu(\\Omega)=1}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28%5COmega%29%3D1%7D&bg=ffffff&fg=000000&s=0 "{\mu(\Omega)=1}").
>
> A [measure
> space](https://en.wikipedia.org/wiki/Measure_(mathematics)#measure_space)
> is a triplet ![{\\Omega = (\\Omega, {\\mathcal F},
> \\mu)}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%28%5COmega%2C+%7B%5Cmathcal+F%7D%2C+%5Cmu%29%7D&bg=ffffff&fg=000000&s=0 "{\Omega = (\Omega, {\mathcal F}, \mu)}")
> where ![{(\\Omega,{\\mathcal
> F})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C%7B%5Cmathcal+F%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega,{\mathcal F})}")
> is a measurable space and
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
> is a measure on that space. If
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
> is furthermore a probability measure, we call ![{(\\Omega, {\\mathcal
> F},
> \\mu)}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%7B%5Cmathcal+F%7D%2C+%5Cmu%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, {\mathcal F}, \mu)}")
> a [probability
> space](https://en.wikipedia.org/wiki/Probability_space).
>
> A set of measure zero is known as a *null set*. A property
> ![{P(x)}](https://s0.wp.com/latex.php?latex=%7BP%28x%29%7D&bg=ffffff&fg=000000&s=0 "{P(x)}")
> that holds for all ![{x \\in
> \\Omega}](https://s0.wp.com/latex.php?latex=%7Bx+%5Cin+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{x \in \Omega}")
> outside of a null set is said to hold *almost everywhere* or *for
> almost every
> ![{x}](https://s0.wp.com/latex.php?latex=%7Bx%7D&bg=ffffff&fg=000000&s=0 "{x}")*.

> **Example 20 (Discrete probability measures)** Let
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> be a discrete measurable space, and for each ![{\\omega \\in
> \\Omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega+%5Cin+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\omega \in \Omega}"),
> let
> ![{p\_\\omega}](https://s0.wp.com/latex.php?latex=%7Bp_%5Comega%7D&bg=ffffff&fg=000000&s=0 "{p_\omega}")
> be a non-negative real number such that ![{\\sum\_{\\omega \\in
> \\Omega} p\_\\omega =
> 1}](https://s0.wp.com/latex.php?latex=%7B%5Csum_%7B%5Comega+%5Cin+%5COmega%7D+p_%5Comega+%3D+1%7D&bg=ffffff&fg=000000&s=0 "{\sum_{\omega \in \Omega} p_\omega = 1}").
> (Note that this implies that there are at most countably many
> ![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}")
> for which ![{p\_\\omega &gt;
> 0}](https://s0.wp.com/latex.php?latex=%7Bp_%5Comega+%3E+0%7D&bg=ffffff&fg=000000&s=0 "{p_\omega > 0}")
> – why?.) Then one can form a probability measure
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
> on
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> by defining
>
> ![\\displaystyle \\mu(E) := \\sum\_{\\omega \\in E}
> p\_\\omega](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5Cmu%28E%29+%3A%3D+%5Csum_%7B%5Comega+%5Cin+E%7D+p_%5Comega&bg=ffffff&fg=000000&s=0 "\displaystyle  \mu(E) := \sum_{\omega \in E} p_\omega")
>
> for all ![{E \\subset
> \\Omega}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E \subset \Omega}").

> **Example 21 (Lebesgue measure)** Let ![{{\\bf
> R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}")
> be given the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra.
> Then it turns out there is a unique measure
> ![{m}](https://s0.wp.com/latex.php?latex=%7Bm%7D&bg=ffffff&fg=000000&s=0 "{m}")
> on ![{{\\bf
> R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}"),
> known as [Lebesgue
> measure](https://en.wikipedia.org/wiki/Lebesgue_measure) (or more
> precisely, the restriction of Lebesgue measure to the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra)
> such that ![{m(\[a,b\]) =
> b-a}](https://s0.wp.com/latex.php?latex=%7Bm%28%5Ba%2Cb%5D%29+%3D+b-a%7D&bg=ffffff&fg=000000&s=0 "{m([a,b]) = b-a}")
> for every closed interval
> ![{\[a,b\]}](https://s0.wp.com/latex.php?latex=%7B%5Ba%2Cb%5D%7D&bg=ffffff&fg=000000&s=0 "{[a,b]}")
> with ![{-\\infty \\leq a \\leq b \\leq
> \\infty}](https://s0.wp.com/latex.php?latex=%7B-%5Cinfty+%5Cleq+a+%5Cleq+b+%5Cleq+%5Cinfty%7D&bg=ffffff&fg=000000&s=0 "{-\infty \leq a \leq b \leq \infty}")
> (this is also true if one uses open intervals or half-open intervals
> in place of closed intervals). More generally, there is a unique
> measure
> ![{m^n}](https://s0.wp.com/latex.php?latex=%7Bm%5En%7D&bg=ffffff&fg=000000&s=0 "{m^n}")
> on ![{{\\bf
> R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}")
> for any natural number
> ![{n}](https://s0.wp.com/latex.php?latex=%7Bn%7D&bg=ffffff&fg=000000&s=0 "{n}"),
> also known as Lebesgue measure, such that
>
> ![\\displaystyle m^n( \[a\_1,b\_1\] \\times \\dots
> \\times\[a\_n,b\_n\]) = (b\_1-a\_1) \\times \\dots \\times
> (b\_n-a\_n)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+m%5En%28+%5Ba_1%2Cb_1%5D+%5Ctimes+%5Cdots+%5Ctimes%5Ba_n%2Cb_n%5D%29+%3D+%28b_1-a_1%29+%5Ctimes+%5Cdots+%5Ctimes+%28b_n-a_n%29&bg=ffffff&fg=000000&s=0 "\displaystyle m^n( [a_1,b_1] \times \dots \times[a_n,b_n]) = (b_1-a_1) \times \dots \times (b_n-a_n)")
>
> for all closed boxes ![{\[a\_1,b\_1\] \\times \\dots
> \\times\[a\_n,b\_n\]}](https://s0.wp.com/latex.php?latex=%7B%5Ba_1%2Cb_1%5D+%5Ctimes+%5Cdots+%5Ctimes%5Ba_n%2Cb_n%5D%7D&bg=ffffff&fg=000000&s=0 "{[a_1,b_1] \times \dots \times[a_n,b_n]}"),
> that is to say products of
> ![{n}](https://s0.wp.com/latex.php?latex=%7Bn%7D&bg=ffffff&fg=000000&s=0 "{n}")
> closed intervals. The construction of Lebesgue measure is a little
> tricky; see [this previous blog
> post](https://terrytao.wordpress.com/2010/09/09/245a-notes-1-lebesgue-measure/)
> for details.

We can then set up general probability theory similarly to how we set up
discrete probability theory:

> **Definition 22 (Probability theory)** In probability theory, we
> choose an ambient probability space ![{\\Omega = (\\Omega,{\\mathcal
> F}\_\\Omega,\\mu)}](https://s0.wp.com/latex.php?latex=%7B%5COmega+%3D+%28%5COmega%2C%7B%5Cmathcal+F%7D_%5COmega%2C%5Cmu%29%7D&bg=ffffff&fg=000000&s=0 "{\Omega = (\Omega,{\mathcal F}_\Omega,\mu)}")
> as the randomness model, and refer to the set
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> (without the additional structures ![{{\\mathcal
> F}\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}_\Omega}"),
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}"))
> as the *sample space* for that model. We then model an *event*
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> by an element
> ![{E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega}")
> of
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
> ![{{\\mathcal
> F}\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}_\Omega}"),
> with each such element describing an event. The *probability* ![{{\\bf
> P}(E)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28E%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(E)}")
> of an event
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> is defined to be the quantity
>
> ![\\displaystyle {\\bf P}(E) := \\mu( E\_\\Omega
> ).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28E%29+%3A%3D+%5Cmu%28+E_%5COmega+%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(E) := \mu( E_\Omega ).")
>
> An event
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> is *surely true* or is the *sure event* if ![{E\_\\Omega =
> \\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega+%3D+%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega = \Omega}"),
> and is *surely false* or is the *empty event* if ![{E\_\\Omega
> =\\emptyset}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega+%3D%5Cemptyset%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega =\emptyset}").
> It is *almost surely true* or an *almost sure event* if ![{{\\bf P}(E)
> =
> 1}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28E%29+%3D+1%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(E) = 1}"),
> and *almost surely false* or a *null event* if ![{{\\bf
> P}(E)=0}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28E%29%3D0%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(E)=0}").
>
> We model random variables
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> taking values in the range
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
> by measurable functions ![{X\_\\Omega: \\Omega \\rightarrow
> R}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%3A+%5COmega+%5Crightarrow+R%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega: \Omega \rightarrow R}")
> from the sample space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> to the range
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}").
> We define real, complex, and scalar random variables as in the
> discrete case.
>
> As in the discrete case, we consider two events
> ![{E,F}](https://s0.wp.com/latex.php?latex=%7BE%2CF%7D&bg=ffffff&fg=000000&s=0 "{E,F}")
> to be equal if they are modeled by the same set: ![{E=F \\iff
> E\_\\Omega =
> F\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE%3DF+%5Ciff+E_%5COmega+%3D+F_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E=F \iff E_\Omega = F_\Omega}").
> Similarly, two random variables
> ![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}")
> taking values in a common range
> ![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
> are considered to be equal if they are modeled by the same function:
> ![{X=Y \\iff X\_\\Omega =
> Y\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BX%3DY+%5Ciff+X_%5COmega+%3D+Y_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{X=Y \iff X_\Omega = Y_\Omega}").
> Again, if the sample space
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
> is understood from context, we will usually abuse notation by
> identifying an event
> ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
> with its model
> ![{E\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BE_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{E_\Omega}"),
> and similarly identify a random variable
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> with its model
> ![{X\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega}").

As in the discrete case, set-theoretic operations on the sample space
induce similar boolean operations on events. Furthermore, since the
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
![{{\\mathcal
F}\_\\Omega}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+F%7D_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal F}_\Omega}")
is closed under countable unions and countable intersections, we may
similarly define the countable conjunction ![{\\bigwedge\_{n=1}^\\infty
E\_n}](https://s0.wp.com/latex.php?latex=%7B%5Cbigwedge_%7Bn%3D1%7D%5E%5Cinfty+E_n%7D&bg=ffffff&fg=000000&s=0 "{\bigwedge_{n=1}^\infty E_n}")
or countable disjunction ![{\\bigvee\_{n=1}^\\infty
E\_n}](https://s0.wp.com/latex.php?latex=%7B%5Cbigvee_%7Bn%3D1%7D%5E%5Cinfty+E_n%7D&bg=ffffff&fg=000000&s=0 "{\bigvee_{n=1}^\infty E_n}")
of a sequence
![{E\_1,E\_2,\\dots}](https://s0.wp.com/latex.php?latex=%7BE_1%2CE_2%2C%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{E_1,E_2,\dots}")
of events; however, we do *not* define uncountable conjunctions or
disjunctions as these may not be well-defined as events.

The axioms of a probability space then yield the [Kolmogorov axioms for
probability](https://en.wikipedia.org/wiki/Probability_axioms):

-   ![{{\\bf
    P}(\\emptyset)=0}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28%5Cemptyset%29%3D0%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(\emptyset)=0}").
-   ![{{\\bf
    P}(\\overline{\\emptyset})=1}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28%5Coverline%7B%5Cemptyset%7D%29%3D1%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(\overline{\emptyset})=1}").
-   If
    ![{E\_1,E\_2,\\dots}](https://s0.wp.com/latex.php?latex=%7BE_1%2CE_2%2C%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{E_1,E_2,\dots}")
    are disjoint events, then ![{{\\bf P}(\\bigvee\_{n=1}^\\infty E\_n)
    = \\sum\_{n=1}^\\infty {\\bf
    P}(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28%5Cbigvee_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%3D+%5Csum_%7Bn%3D1%7D%5E%5Cinfty+%7B%5Cbf+P%7D%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(\bigvee_{n=1}^\infty E_n) = \sum_{n=1}^\infty {\bf P}(E_n)}").

We can manipulate random variables just as in the discrete case, with
the only caveat being that we have to restrict attention to *measurable*
operations. For instance, if
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
is a random variable taking values in a measurable space
![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}"),
and ![{f: R \\rightarrow
S}](https://s0.wp.com/latex.php?latex=%7Bf%3A+R+%5Crightarrow+S%7D&bg=ffffff&fg=000000&s=0 "{f: R \rightarrow S}")
is a measurable map, then
![{f(X)}](https://s0.wp.com/latex.php?latex=%7Bf%28X%29%7D&bg=ffffff&fg=000000&s=0 "{f(X)}")
is well defined as a random variable taking values in
![{S}](https://s0.wp.com/latex.php?latex=%7BS%7D&bg=ffffff&fg=000000&s=0 "{S}").
Similarly, if ![{f: R\_1 \\times \\dots \\times R\_n \\rightarrow
S}](https://s0.wp.com/latex.php?latex=%7Bf%3A+R_1+%5Ctimes+%5Cdots+%5Ctimes+R_n+%5Crightarrow+S%7D&bg=ffffff&fg=000000&s=0 "{f: R_1 \times \dots \times R_n \rightarrow S}")
is a measurable map and
![{X\_1,\\dots,X\_n}](https://s0.wp.com/latex.php?latex=%7BX_1%2C%5Cdots%2CX_n%7D&bg=ffffff&fg=000000&s=0 "{X_1,\dots,X_n}")
are random variables taking values in
![{R\_1,\\dots,R\_n}](https://s0.wp.com/latex.php?latex=%7BR_1%2C%5Cdots%2CR_n%7D&bg=ffffff&fg=000000&s=0 "{R_1,\dots,R_n}")
respectively, then
![{f(X\_1,\\dots,X\_n)}](https://s0.wp.com/latex.php?latex=%7Bf%28X_1%2C%5Cdots%2CX_n%29%7D&bg=ffffff&fg=000000&s=0 "{f(X_1,\dots,X_n)}")
is a random variable taking values in
![{S}](https://s0.wp.com/latex.php?latex=%7BS%7D&bg=ffffff&fg=000000&s=0 "{S}").
Similarly we can create events
![{F(X\_1,\\dots,X\_n)}](https://s0.wp.com/latex.php?latex=%7BF%28X_1%2C%5Cdots%2CX_n%29%7D&bg=ffffff&fg=000000&s=0 "{F(X_1,\dots,X_n)}")
out of *measurable* relations ![{F: R\_1 \\times \\dots \\times R\_n
\\rightarrow \\{ \\hbox{true},
\\hbox{false}\\}}](https://s0.wp.com/latex.php?latex=%7BF%3A+R_1+%5Ctimes+%5Cdots+%5Ctimes+R_n+%5Crightarrow+%5C%7B+%5Chbox%7Btrue%7D%2C+%5Chbox%7Bfalse%7D%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{F: R_1 \times \dots \times R_n \rightarrow \{ \hbox{true}, \hbox{false}\}}")
(giving the boolean range ![{\\{ \\hbox{true},
\\hbox{false}\\}}](https://s0.wp.com/latex.php?latex=%7B%5C%7B+%5Chbox%7Btrue%7D%2C+%5Chbox%7Bfalse%7D%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\{ \hbox{true}, \hbox{false}\}}")
the discrete
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra,
of course). Finally, we continue to view deterministic elements of a
space
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
as a special case of a random element of
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}"),
and associate the indicator random variable
![{1\_E}](https://s0.wp.com/latex.php?latex=%7B1_E%7D&bg=ffffff&fg=000000&s=0 "{1_E}")
to any event
![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
as before.

We say that two random variables
![{X,Y}](https://s0.wp.com/latex.php?latex=%7BX%2CY%7D&bg=ffffff&fg=000000&s=0 "{X,Y}")*agree
almost surely* if the event
![{X=Y}](https://s0.wp.com/latex.php?latex=%7BX%3DY%7D&bg=ffffff&fg=000000&s=0 "{X=Y}")
is almost surely true; this is an equivalence relation. In many cases we
are willing to consider random variables up to almost sure equivalence.
In particular, we can generalise the notion of a random variable
slightly by considering random variables
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
whose models ![{X\_\\Omega: \\Omega \\rightarrow
R}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%3A+%5COmega+%5Crightarrow+R%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega: \Omega \rightarrow R}")
are only defined almost surely, i.e. their domain is not all of
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}"),
but instead
![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")
with a set of measure zero removed. This is, technically, not a random
variable as we have defined it, but it can be associated canonically
with an equivalence class of random variables up to almost sure
equivalence, and so we view such objects as random variables “up to
almost sure equivalence”. Similarly, we declare two events
![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}")
and
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")*almost
surely equivalent* if their symmetric difference ![{E \\Delta
F}](https://s0.wp.com/latex.php?latex=%7BE+%5CDelta+F%7D&bg=ffffff&fg=000000&s=0 "{E \Delta F}")
is a null event, and will often consider events up to almost sure
equivalence only.

We record some simple consequences of the measure-theoretic axioms:

> **Exercise 23** Let ![{(\\Omega, {\\mathcal F}\_\\Omega,
> \\mu)}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%7B%5Cmathcal+F%7D_%5COmega%2C+%5Cmu%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, {\mathcal F}_\Omega, \mu)}")
> be a measure space.
>
> 1.  (Monotonicity) If ![{E \\subset
>     F}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+F%7D&bg=ffffff&fg=000000&s=0 "{E \subset F}")
>     are measurable, then ![{\\mu(E) \\leq
>     \\mu(F)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28E%29+%5Cleq+%5Cmu%28F%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(E) \leq \mu(F)}").
> 2.  (Subadditivity) If
>     ![{E\_1,E\_2,\\dots}](https://s0.wp.com/latex.php?latex=%7BE_1%2CE_2%2C%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{E_1,E_2,\dots}")
>     are measurable (not necessarily disjoint), then
>     ![{\\mu(\\bigcup\_{n=1}^\\infty E\_n) \\leq \\sum\_{n=1}^\\infty
>     \\mu(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28%5Cbigcup_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%5Cleq+%5Csum_%7Bn%3D1%7D%5E%5Cinfty+%5Cmu%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(\bigcup_{n=1}^\infty E_n) \leq \sum_{n=1}^\infty \mu(E_n)}").
> 3.  (Continuity from below) If ![{E\_1 \\subset E\_2 \\subset \\dots
>     }](https://s0.wp.com/latex.php?latex=%7BE_1+%5Csubset+E_2+%5Csubset+%5Cdots+%7D&bg=ffffff&fg=000000&s=0 "{E_1 \subset E_2 \subset \dots }")
>     are measurable, then ![{\\mu(\\bigcup\_{n=1}^\\infty E\_n) =
>     \\lim\_{n \\rightarrow \\infty}
>     \\mu(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28%5Cbigcup_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%3D+%5Clim_%7Bn+%5Crightarrow+%5Cinfty%7D+%5Cmu%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(\bigcup_{n=1}^\infty E_n) = \lim_{n \rightarrow \infty} \mu(E_n)}").
> 4.  (Continuity from above) If ![{E\_1 \\supset E\_2 \\supset
>     \\dots}](https://s0.wp.com/latex.php?latex=%7BE_1+%5Csupset+E_2+%5Csupset+%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{E_1 \supset E_2 \supset \dots}")
>     are measurable and
>     ![{\\mu(E\_1)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28E_1%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(E_1)}")
>     is finite, then ![{\\mu(\\bigcap\_{n=1}^\\infty E\_n) = \\lim\_{n
>     \\rightarrow \\infty}
>     \\mu(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28%5Cbigcap_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%3D+%5Clim_%7Bn+%5Crightarrow+%5Cinfty%7D+%5Cmu%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(\bigcap_{n=1}^\infty E_n) = \lim_{n \rightarrow \infty} \mu(E_n)}").
>     Give a counterexample to show that the claim can fail when
>     ![{\\mu(E\_1)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28E_1%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(E_1)}")
>     is infinite.

Of course, these measure-theoretic facts immediately imply their
probabilistic counterparts (and the pesky hypothesis that
![{\\mu(E\_1)}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%28E_1%29%7D&bg=ffffff&fg=000000&s=0 "{\mu(E_1)}")
is finite is automatic and can thus be dropped):

1.  (Monotonicity) If ![{E \\subset
    F}](https://s0.wp.com/latex.php?latex=%7BE+%5Csubset+F%7D&bg=ffffff&fg=000000&s=0 "{E \subset F}")
    are events, then ![{{\\mathbf P}(E) \\leq {\\mathbf
    P}(F)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathbf+P%7D%28E%29+%5Cleq+%7B%5Cmathbf+P%7D%28F%29%7D&bg=ffffff&fg=000000&s=0 "{{\mathbf P}(E) \leq {\mathbf P}(F)}").
    (In particular, ![{0 \\leq {\\mathbf P}(E) \\leq
    1}](https://s0.wp.com/latex.php?latex=%7B0+%5Cleq+%7B%5Cmathbf+P%7D%28E%29+%5Cleq+1%7D&bg=ffffff&fg=000000&s=0 "{0 \leq {\mathbf P}(E) \leq 1}")
    for any event
    ![{E}](https://s0.wp.com/latex.php?latex=%7BE%7D&bg=ffffff&fg=000000&s=0 "{E}").)
2.  (Subadditivity) If
    ![{E\_1,E\_2,\\dots}](https://s0.wp.com/latex.php?latex=%7BE_1%2CE_2%2C%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{E_1,E_2,\dots}")
    are events (not necessarily disjoint), then ![{{\\mathbf
    P}(\\bigvee\_{n=1}^\\infty E\_n) \\leq \\sum\_{n=1}^\\infty
    {\\mathbf
    P}(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathbf+P%7D%28%5Cbigvee_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%5Cleq+%5Csum_%7Bn%3D1%7D%5E%5Cinfty+%7B%5Cmathbf+P%7D%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{{\mathbf P}(\bigvee_{n=1}^\infty E_n) \leq \sum_{n=1}^\infty {\mathbf P}(E_n)}").
3.  (Continuity from below) If ![{E\_1 \\subset E\_2 \\subset \\dots
    }](https://s0.wp.com/latex.php?latex=%7BE_1+%5Csubset+E_2+%5Csubset+%5Cdots+%7D&bg=ffffff&fg=000000&s=0 "{E_1 \subset E_2 \subset \dots }")
    are events, then ![{{\\mathbf P}(\\bigvee\_{n=1}^\\infty E\_n) =
    \\lim\_{n \\rightarrow \\infty} {\\mathbf
    P}(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathbf+P%7D%28%5Cbigvee_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%3D+%5Clim_%7Bn+%5Crightarrow+%5Cinfty%7D+%7B%5Cmathbf+P%7D%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{{\mathbf P}(\bigvee_{n=1}^\infty E_n) = \lim_{n \rightarrow \infty} {\mathbf P}(E_n)}").
4.  (Continuity from above) If ![{E\_1 \\supset E\_2 \\supset
    \\dots}](https://s0.wp.com/latex.php?latex=%7BE_1+%5Csupset+E_2+%5Csupset+%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{E_1 \supset E_2 \supset \dots}")
    is events, then ![{{\\mathbf P}(\\bigwedge\_{n=1}^\\infty E\_n) =
    \\lim\_{n \\rightarrow \\infty} {\\mathbf
    P}(E\_n)}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathbf+P%7D%28%5Cbigwedge_%7Bn%3D1%7D%5E%5Cinfty+E_n%29+%3D+%5Clim_%7Bn+%5Crightarrow+%5Cinfty%7D+%7B%5Cmathbf+P%7D%28E_n%29%7D&bg=ffffff&fg=000000&s=0 "{{\mathbf P}(\bigwedge_{n=1}^\infty E_n) = \lim_{n \rightarrow \infty} {\mathbf P}(E_n)}").

Note that if a countable sequence ![{E\_1, E\_2,
\\dots}](https://s0.wp.com/latex.php?latex=%7BE_1%2C+E_2%2C+%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{E_1, E_2, \dots}")
of events each hold almost surely, then their conjunction does as well
(by applying subadditivity to the complementary events
![{\\overline{E\_1},\\overline{E\_2},\\dots}](https://s0.wp.com/latex.php?latex=%7B%5Coverline%7BE_1%7D%2C%5Coverline%7BE_2%7D%2C%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{\overline{E_1},\overline{E_2},\dots}").
As a general rule of thumb, the notion of “almost surely” behaves like
“surely” as long as one only performs an at most countable number of
operations (which already suffices for a large portion of analysis, such
as taking limits or performing infinite sums).

> **Exercise 24** Let ![{(\\Omega, {\\mathcal
> B})}](https://s0.wp.com/latex.php?latex=%7B%28%5COmega%2C+%7B%5Cmathcal+B%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(\Omega, {\mathcal B})}")
> be a measurable space.
>
> -   If ![{f: \\Omega \\rightarrow
>     \[-\\infty,\\infty\]}](https://s0.wp.com/latex.php?latex=%7Bf%3A+%5COmega+%5Crightarrow+%5B-%5Cinfty%2C%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{f: \Omega \rightarrow [-\infty,\infty]}")
>     is a function taking values in the extended reals
>     ![{\[-\\infty,\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5B-%5Cinfty%2C%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{[-\infty,\infty]}"),
>     show that
>     ![{f}](https://s0.wp.com/latex.php?latex=%7Bf%7D&bg=ffffff&fg=000000&s=0 "{f}")
>     is measurable (giving
>     ![{\[-\\infty,\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5B-%5Cinfty%2C%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{[-\infty,\infty]}")
>     the Borel
>     ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra)
>     if and only if the sets ![{\\{ \\omega \\in \\Omega: f(\\omega)
>     \\leq t
>     \\}}](https://s0.wp.com/latex.php?latex=%7B%5C%7B+%5Comega+%5Cin+%5COmega%3A+f%28%5Comega%29+%5Cleq+t+%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\{ \omega \in \Omega: f(\omega) \leq t \}}")
>     are measurable for all real
>     ![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}").
> -   If ![{f,g: \\Omega \\rightarrow
>     \[-\\infty,\\infty\]}](https://s0.wp.com/latex.php?latex=%7Bf%2Cg%3A+%5COmega+%5Crightarrow+%5B-%5Cinfty%2C%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{f,g: \Omega \rightarrow [-\infty,\infty]}")
>     are functions, show that
>     ![{f=g}](https://s0.wp.com/latex.php?latex=%7Bf%3Dg%7D&bg=ffffff&fg=000000&s=0 "{f=g}")
>     if and only if ![{\\{ \\omega \\in \\Omega: f(\\omega) \\leq t \\}
>     = \\{ \\omega \\in \\Omega: g(\\omega) \\leq t
>     \\}}](https://s0.wp.com/latex.php?latex=%7B%5C%7B+%5Comega+%5Cin+%5COmega%3A+f%28%5Comega%29+%5Cleq+t+%5C%7D+%3D+%5C%7B+%5Comega+%5Cin+%5COmega%3A+g%28%5Comega%29+%5Cleq+t+%5C%7D%7D&bg=ffffff&fg=000000&s=0 "{\{ \omega \in \Omega: f(\omega) \leq t \} = \{ \omega \in \Omega: g(\omega) \leq t \}}")
>     for all reals
>     ![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}").
> -   If ![{f\_1,f\_2,\\dots: \\Omega \\rightarrow
>     \[-\\infty,\\infty\]}](https://s0.wp.com/latex.php?latex=%7Bf_1%2Cf_2%2C%5Cdots%3A+%5COmega+%5Crightarrow+%5B-%5Cinfty%2C%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{f_1,f_2,\dots: \Omega \rightarrow [-\infty,\infty]}")
>     are measurable, show that ![{\\sup\_n
>     f\_n}](https://s0.wp.com/latex.php?latex=%7B%5Csup_n+f_n%7D&bg=ffffff&fg=000000&s=0 "{\sup_n f_n}"),
>     ![{\\inf\_n
>     f\_n}](https://s0.wp.com/latex.php?latex=%7B%5Cinf_n+f_n%7D&bg=ffffff&fg=000000&s=0 "{\inf_n f_n}"),
>     ![{\\limsup\_{n \\rightarrow \\infty}
>     f\_n}](https://s0.wp.com/latex.php?latex=%7B%5Climsup_%7Bn+%5Crightarrow+%5Cinfty%7D+f_n%7D&bg=ffffff&fg=000000&s=0 "{\limsup_{n \rightarrow \infty} f_n}"),
>     and ![{\\liminf\_{n \\rightarrow \\infty}
>     f\_n}](https://s0.wp.com/latex.php?latex=%7B%5Climinf_%7Bn+%5Crightarrow+%5Cinfty%7D+f_n%7D&bg=ffffff&fg=000000&s=0 "{\liminf_{n \rightarrow \infty} f_n}")
>     are all measurable.

> **Remark 25** Occasionally, there is need to consider uncountable
> suprema or infima, e.g. ![{\\sup\_{t \\in {\\bf R}}
> f\_t}](https://s0.wp.com/latex.php?latex=%7B%5Csup_%7Bt+%5Cin+%7B%5Cbf+R%7D%7D+f_t%7D&bg=ffffff&fg=000000&s=0 "{\sup_{t \in {\bf R}} f_t}").
> It is then no longer automatically the case that such an uncountable
> supremum or infimum of measurable functions is again measurable.
> However, in practice one can avoid this issue by carefully rewriting
> such uncountable suprema or infima in terms of countable ones. For
> instance, if it is known that
> ![{f\_t(\\omega)}](https://s0.wp.com/latex.php?latex=%7Bf_t%28%5Comega%29%7D&bg=ffffff&fg=000000&s=0 "{f_t(\omega)}")
> depends continuously on
> ![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}")
> for each
> ![{\\omega}](https://s0.wp.com/latex.php?latex=%7B%5Comega%7D&bg=ffffff&fg=000000&s=0 "{\omega}"),
> then ![{\\sup\_{t \\in {\\bf R}} f\_t = \\sup\_{t \\in {\\bf Q}}
> f\_t}](https://s0.wp.com/latex.php?latex=%7B%5Csup_%7Bt+%5Cin+%7B%5Cbf+R%7D%7D+f_t+%3D+%5Csup_%7Bt+%5Cin+%7B%5Cbf+Q%7D%7D+f_t%7D&bg=ffffff&fg=000000&s=0 "{\sup_{t \in {\bf R}} f_t = \sup_{t \in {\bf Q}} f_t}"),
> and so measurability is not an issue.

Using the above exercise, when given a sequence
![{X\_1,X\_2,\\dots}](https://s0.wp.com/latex.php?latex=%7BX_1%2CX_2%2C%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{X_1,X_2,\dots}")
of random variables taking values in the extended real line
![{\[-\\infty,\\infty\]}](https://s0.wp.com/latex.php?latex=%7B%5B-%5Cinfty%2C%5Cinfty%5D%7D&bg=ffffff&fg=000000&s=0 "{[-\infty,\infty]}"),
we can define the random variables ![{\\sup\_n
X\_n}](https://s0.wp.com/latex.php?latex=%7B%5Csup_n+X_n%7D&bg=ffffff&fg=000000&s=0 "{\sup_n X_n}"),
![{\\inf\_n
X\_n}](https://s0.wp.com/latex.php?latex=%7B%5Cinf_n+X_n%7D&bg=ffffff&fg=000000&s=0 "{\inf_n X_n}"),
![{\\limsup\_{n \\rightarrow \\infty}
X\_n}](https://s0.wp.com/latex.php?latex=%7B%5Climsup_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n%7D&bg=ffffff&fg=000000&s=0 "{\limsup_{n \rightarrow \infty} X_n}"),
![{\\liminf\_{n \\rightarrow \\infty}
X\_n}](https://s0.wp.com/latex.php?latex=%7B%5Climinf_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n%7D&bg=ffffff&fg=000000&s=0 "{\liminf_{n \rightarrow \infty} X_n}")
which also take values in the extended real line, and which obey
relations such as

![\\displaystyle (\\sup\_n X\_n &gt; t) = \\bigvee\_{n=1}^\\infty (X\_n
&gt; t)
](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%28%5Csup_n+X_n+%3E+t%29+%3D+%5Cbigvee_%7Bn%3D1%7D%5E%5Cinfty+%28X_n+%3E+t%29+&bg=ffffff&fg=000000&s=0 "\displaystyle  (\sup_n X_n > t) = \bigvee_{n=1}^\infty (X_n > t) ")

for any real number
![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}").

We now say that a sequence
![{X\_1,X\_2,\\dots}](https://s0.wp.com/latex.php?latex=%7BX_1%2CX_2%2C%5Cdots%7D&bg=ffffff&fg=000000&s=0 "{X_1,X_2,\dots}")
of random variables in the extended real line [converges almost
surely](https://en.wikipedia.org/wiki/Convergence_of_random_variables#Almost_sure_convergence)
if one has

![\\displaystyle \\liminf\_{n \\rightarrow \\infty} X\_n = \\limsup\_{n
\\rightarrow \\infty} X\_n
](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5Climinf_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n+%3D+%5Climsup_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n+&bg=ffffff&fg=000000&s=0 "\displaystyle  \liminf_{n \rightarrow \infty} X_n = \limsup_{n \rightarrow \infty} X_n ")

almost surely, in which case we can define the limit ![{\\lim\_{n
\\rightarrow \\infty}
X\_n}](https://s0.wp.com/latex.php?latex=%7B%5Clim_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n%7D&bg=ffffff&fg=000000&s=0 "{\lim_{n \rightarrow \infty} X_n}")
(up to almost sure equivalence) as

![\\displaystyle \\lim\_{n \\rightarrow \\infty} X\_n = \\liminf\_{n
\\rightarrow \\infty} X\_n = \\limsup\_{n \\rightarrow \\infty}
X\_n.](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5Clim_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n+%3D+%5Climinf_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n+%3D+%5Climsup_%7Bn+%5Crightarrow+%5Cinfty%7D+X_n.&bg=ffffff&fg=000000&s=0 "\displaystyle  \lim_{n \rightarrow \infty} X_n = \liminf_{n \rightarrow \infty} X_n = \limsup_{n \rightarrow \infty} X_n.")

This corresponds closely to the concept of [almost everywhere
convergence](https://en.wikipedia.org/wiki/Pointwise_convergence#Almost_everywhere_convergence)
in measure theory, which is a slightly weaker notion than pointwise
convergence which allows for bad behaviour on a set of measure zero.
(See [this previous blog
post](https://terrytao.wordpress.com/2010/10/02/245a-notes-4-modes-of-convergence/)
for more discussion on different notions of convergence of measurable
functions.)

We will defer the general construction of expectation of a random
variable to the next set of notes, where we review the notion of
integration on a measure space. For now, we quickly review the basic
construction of continuous scalar random variables.

> **Exercise 26** Let
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
> be a probability measure on the real line ![{{\\bf
> R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}")
> (with the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra).
> Define the *Stieltjes measure function* ![{F: {\\bf R} \\rightarrow
> \[0,1\]}](https://s0.wp.com/latex.php?latex=%7BF%3A+%7B%5Cbf+R%7D+%5Crightarrow+%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{F: {\bf R} \rightarrow [0,1]}")
> associated to
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
> by the formula
>
> ![\\displaystyle F( t ) := \\mu( (-\\infty,t\] ) = \\mu( \\{ x \\in
> {\\bf R}: x \\leq t \\}
> ).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28+t+%29+%3A%3D+%5Cmu%28+%28-%5Cinfty%2Ct%5D+%29+%3D+%5Cmu%28+%5C%7B+x+%5Cin+%7B%5Cbf+R%7D%3A+x+%5Cleq+t+%5C%7D+%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  F( t ) := \mu( (-\infty,t] ) = \mu( \{ x \in {\bf R}: x \leq t \} ).")
>
> Establish the following properties of
> ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}"):
>
> -   (i)
>     ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
>     is non-decreasing.
> -   (ii) ![{\\lim\_{t \\rightarrow -\\infty} F(t) =
>     0}](https://s0.wp.com/latex.php?latex=%7B%5Clim_%7Bt+%5Crightarrow+-%5Cinfty%7D+F%28t%29+%3D+0%7D&bg=ffffff&fg=000000&s=0 "{\lim_{t \rightarrow -\infty} F(t) = 0}")
>     and ![{\\lim\_{t \\rightarrow +\\infty} F(t) =
>     1}](https://s0.wp.com/latex.php?latex=%7B%5Clim_%7Bt+%5Crightarrow+%2B%5Cinfty%7D+F%28t%29+%3D+1%7D&bg=ffffff&fg=000000&s=0 "{\lim_{t \rightarrow +\infty} F(t) = 1}").
> -   (iii)
>     ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
>     is right-continuous, thus ![{F(t) = \\lim\_{s \\rightarrow t^+}
>     F(s)}](https://s0.wp.com/latex.php?latex=%7BF%28t%29+%3D+%5Clim_%7Bs+%5Crightarrow+t%5E%2B%7D+F%28s%29%7D&bg=ffffff&fg=000000&s=0 "{F(t) = \lim_{s \rightarrow t^+} F(s)}")
>     for all ![{t \\in {\\bf
>     R}}](https://s0.wp.com/latex.php?latex=%7Bt+%5Cin+%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{t \in {\bf R}}").

There is a somewhat difficult converse to this exercise: if
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
is a function obeying the above three properties, then there is a unique
probability measure
![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
on ![{{\\bf
R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}")
(the [Lebesgue-Stieltjes
measure](https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration)
associated to
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}"))
for which
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
is the Stieltjes measure function. See Section 3 of [this previous
post](https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/)
for details. As a consequence of this, we have

> **Corollary 27 (Construction of a single continuous random variable)**
> Let ![{F: {\\bf R} \\rightarrow
> \[0,1\]}](https://s0.wp.com/latex.php?latex=%7BF%3A+%7B%5Cbf+R%7D+%5Crightarrow+%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{F: {\bf R} \rightarrow [0,1]}")
> be a function obeying the properties (i)-(iii) of the above exercise.
> Then, by using a suitable probability space model, we can construct a
> real random variable
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> with the property that
>
> ![\\displaystyle F(t) = {\\bf P}( X \\leq
> t)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28t%29+%3D+%7B%5Cbf+P%7D%28+X+%5Cleq+t%29&bg=ffffff&fg=000000&s=0 "\displaystyle  F(t) = {\bf P}( X \leq t)")
>
> for all ![{t \\in {\\bf
> R}}](https://s0.wp.com/latex.php?latex=%7Bt+%5Cin+%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{t \in {\bf R}}").

Indeed, we can take the probability space to be ![{{\\bf
R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}")
with the Borel
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
and the Lebesgue-Stieltjes measure associated to
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}").
This corollary is not fully satisfactory, because often we may already
have chosen a probability space to model some other random variables,
and the probability space provided by this corollary may be completely
unrelated to the one used. We can resolve these issues with product
measures and other joinings, but this will be deferred to a later set of
notes.

Define the [cumulative distribution
function](https://en.wikipedia.org/wiki/Cumulative_distribution_function)
![{F: {\\bf R} \\rightarrow
\[0,1\]}](https://s0.wp.com/latex.php?latex=%7BF%3A+%7B%5Cbf+R%7D+%5Crightarrow+%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{F: {\bf R} \rightarrow [0,1]}")
of a real random variable
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
to be the function

![\\displaystyle F(t) := {\\bf P}(X \\leq
t).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28t%29+%3A%3D+%7B%5Cbf+P%7D%28X+%5Cleq+t%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  F(t) := {\bf P}(X \leq t).")

Thus we see that cumulative distribution functions obey the properties
(i)-(iii) above, and conversely any function with those properties is
the cumulative distribution function of some real random variable. We
say that two real random variables (possibly on different sample spaces)
*agree in distribution* if they have the same cumulative distribution
function. One can therefore define a real random variable, up to
agreement in distribution, by specifying the cumulative distribution
function. See Durrett for some standard real distributions (uniform,
normal, geometric, etc.) that one can define in this fashion.

> **Exercise 28** Let
> ![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
> be a real random variable with cumulative distribution function
> ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}").
> For any real number
> ![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}"),
> show that
>
> ![\\displaystyle {\\bf P}(X &lt; t) = \\lim\_{s \\rightarrow t^-}
> F(s)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28X+%3C+t%29+%3D+%5Clim_%7Bs+%5Crightarrow+t%5E-%7D+F%28s%29&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(X < t) = \lim_{s \rightarrow t^-} F(s)")
>
> and
>
> ![\\displaystyle {\\bf P}(X = t) = F(t) - \\lim\_{s \\rightarrow t^-}
> F(s).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%7B%5Cbf+P%7D%28X+%3D+t%29+%3D+F%28t%29+-+%5Clim_%7Bs+%5Crightarrow+t%5E-%7D+F%28s%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  {\bf P}(X = t) = F(t) - \lim_{s \rightarrow t^-} F(s).")
>
> In particular, one has ![{{\\bf
> P}(X=t)=0}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+P%7D%28X%3Dt%29%3D0%7D&bg=ffffff&fg=000000&s=0 "{{\bf P}(X=t)=0}")
> for all
> ![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}")
> if and only if
> ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
> is continuous.

Note in particular that this illustrates the distinction between almost
sure and sure events: if
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
has a continuous cumulative distribution function, and
![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}")
is a real number, then
![{X=t}](https://s0.wp.com/latex.php?latex=%7BX%3Dt%7D&bg=ffffff&fg=000000&s=0 "{X=t}")
is almost surely false, but it does not have to be surely false.
(Indeed, if one takes the sample space to be ![{{\\bf
R}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}}")
and
![{X\_\\Omega}](https://s0.wp.com/latex.php?latex=%7BX_%5COmega%7D&bg=ffffff&fg=000000&s=0 "{X_\Omega}")
to be the identity function, then
![{X=t}](https://s0.wp.com/latex.php?latex=%7BX%3Dt%7D&bg=ffffff&fg=000000&s=0 "{X=t}")
will not be surely false.) On the other hand, the fact that
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
is equal to *some* real number is of course surely true. The reason
these statements are consistent with each other is that there are
uncountably many real numbers
![{t}](https://s0.wp.com/latex.php?latex=%7Bt%7D&bg=ffffff&fg=000000&s=0 "{t}").
(Countable additivity tells us that a countable disjunction of null
events is still null, but says nothing about uncountable disjunctions.)

> **Exercise 29 (Skorokhod representation of scalar variables)** Let
> ![{U}](https://s0.wp.com/latex.php?latex=%7BU%7D&bg=ffffff&fg=000000&s=0 "{U}")
> be a uniform random variable taking values in
> ![{\[0,1\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,1]}")
> (thus
> ![{U}](https://s0.wp.com/latex.php?latex=%7BU%7D&bg=ffffff&fg=000000&s=0 "{U}")
> has cumulative distribution function ![{F\_U(t) :=
> \\min(\\max(t,0),1)}](https://s0.wp.com/latex.php?latex=%7BF_U%28t%29+%3A%3D+%5Cmin%28%5Cmax%28t%2C0%29%2C1%29%7D&bg=ffffff&fg=000000&s=0 "{F_U(t) := \min(\max(t,0),1)}")),
> and let ![{F: {\\bf R} \\rightarrow
> \[0,1\]}](https://s0.wp.com/latex.php?latex=%7BF%3A+%7B%5Cbf+R%7D+%5Crightarrow+%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{F: {\bf R} \rightarrow [0,1]}")
> be another cumulative distribution function. Show that the random
> variables
>
> ![\\displaystyle X^- := \\sup \\{ y \\in {\\bf R}: F(y) &lt; U
> \\}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++X%5E-+%3A%3D+%5Csup+%5C%7B+y+%5Cin+%7B%5Cbf+R%7D%3A+F%28y%29+%3C+U+%5C%7D&bg=ffffff&fg=000000&s=0 "\displaystyle  X^- := \sup \{ y \in {\bf R}: F(y) < U \}")
>
> and
>
> ![\\displaystyle X^+ := \\inf \\{ y \\in {\\bf R}: F(y) \\geq U
> \\}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++X%5E%2B+%3A%3D+%5Cinf+%5C%7B+y+%5Cin+%7B%5Cbf+R%7D%3A+F%28y%29+%5Cgeq+U+%5C%7D&bg=ffffff&fg=000000&s=0 "\displaystyle  X^+ := \inf \{ y \in {\bf R}: F(y) \geq U \}")
>
> are indeed random variables (that is to say, they are measurable in
> any given model
> ![{\\Omega}](https://s0.wp.com/latex.php?latex=%7B%5COmega%7D&bg=ffffff&fg=000000&s=0 "{\Omega}")),
> and have cumulative distribution function
> ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}").
> (This construction is attributed to Skorokhod, but it should not be
> confused with the [Skorokhod representation
> theorem](https://en.wikipedia.org/wiki/Skorokhod%27s_representation_theorem).
> It provides a quick way to generate a single scalar variable, but
> unfortunately it is difficult to modify this construction to generate
> multiple scalar variables, especially if they are somehow coupled to
> each other.)

There is a multidimensional analogue of the above theory, which is
almost identical, except that the monotonicity property has to be
strengthened:

> **Exercise 30** Let
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
> be a probability measure on ![{{\\bf
> R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}")
> (with the Borel
> ![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra).
> Define the *Stieltjes measure function* ![{F: {\\bf R}^n \\rightarrow
> \[0,1\]}](https://s0.wp.com/latex.php?latex=%7BF%3A+%7B%5Cbf+R%7D%5En+%5Crightarrow+%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{F: {\bf R}^n \rightarrow [0,1]}")
> associated to
> ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
> by the formula
>
> ![\\displaystyle F( t\_1,\\dots,t\_n ) := \\mu( (-\\infty,t\_1\]
> \\times \\dots \\times (-\\infty,t\_n\]
> )](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28+t_1%2C%5Cdots%2Ct_n+%29+%3A%3D+%5Cmu%28+%28-%5Cinfty%2Ct_1%5D+%5Ctimes+%5Cdots+%5Ctimes+%28-%5Cinfty%2Ct_n%5D+%29&bg=ffffff&fg=000000&s=0 "\displaystyle  F( t_1,\dots,t_n ) := \mu( (-\infty,t_1] \times \dots \times (-\infty,t_n] )")
>
> ![\\displaystyle = \\mu( \\{ (x\_1,\\dots,x\_n) \\in {\\bf R}^n: x\_i
> \\leq t\_i \\forall i=1,\\dots,n \\}
> ).](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%3D+%5Cmu%28+%5C%7B+%28x_1%2C%5Cdots%2Cx_n%29+%5Cin+%7B%5Cbf+R%7D%5En%3A+x_i+%5Cleq+t_i+%5Cforall+i%3D1%2C%5Cdots%2Cn+%5C%7D+%29.&bg=ffffff&fg=000000&s=0 "\displaystyle  = \mu( \{ (x_1,\dots,x_n) \in {\bf R}^n: x_i \leq t_i \forall i=1,\dots,n \} ).")
>
> Establish the following properties of
> ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}"):
>
> -   (i)
>     ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
>     is non-decreasing: ![{F(t\_1,\\dots,t\_n) \\leq
>     F(t'\_1,\\dots,t'\_n)}](https://s0.wp.com/latex.php?latex=%7BF%28t_1%2C%5Cdots%2Ct_n%29+%5Cleq+F%28t%27_1%2C%5Cdots%2Ct%27_n%29%7D&bg=ffffff&fg=000000&s=0 "{F(t_1,\dots,t_n) \leq F(t'_1,\dots,t'_n)}")
>     whenever ![{t\_i \\leq
>     t'\_i}](https://s0.wp.com/latex.php?latex=%7Bt_i+%5Cleq+t%27_i%7D&bg=ffffff&fg=000000&s=0 "{t_i \leq t'_i}")
>     for all
>     ![{i}](https://s0.wp.com/latex.php?latex=%7Bi%7D&bg=ffffff&fg=000000&s=0 "{i}").
> -   (ii) ![{\\lim\_{t\_1,\\dots,t\_n \\rightarrow
>     -\\infty} F(t\_1,\\dots,t\_n) =
>     0}](https://s0.wp.com/latex.php?latex=%7B%5Clim_%7Bt_1%2C%5Cdots%2Ct_n+%5Crightarrow+-%5Cinfty%7D+F%28t_1%2C%5Cdots%2Ct_n%29+%3D+0%7D&bg=ffffff&fg=000000&s=0 "{\lim_{t_1,\dots,t_n \rightarrow -\infty} F(t_1,\dots,t_n) = 0}")
>     and ![{\\lim\_{t\_1,\\dots,t\_n \\rightarrow
>     +\\infty} F(t\_1,\\dots,t\_n) =
>     1}](https://s0.wp.com/latex.php?latex=%7B%5Clim_%7Bt_1%2C%5Cdots%2Ct_n+%5Crightarrow+%2B%5Cinfty%7D+F%28t_1%2C%5Cdots%2Ct_n%29+%3D+1%7D&bg=ffffff&fg=000000&s=0 "{\lim_{t_1,\dots,t_n \rightarrow +\infty} F(t_1,\dots,t_n) = 1}").
> -   (iii)
>     ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
>     is right-continuous, thus ![{F(t\_1,\\dots,t\_n)
>     = \\lim\_{(s\_1,\\dots,s\_n) \\rightarrow (t\_1,\\dots,t\_n)^+}
>     F(s\_1,\\dots,s\_n)}](https://s0.wp.com/latex.php?latex=%7BF%28t_1%2C%5Cdots%2Ct_n%29+%3D+%5Clim_%7B%28s_1%2C%5Cdots%2Cs_n%29+%5Crightarrow+%28t_1%2C%5Cdots%2Ct_n%29%5E%2B%7D+F%28s_1%2C%5Cdots%2Cs_n%29%7D&bg=ffffff&fg=000000&s=0 "{F(t_1,\dots,t_n) = \lim_{(s_1,\dots,s_n) \rightarrow (t_1,\dots,t_n)^+} F(s_1,\dots,s_n)}")
>     for all ![{(t\_1,\\dots,t\_n) \\in {\\bf
>     R}^n}](https://s0.wp.com/latex.php?latex=%7B%28t_1%2C%5Cdots%2Ct_n%29+%5Cin+%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{(t_1,\dots,t_n) \in {\bf R}^n}"),
>     where the
>     ![{+}](https://s0.wp.com/latex.php?latex=%7B%2B%7D&bg=ffffff&fg=000000&s=0 "{+}")
>     superscript denotes that we restrict each
>     ![{s\_i}](https://s0.wp.com/latex.php?latex=%7Bs_i%7D&bg=ffffff&fg=000000&s=0 "{s_i}")
>     to be greater than or equal to
>     ![{t\_i}](https://s0.wp.com/latex.php?latex=%7Bt_i%7D&bg=ffffff&fg=000000&s=0 "{t_i}").
> -   (iv) One has
>
>     ![\\displaystyle \\sum\_{(\\omega\_1,\\dots,\\omega\_n) \\in
>     \\{0,1\\}^n} (-1)^{\\omega\_1+\\dots+\\omega\_n+n} F(
>     t\_{1,\\omega\_1}, \\dots, t\_{n,\\omega\_n} ) \\geq
>     0](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5Csum_%7B%28%5Comega_1%2C%5Cdots%2C%5Comega_n%29+%5Cin+%5C%7B0%2C1%5C%7D%5En%7D+%28-1%29%5E%7B%5Comega_1%2B%5Cdots%2B%5Comega_n%2Bn%7D+F%28+t_%7B1%2C%5Comega_1%7D%2C+%5Cdots%2C+t_%7Bn%2C%5Comega_n%7D+%29+%5Cgeq+0&bg=ffffff&fg=000000&s=0 "\displaystyle  \sum_{(\omega_1,\dots,\omega_n) \in \{0,1\}^n} (-1)^{\omega_1+\dots+\omega_n+n} F( t_{1,\omega_1}, \dots, t_{n,\omega_n} ) \geq 0")
>
>     whenever ![{t\_{i,0} \\leq
>     t\_{i,1}}](https://s0.wp.com/latex.php?latex=%7Bt_%7Bi%2C0%7D+%5Cleq+t_%7Bi%2C1%7D%7D&bg=ffffff&fg=000000&s=0 "{t_{i,0} \leq t_{i,1}}")
>     are real numbers for
>     ![{i=1,\\dots,n}](https://s0.wp.com/latex.php?latex=%7Bi%3D1%2C%5Cdots%2Cn%7D&bg=ffffff&fg=000000&s=0 "{i=1,\dots,n}").
>     (*Hint:* try to express the measure of a box
>     ![{(t\_{1,0},t\_{1,1}\] \\times \\dots \\times
>     (t\_{n,0},t\_{n,1}\]}](https://s0.wp.com/latex.php?latex=%7B%28t_%7B1%2C0%7D%2Ct_%7B1%2C1%7D%5D+%5Ctimes+%5Cdots+%5Ctimes+%28t_%7Bn%2C0%7D%2Ct_%7Bn%2C1%7D%5D%7D&bg=ffffff&fg=000000&s=0 "{(t_{1,0},t_{1,1}] \times \dots \times (t_{n,0},t_{n,1}]}")
>     with respect to
>     ![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
>     in terms of the Stieltjes measure function
>     ![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}").)
>
Again, there is a difficult converse to this exercise: if
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
is a function obeying the above four properties, then there is a unique
probability measure
![{\\mu}](https://s0.wp.com/latex.php?latex=%7B%5Cmu%7D&bg=ffffff&fg=000000&s=0 "{\mu}")
on ![{{\\bf
R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}")
for which
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}")
is the Stieltjes measure function. See Durrett for details; one can also
modify the arguments in [this previous
post](https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/).
In particular, we have

> **Corollary 31 (Construction of several continuous random variables)**
> Let ![{F: {\\bf R}^n \\rightarrow
> \[0,1\]}](https://s0.wp.com/latex.php?latex=%7BF%3A+%7B%5Cbf+R%7D%5En+%5Crightarrow+%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{F: {\bf R}^n \rightarrow [0,1]}")
> be a function obeying the properties (i)-(iv) of the above exercise.
> Then, by using a suitable probability space model, we can construct
> real random variables
> ![{X\_1,\\dots,X\_n}](https://s0.wp.com/latex.php?latex=%7BX_1%2C%5Cdots%2CX_n%7D&bg=ffffff&fg=000000&s=0 "{X_1,\dots,X_n}")
> with the property that
>
> ![\\displaystyle F(t\_1,\\dots,t\_n) = {\\bf P}( X\_1 \\leq t\_1
> \\wedge \\dots \\wedge X\_n \\leq
> t\_n)](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28t_1%2C%5Cdots%2Ct_n%29+%3D+%7B%5Cbf+P%7D%28+X_1+%5Cleq+t_1+%5Cwedge+%5Cdots+%5Cwedge+X_n+%5Cleq+t_n%29&bg=ffffff&fg=000000&s=0 "\displaystyle  F(t_1,\dots,t_n) = {\bf P}( X_1 \leq t_1 \wedge \dots \wedge X_n \leq t_n)")
>
> for all ![{t\_1,\\dots,t\_n \\in {\\bf
> R}}](https://s0.wp.com/latex.php?latex=%7Bt_1%2C%5Cdots%2Ct_n+%5Cin+%7B%5Cbf+R%7D%7D&bg=ffffff&fg=000000&s=0 "{t_1,\dots,t_n \in {\bf R}}").

Again, this corollary is not completely satisfactory because the
probability space produced by it (which one can take to be ![{{\\bf
R}^n}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cbf+R%7D%5En%7D&bg=ffffff&fg=000000&s=0 "{{\bf R}^n}")
with the Borel
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
and the Lebesgue-Stieltjes measure on
![{F}](https://s0.wp.com/latex.php?latex=%7BF%7D&bg=ffffff&fg=000000&s=0 "{F}"))
may not be the probability space one wants to use; we will return to
this point later.

**— 4. Variants of the standard foundations (optional) —**

We have focused on the orthodox foundations of probability theory in
which we model events and random variables through probability spaces.
In this section, we briefly discuss some alternate ways to set up the
foundations, as well as alternatives to probability theory itself.
(Actually, many of the basic objects and concepts in mathematics have
multiple such foundations; see for instance [this blog
post](https://terrytao.wordpress.com/2009/10/19/grothendiecks-definition-of-a-group/)
exploring the many different ways to define the notion of a group.) We
mention them here in order exclude them from discussion in subsequent
notes, which will be focused almost exclusively on orthodox probability.

One approach to the foundations of probability is to view the event
space as an *abstract*
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebra
![{{\\mathcal
E}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+E%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal E}}")
– a collection of abstract objects with operations such as
![{\\wedge}](https://s0.wp.com/latex.php?latex=%7B%5Cwedge%7D&bg=ffffff&fg=000000&s=0 "{\wedge}")
and
![{\\vee}](https://s0.wp.com/latex.php?latex=%7B%5Cvee%7D&bg=ffffff&fg=000000&s=0 "{\vee}")
(and
![{\\bigwedge\_{n=1}^\\infty}](https://s0.wp.com/latex.php?latex=%7B%5Cbigwedge_%7Bn%3D1%7D%5E%5Cinfty%7D&bg=ffffff&fg=000000&s=0 "{\bigwedge_{n=1}^\infty}")
and
![{\\bigvee\_{n=1}^\\infty}](https://s0.wp.com/latex.php?latex=%7B%5Cbigvee_%7Bn%3D1%7D%5E%5Cinfty%7D&bg=ffffff&fg=000000&s=0 "{\bigvee_{n=1}^\infty}"))
that obey a number of axioms; see [this previous
post](https://terrytao.wordpress.com/2009/01/12/245b-notes-1-the-stone-and-loomis-sikorski-representation-theorems-optional/)
for a formal definition. The probability map ![{E \\mapsto {\\bf
P}(E)}](https://s0.wp.com/latex.php?latex=%7BE+%5Cmapsto+%7B%5Cbf+P%7D%28E%29%7D&bg=ffffff&fg=000000&s=0 "{E \mapsto {\bf P}(E)}")
can then be viewed as an abstract probability measure on ![{{\\mathcal
E}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+E%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal E}}"),
that is to say a map from ![{{\\mathcal
E}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+E%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal E}}")
to
![{\[0,1\]}](https://s0.wp.com/latex.php?latex=%7B%5B0%2C1%5D%7D&bg=ffffff&fg=000000&s=0 "{[0,1]}")
that obeys the Kolmogorov axioms. Random variables
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
taking values in a measurable space ![{(R, {\\mathcal
B})}](https://s0.wp.com/latex.php?latex=%7B%28R%2C+%7B%5Cmathcal+B%7D%29%7D&bg=ffffff&fg=000000&s=0 "{(R, {\mathcal B})}")
can be identified with their pullback map ![{X^\*: {\\mathcal B}
\\rightarrow {\\mathcal
E}}](https://s0.wp.com/latex.php?latex=%7BX%5E%2A%3A+%7B%5Cmathcal+B%7D+%5Crightarrow+%7B%5Cmathcal+E%7D%7D&bg=ffffff&fg=000000&s=0 "{X^*: {\mathcal B} \rightarrow {\mathcal E}}"),
which is the morphism of (abstract)
![{\\sigma}](https://s0.wp.com/latex.php?latex=%7B%5Csigma%7D&bg=ffffff&fg=000000&s=0 "{\sigma}")-algebras
that sends a measurable set ![{S \\in {\\mathcal
B}}](https://s0.wp.com/latex.php?latex=%7BS+%5Cin+%7B%5Cmathcal+B%7D%7D&bg=ffffff&fg=000000&s=0 "{S \in {\mathcal B}}")
to the event ![{X \\in
S}](https://s0.wp.com/latex.php?latex=%7BX+%5Cin+S%7D&bg=ffffff&fg=000000&s=0 "{X \in S}")
in ![{{\\mathcal
E}}](https://s0.wp.com/latex.php?latex=%7B%7B%5Cmathcal+E%7D%7D&bg=ffffff&fg=000000&s=0 "{{\mathcal E}}");
with some care one can then redefine all the operations in previous
sections (e.g. applying a measurable map ![{f: R \\rightarrow
S}](https://s0.wp.com/latex.php?latex=%7Bf%3A+R+%5Crightarrow+S%7D&bg=ffffff&fg=000000&s=0 "{f: R \rightarrow S}")
to a random variable
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
taking values in
![{R}](https://s0.wp.com/latex.php?latex=%7BR%7D&bg=ffffff&fg=000000&s=0 "{R}")
to obtain a random variable
![{f(X)}](https://s0.wp.com/latex.php?latex=%7Bf%28X%29%7D&bg=ffffff&fg=000000&s=0 "{f(X)}")
taking values in
![{S}](https://s0.wp.com/latex.php?latex=%7BS%7D&bg=ffffff&fg=000000&s=0 "{S}"))
in terms of this pullback map, allowing one to define random variables
satisfactorily in this abstract setting. The probability space models
discussed above can then be viewed as *representations* of abstract
probability spaces by concrete ones. It turns out that (up to null
events) any abstract probability space can be represented by a concrete
one, a result known as the *Loomis-Sikorski theorem*; see [this previous
post](https://terrytao.wordpress.com/2009/01/12/245b-notes-1-the-stone-and-loomis-sikorski-representation-theorems-optional/)
for details.

Another, related, approach is to start not with the event space, but
with the space of scalar random variables, and more specifically with
the space
![{L^\\infty}](https://s0.wp.com/latex.php?latex=%7BL%5E%5Cinfty%7D&bg=ffffff&fg=000000&s=0 "{L^\infty}")
of *almost surely bounded* scalar random variables
![{X}](https://s0.wp.com/latex.php?latex=%7BX%7D&bg=ffffff&fg=000000&s=0 "{X}")
(thus, there is a deterministic scalar
![{C}](https://s0.wp.com/latex.php?latex=%7BC%7D&bg=ffffff&fg=000000&s=0 "{C}")
such that ![{|X| \\leq
C}](https://s0.wp.com/latex.php?latex=%7B%7CX%7C+%5Cleq+C%7D&bg=ffffff&fg=000000&s=0 "{|X| \leq C}")
almost surely). It turns out that this space has the structure of a
commutative tracial (abstract) [von Neumann
algebra](https://en.wikipedia.org/wiki/Von_Neumann_algebra). Conversely,
starting from a commutative tracial von Neumann algebra one can form an
abstract probability space (using the idempotent elements of the algebra
as the events), and thus represent this algebra (up to null events) by a
concrete probability space. This particular choice of probabilistic
foundations is particularly convenient when one wishes to generalise
classical probability to *noncommutative* probability, as this is simply
a matter of dropping the axiom that the von Neumann algebra is
commutative. This leads in particular to the subjects of [quantum
probability](https://en.wikipedia.org/wiki/Quantum_probability) and
[free probability](https://en.wikipedia.org/wiki/Free_probability),
which are generalisations of classical probability that are beyond the
scope of this course (but see [this blog
post](https://terrytao.wordpress.com/2010/02/10/245a-notes-5-free-probability/)
for an introduction to the latter, and [this previous
post](https://terrytao.wordpress.com/2014/06/28/algebraic-probability-spaces/)
for an abstract algebraic description of a probability space).

It is also possible to model continuous probability via a nonstandard
version of discrete probability (or even finite probability), which
removes some of the technicalities of measure theory at the cost of
replacing them with the formalism of [nonstandard
analysis](https://en.wikipedia.org/wiki/Non-standard_analysis) instead.
This approach was [pioneered by Ed
Nelson](http://www.ams.org/mathscinet-getitem?mr=906454), but will not
be discussed further here. (See also
[these](https://terrytao.wordpress.com/2013/12/07/ultraproducts-as-a-bridge-between-discrete-and-continuous-analysis/)
[previous](https://terrytao.wordpress.com/2010/11/27/nonstandard-analysis-as-a-completion-of-standard-analysis/)
[posts](https://terrytao.wordpress.com/2014/06/25/lebesgue-measure-as-the-invariant-factor-of-loeb-measure/)
on the Loeb measure construction, which is a closely related way to
combine the power of measure theory with the conveniences of nonstandard
analysis.)

One can generalise the traditional, countably additive, form of
probability by replacing countable additivity with finite additivity,
but then one loses much of the ability to take limits or infinite sums,
which reduces the amount of analysis one can perform in this setting.
Still, finite additivity is good enough for many applications,
particularly in discrete mathematics. An even broader generalisation is
that of *qualitative* probability, in which events that are neither
almost surely true or almost surely false are not assigned any specific
numerical probability between
![{0}](https://s0.wp.com/latex.php?latex=%7B0%7D&bg=ffffff&fg=000000&s=0 "{0}")
or
![{1}](https://s0.wp.com/latex.php?latex=%7B1%7D&bg=ffffff&fg=000000&s=0 "{1}"),
but are simply assigned a symbol such as
![{I}](https://s0.wp.com/latex.php?latex=%7BI%7D&bg=ffffff&fg=000000&s=0 "{I}")
to indicate their indeterminate status; see [this previous blog
post](https://terrytao.wordpress.com/2013/11/16/qualitative-probability-theory-types-and-the-group-chunk-and-group-configuration-theorems/)
for this generalisation, which can for instance be used to view the
concept of a “generic point” in algebraic geometry or metric space
topology in probabilistic terms.

There have been multiple attempts to move more radically beyond the
paradigm of probability theory and its relatives as discussed above, in
order to more accurately capture mathematically the concept of
non-determinism. One family of approaches is based on replacing
deterministic *logic* by some sort of [probabilistic
logic](https://en.wikipedia.org/wiki/Probabilistic_logic); another is
based on allowing several parameters in one’s model to be unknown (as
opposed to being probabilistic random variables), leading to the area of
[uncertainty
quantification](https://en.wikipedia.org/wiki/Uncertainty_quantification).
These topics are well beyond the scope of this course.



