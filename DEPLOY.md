# Deploying to DigitalOcean App Platform

## Prerequisites
1. A DigitalOcean account
2. Your repository connected to DigitalOcean

## Deployment Steps

1. Create a new app in DigitalOcean App Platform:
   - Go to https://cloud.digitalocean.com/apps
   - Click "Create App"
   - Select your GitHub repository

2. Configure the App:
   - Choose the branch to deploy (main)
   - Select "Dockerfile" as the deployment method
   - Specify `Dockerfile.do` as the Dockerfile path

3. Configure Environment Variables:
   ```
   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=${APP_DOMAIN}
   DJANGO_SECRET_KEY=[generate a secure key]
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_EMAIL=admin@example.com
   DJANGO_SUPERUSER_PASSWORD=[choose a strong password]
   ```

4. Add Database:
   - Click "Add Resource"
   - Choose "Database"
   - Select "Dev Database" (or production tier as needed)
   - The DATABASE_URL will be automatically added to your environment

5. Deploy:
   - Click "Deploy to Production"
   - Wait for the build and deployment to complete

## Troubleshooting

If you encounter issues:
1. Check the app logs in the DigitalOcean dashboard
2. Verify environment variables are set correctly
3. Ensure database migrations completed successfully

## Monitoring

- View logs: Apps > Your App > Components > web > Logs
- Monitor resources: Apps > Your App > Insights
- Check deployment status: Apps > Your App > Deployments