 ## DATASET COLLECTOR 

 This is a simple python library to help machine learning developers collect image and video dataset for their projects.

 With just three lines of python code, you can collect as many images as you desire.

 ```
    EXAMPLE CODE TO COLLECT IMAGES

    # import 'Collector' class
    from Collector import Collector

    # create collector instance 
    mycollector = Collector('folder_name', 0)

    # pass arguments 
        - collect 5 images
        - 'jpg' image format 
        - 1s delay

    mycollector.collect_images(5, 'jpg', 1)

    A new folder 'folder_name' which stores the captured images

 ```

 [!NOTE]
    The video collection implementation is still under development