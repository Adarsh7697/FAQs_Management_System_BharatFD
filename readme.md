# FAQ Management System

A Django-based FAQ management system with multi-language translation support, a WYSIWYG editor, and a REST API. Includes Redis caching for improved performance.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker and Docker Compose (optional)
- Redis (for caching)

---

## 🛠️ Installation


#### **Local Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/Adarsh7697/FAQs_Management_System_BharatFD.git
   cd faq_project



2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
     # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Redis server. If you're using Docker, you can run Redis using:

    ```bash
    docker-compose up -d
    ```

5. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser for Django Admin:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

Now you can access the project at `http://localhost:8000`.

## Docker Setup
Build and Run Containers:
```bash
docker-compose up --build
```

##📡  API Usage

The system exposes a **REST API** to manage and retrieve FAQs.

### Endpoints

1. **GET /api/faqs/**: Get a list of FAQs.
    - Example: `curl http://localhost:8000/api/faqs/`
    - Supports language selection with the `?lang=<language_code>` query parameter.

    **Example Requests:**
    ```bash
    # Fetch FAQs in English (default)
    curl http://localhost:8000/api/faqs/

    # Fetch FAQs in Hindi
    curl http://localhost:8000/api/faqs/?lang=hi

    # Fetch FAQs in Bengali
    curl http://localhost:8000/api/faqs/?lang=bn
    ```

###🛠️  Caching

The API uses **Redis** for caching FAQ translations. By default, the cache is stored in `redis://127.0.0.1:6379/1`.

##🖥️  Admin Panel

You can access the Django admin panel at `http://localhost:8000/admin/`.
- Login with the superuser credentials you created earlier.
- Manage FAQs and their translations.

## Docker Support

This project comes with a `Dockerfile` and `docker-compose.yml` file for containerized deployment.

### Running with Docker

1. Build and run the containers:

    ```bash
    docker-compose up --build
    ```

2. The application will be available at `http://localhost:8000`.

##🧪  Tests

To run tests, make sure to activate your virtual environment and run:

```bash
pytest
```

Unit Tests

Unit tests are included to test:
	•	Model methods (for translation and caching).
	•	API responses (ensure that the FAQ data is correctly returned in different languages).

Git Commit Messages

Follow conventional commit message practices:
	•	feat: Add multilingual FAQ model
	•	fix: Improve translation caching
	•	docs: Update README with API examples

Ensure atomic commits with clear commit messages.

##🤝 Contributing
	1.	Fork the repository.
	2.	Create a new branch: git checkout -b feature-name.
	3.	Make your changes and commit them: git commit -m 'feat: Add feature'.
	4.	Push to your forked repository: git push origin feature-name.
	5.	Create a pull request from your fork to this repository.

##📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
