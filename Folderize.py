from gimpfu import *

def folderize_layers():
      
   for image in gimp.image_list():
      counter = 0
      pdb.gimp_image_undo_group_start(image)
      for layer in image.layers:
         group_name = "Group %d" % counter
         counter = counter + 1
         group = pdb.gimp_layer_group_new(image)
         pdb.gimp_item_set_name(group, group_name)
	 pointer_to_layer = group_name
         pdb.gimp_image_insert_layer(image, group, None, 0)
         #layer_position = pdb.gimp_image_get_layer_position(image, layer.name)
         pdb.gimp_image_reorder_item(image, layer, group, 0)
         #pdb.gimp_image_remove_layer(image, layer)
      pdb.gimp_image_undo_group_end(image)



# Register the script in GIMP
register(
   "python_fu_folderize_layers",
   "Put each layer into a unique folder",
   "Create a group for each later and move the layer into it.",
   "Jolly",
   "Jolly",
   "2024",
   "<Image>/Python-Fu/Layer/Folderize Layers",
   "*",
   [],
   [],
   folderize_layers)

main()
