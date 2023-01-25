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

![image](https://user-images.githubusercontent.com/102811792/214450483-e0617bd1-248f-451d-829b-c4e1e5afa558.png)

## User Stories
I created my User Stories on GitHub using the Issue section and a custom template. After the User Stories were created I connected them into a GitHub project KanBan board. Here are the links for both Issues and Project.

GitHub Issues: __https://github.com/AlexanderJWard/gpu-bytes/issues__ \
GitHub Project: __https://github.com/users/AlexanderJWard/projects/3__

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

### Wireframes
![GPU Bytes](https://user-images.githubusercontent.com/102811792/207378032-64592473-f19a-41ca-a864-ac54cb5e1818.png)



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


