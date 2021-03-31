# **English for Automotive Engineers**

_English for Automotive Engineers_ is the minimum viable project for a mobile-first web application to help advanced English learners learn automotive industry-related vocabulary. The app supplements the textbook for an advanced English course, also entitled English for Automotive Engineers, at the Technical University Munich. This course is taught by me, the app designer.

The full site is deployed via Heroku at: [Automotive Vocabulary Trainer (automotive-vocabulary-trainer.herokuapp.com)](https://automotive-vocabulary-trainer.herokuapp.com/)

**UX**

NOTE: A full user experience design document, detailing the five planes of design for _English for Automotive Engineers_ appears as a separate document. The UX section in this document provides an overview.

In each chapter of the _English for Automotive Engineers_ textbook, students encounter new automotive terms, any of which may appear on a vocabulary task in the final exam. An additional source of vocabulary that may occur in the final exam comes via students&#39; presentations, for which students provide one another with a list of 10 automotive-related terms, and explanations for these terms, that will occur during the presentation. The vocabulary portion of the exam is the one students most frequently have concerns about. To help them study for this part of the exam then, the _English for Automotive Engineers_ app A) gathers all the exam-relevant vocabulary, both from the textbook and the student presentations, in one place, an B) provides students with an effective means of learning this vocabulary using active recall techniques. [The Effect of Word Recall on English Vocabulary Learning | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/document/5476669)

Users of _English for Automotive Engineers_ will be first and foremost participants of the English course of the same name at the Technical University Munich. These participants are primarily from Germany, China, and Spain (though past students have come from a broad range of countries) and are primarily bachelor&#39;s degree students studying automotive engineering, mechanical engineering, or another related subject. The English level of the students is advanced, at least C1 according to the Common European Framework of Reference for Languages (see: [The CEFR Levels (coe.int)](https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions) ).

Users of the web app the will be young, tech-savvy students used to working with the textbook for the English course at the Technical University Munich. As such: the vocabulary on the app should be the same as that in the textbook; the app should provide a means of filtering the vocabulary according to each chapter in the textbook; and, where possible, images used on the site should match those used in the textbook.

**What technology is appropriate?**

The site must work equally well on smaller, medium, and larger devices. Students of the English for Automotive Engineers course customarily bring their laptops and / or tablets to work with in class, and may use the web app as a reference during lessons. However, as the teacher I frequently advise my students to use their &#39;dead time&#39; to learn vocabulary, i.e. time they are on the underground, waiting in line at the supermarket, etc. As such, the app should work well on mobile phones to facilitate this type of learning.

Given the strict data protection laws of the university and of the German and Bavarian governments regarding students&#39; personal information, the website cannot require students to provide email addresses, telephone numbers, their real names, etc.

**Why is this so special?**

_English for Automotive Engineers_ is dedicated specifically to the needs of the English learners on the course of the same name. As such, the web app will provide students with a bespoke and more satisfying learning experience.

**User stories and how the site meets these needs**

User story 1:

&quot;As the teacher of English for Automotive Engineers, I want a one-stop shop to where I can upload all the vocabulary from the textbook, the students upload the vocabulary from their presentations, and where the students can learn the relevant vocabulary using flashcard-like active recall.&quot;

_How the site meets this need:_

- The site includes all the vocabulary from the textbook, allows students to easily add their own from presentations, and displays all vocabulary items in Materialize collapsible accordions which encourage active recall by only displaying the term at first, allowing the user to try to recall the meaning before revealing said meaning with a click. The site also allows the user to display the definition first, clicking to reveal the term after active recall, and to shuffle the order of the vocabulary items.

User story 2:

&quot;As a student preparing to work in the automotive industry, I want a site where I can learn the industry-related vocabulary that I&#39;ll need in my future career.&quot;

_How the site meets this need:_

- The site includes all the vocabulary from the textbook, all of which has been selected by the teacher as automotive-industry-relevant vocabulary, and allows students to upload industry-related vocabulary on automotive topics that they themselves have chosen for their presentations.

User story 3:

&quot;As a student on the English for Automotive Engineers course, I want to an easy way to fulfill the course requirement of making my presentation vocabulary available to my course mates.&quot;

_How the site meets this need:_

- The site provides an easy way for students to upload their vocabulary to a platform that all students in the course have access.

User story 4:

&quot;As a student on the English for Automotive Engineers course, I want to be able to study all the exam-relevant vocabulary from the textbook and the presentations in one place.&quot;

_How the site meets this need:_

- The site gathers all the exam-relevant vocabulary in one place, allows users to search for individual items or find them filtered by topic / textbook chapter, and provides an active recall method of memorizing the terms for the exam via the Materialize collapsible accordions.

**Features: Existing features (For screenshots of features, see the separate UX PDF)**

**All pages**

- The navigation bar allows users to easily navigate the pages of the site by giving them a simple site overview.
- As it provides a cleaner aesthetic on smaller devices, the navigation bar appears on the homepage in the form of a hamburger-style dropdown menu.

**Index.html**

- Via media queries, the background image, navigation bar, and page title will change orientation, from portrait to landscape, depending on the size of the screen.
- Both the image for larger devices and that for smaller devices come from the English for Automotive Engineers course textbook, thus creating a sense of familiarity and cohesiveness for students / users.

**register.html**

- This page allows users to register using simply a username and a password, i.e. to comply with university rules on not gathering personal information from students.
- Both the username and password must be a minimum of 6 characters. If this is not met, the user receives a warning message.
- Users must enter their password twice while registering, to ensure that they have entered the password correctly. If the password does not match, registration fails and the user receives a flask flash message telling them so.
- The bottom of the page contains a prompt and a link to the log in page for those who are already registered.
- Upon successful registration, the user is directed to the profile page, which contains a welcoming flash message and a username-customized instructional message.

**login.html**

- This page allows users to log in to the site.
- The page also contains a link to register.html for those users who have not yet registered.
- If either the username or the password is less than 6 characters, the user receives a warning.
- If either the username or the password is incorrect, the user receives a Flask flash message as a warning.
- Upon successfully logging in, the user is directed to the profile page, which contains a customized welcome back Flask flash message and a username-customized instructional message.

**profile.html**

- The profile page greets new users with a welcoming flash message upon registering and returning users with a username-customized welcome back flash message upon logging in.
- A username-customized message below the flash message informs users of how they can use their profile.
- A &#39;delete account&#39; button allows users to navigate to a delete page where they can easily delete their account if they so wish.
- A list of all automotive terms added to the terms database appears on the user&#39;s profile. Users may read, edit, or delete those terms from their profile page.

**delete.html**

- A large red button in the centre of the screen allows users to delete their profiles.
- A modal pop-up asks for confirmation of the action so that users do not delete their accounts by mistake.

**terms.html**

- This page contains all automotive terms in the database, i.e. from both the course textbook and that users have uploaded from their student presentations.
- A search bar allows users to search all terms for specific terms and key words.
- The terms appear in Materialize collapsible accordion items, allowing users to use active recall techniques to try to remember what a term means before displaying its definition.
- Users may click an &#39;add term&#39; button to navigate to a form which allows them to upload a term from their presentations.
- Users may click a &#39;shuffle&#39; button to shuffle the order in which the terms appear.
- Users may click a &#39;by definition&#39; button to show the definition first, then try to recall which word this definition matches with before opening up the accordion to reveal the answer.
- Each term that the user has themselves added to the database appears with &#39;delete&#39; and &#39;edit&#39; buttons, thus allowing the user to either delete a term from this page (with a modal popup requiring confirmation of the action) or navigate to the edit term page so as to update the content.
- The administrative log-in allows the site administrator to delete or edit all terms, i.e. both those added by the administrator, from the textbook, and those added by other users.

**definitions\_first.html**

- This is the page that users reach by clicking the &#39;by definition&#39; button on terms.html. The page contains all the same features as terms.html, but displays the definition first in the Materialize accordion, the accordion opening up to reveal the term.
- Users may switch back to viewing the terms by term first by clicking the &#39;by term&#39; button (this appears where the &#39;by definition&#39; button appears on terms.html).

**add\_term.html**

- This page allows users to add a new term to the database / site list of terms. Via a form, users add the term, the definition, the topic to which the term belongs, and the source of the definition.
- Via the administrative login, the site admin may attribute the term to any of the topics on the website, i.e. those which correspond to the English course&#39;s textbook. The admin does so by selecting the topic from a dropdown menu. Each topic item in the dropdown contains the corresponding image for that topic on the topics.html page.
- Users other than the site admin may only select &#39;presentations&#39; as the topic to which they attribute a new term, given that students on the English course will only be submitting terms from the presentations they give in class.

**edit\_term.html**

- This page allows users to edit the term, definition, topic, and definition source of any term that they themselves have added. Although the site admin may edit any term that any user has added.
- The user may either complete or cancel the edits by clicking either the &#39;Edit&#39; or &#39;Cancel&#39; buttons.

**topics.html**

- This page contains every topic in the English course textbook from which the terms in the database are drawn.
- The topics are displayed with a photo, where possible the same photo as that used in the corresponding chapter of the course textbook, and the topic title on a button. By pressing the button for a particular topic, users access a list of all the words in the database / site glossary attributed to that specific topic.
- The site admin view of this page also includes buttons which allow the admin to add new topics or edit or delete existing topics. These options are not available to other users.

**add\_topic.html**

- This page allows the site admin to add a new automotive topic name and image to the site by entering the new topic name and the image URL into a form.

**edit\_topic.html**

- This page allows the site admin to change a topic name and image by entering a new topic name and / or image URL into a form.
- The admin may confirm or cancel the changes by clicking either the &#39;Edit topic&#39; or &#39;cancel changes&#39; button.

**get\_topic.html**

- This page provides the user with a list of collapsible accordion vocabulary items matching one specific topic, correlating to a chapter of the same name of the English for Automotive Engineers class textbook.
- The page contains the topic image and the ability to shuffle the order of the terms or display the terms by definition first.
- The user may edit or delete any terms that they themselves have added, although for users other than the administrator this feature will only apply to the items under the Presentations topic.

**topics\_definitions\_first.html**

- This page is reached by clicking the &#39;By definition&#39; button on get\_topic.html. topics\_definitions.html contains all the features of get\_topic.html but displays the vocabulary by definition first and, upon the user&#39;s click, opens up the collapsible accordion to display the term
- Users may return to the get\_topic.html, i.e. terms-first, topic-specific, display by clicking the &#39;by term&#39; button.

**how\_to\_use.html**

- This page contains a custom made, embedded YouTube video which gives users a video tutorial on how to use and make the most of the site.

**Features: Features left to implement**

- Write original definitions for words. At present, the definitions come from dictionaries and websites. For the website to be used properly, copyright-free definitions will need to be written. The definitions used are used only for educational purposes and no copyright infringement is intended.
- Allow users to create a list of words they want to learn most / find most difficult to learn.
- Add a spaced repetition feature to the user-created list, i.e. which shows them words they find difficult more frequently and words.

**Technologies used**

- GitHub: [https://github.com/](https://github.com/)
  - GitHub was used to host the application&#39;s repositories.
- GitPod: [https://www.gitpod.io/](https://www.gitpod.io/)
  - GitPod served as the integrated development environment used to code the site.
- HTML: [https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - The website uses HTML to input the structure and content.
- CSS: [https://developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - The website uses CSS to style the HTML elements.
- Materialize: [Documentation - Materialize (materializecss.com)](https://materializecss.com/)
  - The website uses the Materialize framework to simplify the integration and styling of responsive elements.
- Python: [Welcome to Python.org](https://www.python.org/)
  - Python was used to code the app&#39;s functions.
- Flask: [Welcome to Flask — Flask Documentation (1.1.x) (palletsprojects.com)](https://flask.palletsprojects.com/en/1.1.x/)
  - Flask was used as the framework within which functions were coded.
- Jinja: [Jinja — Jinja Documentation (2.11.x) (palletsprojects.com)](https://jinja.palletsprojects.com/en/2.11.x/)
  - Jinja was used as the templating language for Python.
- jQuery: [https://code.jquery.com/](https://code.jquery.com/)
  - The site uses jQuery to initialize Materialize modal alerts, collapsible accordions, and dropdown menus, and for placement of the navbar.
- Mongo DB Atlas: [https://www.mongodb.com/](https://www.mongodb.com/)
  - Mongo DB Atlas was used as the database to store the automotive terms and topics as well as registered site users.
- Werkzeug: [Utilities — Werkzeug Documentation (1.0.x) (palletsprojects.com)](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
  - Werkzeug was used to hash user passwords
- Google Fonts: [https://fonts.google.com/](https://fonts.google.com/)
  - The site uses Google Fonts to integrate the Lato and Amatic SC fonts into the website.
- Fontawesome: [https://fontawesome.com/](https://fontawesome.com/)
  - The site uses Font Awesome to integrate icons into buttons throughout the site.
- Autoprefixer CSS online: [https://autoprefixer.github.io/](https://autoprefixer.github.io/)
  - Autoprefixer was used to automatically add vendor prefixes to style.css in order to aid cross-browser compatability.
- Favicon.io
  - favicon.io was used to add a favicon to the site. [https://favicon.io/favicon-generator/](https://favicon.io/favicon-generator/)
- word2md.com: [https://word2md.com/](https://word2md.com/)
  - To ensure correct markdown in the first draft of this Read Me file a Microsoft Word document of the text was run through word2md.com. The resulting markdown and text was then edited according to the preferences of the author using rules set out in the _Mastering Markdown_ document at GitHub.com. [https://guides.github.com/features/mastering-markdown/](https://guides.github.com/features/mastering-markdown/)

**Testing**

I manually tested the site for errors by having the Google Chrome Developer Tools console open while performing every user event possible on the site.

To ensure that the site contains valid HTML, the HTML code was checked by direct input using the W3C Markup Validation Service: [https://validator.w3.org/](https://validator.w3.org/)

To check valid CSS, direct input via the W3C CSS Validation Service was used: [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

To test the validity of the jQuery files Esprima was used. [https://esprima.org/demo/validate.html](https://esprima.org/demo/validate.html)

To ensure that Python, Flask, Jinja code remained error-free, the Debug console was set to &#39;True&#39; throughout the entirety of the development process.

To ensure the site&#39;s functionality across various devices, I used the web developer tools inspection feature of each of the following browsers:

- Google Chrome
- Mozilla Firefox
- Microsoft Opera
- Microsift Edge

For each browser, I manually checked the preview of each of the site&#39;s pages and events, in both vertical and horizontal views, for devices ranging from the iPhone 5/SE at the smallest end to a width of 3840px / 4k at the highest.

In addition to checking the application&#39;s functionality using browser developer tools, the site has been manually checked and found to function as desired on the following devices:

- Laptops:
  - Lenovo Yoga 530 (checked by both myself and my wife, Anita)
  - HP 255 G5 Notebook (checked by both myself and my wife, Anita)
  - Macbook Air (checked by my father, George)
  - Lenovo Thinkpad x390 (checked by my colleague, Rose)
- Tablets:
  - Kindle Fire 3 HD (checked by both myself and my wife, Anita)
  - iPad mini 3 (checked by my father, George)
  - iPad (checked by my aunt, Vivien)
- Smartphones:
  - Samsung Galaxy J4+ (checked by myself)
  - Samsung A50 (checked by my wife, Anita)
  - Samsung 20A (checked by my colleague, Elizabeth)
  - Motorola G7 plus (checked by my colleague, Keith)
  - iPhone XR (checked by my brother, Greg)
  - iPhone SE (checked by my friend, Kiril)

**Requirements: Content**

To meet the needs required above, the website requires mixed multimedia content including: text, collapsible accordions, a search function, call-to-action buttons, photographs, an embedded instructional video, and site-wide navigation buttons,

**Deployment**

I deployed _English for Automotive Engineers_ to Heroku. To do so, I went through the following steps:

1. Set up a requirements.text file on GitPod by typing pip3 freeze –local \&gt; requirements.txt into the command line.
2. Added the Procfile by typing echo web: python app.py \&gt; Procfile into the command line.
3. Logged into Heroku.com and, from the dashboard, clicked on _create app._
4. Entered the unique app name of automotive-vocabulary-trainer.
5. Selected the region of Europe.
6. Clicked the _create app_ button.
7. To connect the app I:
  - Clicked _connect to GitHub_ to set up automatic deployment from the GitHub repository.
  - Added my GitHUb username and repository name of Automotive\_Vocabulary\_Trainer.
  - Clicked search to find the repository.
  - Clicked _connect_ to connect the app to the repository.

1. Clicked the _settings_ tab for the app.
2. Clicked the _reveal config vars_ button.
3. Added the following variables:
  - IP, with the value of 0.0.0.0.
  - PORT, with the value of 5000.
  - SECRET\_KEY, with the value from the env.py file.
  - MONGO URI, with the value left blank at this stage.
  - MONGO\_DBNAME, with the value of automotive-vocabulary-trainer.
4. Pushed the two new files to the repository on GitHub, by:
  - Typing git add requirements.txt&quot; then git commit -m &quot;Add requirements.txt.&quot; into the command line.
  - Typing git add Procfile then git commit –m &quot;Add Procfile&quot; into the command line.
  - Typing git push.
5. On Heroku, clicked _Enable automatic displays_ then _Deploy branch_.

To run the code for _English for Automotive Engineers_ locally, one may:

1. Open the main page of the repository at: [GitHub - RossClarkScotland/Automotive\_Vocab\_Trainer](https://github.com/RossClarkScotland/Automotive_Vocab_Trainer)
2. Click the green &quot;Code&quot; button.
3. Click the clipboard icon to copy the project URL.
4. Open a terminal in GitPod, or other Integrated Development Environment.
5. Open the file you wish to clone to.
6. Enter the following command into the terminal:

$ git clone [https://github.com/RossClarkScotland/Milestone2](https://github.com/RossClarkScotland/Milestone-Project-Literary-Edinburgh)

Further details are available via: [https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

**Credits**

**Content:**

- Credit to my fellow Code Institute student, Helen Goatly, for showing me an example of two lines of code that were necessary for the password confirmation check to work (these lines are commented on to this effect in the app.py file).

**Media:**

- All site images come from Pixabay and Unsplash.
- The video embedded in how\_to\_use.html is hosted on YouTube.
- Sample definitions of terms have been taken from: _Atkins, T. and Escudier, M. 2013. A Dictionary of Mechanical Engineering (Oxford Quick Reference), Gorse, C., Johnston, D., and Pritchard, M. 2012. The Oxford Dictionary of Construction, Surveying, and Civil Engineering. Oxford: Oxford University Press, Blockley, D. 2005. The New Penguin Dictionary of Civil Engineering. London: Penguin,_ [www.britannica.com](http://www.britannica.com/), [www.collinsdictionary.com](http://www.collinsdictionary.com/), [https://marketbusinessnews.com](https://marketbusinessnews.com/)_,_ [https://en.oxforddictionaries.com/](https://en.oxforddictionaries.com/)_,_ [https://www.lexico.com](https://www.lexico.com/)_,_ [https://www.mwcog.org](https://www.mwcog.org/)_,_ [https://www.monash.edu/business/marketing/marketing-dictionary](https://www.monash.edu/business/marketing/marketing-dictionary)_,_ [https://www.researchgate.net](https://www.researchgate.net/)_,_ [https://www.health.ny.gov/environmental/indoors/air/pmq\_a.htm](https://www.health.ny.gov/environmental/indoors/air/pmq_a.htm)_,_ [https://www.reddit.com/r/cars/comments/2xivw0/what\_is\_a\_4\_door\_coupe/](https://www.reddit.com/r/cars/comments/2xivw0/what_is_a_4_door_coupe/)_,_ [https://afdc.energy.gov/vehicles/fuel\_cell.html](https://afdc.energy.gov/vehicles/fuel_cell.html)_,_ [https://autoexpertus.com/car-greenhouse/](https://autoexpertus.com/car-greenhouse/)_,_ [https://www.oxfordlearnersdictionaries.com](https://www.oxfordlearnersdictionaries.com/)_,_ [http://lexicon.ft.com](http://lexicon.ft.com/)_,_ [https://www.edmunds.com/glossary](https://www.edmunds.com/glossary)_,_ [https://afdc.energy.gov/vehicles/how-do-plug-in-hybrid-electric-cars-work](https://afdc.energy.gov/vehicles/how-do-plug-in-hybrid-electric-cars-work)_,_ [https://en.oxforddictionaries.com/](https://en.oxforddictionaries.com/)_,_ [https://www.smmt.co.uk/](https://www.smmt.co.uk/)_,_ [https://www.virta.global/vehicle-to-grid-v2g](https://www.virta.global/vehicle-to-grid-v2g)_,_ [https://dictionary.cambridge.org](https://dictionary.cambridge.org/)

**Acknowledgements:**

I would like to thank my wife, Anita, for always being willing to lend a spare pair of eyes and, at times, keeping up an elaborate pretence that I was exhausting every swear word I know in every languages while my code wasn&#39;t working.

I also owe a debt to my father, George, for agreeing to test and give feedback on site functionality, particularly as regards the various iterations of the game.

I am indebted, too, to my colleagues at the TUM Language Centre and my friend Kirill for checking the functionality of the website on their devices.

I would also like to thank my friend Milana for being awesome at all things design and never being unwilling to say when some aspect of design is less than awesome.

Finally, I would like to express my gratitude to my course mentor, Spencer Barribal, for offering encouragement and useful ideas, and to the Code Institute tutors and Slack community for providing advice and for humouring me when I asked stupid questions.