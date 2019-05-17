#Helper Functions

import os
import glob #library to load images from a directory
import matplotlib.image as mpimg

#A helper function which takes in image directory as a parameter and returns a list of images present in the directory
def load_dataset(img_dir):
    
    #Empty list for images
    image_list = []
    
    #List of directoy names present in img_dir
    image_types = ['red','green','yellow']   
    
    #Iterate through different directories inside img_dir
    for im_type in image_types:
        
        #Iterating through every Image file present inside the img_dir/im_type directory
        for file in glob.glob(os.path.join(img_dir,im_type,"*")):
            
            #Loading an Image using mpimg.imread function
            image = mpimg.imread(file)
            
            if not image is None:
                #Appending the image with it's color(label/class)in the image list
                image_list.append((image,im_type))
    
    return image_list