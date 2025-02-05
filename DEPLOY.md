# Deploying to DigitalOcean App Platform

## Prerequisites
1. A DigitalOcean account
2. Your repository connected to DigitalOcean

## Configuration Files
The project includes several configuration files for deployment:

1. `Procfile`: Defines the command to run the application
   - Uses Gunicorn as the WSGI server
   - Sets proper worker configuration
   - Enables debug logging

2. `bin/post_compile`: Post-deployment script
   - Creates necessary directories
   - Runs database migrations
   - Collects static files
   - Creates superuser if needed

## Deployment Steps

1. Create a new app in DigitalOcean App Platform:
   - Go to https://cloud.digitalocean.com/apps
   - Click "Create App"
   - Select your GitHub repository
   - Choose the branch to deploy (main)

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
     * Install Python dependencies
     * Run post_compile script
     * Start the application using Procfile

## Monitoring

- View logs: Apps > Your App > Components > web > Logs
- Monitor resources: Apps > Your App > Insights
- Check deployment status: Apps > Your App > Deployments

## Troubleshooting

1. Check the application logs for any errors:
   - Gunicorn logs will show startup issues
   - Django logs will show application errors
   - post_compile script logs will show initialization issues

2. Common issues:
   - If the app fails to start, check the environment variables
   - If static files are missing, check post_compile script logs
   - If database errors occur, verify migrations completed
   - If buildpack fails, check requirements.txt is valid

3. Deployment logs:
   - Review build logs for dependency installation issues
   - Check post_compile script output for initialization problems
   - Monitor database connection errors
   - Verify Procfile is being detected and used

4. File Permissions:
   - Ensure bin/post_compile is executable (chmod +x)
   - Check directory permissions for staticfiles and mediafiles
   - Verify database user has proper permissions

5. Environment Variables:
   - All required variables must be set
   - DATABASE_URL should be automatically configured
   - DJANGO_ALLOWED_HOSTS must include app domain