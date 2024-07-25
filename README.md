# AirBnB Clone V3

Welcome to the **AirBnB Clone V3** project! This project is part of the Holberton School curriculum and aims to develop a simplified version of the AirBnB platform. This version includes a RESTful API to handle HTTP requests and perform CRUD operations on the backend storage system.

All instructions mentionned here refer to the Holberton School project's tasks. They are already implemented in the project.
## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Tasks](#tasks)
5. [Contributing](#contributing)
6. [License](#license)

## Project Overview

The **AirBnB Clone V3** is a full-stack web development project that introduces a RESTful API built with Flask and SQLAlchemy. This project extends previous versions by incorporating features for managing users, places, cities, states, and amenities through a robust web service.

## Installation

Follow these steps to set up the project:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/holbertonschool-AirBnB_clone_v3.git
    cd holbertonschool-AirBnB_clone_v3
    ```

2. **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    - `HBNB_ENV`: Set to "dev" or "test".
    - `HBNB_MYSQL_USER`: Your MySQL username.
    - `HBNB_MYSQL_PWD`: Your MySQL password.
    - `HBNB_MYSQL_HOST`: Your MySQL host.
    - `HBNB_MYSQL_DB`: Your database name.
    - `HBNB_TYPE_STORAGE`: Set to "file" or "db".

5. **Run the application:**

    ```bash
    python3 -m api.v1.app
    ```

## Usage

Interact with the API using HTTP requests to manage resources such as users, places, cities, states, and amenities. Use tools like `curl` or Postman for testing and development purposes.

## Tasks

### 0. Restart from scratch!

- **Description:** Set up a fresh codebase for version 3 of the project by forking from version 2, updating the repository name, and configuring the project environment.

- **Repository:** [GitHub](https://github.com/your-username/holbertonschool-AirBnB_clone_v3)

### 1. Never fail!

- **Description:** Implement error handling in the API for consistent error messages for HTTP requests. Validate input data and provide appropriate responses.

### 2. Code review

- **Description:** Conduct a code review to ensure adherence to best practices. Refactor and improve code quality, readability, and documentation.

### 3. Improve storage

- **Description:** Integrate SQLAlchemy to enhance the storage engine for ORM support, models, and migrations, allowing more robust data management.

### 4. Status of your API

- **Description:** Create an endpoint to check the API status, returning information about the current state and number of objects in the storage system.

### 5. Some stats?

- **Description:** Extend the status endpoint to include additional statistics about the number of objects stored, such as users, places, and cities.

### 6. State

- **Description:** Implement a view to handle State objects with CRUD operations using RESTful API actions, enabling users to manage state data.

- **Files:** `api/v1/views/states.py`, `api/v1/views/__init__.py`

### 7. City

- **Description:** Develop a view for City objects with complete RESTful API actions, including endpoints for managing city resources.

- **Files:** `api/v1/views/cities.py`, `api/v1/views/__init__.py`

### 8. Amenity

- **Description:** Create a view for Amenity objects that handles CRUD operations using RESTful API, allowing interaction with Amenity data.

- **Files:** `api/v1/views/amenities.py`, `api/v1/views/__init__.py`

### 9. User

- **Description:** Implement a view for managing User objects, including CRUD operations via the API, and ensure secure handling of user data.

- **Files:** `api/v1/views/users.py`, `api/v1/views/__init__.py`

### 10. Place

- **Description:** Create a view for Place objects with all RESTful API actions, enabling management of place data in the application.

- **Files:** `api/v1/views/places.py`, `api/v1/views/__init__.py`

### 11. Reviews

- **Description:** Develop a view to manage Review objects, including CRUD operations for reviews associated with places through the API.

- **Files:** `api/v1/views/reviews.py`, `api/v1/views/__init__.py`

### 12. HTTP access control (CORS)

- **Description:** Implement Cross-Origin Resource Sharing (CORS) to allow API access from different origins, ensuring secure and proper CORS configuration.

- **Files:** `api/v1/app.py`

### 13. Not found

- **Description:** Enhance the API to handle 404 errors consistently across all endpoints, ensuring meaningful error messages for invalid requests.

### 14. Place - Amenity

- **Description:** Create a view for linking Place and Amenity objects with RESTful API actions, allowing for association and disassociation between them.

- **Files:** `api/v1/views/places_amenities.py`, `api/v1/views/__init__.py`

### 15. Security improvements!

- **Description:** Improve the User object by hashing passwords using MD5 and ensuring secure password storage in both the database and file storage.

- **Files:** `models/base_model.py`, `models/user.py`

### 16. Search

- **Description:** Implement a search endpoint to retrieve Place objects based on JSON parameters in the request body, supporting filtering by states, cities, and amenities.

- **Files:** `api/v1/views/places.py`

### 17. Documentation

- **Description:** Use Flasgger to document each API endpoint, enabling easy access to API documentation through a web interface.

- **Command:** Install with `pip3 install flasgger`

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch.**
3. **Commit your changes.**
4. **Push to your fork.**
5. **Open a pull request.**

Ensure your code follows the project's standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
