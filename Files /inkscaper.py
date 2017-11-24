import review_parser, jinja2,os

mijn_artikelen = review_parser.main()

svg = open('utils/test.svg').read()
template = jinja2.Template(svg)

for artikel in mijn_artikelen:
	titel = artikel['title']
	rating = artikel['rating']
	the_bottomline = artikel['the_bottomline']
	version = artikel['version']
	type_of_tool = artikel['type_of_tool']
	usage = artikel['usage']
	functionality = artikel['functionality']
	platform = artikel['platform']
	speech = artikel['speech']
	cost = artikel['cost']
	images = artikel['images']
	fn = titel+'.svg'

	image_path='/Users/marleenvanzalm/Desktop/my_project/the_grand_review/reviews/' #absolute path to where the reviews folder is
	images = images[0] #we arbitrarily choose the first image in the review..
	image = os.path.join(image_path, images) #and give the full path to that image

	try:
		with open (fn, 'w') as f:
			f.write(template.render(titel=titel, rating=rating, the_bottomline=the_bottomline, version=version, type_of_tool=type_of_tool, usage=usage, functionality=functionality, platform=platform, speech=speech, cost=cost, images=images, image=image))
	except Exception as e:
		print (e)
		pass