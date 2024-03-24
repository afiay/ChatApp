
![Python](https://img.shields.io/badge/python-3.11.2-blue.svg)


# ChatApp

ChatApp is a web-based messaging platform that enables users to communicate in real-time. Built with Django, this application demonstrates the use of WebSockets and Channels to provide a seamless chat experience.

# User-Friendly Messaging Interface

Our ChatApp boasts a sleek and intuitive user interface designed for optimal user experience. At a glance, you can enjoy the following features:

- **Effortless User Search**: Quickly find and connect with users through our streamlined search functionality.
- **Instant Communication**: Click 'Send Message' to dive right into conversation with your selected contact.
- **Minimalistic Design**: A clutter-free environment that focuses on what matters most — your conversations.


## Features

- Real-time messaging
- User authentication system
- Responsive design for cross-device compatibility
- Persistent message history

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed:

- Python 3.8+
- Django 5.0.3
- Channels
- Daphne

### Installing

Clone the repository:

```bash
git clone https://github.com/afiay/ChatApp.git
cd ChatApp
```

Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run migrations to create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Now access the application at http://127.0.0.1:8000/chat/.

## Running the tests

Explain how to run the automated tests for this system (if applicable).

## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

- Django - The web framework used
- Channels - For handling WebSockets
- Daphne - ASGI server for Django

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use SemVer for versioning. For the versions available, see the tags on this repository.

## Authors

- Your Name - Initial work - YourUsername

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
