from gimpfu import *
def rule():
	for image in gimp.image_list():
		max_x, max_y = pdb.gimp_image_get_resolution(image)
		for x in range(0, int(max_x), 16):
			pdb.gimp_image_add_hguide(image, x)
			pdb.gimp_image_add_vguide(image, x)

register(
   "python_fu_rule",
   "Place guides every 16px",
   "",
   "Jolly",
   "Jolly",
   "2024",
   "<Image>/Python-Fu/Layer/Rule",
   "*",
   [],
   [],
   rule)

main()
