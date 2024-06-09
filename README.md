 ## DATASET COLLECTOR 

 This is a simple python library to help machine learning developers collect image and video dataset for their projects.

 With just three lines of python code, you can collect as many images as you require.

 ```python

    EXAMPLE CODE TO COLLECT IMAGES

    from datasetcollector.collector import Collector

    # create collector instance with folder name and camera id
    mycollector = Collector('folder_name', 0)

    # collect images 
    mycollector.collect_images(5, 'jpg', 1)

    OUTPUT 
      A new folder 'folder_name' which stores the captured images

 ```

  > [!NOTE]
  > The video collector will be released soon.