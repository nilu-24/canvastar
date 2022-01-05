# canvastar
Full Stack Deep Learning Flask Application which uses CNN to predict the constellation the user draws on the canvas!

# Note
The model.h5 is not added here because the file was too large but the ipynb file is added which was used to create the model

# Inspiration
If you see a constellation, how can you tell which one it is? Before today, you would have to look through a table of all 88 constellations and compare and contrast. But now, you can draw the constellation and have it recognized using machine learning magic! We chose this problem because we had seen an earring in the shape of a constellation but we had no way of telling what it was. We also think it might be helpful for astronomical research and detection purposes too!

# What it does
The UI of the app has a canvas where the user can draw any constellation they want. The drawing on the HTML canvas is then fed into the deep learning model and the app then tells the user what constellation is drawn. The user can also learn more about the constellation as our website connects the user to the Wikipedia site of the constellation they drew.

# How we built it
We used a convolutional neural network in tensorflow to build the model and we experimented with different parameters and regularization methods. Later, we used flask to make a web application where the image drawn on an HTML canvas is fed to the model in the flask backend and the predicted constellation is returned. Our model has an accuracy of 90% on the testing dataset we created.

# Challenges we ran into
The first and foremost challenge we ran into was gathering all the data! We did not use any pre-made dataset from anywhere because we found no dataset containing constellation images. So, we took matters into our own hands and built another website: http://foisy.co where you can draw images which gets stored in our local server and then used to train our model. In total we had to draw about 1,500 constellations!

Another challenge we faced while doing this project was minimizing the overfitting. At first, our model was performing with really high accuracies on training data, but significantly lower accuracies on the testing data. So, we had to learn about regularization techniques on the internet and we decided to apply ‘Dropout’ regularization. After that, our model was performing much better and it was a much generalized model.

# Accomplishments that we're proud of
We are mostly satisfied with the uniqueness of our project and also the fact that we are using data made completely on our own to train the model. We are also proud because our project is unique and interactive in the sense that it uses an HTML canvas where the user can draw images and it is a pretty unique input method to a machine learning model.

# What we learned
Overall, this project was not only just about using a model to classify constellations, but gave us an idea about the entire process / timeline to make a deep learning model using CNNs. We learnt about data preprocessing and normalizing data before passing it to our model. We specifically also learnt about different regularization techniques such as ‘L2’ and ‘dropout’ and how they compare against each other. We learnt the importance of cross validation and regularization because without these, our model was highly overfitting.

Since none of us are webmasters, we learnt a lot about deploying our machine learning model and also worked with flask, jquery, javascript, css and so much more. Moreover, we learnt a lot, not only about CNNs but also about working as a team!

# What's next for CanvaStar
We have so many plans for this app! We plan on generating more data to train the model to make it much more accurate. We also plan on integrating some features like displaying 'fun facts' about the constellation drawn.

