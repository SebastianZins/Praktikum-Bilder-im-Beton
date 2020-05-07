import filter as m

cell_size = 21                                      # cell size for one pixel pattern (height & width)
source = "website/website-pcs/test.png"              	        # image to be transformed
dest = "website/website-pcs/test_.png"                          # image save destination 
ds_value = 0.5                                   	# downscaling value -> 0.4 = 40% of the original size, needed for better computing time
saving = True                                       # determines if transformed image should be saved
show = True 

print("##################################################################################")
print("##################################################################################")
print("###                   Computer Graphics -- Beginner Practical                  ###")
print("###                            << Bilder im Beton >>                           ###")
print("###                                                                            ###")
print("###                        Raphael But, Sebastian Zins                         ###")
print("##################################################################################")
print("##################################################################################")
print("\n\n")
print("Type the source of your file which you want to have transformed.")
source_ = input()
if (source_ == "***"):
    source_ = source
    print(source_)
print("\nDo you want to have your computed file saved? (y/n)")
i = input()
if (i == "y"): 
    saving = True
    print("\nType the destination where your changed file shoul be safed.")
    dest_ = input()
    if (dest_ == "***"):
        dest_ = dest
        print(dest_)
elif (i == "n"): 
    saving = False
    dest_ = ""
print("\nShow the image? (y/n)")
i = input()
if (i == "y"): 
    show = True
elif (i == "n"): 
    show = False


m.start(cell_size, source_, dest_, ds_value, saving, show)