# Simple Social Media API

## Overview

This project is a backend API for a mini social media application.  
Users can register, create posts (with optional image uploads), and like other users' posts.  
It is built with **FastAPI** and supports both JSON and multipart form data.

---

## Features

- **User Registration**
  - Endpoint: `POST /users/`
  - Request body:
    ```json
    {
      "username": "rotimi",
      "email": "rotimi@example.com",
      "password": "rotimi123"
    }
    ```
- **Post Creation**
  - Endpoint: `POST /posts/`
  - Fields: `user_id`, `title`, `content`, optional `image`
  - Supports file upload for images.
- **Feed Listing**
  - Endpoint: `GET /posts/` → list all posts
  - Endpoint: `GET /users/{user_id}/posts` → list posts by a specific user
- **Like Functionality**
  - Endpoint: `POST /posts/{post_id}/like`
  - Request body:
    ```json
    {
      "username": "rotimi"
    }
    ```
  - Increments the like counter for the post.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
