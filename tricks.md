
# Enable vi-mode in the terminal
To enable Vi-mode, edit (or create) the file ~/.inputrc or /etc/inputrc and add the following lines:

set editing-mode vi
set keymap vi-command
# REPL (Read–Eval–Print Loop)


# How to change from Wayland to XORG DISPLAY:
Edit /etc/gdm/custom.conf and add DefautSession=gnome-xorg.desktop to the [daemon] section.
or 
Just change the uncomment the line where there is:
WaylandEnable=false



# Trick command to mount NTFS disk
`fdisk -l` for the list of disks
`mount -o rw,mount,rw -t ntfs /dev/sdc3 /mnt/ntfs/` for the reading and 
writing

# Trick to have access on all properties and methods of JS objects in the REPL

- The <<TAB>> is for pressing tab after the `Object.`
`Object.<<TAB>>` 


# this is to create range in JS.
Array.from(new Array(20), (x,i) => i + *lowerBound*) 

# this is to create dictionaries or Maps in JS.

new Map([iterable])

example: 

array = [['smile','[[f9:smaile]]'], ['sad', '[[f9:sad]]']] // list

dictionary = new Map(array) ---> Map { 'smile' => '[[f9:smile]]', 'sad' => '[[f9:sad]]' }

-keys can be accesible through the method 'get' of the class Map: dictionary.get('smile') ---> '[[f9:smile]]'


#Object in JS are similar to dictionary in python

- This is how to assign new value in an Object

obj["key3"] = "value3"; => obj = {'key3': 'value3'}

- This is how you get the keys and the values returned in and array in the same order as in the Object

Object.keys(obj) => ['key3']

Objec.values(obj) => ['value3']

#Regex with String.match(regex_syntax)

`let x = 'is2 Thi1s T4est 3a'`

`x.match(/\d/g); => ['2', '1', '4', '3']`


# I just use this to see currently used modules:

import sys as s
s.modules.keys()
which shows all modules running on your python.

For all built-in modules use:

s.modules
Which is a dict containing all modules and import objects.

# Location of .bashrc file in Fedora Linux 25 for custom commands

home/user_name/.bashrc (will preferably work in administrator mode, but works in guest mode on my Fedora Linux though)

# How to make aliases of directories with names which has spaces

alias xxx = "cd '/home/welcome here/xxx/'"

# Some bs4 module tools

job_links = page_download_soup.select('a.icon-eye') => bs4.BeautifulSoup.select('a.icon-eye') => returns the needed html element corresponding to the <a> with a class = "icon-eye"

print(type(page_download_soup.select('a.icon-eye')[0].get_text())) => bs4.BeautifulSoup.select('a.icon-eye')[0].get_text() => prints out the text in between the tags.

job_links[0].get('href') => the bs4.BeautifulSoup.get('href') => returns the links in the href = "www.example.com" (like here it will be www.example.com)

# With re module in Python and his method findall()

You can collect all the selected characters with a reqular expression
in a list, which can be powerfull to later on choose on 
what you want.

# How to manually (add or get) modules in python environment or path in Fedora.

To add a path, launch ipython and type:

import sys
sys.path.append("path/to/Modules")
print sys.path

Note: You only have to update your PYTHONPATH once, not every time you use Python!

So now your path is updated but this is only the path to your master Python folder.

In order to have Python see the modules inside each subdirectory, add a blank file called __init__.py to each subdirectory (with two underscores on each side).

Then

# this is a trick to know path to some installed  packages

$ source `which virtualenvwrapper.sh`

The backticks are command substitution - they take whatever the program prints out and put it in the expression. In this case "which" checks the $PATH to find virtualenvwrapper.sh and outputs the path to it. The script is then read by the shell via 'source'


# This trick is for my folder structures horizontal or vertical using the 'mkdir' command in the terminal:

And an even more powerful command, creating a full tree at once (this however is a Shell extension, nothing mkdir does itself):

`mkdir -p tmpdir/{trunk/sources/{includes,docs},branches,tags}`

