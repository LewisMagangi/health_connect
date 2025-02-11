# Health Connect - Technical Stack Specification

## Stack Components Breakdown

| Component | Technology | Details |
|-----------|------------|----------|
| Backend Framework | Django & DRF | - Django 4.2+ for core functionality<br>- Django REST Framework for API development |
| Database Layer | PostgreSQL & Redis | - PostgreSQL as primary database<br>- Redis for caching and session management |
| Task Processing | Celery | - Celery with Redis/RabbitMQ as message broker<br>- Async task processing for emails, notifications |
| Authentication | JWT | - JSON Web Tokens via DRF<br>- Token-based authentication for API |
| Web Server | Nginx | - Reverse proxy<br>- Static file serving<br>- Load balancing |
| App Server | uWSGI/ASGI | - uWSGI for WSGI applications<br>- ASGI for WebSocket support |
| Frontend | React | - React 18+ for UI development<br>- CSS3 for styling<br>- Modern JavaScript (ES6+)<br>- Vite for build tooling |
| Container Runtime | Docker | - Containerized development and deployment<br>- Docker Compose for local development |
| Cloud Infrastructure | K8s & Cloud | - Kubernetes orchestration<br>- Major cloud provider support (AWS/GCP/Azure)<br>- CI/CD pipeline integration |

## Infrastructure Diagram
```
[Client] → [Nginx] → [uWSGI/ASGI] → [Django/DRF]
                                  ↓
                    [PostgreSQL] ← → [Redis]
                                  ↓
                              [Celery]
```

## Development Environment Requirements
- Docker & Docker Compose
- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Redis 6+

## Frontend Development Requirements
- Node.js 18+
- React 18+
- Vite
- Modern CSS features
- Browser compatibility: Latest 2 versions of modern browsers

## Deployment Considerations
- Containerized deployment using Docker
- Kubernetes cluster management
- Cloud provider agnostic design
- Automated CI/CD pipelines
- Infrastructure as Code (IaC)

## Scaling Strategy
- Horizontal scaling via K8s
- Redis caching layer
- Database replication
- Load balancing with Nginx
