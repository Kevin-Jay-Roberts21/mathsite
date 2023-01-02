from django.shortcuts import render
from .forms import SearchAllPages
from bs4 import BeautifulSoup
import os

# Create your views here.
def home(response):
	template_name = "main/home.html"
	action = "/home/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})

def theGreatBooks(response):
	template_name = "theGreatBooks/theGreatBooks.html"
	action = "/theGreatBooks/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def theGreatConversation(response):
	template_name = "theGreatBooks/theGreatConversation.html"
	action = "/theGreatConversation/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def theIliadOfHomer(response):
	template_name = "theGreatBooks/theIliadOfHomer.html"
	action = "/theIliadOfHomer/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def theOdyssey(response):
	template_name = "theGreatBooks/theOdyssey.html"
	action = "/theOdyssey/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})


def research(response):
	template_name = "research/researchHome.html"
	action = "/researchHome/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})

def examples(response):
	template_name = "examples/examplesHome.html"
	action = "/examplesHome/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})

def myClasses(response):
	template_name = "myClasses/myClassesHome.html"
	action = "/myClassesHome/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def calculus1Class(response):
	template_name = "myClasses/calculus1Class.html"
	action = "/calculus1Class/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def calculus2Class(response):
	template_name = "myClasses/calculus2Class.html"
	action = "/calculus2Class/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def calculus3Class(response):
	template_name = "myClasses/calculus3Class.html"
	action = "/calculus3Class/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def linearAlgebraAndDifferentialEquationsClass(response):
	template_name = "myClasses/linearAlgebraAndDifferentialEquationsClass.html"
	action = "/linearAlgebraAndDifferentialEquationsClass/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def linearAlgebraClass(response):
	template_name = "myClasses/linearAlgebraClass.html"
	action = "/linearAlgebraClass/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})
def ordinaryDifferentialEquationsClass(response):
	template_name = "myClasses/ordinaryDifferentialEquationsClass.html"
	action = "/ordinaryDifferentialEquationsClass/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})

def search(response):
	template_name = "main/searchHome.html"
	action = "/searchHome/"
	if response.method == "POST":
		searchPages = response.POST["searchPages"]
		templates = runSearch(searchPages)
		return render(response, "main/searchHome.html", {action:action, "templates":templates})
	else:
		return render(response, template_name, {action:action})
	return render(response, template_name, {})

def runSearch(word):
	# open all templates and search for the word
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	# Define the filename and the full file path
	allTemplates = ['examples/examplesHome', 'theGreatBooks/theGreatBooks', 'theGreatBooks/theGreatConversation', 'theGreatBooks/theIliadOfHomer', 'theGreatBooks/theOdyssey', 'main/home', 'myClasses/myClassesHome', 'myClasses/ordinaryDifferentialEquationsClass', 'myClasses/calculus1Class', 'myClasses/calculus2Class', 'myClasses/calculus3Class', 'myClasses/linearAlgebraClass', 'myClasses/linearAlgebraAndDifferentialEquationsClass', 'research/researchHome']

	templatesContainingWord = []
	for i in range(len(allTemplates)):
		file = allTemplates[i]
		filename = file + '.html'
		filepath = BASE_DIR + '/main/templates/' + filename

		path = open(filepath, 'r')
		with open(filepath, 'r') as fp:
			lines = fp.readlines()

		templateString = "";
		for i in range(len(lines)):
			templateString += lines[i]
		
		soup = BeautifulSoup(templateString, "html.parser")

		# NOTE: I'm only checking everything that's in a p or h2 tag. So make sure that all content is in one of the two
		allText = []
		for para in soup.find_all("p"):
			allText.append(para.get_text())
		for title in soup.find_all("h2"):
			allText.append(title.get_text())
		
		for text in allText:
			text = text.lower()
			word = word.lower()

			if word in text:
				templateChunk = []
				wordCount = countWordOccurances(word, allText)
				niceTemplate = stripFolderName(file).replace("/", "")
				templatePath = stripFolderName(file)
				templateChunk.append(templatePath)
				templateChunk.append(niceTemplate)
				templateChunk.append(wordCount)
				templatesContainingWord.append(templateChunk)
				break
	
	return templatesContainingWord

def countWordOccurances(thisWord, thisText):
	wordCount = 0
	for i in thisText: 
		wordCount += i.lower().count(thisWord)
	return wordCount



def stripFolderName(path):
	for i in range(len(path)):
		if path[i] == "/":
			path = path[i:] + "/"
			break
	return path