If one is using variables with mkdir in a bash script, POSIX `special' built-in command 'eval' would serve its purpose.

```DOMAIN_NAME=includes,docs
eval "mkdir -p tmpdir/{trunk/sources/{${DOMAIN_NAME}},branches,tags}"```

This will create:

          tmpdir
    ________|______
   |        |      |
branches   tags  trunk
                   |
                 sources
               ____|_____
              |          |
          includes     docs


# MEAN Stack

## MiddleWare Functions (multiple definitions):

- Definition 01:

Middlewares are functions executed in the middle after the input/source then produces an output which could be the final output or could be used by the next middleware until the cycle is complete.

It is like a product that goes through an assembly line where it gets modified as it moves along until it gets completed, evaluated or gets rejected.

A middleware expects some value to work on (i.e. parameter values) and based on some logic the middleware will call or not call the next middleware or send a response back to the client.

If you can't still grasp the middleware concept, it is in a way similar to the Decorator or Chain of command patterns.

- Definition 02: By Barum Rho

After simplifying things, a web server can be seen as a function that takes in a request and outputs a response. So if you view a web server as a function, you could organize it into several pieces and separate them into smaller functions so that the composition of them will be the original function.

Middlewares are the smaller functions that you can compose with others and the obvious benefit is that you can reuse them.


- Definition 03: By MNR

Keep things simple, man!

Note: the answer is related to the ExpressJS builtin middlware cases, however there are different definitions and use cases of middlewares.

From my point of view, middleware acts as utility or helper functions but its activation and use is fully optional by using the app.use('path', /* define or use builtin middleware */) which don't wants from us to write some code for doing very common tasks which are needed for each HTTP request of our client like processing cookies, CSRF tokens and ..., which are very common in most applications so middleware can help us do these all for each HTTP request of our client in some stack, sequence or order of operations then provide the result of the process as a single unit of client request.

Example:

Accepting clients requests and providing back responses to them according to their requests is the nature of web server technology.

Imagine if we are providing a response with just "Hello, world!" text for a GET HTTP request to our webserver's root URI is very simple scenario and don't needs anything else, but instead if we are checking the currently logged-in user and then responding with "Hello, Username!" needs something more than usual in this case we need a middleware to process all the client request metadata and provide us the identification info grabbed from the client request then according to that info we can uniquely identify our current user and it is possible to response to him/her with some related data.

Hope it to help someone!

# Fixing ENOSPC error with nodemon

echo fs.inotify.max_user_watches=582222 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p



# NewBell Documentation

	- Overview

		- What is the problem?

			In this last decade social networks became viral in almost all the world being one of the most used way of  interaction between human being of different regions on the globe. We are talking of more than 2.9 billions of users in the whole world.
			Thus came out of it several opportunities for different businesses and  area of activities from cooporate to small associations. Thus came with it the need of other profesional activities like software engineering, web designing, to digital marketing.

			This last one digital marketing have even made a whole new ecosystems to come up.
			Let define briefly what is digital marketing: It is just the broth usage of digitalize tools to get from social networds potential users, take them through a personalized or model journey so that they can become member(s) of one or many services being offered.

			In this direction then the use of the digital tools and plateforms for the digital marketers can become overwhelming some of them will be using more than 10 plateforms with more than 5 tools per social platforms.So at some point the ratio between their goals and their achievements is not getting better, so they are obliged to recrute more peoples to do some very repetitive jobs, and it ends up costing them more and sometimes not that much effectiove.

			So the problem here is all those repetitive tasks being needed to be used in other to maintain their different platforms to keep being active thus financially and timely costful for the digitall marketing industry.


		- How do we intend to solve this problem?


			 Our intention here is to solve all the repetitive tasks by automating many of them with an intuitive flow and a nice user experience, that can positively balance the ratio between goals and achievements of any digital marketers and even improve the user experience and customer acquisitions process on their plateform, in a more reliable and cheaper way.

		Email marketing tool
		SEO Tools
		Design Tools
		Content Marketing Tools	


	- Requirements

	NewBell is a web application which in his earlier version will be focusing on offering services of automation campagnain on on the social network Facebook and particularly on Facebook messenger plateform.

	The automation campaign on Facebook messenger will mostly help the digital marketers to be able to predefine  through a friendly user interface a set of basic to advance dialogues templates, that when activated or enabled for any of their pages Facebook messenger platform application, would automatically make that dialogue pattern to be adopted by their Facebook messenger plateform application based on some triggers from the pages visitors or page fans.

	# NewBell Signing Up process:
		Every visitor of NewBell web application can if they want to join our platform for free by signing up with an email and password or by joining with one of their already owned social networks (Facebook, Google+, Github, Twitter, etc...)
		
		# What will be available to them?:
		- Every user will own a dashboard that will permit him/her to start a variety of automation activities on their social networks accounts.
		** For now we intend to start with only Facebook
		# Users prerequirements for automation activities to be a Go for them:
			- An account with the concerned social network.
			- Administration level page, group etc for some of the social networks.
			- And in some cases some already activated application(s) with some particular services  in the the corresponding social network(s).
		# Users Prerequirements for our first functionality to be a Go for them:

		In terms to be able to use our web application services on NewBell a user should have:

		- An active Facebook Account.
		- At least an active Facebook Page.
		- At least an active Facebook messenger platform application. 



	# Eligible user journey

		The user with the intend to create an automated campaign on NewBell will need to go through this basic process.

		# First Page (Home)
		
			* Elements appearing on the first page:

				- Join or Join with Facebook or Sign UP (Call to action)


			* Possible actions on the first page:

				- Join the NewBell web application with your facebook credentials (Some special permissions will be happening in the background here)


		# Second Page (User Dashboard)

			* Elements appearing on the second page:

				- Automation Campaign
			* Possible actions on the second page:
			

# Tutoring Mentoring and Mentoring

PREMIERES NECESSITES:
- connexion a internet de 4 Mbits/s par fibre optique 25.000 frs le mois (CAMTEL) (6 MOIS)

- Creation de l'entreprise comme entreprise de service de (Training, tutoring, mentoring et autres domaines academiques et professionnels en ligne et hors ligne.