# Simple Social Media API

## Overview

This project is a backend API for a mini social media application.  
Users can register, authenticate with JWT, create posts (with optional image uploads), update/delete their posts, and like other users' posts.  
It is built with **FastAPI** and supports both JSON and multipart form data.

---

## Features

### 👤 User Management

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
- **User Login**
  - Endpoint: `POST /users/login`
  - Returns JWT access token
- **List Users**
  - Endpoint: `GET /users/`
- **Delete User**
  - Endpoint: `DELETE /users/{username}`

---

### 🔑 Authentication

- **Login (Swagger integration)**
  - Endpoint: `POST /auth/login`
- **Get Current User**
  - Endpoint: `GET /auth/me`
- **Verify Token**
  - Endpoint: `GET /auth/verify`
- **Logout**
  - Endpoint: `POST /auth/logout`

---

### 📝 Posts

- **Post Creation**
  - Endpoint: `POST /posts/`
  - Fields: `title`, `content`, optional `image`
  - Supports file upload for images
- **List All Posts**
  - Endpoint: `GET /posts/`
- **Get Single Post**
  - Endpoint: `GET /posts/{post_id}`
- **List Posts by User**
  - Endpoint: `GET /posts/user/{username}`
- **Update Post**
  - Endpoint: `PUT /posts/{post_id}`
  - Only owner can update
- **Delete Post**
  - Endpoint: `DELETE /posts/{post_id}`
  - Only owner can delete
- **Like Functionality**
  - Endpoint: `POST /posts/{post_id}/like`
  - Request body:
    ```json
    {
      "username": "rotimi"
    }
    ```
  - Increments the like counter for the post

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
