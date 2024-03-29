# GPU Bytes

![image](https://user-images.githubusercontent.com/102811792/214440879-cb484a11-70a4-447c-bc18-5f2e4ea63570.png)

## Author
Alex Ward

## Live Site
The fully deployed version can be found here: https://gpu-bytes.herokuapp.com/

## Repository
My repository can be found here: https://github.com/AlexanderJWard/gpu-bytes 

## Introduction
GPU Bytes is a purely educational website blog. It's aimed at computer enthusiasts looking to educate themselves and learn about new technologies released. Additionally, they can get information about the latest and greatest Graphical Processing Units (GPUs).

# Table of Contents

# Table of contents

- [GPU Bytes](#gpu-bytes)
  - [Author](#author)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [User Experience](#user-experience)
  - [Target Audience](#target-audience)
  - [Design Choices](#design-choices)
- [Information Architecture](#information-architecture)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Choice](#database-choice)
  - [Data Models](#data-models)
- [Agile Process](#agile-process)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Agile Tool](#agile-tool)
- [Features](#features)
  - [Feature MP4 Showcase](#feature-mp4-showcase)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Validation Testing](#validation-testing)
  - [Defects](#defects)
  - [Outstanding Defects](#outstanding-defects)
- [Deployment](#deployment)
  - [Development Deployment](#development-deployment)
  - [Production Deployment](#production-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

# User Experience

## Target Audience
I believe the target audience is anyone interested in technology. Perhaps more specifically aimed at people who play computer games on PC. Because the contents of GPU Bytes are related to graphics cards designed for medium to high-end PC gaming, this makes sense as that's NVIDIA and AMD's speciality. Despite this, the blog section is more accessible about generic technology news covering the whole industry. The site is more likely to appeal to younger men between 18 - 50, the majority under 30.

## Design Choices
Because of the target audience, I decided to design the website with a modern easy-to-access look and feel. Keeping the user experience clutter-free was my main goal. I used colors based on both GPU manufacturers and added minimal animations to the title and page navigation. All the GPU information is displayed clearly to avoid user frustration when looking at the specifications of a graphics card. Users can easily see the number of likes on a post as it's contrasted with the text.

### Colors
My main choice with the colors was to go with strong contrasting black and white to realy stand out on the page and compliment it with the red and green used by both graphics card manufacturers NVIDIA & AMD. I use the red in hover effects and also in some of the buttons used throughout, the green is used for edit and yes buttons throughout.

![image](https://user-images.githubusercontent.com/102811792/214435673-028a1cc6-327d-42b2-9b98-3392ba6d3260.png)

### Typography
My two fonts work well together and complement each other as both are sans-serif fonts. For the titles and headers, I used Quicksand which is a modern-looking font without sharp edges and is very easy to read. The second font is Source Sans Pro which I used for content text and GPU specs. Source Sans Pro works well with Quicksand and suits the overall design choice.

![image](https://user-images.githubusercontent.com/102811792/214450549-bf1ef833-f4d8-4309-9c87-c5eddfb1a3a0.png)

https://fonts.google.com/specimen/Quicksand

![image](https://user-images.githubusercontent.com/102811792/214450483-e0617bd1-248f-451d-829b-c4e1e5afa558.png)

https://fonts.google.com/specimen/Source+Sans+Pro

### Images
I used images such as computer fans and graphics cards to match the overall theme and design choice. Font Awesome icons were chosen because they best fit the buttons used. The pencil icon represents the ability to edit, trash can is perfect for the delete buttons. Fire icon represents leaving a like on the post.

![image](https://user-images.githubusercontent.com/102811792/214524707-61c13506-60a2-4560-b727-e50b7ca5f026.png)

![image](https://user-images.githubusercontent.com/102811792/214525580-bcf3e93b-5639-49fe-a666-339c51797d1f.png)

### Design Elements

> - buttons
> - cards
> - drop down menu
> - desktop navigation
> - mobile navigation
> - footer
> - textarea
> - text input
> - pagination
> - images
> - icons

### Animations and Transactions

- Fan image rotation

https://user-images.githubusercontent.com/102811792/214969262-2a2fb354-ac03-41f5-9b34-e155464dd681.mp4


- Hover effects on buttons, drop down, and navigation

https://user-images.githubusercontent.com/102811792/214969626-e9805de1-8cbe-4785-ad11-08911526a4a1.mp4

- Pagination next and previous fan animation

https://user-images.githubusercontent.com/102811792/214969843-cf181db7-3be9-4b3c-bb1f-064f769dea90.mp4

### Frameworks

For my framework, I chose to use Boostrap as it's something I've started to learn and am most familiar with it. Fitting perfectly with my design elements the framework supports everything I require for this website.

### Custom Styles

I made custom changes to some of the bootstrap classes in my __style.css__ file located in __Static/CSS__ folder structure. I used CSS to change the color of btn-success and btn-warning so they match my chosen design colors. Further changes can be found in the aforementioned CSS file.

![image](https://user-images.githubusercontent.com/102811792/214534235-e681b4d3-fc2a-4227-817a-a5450f09d0b9.png)

### Wireframes

#### Basic View - Not logged in

![image](https://user-images.githubusercontent.com/102811792/214549349-610f6538-cad0-4d02-899f-f5365085a029.png)

#### Mobile View - Mix of not logged in and as admin

![image](https://user-images.githubusercontent.com/102811792/214546987-239a6a2a-3ab2-43e2-a03b-f488aa0e3b1c.png)

#### Tablet View as admin (C.R.U.D)

![image](https://user-images.githubusercontent.com/102811792/214550675-51afe36d-5986-43ea-8425-8517d19b0e60.png)

#### GPU List View as admin (C.R.U.D)

![image](https://user-images.githubusercontent.com/102811792/214547133-488e6098-ce5e-4326-bac7-64a7f53438e3.png)

#### GPU detail - general user logged in

![image](https://user-images.githubusercontent.com/102811792/214547245-3148d585-9ef4-416b-a339-eebcf97ec08b.png)

#### Blog detail - general user logged in
![image](https://user-images.githubusercontent.com/102811792/214547291-40afd0af-c44d-4455-b6f9-aa22d66110df.png)

#### Confirm delete as admin

![image](https://user-images.githubusercontent.com/102811792/214547398-e4432522-cd90-49ed-a0fc-8fa35d34c65f.png)

#### Edit & Create Form as admin

![image](https://user-images.githubusercontent.com/102811792/214547480-5a811a64-1248-4b6a-bbf6-708b36eaa347.png)

- Admin users can see the Admin navigation button to take them to the Django admin console. They can also see an admin section of the dropdown menu in the GPU list view which displays all GPUs including drafts.

# Information Architecture

## Entity Relationship Diagram

![ERD](https://user-images.githubusercontent.com/102811792/214671212-17b40606-6343-4a01-b710-eb325c75af23.png)

## Database Choice

The database of choice is postgres because the data is relational and heroku manages this easily with a low cost.

## Data Models

### Post Model

Model taken from the I think therefore I blog Code Institute example blog, excluding the sourced from field.

- [x] Create - Admin Users can create new blog posts
- [x] Read - Site Users can view blog posts 
- [x] Update - Admin Users can update blog posts
- [x] Delete - Admin Users can delete blog posts

| Key          | Name           | Type             |
|--------------|----------------|------------------|
|              | Title          | CharField[200]   |
| ForeignKey   | Author         | User Model       |
|              | Created Date   | DateTime         |
|              | Updated Date   | DateTime         |
|              | Content        | TextField        |
|              | Featured Image | Cloudinary Image |
|              | Excerpt        | TextField        |
| Many to Many | Likes          | User Model       |
|              | Slug (unique)  | SlugField        |
|              | Status         | Integer          |
|              | Sourced From   | URLField         |

### Comment Model

Model taken from the I think therefore I blog Code Institute example blog, excluding brand field

- [x] Create - Registered Users can create a new comment
- [x] Read - Site Users can view all comments
- [ ] Update - Currently no user update function on this table. Admin can update comments in Django admin console
- [ ] Delete - Currently no user delete function on this table. Admin can delete comments in Django admin console

| Key          | Name           | Type             |
|--------------|----------------|------------------|
| ForeignKey   | Post           | Post Model       |
|              | Name           | CharField[80]    |
|              | Email          | EmailField       |
|              | Body           | TextField        |
|              | Created On     | DateTimeField    |
|              | Approved       | BooleanField     |
|              | Brand          | Integer          |

### GPU Model

- [x] Create - Admin Users can create new GPUs
- [x] Read - Site Users can view GPUs and filter them
- [x] Update - Admin Users can update GPUS
- [x] Delete - Admin Users can delete GPUs

| Key          | Name           | Type             |
|--------------|----------------|------------------|
|              | Name           | CharField[200]   |
|              | GPU Brand      | Integer          |
|              | Created On     | DateTime         |
|              | Updated On     | DateTime         |
|              | Content        | TextField        |
|              | Image          | Cloudinary Image |
|              | Memory Size    | Integer          |
|              | Memory Type    | CharField[10]    |
|              | Base Clock     | SmallInteger     |
|              | Boost Clock    | SmallInteger     |
|              | Other Specs    | TextField        |
|              | Date Released  | DateField        |
|              | Slug (unique)  | SlugField        |
|              | Status         | Integer          |
|              | Sourced From   | URLField         |

# Agile Process

## Project Goals

- Registered users can interact with other users by leaving comments and liking posts they enjoy.
- Admin users can create new blog posts and add the latest GPUs with related specs.
- Admin users can modify existing posts and GPUs to update information that may have changed.
- Admin users can delete existing posts and GPUs to remove them from the database.
- Users can read and enjoy blog posts on various topics.
- Users can easily view and learn about GPUs and what specs they have.

## User Stories

1. As a **Site User** I can **view a list of GPU blog posts** so that **I can choose what GPU news and information to read**
2. As a **Site User** I can **click on a GPU blog post** so that **I can see the selected GPU blog post text contents**
3. As a **Site User** I can **sign up for an account** so that **I can like and comment on GPU blog posts, NVIDIA cards and AMD cards**
4. As a **Site User** I can **navigate to the NVIDIA page** so that **I can view a list of NVIDIA graphics cards**
5. As a **Site User** I can **click on an NVIDIA graphics card** so that **I can see detailed information about that card**
6. As a **Site User** I can **navigate to the AMD page** so that **I can view a list of AMD graphics cards**
7. As a **Site User** I can **click on an AMD graphics card** so that **I can see detailed information about that card**
8. As a **Site User or Site Admin** I can **view comments on a GPU blog post** so that **I can read user comments**
9. As a **Site User** I can **leave comments on a GPU blog post** so that **I can voice my opinion and interact with other users**
10. As a **Site User or Site Admin** I can **view number of likes on a GPU blog post** so that **I can see which posts are popular with users**
11. As a **Site User** I can **like a GPU blog post** so that **I can interact to let users know I liked the content**
12. As a **Site User** I can **optionally choose NVIDIA or AMD when posting** so that **other users viewing my comment know the brand of GPU I'm using**
13. As a **Site Admin** I can **create, read, update and delete posts** so that **I can manage blog content on the home, NVIDIA and AMD pages**
14. As a **Site Admin** I can **approve or disapprove comments** so that **I can filter out objectionable comments**
15. As a **Site Admin** I can **create draft posts** so that **I can finish writing the content later**
16. As a **Site User** I can **view a paginated list of posts** so that **posts are easily viewed**

## Agile Tool

I created my User Stories on GitHub using the Issue section and a custom template. After the User Stories were created I connected them into a GitHub project KanBan board. Here are the links for both Issues and Project.

GitHub Issues: __https://github.com/AlexanderJWard/gpu-bytes/issues__
GitHub Project: __https://github.com/users/AlexanderJWard/projects/3__

### User Story Example

Here is my User Story template in GitHub:

![image](https://user-images.githubusercontent.com/102811792/214451470-9b573ce0-76c7-41ad-987c-968ee5a3c9d5.png)

# Features

## Feature MP4 Showcase

### Change GPU Views

- Admin option allows the superuser to see all GPUs together and to see drafts

https://user-images.githubusercontent.com/102811792/214970243-75f717a3-b40b-49c5-8fb5-8b8114a1a93a.mp4

### Change Post View

- View all option allows the superuser to see drafts

https://user-images.githubusercontent.com/102811792/214973836-a14d9693-4f57-4251-9456-28c3a0caa7e6.mp4

### Approve Comments in Django Admin

https://user-images.githubusercontent.com/102811792/214973402-593cc867-be00-497d-b56b-a8b8408d9a00.mp4

### Like / Unlike Post

https://user-images.githubusercontent.com/102811792/214973712-1ff9bee1-0b70-4e45-8314-bdce8a56c9bb.mp4

## Implemented Features

### Header

The header has different navigation buttons based on what type of user is logged in or if the user is not authenticated. This allows all users to navigate through the site with ease. **Home** takes the user to the default Post List view, **GPUs** takes the user to the default GPU list view, **Admin** takes a superuser to the Django admin panel, **Register** takes an unauthenticated user to the custom sign up page, **Login** takes an unauthenticated user to the custom login page, **Logout** takes any authenticated user to the logout confirmation page.

__Unauthenticated User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214690331-ad11c4d8-51e7-40fc-bedb-75914f265d62.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214692747-1ac760ff-ecb2-4c31-bf20-edc02143b8ac.png)

__General Authenticated User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214690957-1a88a48c-c554-45f8-b344-cfed0ecfa6f8.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214692874-473560ca-92cd-4fbc-964d-b0e1899a9b0d.png)

__Admin User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214690077-8c812ce2-6849-470f-8ccd-2e4be5d0d701.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214692962-a87acefc-d9da-41ae-ad5a-e34209722d41.png)

### Footer

__All Users__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214691058-4b1ff706-a2d1-4e06-a287-54be16e669b1.png)

Footer taken from I think therefore I blog CI example blog

### Post List

The default home page of the blog containing all the tech posts created by admin users. From here all users can open and view posts, admin users can click on the edit and delete buttons to take those actions for each post. They can also click on the Add a Post button to create a new post in the database.

__General Authenticated User & Unauthenticated User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214691425-af1cf975-d9e3-43b8-9fea-2ad8e9ded376.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214694103-26608c90-34d8-430e-b8a9-040a436c0675.png)

__Admin User__

- Admin Drop Down View

As an admin user you can open the drop down menu and select **View All** which changes the view to show all posts including drafts which regular users won't be able to normally view.

![image](https://user-images.githubusercontent.com/102811792/214697057-e0b7d394-f29b-458a-9838-f9643dc2a84e.png)
![image](https://user-images.githubusercontent.com/102811792/214697118-bb75095c-fce3-45a8-ae6d-6793e577aed4.png)

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214691252-60363a78-a188-4ce8-9197-86f2ca505a26.png)

- Tablet

![image](https://user-images.githubusercontent.com/102811792/214695834-66dd0720-5fa2-4ebf-b74d-33e7027e13c7.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214696055-47c2be0c-999c-4b56-83c1-1261e9d50744.png)

### GPU List

The GPU list shows all the graphics cards added by an admin user, these can be clicked and viewed by all users. Admin users can click the edit and delete buttons to complete the action for each GPU, there is also an Add GPU button to create a new entry in the database. All users can click the **Sort By** dropdown menu to change the view between **View All**, **AMD**, and **NVIDIA** which filters the view based on GPU.

__General Authenticated User & Unauthenticated User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214691749-9fd2ab87-f266-4a14-a0d1-886a1b447c42.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214699377-923a42ab-b437-438e-aea9-db64126f0d6b.png)

__Admin User__

- Admin Drop Down  View

The admin user can see an **Admin** option in the drop down which shows all GPUs including drafts which regular users cannot view.

![image](https://user-images.githubusercontent.com/102811792/214700574-d8fbdce7-4f28-4068-8624-3395acf3999d.png)
![image](https://user-images.githubusercontent.com/102811792/214700755-8992b7df-b902-4b83-9eac-d5c2697abd6b.png)

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214691637-425de9a4-786d-402f-b3fa-cc8deb1e6abd.png)

- Tablet

![image](https://user-images.githubusercontent.com/102811792/214700408-71a7476c-d74a-47ed-ac18-c3677887f25d.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214700471-cfeb99c8-a8c7-4fca-95a8-67381bf5a1d0.png)

### Post Detail

This is the post detail view when a user clicks on a post that shows the post image and content as well as letting authenticated users leave a comment and like the post.

__Unauthenticated User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214700983-11feec39-bf2c-4f83-b6c3-8ee3384df0a7.png)
![image](https://user-images.githubusercontent.com/102811792/214701078-10699a75-d6ce-4c49-8508-79fc4e14f8ef.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214701832-7f001209-f44d-42b7-be3f-53bd1f71cc86.png)
![image](https://user-images.githubusercontent.com/102811792/214701908-1ba78d6e-cfc6-4404-91a0-c6a4eb8f8696.png)

__Authenticated Users__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214701291-88e93f50-9ea7-42d5-b749-b139d608fd1a.png)
![image](https://user-images.githubusercontent.com/102811792/214701360-0a18e2fc-b884-4803-b2a8-5bae1d95d4e5.png)
![image](https://user-images.githubusercontent.com/102811792/214701425-452a36b8-5c04-4055-8c37-a529d537f678.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214701625-3a9c6345-13e5-479e-bd6c-223b618b565a.png)
![image](https://user-images.githubusercontent.com/102811792/214701740-673bf3a8-5111-4164-9d2e-d97b5c3369c3.png)

### GPU Detail

This is the GPU detail view after a user clicks on a GPU that shows all related content and specs for that GPU.

__All Users__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214703539-be66e364-9d84-472f-a686-39aa4e6c5290.png)
![image](https://user-images.githubusercontent.com/102811792/214703593-ccf546ac-d600-4bea-b296-ea2202ef96b2.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214703681-0c750ca0-6182-4aef-b262-e2eb8dfcb18e.png)
![image](https://user-images.githubusercontent.com/102811792/214703730-34931771-629a-4ad2-b043-e4d5b96e9742.png)

### Login

The login page that shows for all users who are not logged in, it allows them to enter a username and password.

__Unauthenticated User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214703958-270994a1-56ab-4f18-b019-6a9f6274bdfc.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214704020-5daa091b-6d3e-45b7-9e3b-61a4f1d9174a.png)
![image](https://user-images.githubusercontent.com/102811792/214704057-d3679995-1ba1-4f39-adb9-d20f9e92d4d0.png)

### Logout

The logout page shows for all authenticated users and is a confirmation page asking the user to press either yes or no to logout or be redirected to the home page.

__Authenticated Users__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214704970-435e0e37-2389-4b0b-a3d3-582b54af738b.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214705042-756b9825-7af0-4e68-94c7-14259da70228.png)

### Signup

The signup page shows for all unauthenticated users, it allows them to register an account by creating a username, password then confirm the password.

__Unauthenticated User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214705390-3e24544c-154b-4659-b527-a97fd1c519c7.png)

- Mobile

![image](https://user-images.githubusercontent.com/102811792/214705453-0979fc83-537f-400d-932e-2a9803e01931.png)
![image](https://user-images.githubusercontent.com/102811792/214705483-ce5a76d0-1e17-4614-a47f-df152ee59f88.png)

### Update Record

The update record view for editing both post and GPU. This allows an admin to update each field and submit the changes to the database.

__Admin User__

- Desktop (Post)

![image](https://user-images.githubusercontent.com/102811792/214706139-b4618331-64aa-46ec-b98f-f925bd26bf67.png)
![image](https://user-images.githubusercontent.com/102811792/214706187-bc24dbf4-780d-43f8-97ed-9ec54401df5b.png)

- Desktop (GPU)

![image](https://user-images.githubusercontent.com/102811792/214706312-e2250869-6b6f-47dc-8de7-4ce2e93402cd.png)
![image](https://user-images.githubusercontent.com/102811792/214706389-95afcd5c-dd50-4e85-97c8-7db1a2fbce2e.png)
![image](https://user-images.githubusercontent.com/102811792/214706446-0d92174f-a994-4886-97bc-8462a67a5317.png)

### Delete GPU

The delete gpu view is a confirmation page to ensure the admin is positive they want to delete the gpu from the database.

__Admin User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214708250-5f6f3f6b-ec02-4c16-8d7b-65eb9653ddb5.png)

### Delete Post

The delete post view is a confirmation page to ensure the admin is positive they want to delete the post from the database.

__Admin User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214707271-976b390a-41d7-4f30-b3b1-fdf76e0ab86e.png)

### Create GPU

Create gpu view is very similar to the update view but the fields are not pre-populated and are waiting to be filled in with data to create a new record in the database.

__Admin User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214710673-dcefb0b1-f423-445d-8291-191589c98cbb.png)
![image](https://user-images.githubusercontent.com/102811792/214710711-ff30b068-0469-46da-9ae8-ea4a8bd789c5.png)
![image](https://user-images.githubusercontent.com/102811792/214710762-ee8c587e-077d-4ce5-8d2e-786eba9dfac8.png)

### Create Post

Create post view uses the same form as update record except the fields are blank waiting for new data to be entered into the database.

__Admin User__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214710846-30f80f91-adb8-4e6d-a35b-be7418772586.png)
![image](https://user-images.githubusercontent.com/102811792/214710877-2d0c0be7-ef86-46a5-8c63-c452adc8ef53.png)

### Custom 404 Page

My custom 404 page which shows when an incorrect URL is entered. This has a button to return the user to the home page.

__All Users__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214711578-1da40bae-f3a4-457d-af82-e2cc734a2bac.png)

### Custom 403 Page

My custom 403 page which shows when a user without permission tries to access something only an admin can. This has a button to return the user to the home page.

__All Users__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214715965-08491057-ddf6-4767-9f68-4fd20e83e557.png)

### Custom 500 Page

My custom 500 page which shows when a server error has occured. This has a button to return the user to the home page.

__All Users__

- Desktop

![image](https://user-images.githubusercontent.com/102811792/214716045-29cc49e3-5893-4470-b1cc-6efe70413448.png)

## Future Features

I would like to add full CRUD functionality to the comments model to allow users to delete and edit their comments on each post. I would also like to allow the admin user to be able to toggle comments awaiting approval and approve them directly from the page. Another feature I would like to add is a profile page users can customize various parts of their account.

# Testing

## Manual Testing 

All manual testing has been done in a Google Sheet found here:

https://docs.google.com/spreadsheets/d/19L0qwkOOp45HYHdCvJuMC4G8VYrlFVN3yKtp6tiavgI/edit?usp=sharing

## Compatibility and Responsive Testing

| Device                              | Browser        | OS                    | Viewpoint   |
|-------------------------------------|----------------|-----------------------|-------------|
| Real laptop: Dynabook Satellite Pro | Microsoft Edge | Windows 11            | 1536 x 864  |
| Real phone: One Plus 7 Pro          | Google Chrome  | Android v11 Oxygen OS | 385 x 833   |
| Real laptop: HP 250 G7              | Google Chrome  | Windows 10            | 1306 x 864  |
| Emulation: iPhone SE                | Microsoft Edge | Windows 11            | 375 x 667   |
| Emulation: iPad Air                 | Microsoft Edge | Windows 11            | 1180 x 820  |
| Real desktop: Custom build          | Firefox        | Windows 10            | 2560 x 1440 |
| Real laptop: Microsoft Surface      | Google Chrome  | Windows 11            | 1280 x 720  |
| Emulation: iPad Mini                | Microsoft Edge | Windows 11            | 768 x 1024  |
| Real tablet: iPad (9th Gen)         | Safari         | IOS 15.5              | 1024 x 1366 |

## Accessibility Testing

### Accessibility Audits

- Login

![image](https://user-images.githubusercontent.com/102811792/214954399-0307cb64-7c9c-4c29-913c-144ffef35e61.png)

- Register

![image](https://user-images.githubusercontent.com/102811792/214954526-5582c9d9-a686-4515-88f2-62d1d72f43c4.png)

- Logout

![image](https://user-images.githubusercontent.com/102811792/214954759-84c7848f-91bb-4ef7-8349-ec2a3d65c124.png)

- Post List

![image](https://user-images.githubusercontent.com/102811792/214954922-b6969da8-5f0e-4b18-b55f-90bbb927df2d.png)

- GPU List

![image](https://user-images.githubusercontent.com/102811792/214955044-01e1c5e1-82bb-4725-b522-f20876e65622.png)

- Post Detail

![image](https://user-images.githubusercontent.com/102811792/214958707-8483978e-7e74-4b5c-8729-2449a607842e.png)

- GPU Detail

![image](https://user-images.githubusercontent.com/102811792/214958811-a4ed98a9-3884-452a-81f7-09baa5313a9b.png)

- Update Form

![image](https://user-images.githubusercontent.com/102811792/214958933-6959baac-eaea-4f50-b210-3718fe0a336f.png)

- Delete GPU

![image](https://user-images.githubusercontent.com/102811792/214959240-7bb06828-6895-4652-b47d-ac3727adfebe.png)

- Delete Post

![image](https://user-images.githubusercontent.com/102811792/214959322-77414e4e-e666-48ed-8cbf-a347375ce76a.png)

- Add GPU

![image](https://user-images.githubusercontent.com/102811792/214959423-629e1271-96c4-4671-a736-ad8102659a7d.png)

- Add Post

![image](https://user-images.githubusercontent.com/102811792/214959501-2fb46043-8cf1-430e-b20d-ca3378fdcd51.png)

- 403 Page

![image](https://user-images.githubusercontent.com/102811792/214959592-253462ca-2c1e-4805-bb64-b4ece5a0baad.png)

- 404 Page

![image](https://user-images.githubusercontent.com/102811792/214959676-4c1b748e-86bd-47d1-822b-23ed3e370015.png)

- 500 Page

![image](https://user-images.githubusercontent.com/102811792/214959809-143e94dc-6c25-4a1e-b6e0-360a7e4d0501.png)

## Validation Testing

### CSS Validation

- Style.css

Located in the Static/CSS folder and validated by https://jigsaw.w3.org/css-validator/#validate_by_input

![image](https://user-images.githubusercontent.com/102811792/214902689-57d64031-1b8a-4035-9124-ea1e2e5d581c.png)

### HTML Validation

- Login

![image](https://user-images.githubusercontent.com/102811792/214903542-1b4ba651-7da4-4939-82e4-fa8ede2a9a2c.png)

- Register

![image](https://user-images.githubusercontent.com/102811792/214903738-477329b1-83ce-407d-b5e8-bff348074c2a.png)

- Logout

![image](https://user-images.githubusercontent.com/102811792/214904058-aff1d3f8-6488-46fb-beee-604e610d424d.png)

- Post List

![image](https://user-images.githubusercontent.com/102811792/214905221-2b5f4cd0-9b75-4e81-8998-2cb89fa96d98.png)

- GPU List

![image](https://user-images.githubusercontent.com/102811792/214905388-af962029-1e81-4311-b1d0-4e8b7a645db0.png)

- Post Detail

![image](https://user-images.githubusercontent.com/102811792/214907625-814c7c82-a9f3-40bc-b304-40493e70de16.png)

- GPU Detail

![image](https://user-images.githubusercontent.com/102811792/214908771-0fe2cd7c-79c2-48e5-8258-11409fa965e6.png)

- Update Form

![image](https://user-images.githubusercontent.com/102811792/214910472-9d50ff64-0071-41fe-bf5b-e61b018dd534.png)

- Edit GPU

![image](https://user-images.githubusercontent.com/102811792/214910563-4795990c-db90-437f-b2b8-2d661e698b4f.png)

- Edit Post

![image](https://user-images.githubusercontent.com/102811792/214910660-cdbbc2d2-ddb6-4ebe-a698-94e163d0371e.png)

- Delete GPU

![image](https://user-images.githubusercontent.com/102811792/214910959-e55fc4df-281a-472b-81a7-0113f23d96a7.png)

- Delete Post

![image](https://user-images.githubusercontent.com/102811792/214911787-9342c9d9-df31-45f6-8348-f84747731e4b.png)

- Add GPU

![image](https://user-images.githubusercontent.com/102811792/214912093-5a78b70d-9951-4aee-b6e5-55977fe7953c.png)

- Add Post

![image](https://user-images.githubusercontent.com/102811792/214912226-6b097889-f853-473c-81ea-ee9e934a1b4f.png)

- 403 Page

![image](https://user-images.githubusercontent.com/102811792/214912737-18df32d3-77ef-407d-871c-7e85c7a082fb.png)

- 404 Page

![image](https://user-images.githubusercontent.com/102811792/214912825-9c262c4e-5bbc-4cb1-8e9c-6e2bd9062c55.png)

- 500 Page

![image](https://user-images.githubusercontent.com/102811792/214912949-7b201def-d997-427c-aa86-c00feb20abb5.png)

### Python Validation

- Manage.py

![image](https://user-images.githubusercontent.com/102811792/214919019-4f7c9b66-61e5-4b08-bfd0-203a31cc34ed.png)

- Settings.py

![image](https://user-images.githubusercontent.com/102811792/214919731-81c88fe5-ef60-4c1f-8c63-28b7401a7d5b.png)

- Gpubytes Urls.py

![image](https://user-images.githubusercontent.com/102811792/214919958-17901762-4333-48d7-9e9f-59e4ce3977fb.png)

- Blog Urls.py

![image](https://user-images.githubusercontent.com/102811792/214920353-6b05fd46-d9ab-4c89-bc25-c030da47c127.png)

- Models.py

![image](https://user-images.githubusercontent.com/102811792/214920977-8049792c-b5c1-4e93-8b72-854e78aa9fdf.png)

- Forms.py

![image](https://user-images.githubusercontent.com/102811792/214921594-33da21b6-702e-4656-91ce-a47d77c25dfa.png)

- Admin.py

![image](https://user-images.githubusercontent.com/102811792/214921952-06930741-9194-4190-98bf-7c5f9c8efdc1.png)

- Views.py

![image](https://user-images.githubusercontent.com/102811792/214923130-caac217c-5925-400b-aea7-06ff6d6487df.png)

## Defects

Issues are tracked on GitHUb at the following link: https://github.com/AlexanderJWard/gpu-bytes/issues

## Outstanding Defects

The following issue is a small visual bug where all posts are not equal height, ideally all posts should be the same height being responsive based on the post with the greatest height.

This issue can be found here: https://github.com/AlexanderJWard/gpu-bytes/issues/27

# Deployment

## Development Deployment

1. Add the following browser extension to Google Chrome or Microsoft Edge from here: https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki

![image](https://user-images.githubusercontent.com/102811792/214961898-2d5055f9-521c-485b-a914-3803a209c180.png)

2. Navigate to the GitHub repository located here: https://github.com/AlexanderJWard/gpu-bytes

3. Press the green Gitpod button at the top of the repository.

![image](https://user-images.githubusercontent.com/102811792/214961990-49cbc324-1d71-401a-982f-1684e5d11675.png)

4. If the pip version is out of date run this command: __pip3 install --upgrade pip__

5. Create a new file called env.py in the root directory.

6. Put the following text in the env.py replacing "YOUR VALUE" with relevant values.

import os

os.environ["SECRET_KEY"] = "YOUR_VALUE"
os.environ["CLOUDINARY_URL"] = "YOUR_VALUE"
DEV=True

7. Type pip3 install -r requirements.txt to install required python packages

8. Migrate the database with the following command: __python3 manage.py migrate__

8. Create a Django superadmin user by running the following command: __python manage.py createsuperuser__

9. Run the server by typing in the following command: __python3 manage.py runserver__

## Production Deployment

1. Deploy the site to Heroku. Create an account on Heroku and login.

2. Create a new app, give it a name and choose a region.

![image](https://user-images.githubusercontent.com/102811792/214965318-84e4c192-a99c-450c-af78-265dd329d23f.png)

3. Enter payment information and choose a plan.

4. Navigate to the settings tab

![image](https://user-images.githubusercontent.com/102811792/214965466-dfc99465-3f8c-4c01-8347-75d4d53359d2.png)

5. Reveal config vars and enter the following fields, fill in the values as required.

SECRET_KEY
CLOUDINARY_URL
COLLECT_STATIC

![image](https://user-images.githubusercontent.com/102811792/214965865-aa6c9cd7-e324-4d2b-8f39-a7181d22fb68.png)

6. Navigate to the Deploy tab.

![image](https://user-images.githubusercontent.com/102811792/214966238-f24fcb1b-a2cd-4829-959e-b7388c07c377.png)

7. Choose GitHub, login with credentials and choose the repository.

![image](https://user-images.githubusercontent.com/102811792/214966477-23c3cb39-a228-48d1-ab1e-7ebb4b145e08.png)

8. Choose the branch 'main' and click Deploy. Click Enable Automatic Deploys if desired to auto deploy every time the repository is updated.

# Credits

## Content

- Footer, Post and Comment model based off Code Institute 'I think therefore I blog' example project.

- GPU content taken from the product page of each card. Links are shown on each GPU detail page under "Sourced From" model field.

## Media

- Placeholder image taken from  Pexels. Photo by Sergei Starostin: https://www.pexels.com/photo/graphics-card-in-close-up-photography-6704945/

- Fan Vectors by Iyi Kon on Vecteezy.com. https://www.vecteezy.com/vector-art/351514-charging-fan-vector-icon

- Account Photo by Dave Morgan: https://www.pexels.com/photo/computer-exhaust-fan-2643596/

### Post Images

- https://www.pexels.com/photo/internet-technology-computer-business-4581816/

- https://www.pexels.com/photo/a-person-holding-a-smartphone-9242887/

- https://www.pexels.com/photo/red-and-black-abstract-painting-1820563/

### GPU Images

- https://www.amd.com/en/products/graphics/amd-radeon-rx-7900xtx

- https://www.nvidia.com/en-gb/geforce/graphics-cards/40-series/rtx-4090/

- https://www.nvidia.com/en-gb/geforce/graphics-cards/40-series/rtx-4080/

- https://www.amd.com/en/graphics/amd-radeon-rx-6700-series


## Acknowledgments

- Code Institute 'I think therefore I blog' example project

- Mentor helped me with the class based views (CreateView, UpdateView, DeleteView)
