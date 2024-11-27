# Lession 4.5: Hello Webapp World
#
# This starter code will illustrate how we can create a webserver that writes out
# a "Hello World" to the browser usig the webapp2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4150259168/m-48722218

#The following first snippet works, the second one works now!

import webapp2

form="""
<form action="http://www.google.com/search">
    <input name="q">
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers["Content-Type"] = "text/plain"
        self.response.out.write(form)

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug = True)

#The following snipppet works

import webapp2

form="""
<form action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers["Content-Type"] = "text/plain"
        self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers["Content-Type"] = "text/plain"
        q = self.request.get("q")
        self.response.out.write(q)       

app = webapp2.WSGIApplication([('/', MainPage),
                             ('/testform', TestHandler)],
                              debug = True)

#This will show the HTTP GET output

import webapp2

form="""
<form action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers["Content-Type"] = "text/plain"
        self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers[Content-Type'] = 'text/plain'
        #q = self.request.get("q")
        #self.response.out.write(q)    

        self.response.headers['Content-Type'] = 'text/plain'   
        self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/testform', TestHandler)],
                              debug = True)

#HTTP Output looks like this - the above is a handy tool for debugging to be able to see where
#something broke in the HTML code

GET /testform?q=udacity+ia+awesome HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us
Dnt: 1
Host: localhost:10080
Referer: http://localhost:10080/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9
X-Appengine-Country: ZZ

#HTTP output for POST instead of GET
POST /testform HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us
Content-Length: 11
Content-Type: application/x-www-form-urlencoded
Content_Length: 11
Content_Type: application/x-www-form-urlencoded
Dnt: 1
Host: localhost:10080
Origin: http://localhost:10080
Referer: http://localhost:10080/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9
X-Appengine-Country: ZZ

q=some+text

#Using POST

import webapp2

form="""
<form method="post" action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers["Content-Type"] = "text/plain"
        self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        #self.response.headers[Content-Type'] = 'text/plain'
        #q = self.request.get("q")
        #self.response.out.write(q)    

        self.response.headers['Content-Type'] = 'text/plain'   
        self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/testform', TestHandler)],
                              debug = True)

# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
          valid = string.capitalize(month)
          if valid in months:
            return valid
          else:
            return None

print valid_month("january") 
# => "January"    
print valid_month("January") 
# => "January"
print valid_month("foo")
# => None
print valid_month("")
# => None


string.capitalize(word)¶
Return a copy of word with only its first character capitalized.

A Note on Optional Parameters
Youre about to see code that looks like this
And this can be pretty hard to understand.

Note how write_form takes two parameters, self and error. But notice that it says error="". 
This is an example of an optional parameter. 
It means that you can specify a value for the error parameter when you call the function
but you don't have to. 
If you don't specify a value, it will take a default value (in this case, the empty string "").

# User Instructions
# 
# Write a function 'sub_m' that takes a 
# name and a nickname, and returns a 
# string of the following format: 
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
# 

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return
    
#print sub_m("Mike", "Goose") 
# => "I'm Goose. My real name is Mike, but my friends call me Goose."

#the following code does not work 

# Lession 4.6: Responding Based on Verification

# This session will show us how we can put in custom responses in our server in order to respond
# to a user whether the birthday entered is valid or not

# https://www.udacity.com/course/viewer#!/c-nd000/l-4175328805/m-48714318


import webapp2

form = """
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type="text" name="month">
    </label>

    <label> Day
        <input type="text" name="day">
    </label>

    <label> Year
        <input type="text" name="year">
    </label>

    <div style="color:red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

def valid_month(month):
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2020:
            return year

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": month,
                                        "day": day,
                                        "year" year})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("That doesn't look correct to me my friend",
                            user_month, user_day, user_year)
        else:
            self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([("/", MainPage)], debug = True)

# Lession 4.7: Introducing Templates

# We introduce templates to build complicated strings using the Jinja2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-686598825

import os

import jinja2
import webapp2

# Set up jinja environment

template_dir = os.path.join(os.path.dirname(__file__), "templates")

# Instructor Notes:
# Suggest to print out template_dir to see how the file path is being constructured.
# You can find the print out in the Logs in Google App Engine (GAE). For Windows and Mac users,
# you need to click on the "Logs" button to be able to see the print messages

# print "###" # These hash marks helps us locate our print statement from the rest of the messages
              # Google App Engine gives us
# print template_dir
# print "###"

# For Windows Users, you need to add in a logging flag for GAE to print out your
# statements appropriately. Please go here to download the "Google App Engine Troubleshooting"
# guide to learn how to add in the logging flag:
# https://www.udacity.com/course/viewer#!/c-nd000/l-4166899177/m-3974308850

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""
item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        output = form_html
        output_hidden = ""

        items = self.request.get_all("food")
        if items:
            output_items = ""
            for item in items:
                output_hidden += hidden_html % item
                output_items += item_html % item

            output_shopping = shopping_list_html % output_items
            output += output_shopping

        output = output % output_hidden

        self.write(output)

app = webapp2.WSGIApplication([("/", MainPage)])

# http://jinja.pocoo.org/

# Lession 4.7: Escaping Templates

# Escaping HTML characters is an important function to learn because this prevents
# unintended HTML code from rendering on the browser, stopping malicious users from
# abusing your site.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-668210172

import os
import jinja2
import webapp2

# Set up jinja environment

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Handler(Handler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items = items)

app = webapp2.WSGIApplication([("/", MainPage)])

Remember all that you can do with templates! You can:

Use Template Inheritance: This lets you define a base template which you can later plug new HTML into. This is useful when, for example, you want to have a consistent header and footer across your app.

Add Repeated Elements: If you've got many divs that all have the same structure, it's much better to use a for loop. For example...

{% for concept in concepts %}
<div class="concept">
  <div class="concept-title">
    {{ concept[0] }}
  </div>
  <div class="concept-description">
    {{ concept[1] }}
  </div>
</div>
{% endfor %}
Add Conditionality: Maybe you only want to add something if something else is true. Jinja let's you use if statements to do this.

So don't code yet! Instead, spend some time (10-30 minutes) thinking about how you may want to take advantage of HTML templates.

 Previous

https://cloud.google.com/appengine/docs/python/gettingstartedpython27/templates

https://discussions.udacity.com/t/stage-4-webcasts/16367

https://discussions.udacity.com/t/stage-4-webcasts/16367/6

Udacity First reviewer feedback on code

Setting autoescape=True the moment you instantiate your Jinja environment is 
perhaps one of the most effective ways 
of ensuring that your application remains protected against HTML injection attacks, well done!

Great use of class inheritance, using the inherited methods help you avoid repetition, well done!

Udacity reviewer suggestion

Both of the request handlers above (notes and main page) can be implemented with 
a single one by using weapp2's uri mapping functionality.
This can be particularly convenient if you have a large number of pages.

For example:

class MyHandler(Handler):`
    def get(self, page):
    self.render("{0}.html".format(page))
Then configuring webapp2.WSGIApplication as follows:

app = webapp2.WSGIApplication([...,('/(.+)', MyHandler),...], debug=True)
The /(.+) string above is actually a regular expression
and the (.+) will match one or more characters or decimal digits 
which webapp2.WSGIApplication will pass along to MyHandler as positional arguments. 
Notice that in MyHandler above we have page as our first positional argument.

You can read more about app engine URI routing here:
https://webapp-improved.appspot.com/guide/routing.html
