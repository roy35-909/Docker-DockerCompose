# Hello World Animation Counter App

A simple Flask application that displays "Hello World" with beautiful animations and counts clicks in a database.

## Features

- Interactive "Hello World" text with click animations
- Particle animation background with connecting lines
- Click counter stored in SQLite database
- Complete Docker setup for easy deployment
- Responsive design

## Prerequisites

- Docker and Docker Compose
  - [Install Docker](https://docs.docker.com/get-docker/)
  - [Install Docker Compose](https://docs.docker.com/compose/install/)

OR

- Python 3.9 or higher
- pip (Python package manager)

## Project Structure

```
hello-world-app/
├── app.py                  # Main Flask application
├── templates/              # HTML templates
│   └── index.html          # Main page with animations
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
└── README.md               # This file
```

## Installation and Setup

### Option 1: Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd hello-world-app
   ```

2. Build and start the Docker container:
   ```bash
   docker-compose up --build
   ```

3. The application will be available at http://localhost:5000

### Option 2: Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd hello-world-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. The application will be available at http://localhost:5000

## User Manual

### Home Page

When you open the application, you'll see:
- "Hello World" displayed in the center of the screen
- A counter showing how many times the text has been clicked
- Beautiful animated particles moving in the background

### Interacting with the App

1. **Click the "Hello World" text**:
   - A ripple animation will appear from where you clicked
   - The text will pulse briefly
   - The counter will increment by one
   - This count is stored persistently in the database

2. **View Counter**:
   - The counter displays the total number of clicks across all sessions
   - The count is stored in a SQLite database
   - With Docker, the database is persisted using a volume

### Data Persistence

- The application uses SQLite to store the click count
- When using Docker, the database file is stored in a volume to ensure data persists between container restarts
- The database is automatically initialized on first run

## Development Notes

### Database

The application uses SQLAlchemy with SQLite. The database schema is simple:

- Table: `counter`
  - Column: `id` (Primary Key)
  - Column: `count` (Integer)

### Backend

- Built with Flask
- Uses Flask-SQLAlchemy for database operations
- Simple API endpoint `/increment` for updating the counter

### Frontend

- Vanilla JavaScript for all interactions
- Canvas-based particle animation
- CSS animations for visual effects

## Troubleshooting

- **Port already in use**: If port 5000 is already in use, modify the `docker-compose.yml` file to map to a different port:
  ```yaml
  ports:
    - "8080:5000"  # Change 8080 to any available port
  ```

- **Database issues**: If you encounter database problems, you can reset the database by removing the `instance` directory (or the `counter.db` file within it) and restarting the application.

- **Docker volume permissions**: If you encounter permission issues with the Docker volume, you may need to adjust the permissions:
  ```bash
  sudo chown -R $USER:$USER instance/
  ```

## License

This project is open-source and available under the MIT License.