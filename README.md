# Casai - Backend Applicant Test
This repository will be used by applicants to collaborate with casai to upload the results of their technical evaluation here, via pull request (PR).

* Make a fork of this repository, with your github user and resolve the technical test problems.

## 1.- Edit this readme file and complete the next data:
#### Full Name: Marco Antonio Islas Cruz
#### Personal Email: marco.islas@gmail.com
* Make a commit with the label "[+] Personal Info"

## Problems & instructions

### 2.- Blog application
The objective for the first part of the test is to create an API for publishing posts and also publish comments for these posts (kind of blog).
* Make a commit with the label "[+] Blog API"

#### Rules:
 - The API must be done on django.
 - The post model must have **title**, **published_date**, **is_active**, **content** (html content), and **related_tags** (for easy search) fields.
 - The comment model must have **title**, **comment**, **send_date**, **related_user** fields.
 - Just **is_staff** users can publish post on the blog and edit just their own posts.
 - Just logged users can send comments for the post.
 - Everyone can see the post if they are active (**is_active** field).
 - Just **is_admin**  users can delete posts.

### 3.- Unit test
The second part of this project are the unit tests.
* Make a commit with the label "[+] Blog API unit test"

#### Rules:
 - Create an unit test related to login
 - Create an unit test related to posts
 - Create an unit test related to comments

### 4.- Pull Request
* Make a PR to this repository with title "Backend Applicant - Your Name"

# Happy Coding :)
