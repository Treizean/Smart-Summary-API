# Smart Summary API

Smart Summary API is a lightweight Flask application that allows users to submit raw text and receive a concise summary generated using OpenAI's GPT model. The API is designed to demonstrate the integration of Generative AI (GenAI) within a cloud-hosted microservice using Python, Flask, and AWS EC2.

## Features

- RESTful API built with Flask
- Summarizes any text using OpenAI's GPT-3.5 model
- Secure configuration via environment variables
- Deployed on AWS EC2 with flexible port control
- Logs request metadata for analysis and debugging

## Tech Stack

- Python 3.11
- Flask
- OpenAI API
- python-dotenv
- AWS EC2 (Ubuntu)
- Postman (for testing)
- PuTTY (for SSH access from Windows)

## Endpoints

### `POST /summarize`

Takes in raw text and returns a summarized version.

**Request Example:**

```http
POST http://<your-ec2-ip>:5050/summarize
Content-Type: application/json
