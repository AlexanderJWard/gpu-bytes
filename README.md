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
__TO BE ADDED__

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
TO BE ADDED IF TIME

### Frameworks

For my framework, I chose to use Boostrap as it's something I've started to learn and am most familiar with it. Fitting perfectly with my design elements the framework supports everything I require for this website.

### Custom Styles

I made custom changes to some of the bootstrap classes in my __style.css__ file located in __Static/CSS__ folder structure. I used CSS to change the color of btn-success and btn-warning so they match my chosen design colors. Further changes can be found in the aforementioned CSS file.

![image](https://user-images.githubusercontent.com/102811792/214534235-e681b4d3-fc2a-4227-817a-a5450f09d0b9.png)

### Wireframes

#### Basic View
![image](https://user-images.githubusercontent.com/102811792/214549349-610f6538-cad0-4d02-899f-f5365085a029.png)

#### Mobile View
![image](https://user-images.githubusercontent.com/102811792/214546987-239a6a2a-3ab2-43e2-a03b-f488aa0e3b1c.png)

#### Tablet View as admin (C.R.U.D)
![image](https://user-images.githubusercontent.com/102811792/214550675-51afe36d-5986-43ea-8425-8517d19b0e60.png)

#### GPU List View as admin (C.R.U.D)
![image](https://user-images.githubusercontent.com/102811792/214547133-488e6098-ce5e-4326-bac7-64a7f53438e3.png)

#### GPU detail
![image](https://user-images.githubusercontent.com/102811792/214547245-3148d585-9ef4-416b-a339-eebcf97ec08b.png)

#### Blog detail
![image](https://user-images.githubusercontent.com/102811792/214547291-40afd0af-c44d-4455-b6f9-aa22d66110df.png)

#### Confirm delete
![image](https://user-images.githubusercontent.com/102811792/214547398-e4432522-cd90-49ed-a0fc-8fa35d34c65f.png)

#### Edit & Create Form
![image](https://user-images.githubusercontent.com/102811792/214547480-5a811a64-1248-4b6a-bbf6-708b36eaa347.png)



## User Stories
I created my User Stories on GitHub using the Issue section and a custom template. After the User Stories were created I connected them into a GitHub project KanBan board. Here are the links for both Issues and Project.

GitHub Issues: __https://github.com/AlexanderJWard/gpu-bytes/issues__ \
GitHub Project: __https://github.com/users/AlexanderJWard/projects/3__

Here is my User Story template in GitHub:
![image](https://user-images.githubusercontent.com/102811792/214451470-9b573ce0-76c7-41ad-987c-968ee5a3c9d5.png)

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

## Design




## Data Models

### Blog Post

- [ ] Create - Admin Users can create new blog posts
- [x] Read - Site Users can view blog posts 
- [ ] Update - Admin Users can update blog posts
- [ ] Delete - Admin Users can delete blog posts

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

### Comment

- [x] Create - Registered Users can create a new comment
- [x] Read - Site Users can view all comments
- [x] Update - Registered Users can update a comment they created
- [x] Delete - Registered Users can delete a comment they created

| Key          | Name           | Type             |
|--------------|----------------|------------------|
| ForeignKey   | Post           | Post Model       |
|              | Name           | CharField[80]    |
|              | Email          | EmailField       |
|              | Body           | TextField        |
|              | Created On     | DateTimeField    |
|              | Approved       | BooleanField     |


