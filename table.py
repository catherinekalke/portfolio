from collections import namedtuple
import sqlite3

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]


# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# make the function query() return the number of votes for the link whose ID is
# 15
#BELOW CODE DOES NOT WORK

#class Link(tuple):
#    'Link(id,submitter_id,submitted_time,votes,title,url)'

#    def query(find_id):
#        for id in links:
#            if id == find_id:
#                return tuple(votes)
#           else:
#                return None
        
#print query(15)

#UDACITY defined the code this way
def query():
    for l in links:
        if l.id == 15:
            return l.votes 

print query()
    
# TASK
#
# make the function query() below return:
# - a list of Links submitted by user 62443
# - sorted by ascending submission time

from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]


# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# make the function query() return a list of Links submitted by user 62443, by
# submission time ascending


def query():
    submissions = []
    for l in links:
        if l.submitter_id == 62443:
            submissions.append(l) 
    submissions.sort(key = lambda x: x.submitted_time)         
    return submissions

print query()   
    
#make and populate a table

db = sqlite3.connect(':memory:')
db.execute('create table links ' + '(id integer, submitter_id integer, submitted_time integer, ' + 'votes integer, title text, url text)')
for l in links:
    db.execute('insert into links values(?,?,?,?,?,?)', l)

def query():
    cursor = db.execute("select title from links")
    results = c.fetchall()
    return results

def query():
    cursor = db.execute("select * from links")
    for link_tuple in cursor:
        link = Link(*link_tuple)
        print link.votes
# The above is python syntax for passing all of the parameters in this tuple as arguments to the function
# The above line is a constructor

print query()

def query():
    c = db.execute("select * from links where id = 2")
    link = Link(*c.fetchone())
    return link.votes

print query()

# QUIZ - make the function query() return the ID of the link that was 
# submitted by user 62443 and has > 1000 votes. 

def query():
    c = db.execute("select * from links where submitter_id = 62443 and votes > 1000")
    link = Link(*c.fetchone())
    return link.id

print query()
 
# QUIZ - make the function query() return a list of the IDs of the links 
# that were submitted by user 62443 sorted by submission time ascending. 
def query():
    submissions = []
    c = db.execute("select * from links where submitter_id = 62443 order by submitted_time asc")
    for link_tuple in c:
        link = Link(*link_tuple)
        submissions.append(link.id)
    return submissions

print query()

# QUIZ - make the function query() return a list of the IDs of the links 
# that were submitted by user 62443 sorted by submission time ascending.
# Following is a simpler cleaned up code for doing this

def query():
    c = db.execute("select id from links where submitter_id = 62443 order by submitted_time asc")
    results = [t[0] for t in c]
    return results

print query()

# QUIZ - implement the function link_by_id() that takes a link's ID and returns
# the Link object itself
def link_by_id(link_id):
    for l in links:
        if l.id == link_id:
            return l
    
print link_by_id(7)

# QUIZ - implement the function build_link_index() that creates a python dictionary
# the maps a link's ID to the link itself

def build_an_index():
    index = {}
    for l in links:
        index[l.id] = l
    return index

print build_an_index()

link_index = build_an_index()

def link_by_id(link_id):
    return link_index.get(link_id)
# Can also use return link_index.get(link_id)
# This will return None if the function cannot find the argument in link_by_id

print link_by_id(4)
# For each Link object we should have the following mapping in the dictionary:
#id of Link object: Link object

# QUIZ - implement the function add_new_link() that both adds a link to the 
# "links" list and updates the link_index dictionary. 
def add_new_link(link):
    links.append(link) 
    link_index[link.id] = link

l = Link(50, 1, 1, 1, "title", "url")
add_new_link(l)

print links[-1]
print link_by_id(50)

#The app.yaml file
#You’ve seen the app.yaml file a few times already, but you might be confused as to exactly how it works. For the next few sections, please follow along on Google’s Cloud Playground by following these steps:

#https://cloud-playground.appspot.com/playground/
#click ‘+ make a copy’ for the Hello World example
#click 'open project' for ‘Copy of Hello World’
#As Steve explained, the YAML file will handle requests from the browser and make sure that they are directed to the right place, but how does that work in terms of the code? For requests to app-name.appspot.com/favicon.ico, we see the server directs the browser to where we’ve uploaded the favicon (the small icon that you see in the title or next to the URL).

#On line 12, however, things get a bit more complex. This /.* is what’s called a regular expression. Regular expressions are a way of matching strings using symbols.

#There are all sorts of regular expressions that can match many different kinds of strings. To learn more about regular expressions (or regexes as they are more colloquially known) take a look here. We won’t be using regular expressions too much in the course, so it’s okay if you don’t understand all of this right now.

#The . symbol is a catch-all, which allows us to match any single character. The * symbol means the expression will match any number of characters which match the previous symbol. So if we have a /.* , that will allow us to essentially match all strings that come after the last forward slash in the URL and direct them to main.app.

#In other words app-name.appspot.com/index, app-name.appspot.com/$$$, and app-name.appspot.com/ will all be directed to the same python file. The only exception is app-name.appspot.com/favicon.ico since we’ve specially defined that and the handler checks it first.

#The main.py file
#You’ll see the same /.* near the bottom of the main.py file. This handler directs the script to run a given function when the browser requests a certain page. Right now, it directs all requests that match to the MainHandler function, which prints ‘Hello, World.’ to the main page. The following quiz outlines how this works.

# Previous

#https://cloud.google.com/appengine/docs/python/gettingstartedpython27/usingdatastore

#Questions about Datastore

#When you can answer these questions you are ready to continue.

#The first two questions have to do with the Greeting class code, which looks like this:

#There's a line of code that says content = ndb.StringProperty(indexed=False).
#Will you be able to make queries based on content if you use indexed=False?

#The Guestbook class has a post method, which has lines of code to create a new instance 
#of the Greeting class and set the value of author and content. 
#Why doesn't this code ever set the value of date?

#The syntax for making datastore queries is slightly different than pure SQL, 
#but very similar. In your locally running version of this guestbook app, 
#add a few entries and notice the order that they display in your browser. 
#Can you get them to display in the opposite order by removing a single character 
#from the code in guestbook.py?
