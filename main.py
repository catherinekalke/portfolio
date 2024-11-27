
import os
import webapp2
import jinja2
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


#Define parameters for Lesson, Module, and Notes
#Need to define handler for the notes page
## Pass the paramters for Lesson, Module, and Notes to the notes page handler 
## allow that to be used by the template to display the html as defined
class NotesHandler(Handler):
	def get(self):
		Lesson = "Lesson Four"
		self.render('notes.html', Modules = module_example, Lesson = Lesson)


class MainHandler(Handler):
    def get(self):
      	self.render('main.html')

class CommentPage(Handler):
    def get(self):
        wall_name = self.request.get('wall_name',DEFAULT_WALL)
        if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL

        posts_to_fetch = 10
        # If we came from a page that had more than 10 posts, we are continuing
        # the page
        cursor_url = self.request.get('continue_posts')

        # Start creating an arguments dictinoary to pass on to our jinja2 templates
        # when we render the page.
        arguments = {'wall_name': wall_name}

        # Ancestor Queries, as shown here, are strongly consistent
        # with the High Replication Datastore. Queries that span
        # entity groups are eventually consistent. If we omitted the
        # ancestor from this query there would be a slight chance that
        # Greeting that had just been written would not show up in a
        # query.
        # [START query]
        posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)

        # The function fetch_page() takes a query object and returns three things:
        # a list of post objects, a cursor to indicate where I am currently in the
        # database and a boolean to indicate whether there are more posts that I
        # can further get
        posts, cursor, more = posts_query.fetch_page(posts_to_fetch, start_cursor =
            Cursor(urlsafe=cursor_url))
        # [END query]

        # If there are more posts, we'll add a parameter so we can process this
        # parameter in the next GET request
        if more:
            arguments['continue_posts'] = cursor.urlsafe()

        # Add our posts to our argument dictionary to pass on to the jinja2 template.
        # This is how we pass our past posts data into jinja2 to process the HTML.
        arguments['posts'] = posts

        # If a person is logged in to Google's Services
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            user = 'Anonymous Poster'
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        # Create an arguments dictionary to pass onto the jinja2 templates
        arguments['user_name'] = user
        arguments['url'] = url
        arguments['url_linktext'] = url_linktext

        # Write Out Page
        self.render('posts.html', **arguments)


DEFAULT_WALL = 'Public'

def wall_key(wall_name=DEFAULT_WALL):
	return ndb.Key('Wall', wall_name)

class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=True)
    name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)

class Post(ndb.Model):
    """A main model for representing an individual post entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class PostWall(Handler):
    def post(self):
        # We set the same parent key on the 'Post' to ensure each
        # Post is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        
        #wall_name = self.request.get('wall_name',DEFAULT_WALL)
        wall_name = 'Public'

        post = Post(parent=wall_key(wall_name))

        # When the person is making the post, check to see whether the person
        # is looged into Google
        if users.get_current_user():
            post.author = Author(
                    identity=users.get_current_user().user_id(),
                    name=users.get_current_user().nickname(),
                    email=users.get_current_user().email())

        # Get the content from our request parameters, in this case, the message
        # is in the parameter 'content'
        content = self.request.get('content')



        # Make sure we can convert all types of string that we may get to unicode
        # This helps ensure we can process other other languages besides English
        if type(content) != unicode:
            post.content = unicode(self.request.get('content'),'utf-8')
        else:
            post.content = self.request.get('content')

        valid_content, error = ValidateWall(content)
        if valid_content == False:
        	self.render('error.html', Error = error)
    	else:
    		post.put()
    		query_params = {'wall_name': wall_name}
    		self.redirect('comments?' + urllib.urlencode(query_params))



# [END wall]


def ValidateWall(content):
	valid = True
	error = {}
	if content.isspace == True:
		error = "C'mon, at least put something before subitting.."
		valid = False
	if len(content) < 2:
		error = "You really should have more than that to say"
		valid = False
	if len(content) > 500:
		error = "Woe there, I don't need your life story, but thanks"
		valid = False
	return valid, error



app = webapp2.WSGIApplication([
	('/', MainHandler),
    ('/comments', CommentPage),
    ('/notes', NotesHandler),
    ('/sign', PostWall)
], debug=True)

module_example = [
		['Servers', 'Servers are machines/computers on the Internet that respond to user request and host applications. When a request is made to a server, a request line is sent followed by a number of headers that include information about the GET request. The server then responds with a message with headers of its own including status codes etc.'], 
		['Importance of Validating Input', 'If input is not validated it can break the form and funtionality of the application you are delivering, even allowing hackers to misuse code. It also allows the application tp provide feedback to the user on what their error was so they may correct it for a more functional web application.'],
		['HTML Templates and Abstractions', 'Repetition is inefficient and can make programs unnecessarily long and complex, leading to a greater propensity for errors. HTML templates allow for minimum repetition when writing code by having a set syntax of HTML with variables in it to be defined by the web application such that the page can be rendered dynamically with the appropriate data without that data needing to be hardcoded. Abstraction allows for HTML inputs to be converted so as not to interfere with the HTML display']
		
		]


