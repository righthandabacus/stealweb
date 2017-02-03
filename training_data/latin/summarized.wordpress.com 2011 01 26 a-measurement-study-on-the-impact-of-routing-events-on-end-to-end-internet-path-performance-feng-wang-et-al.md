A Measurement Study on the Impact of Routing Events on End-to-End Internet Path Performance, Feng Wang et.al.
-------------------------------------------------------------------------------------------------------------

January 26, 2011 at 6:06 pm · Filed under
[Uncategorized](https://summarized.wordpress.com/category/uncategorized/)
·Tagged [BGP](https://summarized.wordpress.com/tag/bgp/),
[Measurement](https://summarized.wordpress.com/tag/measurement/),
[Routing](https://summarized.wordpress.com/tag/routing/)

**BGP:**

-   Path vector Protocol : Routers advertise path (sequence of AS’s) to
    neighbors
-   Stateful: Only advertise changes: new route, or withdrawal
-   Policy-based: Select single best-route for each prefix, local
    policies
-   Over the same network, peering with a neighbor is consistent with
    the requirements of TCP

**Q.** *Is the entire path vector required? Would only the next-hop
information suffice?* **A.**No, if only next-hop is known, then policy
decisions cannot be made.

**Q**. *How much overhead do keepalive messages in BGP cause?* **A.**
The overhead is low, and the usefulness in keeping the session alive
achieves the aims of statefulness as well as security.

**Preliminaries:**

**Q.** *Should we expect routing changes to affect end-to-end
performance? Is it unavoidable?* **A**. The design principle of “Route
around failure” does not state explicitly that the endpoint should know
about the failure. Thus it is not absolutely expected that routing
events must affect end-to-end performance. This explains the motivation
for such a measurement study.

**Q.** *Why wasn’t it until 2005 that this study took place? What makes
it hard to conduct such a study?* **A.** Since the PlanetLab nodes used
for the study were not previously available, it was difficult to observe
routing events on a large scale prior to 2005.

**Q**. *What tools are available for measurement studies like this one?*
**A**. There are hardly any tools apart from rudimentary end-to-end
tools such as ping, traceroute and Wireshark. It is hard to
differentiate packets at nodes. Allowing tools for filtering packets can
also pose security concerns. ISPs sometimes intentionally drop ICMP
packets to reduce congestion and disallow people from looking inside
their networks, as this could lead to leaking of competitive
information. That is why even traceroute names nowadays are hard to
figure out.

*The network does not make it easy for such measurement studies to be
conducted*.

**Some Details:**

**Q.** *Why does a router have a Minimum Route Advertisement Interval
(MRAI)?* **A.** The MRAI enables the nodes to give the latest route
information rather than information about every update. This makes sure
that route-flapping does not occur.

Q. *What is a “no valley” policy?* A. A no-valley policy is one in which
a router selectively chooses not to advertise certain routes to a peer,
since it would result in additional traffic that would be carried for
free. Such traffic would lead to lower revenues and is therefore a
negative incentive.

**Q**. *What is a “prefer customer” policy?* **A.** A router would
always prefer carrying traffic for a customer rather than other sources
to traffic, so that the customer gets good performance over the network.

**Q.** *What are BGP Beacons and why were they set up?* **A**. BGP
Beacons are prefixes known to routers that were specifically set up for
testing BGP. The beacons may or may not have end hosts, and the RFC does
not specifically state that they must. In the paper, these beacons are
used to emulate failover and recovery events realistically.

**Q.** *Why use BGP beacons?* **A.** BGP beacons allow emulation of real
traffic, without ever using useful information with these prefixes. This
enables privacy of data and can allow measurement studies without
compromising user security.

**Route Failover**

**Q.** *How do they identify route failures?* **A.** ICMP Host
unreachable messages are used to identify route failures. Usually
routers would return default records in the case a route is not found.
But since the ISPs involved here are Tier 1 ISPs, they do not have
default records and will return ICMP messages instead.

**Q.** *Why do they say they under-estimate ICMP packet loss?* **A.**
ICMP messages involve the processor on the router. This means that in
order to avoid attacks, some ICMP packets will be filtered out. Thus the
ICMP messages observed do not represent the entire fraction of those
actually generated.

**Q.** *How do they create a controlled route failure event?* **A**. The
BGP beacons intentionally withdraw routes, leading to controlled route
failure events.

**Loss Bursts During Route Failover**

**Analysis:** They report up to 480 consecutive packets lost during a
failover.

This measurement was estimated by looking at gaps in sequence numbers of
messages. A typical endpoint may receive a packet every 50 ms,
corresponding to around 20 packets/s . Thus the loss of 480 consecutive
packets is close to 25 seconds of lost data.

The understated and shocking result in from this paper is that several
long bursts are observed, each of which is many seconds long. This
result made this paper a very widely built upon and studied paper.

**Q**. *Is this unavoidable?* Are the bursts reasonable and technically
feasible? **A.** No. the bursts are almost 3 orders of magnitude greater
than expected.

**Q.** *Is this an inherent property of BGP?* **A**. No. It may be
possible that speed o recovery depends on the policy. But the policy
would always try to increase this speed to keep its customers satisfied.
Storing and using potentially free paths may be expected to lead to
faster recovery.

**Q**. *How does this compare to what a user could expect?* **A.** A
user would see a huge latency (~25 s), and would not expect the latency
to be this large.

**Q.** *Why are there often two or more bursts of packet loss?* **A**.
The main reason for multiple bursts may be unsynchronized clocks. When a
route changes, different nodes on the route may notice the change at
different times. Thus before all the nodes converge on the new route,
there may be sporadic connectivity, leading to multiple bursts.
Sometimes the routes may take even minutes to converge, and there may be
some pathological cases which take even longer. This observation is
consistent with the policies and incentives involved, leading to the
inference that the protocol may have some fundamental problems.

Curiously, in most cases in the results, there are exactly two bursts.
This may be because there are much larger number of paths than before
and the convergence may be faster.

**Q.** *How interconnected are ISPs?* **A.** ISPs show a lot of
diversity. There may be some which are richly interconnected in the
logical sense, whereas others may be sparsely connected. Typically one
would expect an ISP to have 10-40 switching centers.

*The takeaway from this analysis is that lot of data gets lost during
such failures. Also it is important to ask questions about the numbers
in such measurement studies.*

**Route Recovery**

***Q.** Can packets be lost when a new route is added, or a failed route
returns?* **A.** Yes, new paths may create loops. Forwarding loops may
be created when a route changes, causing disruption in packet traffic.

**Q***. How are loops detected?* **A**. Loops are detected by observing
ICMP messages for TTL exceeded.  If the TTL exceeded message is seen
then some packet is being forwarded in a loop.

**Q.** *Why are loops created when a path is added?* **A.** If the graph
is richly connected, then a new route is equivalent to a failed route,
in the sense that the nodes need to know the new information about the
route. In both cases information propagates through the nodes, and
results in packet loss if the nodes are unsynchronized. Thus before the
nodes converge to the new route, forwarding loops could be created.

**Conclusions**

-   Multiple bursts of packet loss occur due to routing changes
-   Forwarding loops may occur during to route recovery
-   MRAI tuning may be able to reduce packet loss
-   Storing a second best path may improve performance

***Q.** What tools would you want for better measurement studies?*

-   Impose that measurements are required
-   Tools for measuring topology and congestion on links would by
    themselves go a long way to understanding behavior of the network.

***Q**. How might we design a better “BGP”?*

-   More measurement infrastructure is needed
-   Router policies between AS’s could be modified
-   Synchronize clocks by using GPS signals
-   Mark packets with which generation of routes to use, in order to
    overcome unsynchronized clocks
-   Enable a tighter coupling between Layers 2 and 3 of the network.



