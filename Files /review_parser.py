#!/usr/bin/env python3

#a little script to parse the grand reviews

#usage 1: python3 utils/review_parser.py
#outcome 1: will print out a dictionary with named values of all reviews, also will indicate which reviews don't fit the template

#usage 2: add the following to your other python script (not as a comment):
# import utils.review_parser
# reviews = utils.review_parser.main()

#outcome 2:ui
# you can now call import the parsed reviews from within another script

def main():

    #imports a library which gives us extra utilities to deal with files
    import os

    review_path = 'reviews'

    articles = [] #a list which will store all our articles once processed
    for review in os.listdir(review_path):
        article = {} #for each article we make a dictionary so we can search for values (like 'title') later
        if not review == 'review_template.md' or review.lower() == 'readme.md':
            try:
                review_text = open(os.path.join(review_path,review)).read() #open the review
                review_text_lines = review_text.splitlines() # split it into lines
                review_text_filtered = list(filter(None,review_text_lines)) # filtering out all empty lines

                platform = []
                functionality = []
                type_of_tool = []
                usage = []
                images = []

                #we store each review as two lists which are shifted by one position, so that we can ask for the 'next_line' as we iterate through the 'current_line'
                for current_line, next_line in zip(review_text_filtered, review_text_filtered[1:]+review_text_filtered[:1]):
                    if current_line.startswith('## The Good'):
                        the_good = next_line
                    if current_line.startswith('## The Bad'):
                        the_bad = next_line
                    if current_line.startswith('## The Bottomline'):
                        the_bottomline = next_line
                    if '#### Overall Rating:'.lower() in current_line.lower():
                        rating = current_line.split(': ')[1]
                    # objective info
                    if current_line.startswith('### The official website of the tool'):
                        website = next_line
                        if not 'http' in website:
                            website = '--- !! no url on first line: ' + slug
                            # notifies if there is no html on next_line
                    if current_line.startswith('### Who makes it?'):
                        developer = next_line
                    if current_line.startswith('### Is there an official documentation and if so where?'):
                        documentation = next_line
                    if current_line.startswith('### Is there a user forum/ bug tracker/ issue tracker and if so where?'):
                        forum = next_line   
                    if '### Which version of the software did you review?' in current_line:
                        version = next_line
                #!! these only work if everyone edits input with ~ in between every |
                    if "* what is it :" in current_line: #extract if the tool functions online or after install
                        answer = current_line.split(":")[1].split('|')
                        for item in answer:
                            if not "~" in item:
                                type_of_tool.append(item)
                    if "* what is it for ?" in current_line: #extract if the tool functions online or after install
                        answer = current_line.split(":")[1].split('|')
                        for item in answer:
                            if not "~" in item:
                                usage.append(item)
                    if "* this tool functions :" in current_line: #extract if the tool functions online or after install
                        answer = current_line.split(":")[1].split('|')
                        for item in answer:
                            if not "~" in item:
                                functionality.append(item)
                    if "* this tool is available for :" in current_line: #extracts the platform(s) the tool is available for
                        answer = current_line.split(":")[1].split('|')
                        for item in answer:
                            if not "~" in item:
                                # print(item)
                                platform.append(item)
                    if "* this tool is :" in current_line: #is the tool free speech or free beer
                        answer = current_line.split(":")[1].split('|')
                        for item in answer:
                            if not "~" in item:
                                speech = item
                    if "* does this tool have a paid version available?" in current_line: #finds out if the tool has a paid version
                        answer = current_line.split("?")[1].split('|')
                        for item in answer:
                            if not "~" in item:
                                cost = item
                    if current_line.startswith('### The user interface:'):
                        ui = next_line
                    if current_line.startswith('#### What would/could a designer use this tool for?'):
                        what_could = next_line
                    if current_line.startswith('!['): 
                        current_line = current_line.split(']')
                        screenshot = current_line[1].strip("()")
                        images.append(screenshot)



                title = review_text_filtered[2].strip('## ')
                author = review_text_filtered[3].split('by ')[1]
                slug = title.lower()+'_'+author.lower().split()[0] #this now only takes the first name..?

                try:
                    date = review_text_filtered[-1].split(',')[1].strip('[]')
                except:
                    date= review_text_filtered[-1].strip('[]')

                #saving data in our dictionary
                article['date'] = date
                article['text'] = review_text_filtered
                article['the_good'] = the_good
                article['the_bad'] = the_bad
                article['the_bottomline'] = the_bottomline
                article['website'] = website
                article['developer'] = developer
                article['documentation'] = documentation
                article['forum'] = forum
                article['version'] = version
                article['rating'] = rating
                article['title'] = title
                article['author'] = author
                article['slug'] = slug
                article['type_of_tool'] = type_of_tool
                article['usage'] = usage
                article['functionality'] = functionality
                article['platform'] = platform
                article['speech'] = speech
                article['cost'] = cost
                article['ui'] = ui
                article['what_could'] = what_could
                article['images']= images

                articles.append(article)


            except Exception as e:
                print('Error processing', review,'does not fit the new template\n')
                print(e)

    return(articles)

if __name__ == "__main__":
    main()
