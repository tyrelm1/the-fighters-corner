# The Fighters Corner (Capstone Project 4)
![mockup](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/043279b2-25f1-4cfa-86ac-0e26a4dfcdae)
[The Fighters Corner ]([https://the-fighters-corner-a28ffa4cb9ae.herokuapp.com/]), your ultimate destination for gaming news, events, and community discussions! Whether you're a seasoned gamer or just getting started, this blog is your go-to source for all things related to the fighting gaming world.

# Purpose
The website is built using the Django framework, which provides the backend functionality, such as user authentication, data management, and routing, and handles the majority of the front end. One key feature of the website is a React component that allows real-time communication and updates through the use of WebSockets. This allows a seamless and interactive user experience as certain parts of the website update in real time without the need for page refreshes. Overall, the website combines the power and flexibility of Django with the dynamic capabilities of React and WebSockets to deliver a smooth and responsive user experience.

The website provides all the essential features, such as creating a personal account, searching and filtering posts, adding and managing posts, bookmarking posts the users find useful, commenting on posts, and sending direct messages to other users in real time. 

The website was developed as a Hackathon Capstone Project #4 for the Code Institute's Full Stack Developer course.  

[The live website is available here](https://the-fighters-corner-a28ffa4cb9ae.herokuapp.com)
___

# UX Design
## User stories

Target audiences:
- Gamers especially in the fighting game community (U)
- Individuals who are passionate about fighting games  (I)

### As a **first time user**

- I want to be able to access the website from any device.
- I want to easily understand the main purpose of the site and learn more about the topic.
- I want to be able to easily navigate and find content.
- I want to create my personal account to see posts.
- I want to create an account.
- I want to easily access a category of posts I need and to be able to search through them.
- I want to open a post on a separate page to see all the details.
- I want to be able to create a post myself.
- I want to know more about other users that I interact with.


### As a **returning user**

- I want to be sure my data is protected.

- I want to be able to access the navbar at any point or go back to the top to navigate fast.

- I want posts to be paginated so it helps me remember on what page I saw something interesting or stay on the same page if I accidentally refresh the page.

- I want to be able to write comments to describe my experience of interacting with an offer.

- I want to be able to update and delete my posts.

- I want to be able to update my user profile.

- I want to be able to reset my password if I forget it.

___
## UAC
User Acceptance Criteria based on the user stories:

<span id="uac1">1.</span> The website should be fully responsive and accessible on any device, including desktop, tablet, and mobile.

<span id="uac2">2.</span>  The website should have a clear homepage that clearly describes how to navigate through the webpage.

<span id="uac3">3.</span>  The website should have a clear and intuitive navigation menu that allows users to easily find and access the content.

<span id="uac4">4.</span>  The website should have a registration form that allows users to create a personal account.

<span id="uac5">5.</span>  he registration process should be fast and easy, but also secure, using encryption and other security measures.

<span id="uac7">6.</span>  The registration process should be fast and easy, but also secure, using encryption and other security measures.

<span id="uac10">7.</span>  Each post should have a link that allows users to view it on a separate page, where they can see all the details and information about the post.

<span id="uac12">8.</span>  The website should have a form that allows registered users to create their own posts.

<span id="uac13">9.</span>  Each post should have a contact button or form that allows users to contact the author of the post.

<span id="uac14">10.</span>  The website should have a user profile page that displays information about other users that a user interacts with.

<span id="uac15">11.</span>  The website should display live notifications to users when another user responds to their message.

<span id="uac16">12.</span>  The website should have links to its social media pages, such as Facebook, Twitter, Instagram, etc.

<span id="uac23">13.</span>  The website should divide the posts into pages so that users can easily navigate through them.

<span id="uac26">14.</span>  The website should allow registered users to leave comments on posts, in order to share their experience and feedback.

<span id="uac27">15.</span>  The website should allow registered users to edit and delete their own posts, if they need to.

<span id="uac29">16.</span>  The website should allow registered users to update their profile information and personal details.

<span id="uac30">17.</span>  The website should have a password reset feature that allows registered users to reset their password in case they forget it.
___


## Structure


### Home Page
![FireShot Capture 002 - Multi Device Website Mockup Generator - techsini com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/d6003f77-1e26-4c30-bf9f-a7630d15f068)

- Displays the main purpose and topic of the site with a few posts for you to view.
- Addresses questions and doubts the first-time users might have and provides a contact form.
- Presents opportunities for navigation 
    #### User Goal:
    >   - Understand the main purpose of the website.
    >   - Be able to contact the site owners to ask more questions or report technical problems signing up/in.
    >   - Easily navigate and interact with the website.
    >   - Learn more about the project on social media.
    #### Website Goal:
    >   - Inform the user about the main purpose.
    >   - Interest and eyecatching.
    >   - Call to action.
    >   - Initiate future engagement, such as following on social media, signing up, attend events.
    >   - Provide a seemless user experience.

### Sign Up Page
![](readme/assets/mockup-signup.png)![FireShot Capture 002 - Multi Device Website Mockup Generator - techsini com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/e4747144-8661-4716-a323-5be71a0ad5d4)

- Allows to sign up.
- Allows to sign up with existing social media accounts.
    #### User Goal:
    >   - register an account

    #### Website Goal:
    >   - Allow the user to sign up easily.
    >   - Provide an easy sign up and a seemless user experience.

### Sign In Page
![](readme/assets/mockup-signin.png)![FireShot Capture 010 - The Fighters Corner - the-fighters-corner-a28ffa4cb9ae herokuapp com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/e24c950b-6f78-48b4-ba3a-563dbf13b7aa)

- Allows to sign in.

    #### User Goal:
    >   - Sign in.
    #### Website Goal:
    >   - Allow the user to sign in easily.
    >   - Provide aesthetically pleasing user experience.

### Posts Page
![](readme/assets/mockup-posts.png)![FireShot Capture 012 - The Fighters Corner - the-fighters-corner-a28ffa4cb9ae herokuapp com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/a0a245c4-4517-41df-8b57-d555714c3390)

- Shows posts.
- Allows users to easily find and access specific categories of posts.
- Allows opening each post on a separate page.
- Posting vailable only for authenticated users.
    #### User Goal:
    >   - Browse the posts.
    >   - Easily find and access specific categories of posts
    >   - Open posts to see them in detail.
    #### Website Goal:
    >   - Provide a list of posts.
    >   - Provide comprehensive information on each post in a preview.

### Post Detail Page
![](readme/assets/mockup-fullpost.png)![FireShot Capture 011 - The Fighters Corner - the-fighters-corner-a28ffa4cb9ae herokuapp com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/31256c1d-9f60-4e63-9742-80d01aa822c0)

- Shows a post in detail.
- Allows to see and write comments about the post.
- Allows you to manage the post if you are the author.
- Available only for authenticated users.
    #### User Goal:
    >   - See a post in detail.
    >   - See comments other users left about the post.
    >   - Leave your comments.
    >   - Contact the author of the post.
    >   - Manage the post, if you are the author.
    #### Website Goal:
    >   - Show a post in detail.
    >   - Allow the user to interact with the post.
    >   - Allow users to contact each other.
    >   - Provide user experience.

### Update Post Page
![](readme/assets/mockup-createpost.png)![FireShot Capture 013 - The Fighters Corner - the-fighters-corner-a28ffa4cb9ae herokuapp com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/e4f6ee6f-898a-46c9-a6d6-c22534bb6e28)

- Create a post. backend
- Allows updating an existing post.
- Available only for authenticated users.
    #### User Goal:
    >   - Create a new post.
    >   - Update your posts.
    #### Website Goal:
    >   - Allow the user to create/update a post.
    >   - pleasing user experience.

### Delete Post Page
![](readme/assets/mockup-delete.png)![FireShot Capture 014 - The Fighters Corner - the-fighters-corner-a28ffa4cb9ae herokuapp com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/22b6762d-8665-413b-9e9a-bc8e5dafafd9)

- Confirms if the user wants to delete their post.
- Available only for authenticated users.
    #### User Goal:
    >   - Delete a post.
    >   - Being able to change your mind if you pressed "Delete" accidentally.
    #### Website Goal:
    >   - Confirm with the user deletion of the post.
    >   - Provide aesthetically pleasing user experience.

### About Page
![](readme/assets/mockup-profile.png)![FireShot Capture 015 - The Fighters Corner - the-fighters-corner-a28ffa4cb9ae herokuapp com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/3164cb05-d5b3-412c-bda0-5d1a37ad4583)

- Shows the creators profile.
- Shows the authors post details.
    #### User Goal:
    >   - See a profile in detail.
    >   - Learn more about other users you are going to interact with.
    #### Website Goal:
    >   - Allow the user to see saved posts.
    >   - Provide user experience.



### Event Page
![](readme/assets/mockup-messenger.png)![FireShot Capture 003 - The Fighters Corner - the-fighters-corner-a28ffa4cb9ae herokuapp com](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/c2ae79e4-819f-45e4-a76f-1b31d002c00d)
- Displays a events list on the front end.
- Allows users to to pick a list of events.
- Available only for authenticated users.
    #### User Goal:
    >   - select a event.
    >   - put in a RSVP request

    >   - Receive message notification of successful invitation
    #### Website Goal:
    >   - Allows users to see the latest event 
    >   - Displays a list of events that are soon starting.
    >   - Provide aesthetically pleasing user experience.

![](readme/assets/mockup-chat.png)

[Back to the Top](#help-u-website-milestone-project-4)
___
# Wireframes

### Home Page  
[blog wireframe]![Blog wireframes](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/e7ed6426-f765-46bb-a4c6-f995efa59ccd)

### Sign Up Page

[Sign up wireframe]![Sign up wireframe](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/5ac09911-902c-4a9a-9215-f05eb87b661e)

### Posts Page
[posts wireframe]![posts wireframe](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/ee302e72-ff80-4a0a-b4f1-4e2b673a352d)

### About 
[about me wireframe]![about me wireframe](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/e9e7c628-89cd-49c9-895a-dddaaef7d7eb)

### Events Page
[events page wireframe] ![event list html](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/2a5c99a6-85f5-47ec-9eee-6bdcb1e0a0e5)
___
# Development Plan

## Agile design

The development of the website has followed an Agile methodology, using GitHub's projects to prioritize and track user stories and features. The approach enabled the implementation of ideas based on their level of importance, ensuring that the website functionality and user experience were not compromised. The following categories were applied, as well as corresponding labels were created:
- Not Began
- To Do
- Done
- Nice to have

[nice to haves](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/db4dfad4-7a47-4c5a-ba35-d913c8f2c7db)




The development followed an AGILE approach, which allowed for the delivery of a functional site. The project was constrained by time limitations, which resulted in some initially listed features not being implemented. However, AGILE methodology is incredibly helpful in situations like this, as it allows for the prioritization and tracking of user stories. Completed user stories are in the "Done" section and the ones that were not prioritised for the first iteration are currently in the "To Do" section to be covered in the next iteration. 

[See the current state of the project here.](https://github.com/users/tyrelm1/projects/6/views/2)

___
# Design

## Design

The website is meant to have a simple layout and a clean design. The home page is aimed at giving a professional and informative impression, , which is achieved by little details, such as a cool landing image and a footer with social icons. A main frame for design, mainly composition and alignment-wise
### Colour Scheme

![colour scheme](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/7004a729-2ef8-40a9-ac4b-9e35de59b8f8)


The colour scheme is mainly purples , with dark and blue undertones , initially i was going to go with that as an overall design but as it progressed i knew that i would be evident that i would need to add brighter text so it would not clash so i incorporated white and light blue for easier viewing.


### Images

The images in this project were sourced from [Unsplash](https://unsplash.com/) 

### Visual Effects

#### Hover effect
The navbar links, all links and buttons include a hover-over effect to make the experience more interactive and navigation more intuitive. When the user engages with the link or hovers over the link, its colour or background colour changes.

___
# Data Model

![FireShot Capture 017 - Blank diagram_ Lucidchart - lucid app](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/778d3658-71a9-4ae5-a3cc-d8e502b76cb2)

![flowchart](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/c26ddfc2-b41a-413c-8c0d-e875f028f205)


___
# Features

## Auth 

Authentication is particularly important for Help U, as the subject is quite sensitive and people are vulnerable asking for help, so it should be confidential within the community and available only for authenticated users. Thus the website, besides the home page is available only for authenticated users. 

One of the key features of [django-allauth](https://django-allauth.readthedocs.io/en/latest/) is its support for OAuth. OAuth is an open standard for authorization that allows users to share their private resources stored on one site with another site, without having to share their credentials. OAuth allows users to grant a third-party application access to their resources without having to reveal their password. This is useful for scenarios where users want to give access to their resources to a third-party application without having to provide their credentials.

One of the main reasons I chose to use [django-allauth](https://django-allauth.readthedocs.io/en/latest/) is because of its flexibility and support for various authentication methods. Another reason is because of its scalability. The library is built on top of the Django framework and it is actively maintained and widely used in production, which means that it is likely to be compatible with the latest Django versions and have a solid user base.

### User Authentication 

![](readme/assets/mockup-signin.png)

The project uses a custom user model with email as a user id, instead of using Django's built-in User model, which means that users to register and log in to the website need to use their email address instead of a traditional username, it also uses a custom sign up form. Users are logged in automatically after they verify their email addresses. However, users will not be logged in automatically after resetting their password. The ACCOUNT_SESSION_REMEMBER is set to True which means that the session will be remembered even if the user closes the browser. The email confirmation link will be signed using HMAC (Hash-based message authentication code) for security. The account login attempts are limited to 10 which means that the account will be locked for 50 minutes after 10 failed login attempts. 

### User Registration 

![](readme/assets/mockup-signup.png)

Even though the website's registration process includes an email as the primary identifier for user accounts, as well as the requirement for users to provide their first and last name. This is to ensure that users are using their real names and photos, which helps to build trust among the community. To verify the authenticity of users and prevent fraud, the registration process includes email verification. In addition, phone number verification will be set up in production using services like WebOTP, Veriphone, or Twilio, to further secure the registration process.
The registration process requires users to enter their password twice to ensure that they have typed it correctly. This is an important security measure, as it helps to prevent users from accidentally entering the wrong password.


### Reset password 

The website also provides a password reset feature, which is an important security feature that allows users to reset their password if they have forgotten it or if their account has been compromised. AllAuth sends out an email notification to the user with a link to reset their password, which ensures that only the user can reset the password of their account. The password reset feature provides a better user experience by allowing users to regain access to their accounts quickly and easily, which helps to increase user engagement and retention.


## Responsive 

The website has been designed with flexibility and aesthetic appeal in mind, ensuring that it is responsive and visually pleasing on all screen sizes and resolutions, starting at 600px. 
Responsiveness was achieved by utilizing Bootstrap in combination with JavaScript. This allowed for the rearrangement of page components to optimize the user experience on different screen sizes. Breakpoints were chosen based on typical device screen sizes and the goal of providing the best possible presentation of content for all screens. Breakpoints are not strictly consistent *particularly for smaller screens) but it is done intentionally to provide a better presentation of the content for all screens, the 992px breakpoint is common for laptops, the media query at this breakpoint adjusts the font size of the logo to make it more suitable for smaller screens. The 1200px breakpoint was chosen to target larger desktop screens and ensure that the website looks good on those devices as well, to stop the content from further expanding and make sure that the website layout is not broken or distorted on large screens.

## Accessibility

The website is designed and developed with accessibility in mind: it provides alternative text for images, using semantic HTML elements, aria-labels and providing adequate colour contrast. Keyboard navigation is possible. It also works with screen readers, however, there's room for improvement in this aspect, to ensure that it is fully accessible to users with disabilities.




### Update 

![]![update png](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/a14289ad-a9b0-4c3b-b264-7d21098a9501)


Users can update their profile information at any time. This feature allows them to make changes to their personal information and blog posts.
This feature is beneficial for users as it allows them to keep their profile information up to date and accurate, which is in many ways essential for the purpose of the website. It also allows them to update their comment at any time. 


## Page elements


### Navbar 

![nav bar](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/548d0e7b-8b18-44db-966e-8cba2ca035d7)

The navbar is a key feature of the website, located at the top of the page in a sticky position and it is always visible to the user, even when scrolling down the page. The navbar provides a clear and easy way for users to navigate the website. The website name is prominently displayed in the navbar, providing users with a clear indication of the website they are currently visiting. If the user is logged in,

The navbar also includes several links that aid navigation on the website. The "About" link provides information about the website and its purpose. The "Login" and "Register" links are used for user authentication and are only visible to unauthenticated users. Once the user logs in, they will not see these links anymore and "Log out" will be displayed instead. The page "Posts" are only displayed to authenticated users, otherwise, it's the "Home" page. The user must be logged in to access all pages on the website, except for the home page. 



### Footer 

![footer bar](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/8ab642e1-edda-4689-9b29-e8b2872cbd21)

The website's footer is designed to provide users with useful information and navigation options in a clear and organized manner. It is split into four columns, each serving social link to different websites. 

### About 

![about me](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/fc6a28d7-2ed6-45f6-8b89-a9c2dda1a128)

The "About" section of the website provides information about the purpose and mission behind the website. There is a brief introduction about the organization and its objectives, it also calls the visitor to learn more about the topic, empathise and engage. 


### Posts

![posts](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/b466b00e-58ba-4226-b24e-36db6613e76f)


The posts list page is the main hub for users to browse and discover offers that they are interested in. Each post is presented in a card format, with a title, an image, a location, and a short description preview. This format allows users to quickly scan through the posts and get a general sense of what each offer is about. Additionally, a map toolkit is also provided to help users understand the location of the offer and how relevant it is to them. This allows for an efficient and user-friendly experience, making it easy for users to find what they are looking for. Users can also filter the posts by checking off the "give" or "receive" checkboxes and the posts will be filtered accordingly.



### Pagination 

![pagination](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/ce801a71-a17d-4646-9fdd-13a71cb788a4)

The pagination on the website is set to display 12 posts per page. This means that when a user visits the page with posts, they will see a maximum of 12 posts at a time. If there are more than 12 posts, the user will be able to navigate through the pages using the pagination controls. This allows the user to easily view a specific set of posts and avoid scrolling through a large number of posts at once. Additionally, this feature helps to improve the performance of the website by not loading all the posts at once.



### Post Detail View 

![post detail](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/f99324c3-3fc1-41d5-8785-a6f2623138f0)

The post detail view provides a detailed view of a specific post. The view includes an image of the offer and a map with a closer view of the location of the offer. The map allows the user to understand the area and neighbourhood of the offer. This map includes different scales, such as a zoomed-in view of the area and neighbourhood, compared to a more distant scale that is given on the Posts List page for an approximate understanding of where the city is located. 
There is also a detailed description of the offer, a link to the user profile of the author, and buttons to write a comment and contact the author directly. The "Say thank you" button allows the user to express gratitude for the offer, and the "Contact" button allows the user to proceed with discussing the offer with the author. 

### Comments 

![comments](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/b857e072-4d88-49fa-9520-b850360d82eb)

The comment section on the post detail view allows users to leave feedback. It is comprised of a list of existing comments that are displayed in chronological order, with the most recent comments appearing at the top. Each comment includes the name and userpic of the person who left the comment, as well as the comment text itself. Additionally, there is a form for users to leave their comments. The comment section is designed to be intuitive and easy to use, with a clear and simple layout that makes it easy for users to understand the context of the conversation.

## **Feature considerations**

1. Phone number verification.
2. API functionality.
3. User Profile Pictures.
4. different images for blog.
___
# Testing

## User Story Testing

| Expectations                                                                                 | Realisation                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a **first time user**                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| I want to be able to access the website from any device. | The website is fully responsible and accessible on all screen sizes, starting at 600px.|
| I want to easily understand the main purpose of the site and learn more about the Fighting Game Community.                           | The Home page concisely and comprehensively introduces the main aspects, including the Events section and the about Form in case the user has any questions.                       |
| I want to be able to easily navigate and find content.  | 1. The navbar with a sticky top position is always present on the screen and allows for navigating the website from any point on the website.<br> 2. The main navigation links are duplicated in the footer. <br> 3. The live search is available on the Posts page.                    
| I want to create my personal account to see posts.                                                                     | The user can register a new account.                                                             |
|I want to sign up with my social accounts, such as Google or Facebook.                           | The user can sign up using their existing social media account.                                                                                                                 |
| I want to create an account fast, but I want it to be secure.                                                  | 1. Authentication is handled by Allauth. <br> 2. Email verification is required.        
| I want to be able to contact somebody and receive a response without signing up if I have doubts or queries.                    | The website provides a contact form.                                                                                                                                                                             
| I want to open a post on a separate page to see all the details.                                                              | Posts could be opened on a separate page to view them in detail.                                                                                                      |
|I want a map attached to each post to understand where the offer/request is.  | 1. A map toolkit is available in the post preview on the Posts page. <br> 2. A bigger map in a detailed view.                                                                            ||
| I want to be able to create a post myself.                   | "New Post" button is available on the Posts page and every user can create their own post, which will be published after moderation.                                                                                                                                               
| I want to know more about other users that I interact with.              | Links to the user's profile are available from the Posts page, Detail view and Chat.                                                                             
| I want to be immediately notified when another user responds. | Real-time notifications are available in the navbar and inside the Messenger app. |
| I want to learn more about the project on social media. | The social media links are available in the footer and accessible from every page. |
| I want to receive feedback from the website about what's happening to know if something went wrong. | 1. Django messages inform the user about the status of their actions. <br> 2. Loaders inform the user about the process of loading. <br>3. Error messages notify the user if something goes wrong. |
|  As a **frequent user**                                                                               |                                                                                |
|  I want to be sure my data is protected.          | The app is additionally secured by Stunnel.      |  |
| I want to access the messenger from anywhere on the website.          | The message icon is available in the navbar and accessible at any point.          ||
| I want to be able to access the navbar at any point or go back to the top to navigate fast. | The navbar with a sticky top position is always present on the screen and allows for navigating the website from any point on the website. |
|I want posts to be paginated | Posts are paginated by 3. |
| I want to be able to write comments to describe my experience of interacting with an offer. | Users can leave their comments in the detailed post view. |
| I want to be able to update and delete my posts. | Users can update and delete their posts, the buttons for it are available in the detailed post view. |
| I want to be able to update my user profile. | Users can update their user profile, the button is available in the detailed profile view. |

___
   
## Manual Testing

The project includes extensive automated testing.

The app was manually tested in Chrome, Safari and Firefox on MacBook.







### Code validation

1. **[W3 Markup Validation](https://validator.w3.org/) - HTML Validation**

All pages were run through HTML Validator. No errors were detected.

**Home Page**

![home](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/58684794-f3ba-4b7d-9d43-86af3ba1495c)



**Posts Page**

![valid](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/f5149246-9551-4e39-abc6-31e7f3652bac)



**Sign Up**

![sign up](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/72de2f38-a191-4a52-b7e7-a2cf76b95c1d)

**Post Detail Page**

![detail valid](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/72124ac8-c9b7-4bc1-86b1-7801f23b44f3)

**about me**

![about me valid](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/86c9814e-7602-4285-beaf-1eb6b8b39835)


 **CSS Validation**
 
 ![css](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/f434e187-2df1-45d3-b584-bd19850b4687)
  
  CSS Stylesheet was run through CSS Validator. No errors were detected.

![](readme/assets/code_validation/valid_css.png)

3. **[CI Python Linter](https://pep8ci.herokuapp.com) - Python Validation**

All Python files were run through CI Python Linter. No errors were detected.

**MAIN APP**

![admin](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/79d45d63-898a-4174-bd01-bd92752f2001)

![project model](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/05ee83c9-bebb-4eb0-a1f1-57268d72be6b)

![project main  event](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/34a7e464-9b8f-4db7-9de6-c4eb1e1ce5b9)

![urls](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/9af45901-a8cd-4fe8-8e2c-5672df838089)

**Posts APP**

![project model](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/5ed50851-4c37-41c8-bfd7-d9839039331d)

![valid post](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/463e97e8-f119-4778-a089-f2bf2e2a84e5)


![post valid](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/dd5e5f21-f073-4309-9a88-c3b6b77a2eb3)




4. **[JS Hint](https://jshint.com/) - JS Validation**

All JS files were run through JS Hint. No errors were detected.



### Lighthouse 
**Home**

![home](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/bd032ef5-b30f-45f9-94b7-7508b7ecd217)

**Event List**

![lighthouse eventlist](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/fa86c087-a126-4c0d-9033-0b122e4acedc)

**About Page**

![lighthouse about](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/86a8a8a4-a00f-4dd1-864f-a842a28b5be1)

**Post Detail**

![post detail lighthouse](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/92dbc7b8-4155-4601-8a45-e859269ce25f)

**Event Detail**

![event detail lighthouse](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/97f81a1c-4a5a-4f23-a6bf-4c4b048312ea)

**Sign Out Page**

![sign out lighthouse](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/c6daa41c-bd7d-4ed0-9940-a4856e9043d1)

**Sign Up Page Sign In Page**

![sign up light house](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/7a441ba7-747c-4c01-9bc4-c8ae56291ed9)

**Mobile Now**


**mobile Sign in menu**


![mobile sign in](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/545ca1ca-7f87-463e-aa88-cfa1ae61c0e6)

**Assessed both post and event details for mobile**

![event and post detail mobile](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/bf589e1c-11d2-4c12-9ccf-8ae4f1499f46)

**Mobile Aboout Page**


![event list and blog list mobile](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/ce52c6bf-ab02-42e1-9826-8261468d381c)

**About Me Mobile**


![about mobile](https://github.com/tyrelm1/the-fighters-corner-test/assets/153202154/f90ba3df-cb3e-4767-a0a0-bcc20376fbde)



# Technologies
## Languages
- Python+Django, JavaScript, HTML, CSS
## Programs, frameworks, libraries
- [Django](https://www.djangoproject.com/) for backend and frontend functionality.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/) for authentication, registration and account management.
- [PostgreSQL](https://www.postgresql.org/) relational database.
- [Psycopg](https://www.psycopg.org/) PostgreSQL adapter for Python.
- [Elephant SQL](https://www.elephantsql.com/) to manage PostgreSQL databases.
- [Babel](https://babeljs.io/) for compiling JS.
- [Webpack](https://webpack.js.org/) for bundling JS.
- [Bootstrap](https://getbootstrap.com/) for styling.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) for pretty forms.
- [Crispy Bootstrap](https://pypi.org/project/crispy-bootstrap5/) for styling Crispy forms.
- [jQuery](https://jquery.com/) (JS library) for additional functionality.
- [Google Fonts](https://fonts.google.com/) for typography.
- [Gitpod](https://gitpod.io/) IDE to develop the app.
- [GitHub](https://GitHub.com/) to host the source code.
- [Heroku](https://www.heroku.com/) to deploy and host the live app.
- [Cloudinary](https://cloudinary.com/) for storing and serving static files.
- [Favicon.io](https://www.favicon.io/) to create the website favicon.
- [Techsini](https://tecnisih.com) to create the Mockup image in this README.
- [W3C HTML Markup Validator](https://validator.w3.org/) to validate HTML code.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code.
- [JS Hint](https://jshint.com/) to validate JS code.
- [CI Python Linter](https://pep8ci.herokuapp.com) to validate python code.
- [LucidChart](https://lucid.app/documents#/dashboard) for flowcharts.




___

# Deployment

## Github
The project was created by navigating to the CI template and clicking 'Use this template'. After a new repository was given a name, I navigated to Gitpod, where the entire project was developed. Then the Project was created and issues were added to follow the Agile methodology.

## Heroku
Heroku was used to host the app. Heroku is a container-based cloud Platform for building, deploying and managing apps. To enable ongoing responsive testing and avoid a heart attack when approaching the deadline this project was deployed to Heroku in its early stages. This was achieved through the following steps: 

1. Use the `pip freeze -> requiremnts.txt` command in the terminal to create a list of libraries that need to be installed.

2. Login or create an account on [Heroku](https://www.heroku.com/). Click `new` in the top right corner and choose `create new app`. Choose a unique app name and your region and click `create app`.

3. Navigate to the `Settings` tab, and click `Reveal Config Vars`.

**Setup External Services:**

  * 1.  Log in or create an account on [Cloudinary](https://cloudinary.com/).
    2.  Navigate to the `Dashboard` on Cloudinary, copy and store the value of the 'API Environment Variable" ( begins with cloudinary:// ) and paste it into your config vars `CLOUDINARY_URL` = `cloudinary://<your_value>`
___
  * 1. Log in or create an account on [ElephantSQL](https://www.elephantsql.com/).
    2. Create a new instance. Select the free plan Tiny Turtle and leave the tags blank.
    3. Select the region and choose the nearest data centre to your location or the one that works. The closest to me was down when I was creating mine.
    4. Click 'review' and check the details and click the button to create the instance.
    5. Click on the instance you created copy the ElephantSQL database URL from the instance details and paste it into your config vars `DATABASE_URL` = `postgres://<your_value>`
    4. Add Django secret key to config vars `SECRET_KEY` and `DISABLE_COLLECT_STATIC` = 1
    6. Navigate to the `Deploy` tab and select GitHub as a deployment method.
    7. Find a repository to connect to and choose the branch to deploy.
    8. Enable automatic deployment, cross your fingers and deploy the branch. 
    9. Wait for the app to build, click on `View`.
    10. Go back to config vars and remove `DISABLE_COLLECT_STATIC` = 1
    
### Fork GitHub Repo

Forking in GitHub allows you to create a copy of a repository on your own account, where you can view or make changes without affecting the original repository. To fork a repository, you can follow these steps:

    1. Navigate to the [repository](https://github.com/tyrelm1/the-fighters-corner-test) on GitHub.
    2. Click the "Fork" button, located on the top right of the page.
    3. Choose the account where you want to fork the repository.
    4. Once the process is completed, you will have a copy of the repository on your own account.

    It's important to keep in mind that if you are not a member of an organization on GitHub, you will not be able to fork your own repository. You might want to create another account to do so.

### Clone GitHub Repo

Another option is to create a local clone of the repository: 

1. Navigate to the [repository](https://github.com/oks-erm/help-u) on GitHub.
3. Locate the `Code` button at the top, above the repository file list.
4. Select a clone method, and click the `copy` button to copy the URL to your clipboard.
5. Open the IDE of your choice, and open Git Bash.
6. Change the current working direction to the location where you want to create a clone.
7. Type `git clone` and paste the URL from the clipboard.
8. `$ clone https://github.com/oks-erm/help-u`
9. Press `Enter` and the local clone will be created.



___

# Credits

## Media

- [Unsplash](https://unsplash.com/),

**heavily Inspired By This Blog**

[](https://fightrise.com/)

 
## Acknowledgements

I would like to thank my peers and the coding coaches for being so supportive , my cohort facilitator Iris for being absolutely brilliant , my tutor Ronan McClelland, for his guidance the few days i had was invalubale , .

