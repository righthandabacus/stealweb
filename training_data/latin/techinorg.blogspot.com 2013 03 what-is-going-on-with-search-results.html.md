### [What is going on with the search results?](http://techinorg.blogspot.com/2013/03/what-is-going-on-with-search-results.html)

When I see googlers in online forums defending the search results they
often ask for data sets showing the problem. This isn't a data set but
here should be some reproducible test cases that fails horribly for what
was once the undisputed place to go for relevant search results.  
  
  
### Example 1: "sublime text 2" "focus group"

**Query:** "sublime text 2" "focus group"  
**Expected result:** Documents including the word groups "sublime text
2" and "focus group".  
**First result**: <http://www.sublimetext.com/2>  
**Problem:** Irrelevant  
**Possible explantion**: Extensive linking using  "focus group"as link
text? (Doesn't prevent it from being utterly irrelavant.)  
### Example 2: cisco "anyclient"

**Query**: cisco "anyclient"  
**Expected results**: A list of documents containing something like
cisco + the exact word "anyclient"  
**First page of results:** All results are for "AnyConnect". Which seems
to be the correct product name but was *not what I was searching for.* I
was searching to see if anyclient was a common mistake, if there had
been a product called anyclient etc so I would not embarrass myself.  
**Problem:** *Silent* rewrite of my query. I'm all for usability
features like suggest, "Did you mean" etc. "Showing results for
&lt;something else&gt;, did you mean &lt;what you searched for&gt;?" is
a pita to me but I can see it being useful for less technically inclined
people and people who hasn't developed the same kind of tunnel vision as
me. *Silently* rewriting counts as bug or arrogance in my book.  
  
  
Trying to get around these issues
---------------------------------

### Report the problem

This is obviously a bug so lets report it. Done. Months ago. No change
yet.  
[![](http://3.bp.blogspot.com/-2lXEUtrYMDw/URskbuJDBAI/AAAAAAABEGM/hFAnHk1Tgq4/s640/snapshot9_web_ready.png)](http://3.bp.blogspot.com/-2lXEUtrYMDw/URskbuJDBAI/AAAAAAABEGM/hFAnHk1Tgq4/s1600/snapshot9_web_ready.png)
Image showing Googles error reporting interface. Trying to report the
problem is an exercise in futility. They may or may not fix it but on
one point they are very clear:  They will never inform you. The only way
you will ever know is if you see a change sometime.
  
### Activate the "verbatim" search tool

 Turns out Google has thought of this. Here is the verbatim ("ordrett")
search tool. Good idea, one minor flaw: It doesn't work!  
  
<table>
<tbody>
<tr class="odd">
<td><a href="http://4.bp.blogspot.com/-_N34MEKEK3U/URsokQlNK0I/AAAAAAABEGo/1TCIMjGDWpc/s1600/snapshot14.png"><img src="http://4.bp.blogspot.com/-_N34MEKEK3U/URsokQlNK0I/AAAAAAABEGo/1TCIMjGDWpc/s640/snapshot14.png" /></a></td>
</tr>
<tr class="even">
<td>No, &quot;Backup Exec&quot; is not &quot;Shopify&quot;. And this is hardly what I'd call verbatim.</td>
</tr>
</tbody>
</table>

  
### Using another search engine

I love competition. So I tried with a couple of other search engines.  
  
<table>
<tbody>
<tr class="odd">
<td><a href="http://2.bp.blogspot.com/-RCC0ASv5okw/URspaFR424I/AAAAAAABEG0/AMXWO5FlElM/s1600/snapshot19.png"><img src="http://2.bp.blogspot.com/-RCC0ASv5okw/URspaFR424I/AAAAAAABEG0/AMXWO5FlElM/s640/snapshot19.png" /></a></td>
</tr>
<tr class="even">
<td>DuckDuckGo also insists that BackupExec is relevant when searching for Shopify.</td>
</tr>
</tbody>
</table>

  



