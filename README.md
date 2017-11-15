# site-generator

A python script to make websites and populate them

This is the start to one of the tools I made when I worked at Rack City Media. We had a need for to roll out several landing pages a day. Some kinds of landing pages were less involved and could be generated automatically. I built a command line tool to do what we need based on the code that I am sharing here. 

## What is it for?

The solution I needed was an automated way to create multiple websites of varying depth with static content displaying a link.

## What does it do?

I hope it just inspires you. This code was a step along the way me for me to build something. 

It takes a list of domain names, and a list of paths. It will build an index.php file at each level of the web path. So then you might have a list of images, paragraphs, and links to display. Or what ever you want to do.

## How to use it

Replace the dummy filepath in CreatePath.py. This path represents the public directory where all your websites are hosted. In the main.py, fill out at least the domains and file_paths lists. Then hit run. You should see that it generated all files in the folder called targetFolder.
