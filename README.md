# photo-gallery
## Author
Norah Waswala
## Project Description
 A personalized gallery application that allow user to display photos for others to see.Others can share,kike and comment the image they like.
## Demo
![screen](/app/static/image/screen.png)
## User Story
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|
|Subscription | **Email Address**| Flash message "Succesfully subsbribed to D-Blog"|
## Requirements
The application requires the following installations to operate:
* SQL database
* pyperclip
* pip
* django
### Technologies Used
* Python3.8
* django
* Heroku
### Project Setup Instructions
* Open Terminal {Ctrl+Alt+T}
* Fork the repository
* Git clone https://github.com/Norah-Waswala/photo-gallery.git
* code . or atom . depending on the text editor of your choice
* * Move to the folder and install requirements
* cd my-gallery
* pip install -r requirements.txt
* Exporting Configurations
* export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
## Support and contact details
For more information, find me at my email (https://norah.waswala15@gmail.com)

## link to live site on heroku pages

## License and copyright information
[MIT LICENSE](LICENSE)
Copyright (C) [2022] [@ Norah-Waswala]
