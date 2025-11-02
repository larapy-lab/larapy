# My Larapy Project

A web application built with the Larapy framework.

## Requirements

- Python 3.11+
- Redis (optional, for cache/queue)
- PostgreSQL/MySQL (optional, SQLite by default)

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -e .
   ```
3. Copy environment file:
   ```bash
   cp .env.example .env
   ```
4. Run migrations:
   ```bash
   python artisan migrate
   ```
5. Start the server:
   ```bash
   python artisan serve
   ```

Visit: http://localhost:8000

## Development

Run tests:
```bash
pytest tests/
```

Run linters:
```bash
black .
ruff check .
```

## Documentation

Visit [https://docs.larapy.dev](https://docs.larapy.dev) for comprehensive framework documentation.

## License

The Larapy framework is open-sourced software licensed under the [MIT license](LICENSE).
