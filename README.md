# CC Lab-2: Event Management Web Application ( Monolithic Architecture )

A FastAPI-based event management system with user authentication, event registration, and load testing capabilities. This lab demonstrates building a scalable web application with database operations and performance testing using Locust.

## Project Overview

This project implements a web application for managing college events and user registrations. Users can register, log in, view available events, and register for events. The application includes load testing scenarios to evaluate performance under various user loads.

**SRN:** PES2UG23CS464

## Features

- **User Authentication**: User registration and login system
- **Event Management**: Browse available events with registration fees
- **Event Registration**: Users can register for events
- **Persistent Storage**: SQLite database for users, events, and registrations
- **Load Testing**: Locust-based performance testing for multiple user scenarios
- **Web Interface**: HTML templates for user interactions

## Project Structure

```
CC Lab-2/
├── main.py                          # FastAPI application and main routes
├── database.py                      # SQLite database connection setup
├── insert_events.py                 # Script to populate initial events
├── requirements.txt                 # Python dependencies
├── templates/                       # Jinja2 HTML templates
│   ├── base.html                   # Base template
│   ├── register.html               # User registration page
│   ├── login.html                  # User login page
│   ├── events.html                 # Events listing page
│   ├── my_events.html              # User's registered events
│   ├── checkout.html               # Checkout/payment page
│   └── error.html                  # Error page
├── checkout/                        # Checkout logic module
│   └── __init__.py
└── locust/                          # Load testing scripts
    ├── events_locustfile.py        # Events page load test
    ├── checkout_locustfile.py      # Checkout flow load test
    ├── myevents_locustfile.py      # My events page load test
    └── locust/
        └── journey_locustfile.py   # Complete user journey test
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT
)
```

### Events Table
```sql
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    fee INTEGER
)
```

### Registrations Table
```sql
CREATE TABLE registrations (
    username TEXT,
    event_id INTEGER
)
```

## Available Events

The application comes with pre-configured events:
- Hackathon (₹500)
- Dance Battle (₹300)
- AI Workshop (₹400)
- Photography Walk (₹200)
- Gaming Tournament (₹350)
- Music Night (₹250)
- Treasure Hunt (₹150)
- Stand-up Comedy (₹300)
- Robo Race (₹450)

## Installation

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database with Events:**
   ```bash
   python insert_events.py
   ```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

### Available Routes

- `GET /register` - Registration page
- `POST /register` - Submit registration form
- `GET /login` - Login page
- `POST /login` - Submit login credentials
- `GET /events?user={username}` - View all available events
- `GET /register_event/{event_id}?user={username}` - Register for an event
- `GET /my-events?user={username}` - View user's registered events

## Load Testing with Locust

Locust is used to simulate multiple users and measure application performance.

### Running Load Tests

1. **Events Page Load Test:**
   ```bash
   locust -f locust/events_locustfile.py -h
   ```

2. **Checkout Flow Load Test:**
   ```bash
   locust -f locust/checkout_locustfile.py -h
   ```

3. **My Events Page Load Test:**
   ```bash
   locust -f locust/myevents_locustfile.py -h
   ```

4. **Complete User Journey Test:**
   ```bash
   locust -f locust/locust/journey_locustfile.py -h
   ```

Each Locust command opens a web interface (default: `http://localhost:8089`) where you can:
- Specify number of users to simulate
- Set spawn rate
- View real-time metrics
- Monitor response times and throughput

## Dependencies

- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **Jinja2**: Template engine
- **python-multipart**: Form data parsing
- **Locust**: Load testing tool

## Key Implementation Details

- **SQLite Database**: Lightweight, file-based database stored as `fest.db`
- **Template Rendering**: Dynamic HTML pages using Jinja2
- **Form Handling**: FastAPI Form objects for receiving user input
- **Redirects**: Used for post-login/post-registration flow
- **Error Handling**: Basic exception handling for duplicate username registration

## Performance Characteristics

- Event listing includes intentional computational workload (waste loop) to simulate real-world processing
- Database queries use parameterized statements to prevent SQL injection
- Joins are used for complex queries (e.g., getting user's registered events)

## Security Notes

⚠️ **Educational Use Only**: This application demonstrates basic functionality and is not production-ready. Security considerations:
- Passwords are stored in plain text (use proper hashing in production)
- No CSRF protection implemented
- SQL injection vulnerability prevention uses parameterized queries
- Session management is minimal

## Future Enhancements

- User session management with JWT tokens
- Payment integration for checkout
- Admin dashboard for event management
- Email notifications for event registration
- Search and filtering for events
- User profile management
