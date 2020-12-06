from pathlib import Path
from typing import List
import shutil


class Parser:
    extensions: List[str] = []

    def __init__(self):
        pass

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path: Path, dest, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(self, path: Path, source, dest):
        destination = dest / path.relative_to(source)
        shutil.copy2(path, destination)


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)


# n this module we will create a Parser base class that will have several functions that
# will help when converting Markdown and ReStructuredText to HTML.
#
# To start, open the ssg/parsers.py file. We will add a few type annotations, one of which requires
# an import. Import List from typing. Also, import Path from pathlib.
#
# Next, create a class called Parser. Create a variable called extensions a
# nd assign it an empty list. Annotate extensions with the type List[str].
#
# 2
# Validate Extensions
#
# We will need to know whether certain files have a parser. This will be done by looking at the extension.
#
# Create a new method in the Parser class called valid_extension(). This method should accept an extension, and return whether or not that extension is in the class variable self.extensions. Hint: This method is part of the Parser methods so it should accept self as an argument.
#
# 3
# Base parse() method
#
# Since the Parser class is a base class, we will create a method that will need to be implemented in any subclass.
#
# Call this method parse(), it should accept a path, source, and dest. Annotate each of these with the Path type.
#
# In the body, raise the NotImplementedError.
#
# 4
# Parser read() method
#
# The Parser class will need to be able to read the contents of a file.
#
# Create a method called read() that accepts a path. Use a with statement, and a call to open() to open path for reading as file.
#
# In the body of the with statement, return what is read() from file.
#
# 5
# Parser write() method
#
# Still in the Parser class, create a method called write() that accepts the following arguments: path, dest, and content. Also, add an argument called ext with a default value of ".html".
#
# In the body of the write method, create a variable called full_path. This variable will need to contain the full path to the file being written to.
#
# The first part of the path is self.dest.
#
# The second part names to be the name of the file with a new extension.
#
# So after a / operator, call with_suffix() on path passing in ext. Chain on the name property. Hint: destination / with_suffix().name.
#
# 6
# Open file for writing
#
# Still in the write() method, use with and open() to open full_path for writing as file.
#
# In the body of the with statement, write() content to file.
#
# 7
# Parser copy() method
#
# Move back to the top of the page and import shutil. We'll this use this library to copy resources to the correct location.
#
# Below the exiting methods in the Parser class, create a new method called copy(). This method should accept the following arguments path, source, and dest.
#
# In the body, use the copy2 method (from the shutil module) to copy the file at path to the correct location in the destination folder structure.
#
# This can be done by passing path as the first argument to copy2 and the second argument is made up of the dest / and the path relative to the source.
#
# 8
# ResourceParser subclass
#
# Create a class called ResourceParser that is a sub-class of Parser. Create a class attribute called extensions and assign it a list with five extensions, ".jpg", ".png", ".gif", ".css", and ".html".
#
# Implement the parse() method in the ResourceParser class. It should have the same signature as in the base class Parser.
#
# In the body, call the inherited copy() method. Which is inherited from Parser. Pass in path, source, and dest to copy().
#
# 9
# Available parsers
#
# Open ssg/site.py, and add a parameter to the constructor parameter list called parsers. Set the default value to of parsers to None.
#
# In the body of the constructor, set a new instance variable called parsers to the expression parsers or [].
#
# 10
# Parser configuration
#
# Open ssg.py, and at the top import ssg.parsers.
#
# Find the config dictionary in the main function and add a new key value pair as follows:
#
# Key - parsers
# Value - List with one element: [ssg.parsers.ResourceParser()]
# 11
# Site class load_parser() method
#
# Back in ssg/site.py, add a new method to the Site class called load_parser() below the existing methods. This method should accept a single parameter called extension.
#
# The first statement in the method should be a for loop that cycles through self.parsers. Call the loop-value parser.
#
# The body of the for loop should have an if statement that tests if extension is a valid_extension(). Hint: parser is an instance of the Parser class, so it will have a valid_extension() method.
#
# Return parser in the if statement.
#
# 12
# Site class run_parser() method
#
# Still in the Site class, add a new method called run_parser(). This method should accept a parameter called path.
#
# In this method, call load_parser(), passing in path.suffix, and save the result to a variable called parser.
#
# 13
# Call the parse() method
#
# Still in the run_parser() method, test if parser is not None. If parser is not None, then call the parse() method of parser.
#
# Pass path as the first argument to the parse() method. Then, pass source and dest, both of which are instance variables to the parse() method.
#
# Add an else to the if that prints the message Not Implemented.
#
# 14
# Run the parser
#
# To connect everything together, find the if statement in the build() method. Add an elif that tests whether path is a file.
#
# If path is a file, then call run_parser(), passing in path. Hint: run_parser() is part of the Site class.
#
# Push your code to GitHub
# to check your work.
#
# Check my work
# Projects logo
# Build a Static Site Generator with Python
#     1