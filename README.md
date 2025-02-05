# Afro-Renaissance Movement

A platform dedicated to unleashing the power of human capital as the catalyst for Africa's economic and social transformation.

## Deployment to DigitalOcean App Platform

1. Fork this repository to your GitHub account.

2. Create a new app on DigitalOcean App Platform:
   - Go to [DigitalOcean Apps](https://cloud.digitalocean.com/apps)
   - Click "Create App"
   - Select your GitHub repository
   - Choose the branch to deploy (main)

3. Configure Environment Variables:
   Required environment variables will be automatically set up from the app.yaml configuration, but you need to set values for:
   - `DJANGO_SECRET_KEY`: Generate a secure secret key
   - `DJANGO_SUPERUSER_PASSWORD`: Choose a strong password for the admin user

4. Deploy the App:
   - Click "Deploy to Production"
   - The deployment process will:
     - Install dependencies
     - Run database migrations
     - Create superuser
     - Initialize sample data
     - Collect static files

5. Access Your App:
   - Once deployed, you can access your app at the provided URL
   - Admin interface will be at `/admin`
   - Login with:
     - Username: admin
     - Password: (the one you set in DJANGO_SUPERUSER_PASSWORD)

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/afro-renaissance.git
cd afro-renaissance
```

2. Create a .env file:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Build and run with Docker:
```bash
docker compose up -d
```

4. Access the development server at http://localhost:8080

## Features

- Manifesto Section: Core principles and vision
- Blog: Articles and discussions
- Social Platform: Community interaction
- User Profiles: Personal spaces for members
- Responsive Design: Works on all devices

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.