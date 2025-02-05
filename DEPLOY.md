# Deploying to DigitalOcean App Platform

## Prerequisites
1. A DigitalOcean account
2. Your repository connected to DigitalOcean

## Configuration Files
The project includes several configuration files for deployment:

1. `Dockerfile.do`: Custom Dockerfile for DigitalOcean deployment
   - Uses Python 3.13
   - Sets up proper environment variables
   - Handles static files and migrations
   - Uses Gunicorn configuration

2. `python.config`: Python runtime configuration
   - Specifies Python version
   - Sets entry point
   - Configures environment variables

3. `gunicorn.conf.py`: Gunicorn server configuration
   - Sets up Python path
   - Configures workers and threads
   - Handles logging
   - Pre-loads WSGI application

## Deployment Steps

1. Create a new app in DigitalOcean App Platform:
   - Go to https://cloud.digitalocean.com/apps
   - Click "Create App"
   - Select your GitHub repository
   - Choose the branch to deploy (main)
   - Specify `Dockerfile.do` as the Dockerfile path

2. Configure Environment Variables:
   ```
   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=${APP_DOMAIN}
   DJANGO_SECRET_KEY=[generate a secure key]
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_EMAIL=admin@example.com
   DJANGO_SUPERUSER_PASSWORD=[choose a strong password]
   ```

3. Add Database:
   - Click "Add Resource"
   - Choose "Database"
   - Select "Dev Database"
   - The DATABASE_URL will be automatically added to your environment

4. Deploy:
   - Click "Deploy to Production"
   - The deployment process will:
     * Install dependencies
     * Run database migrations
     * Create superuser
     * Collect static files

## Monitoring

- View logs: Apps > Your App > Components > web > Logs
- Monitor resources: Apps > Your App > Insights
- Check deployment status: Apps > Your App > Deployments

## Troubleshooting

1. Check the application logs for any errors:
   - The Gunicorn configuration includes debug-level logging
   - All output is directed to stdout/stderr for easy viewing

2. Common issues:
   - If the app fails to start, check the environment variables
   - If static files are missing, verify the collectstatic command ran successfully
   - If database errors occur, ensure migrations completed successfully

3. Deployment logs:
   - Review build logs for any dependency installation issues
   - Check runtime logs for application startup problems
   - Monitor database connection errors in the logs