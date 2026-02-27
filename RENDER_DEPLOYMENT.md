# Render.com Deployment Guide

This guide will help you deploy the Django Store Management System to Render.com.

## Prerequisites

1. A Render.com account (Sign up at https://render.com)
2. Your code pushed to GitHub
3. A GitHub repository linked to Render

## Step 1: Create a PostgreSQL Database on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" > "PostgreSQL"
3. Fill in the details:
   - **Name**: `store-management-db`
   - **Database**: `store_management`
   - **User**: `store_user`
   - **Region**: Choose your region
   - **PostgreSQL Version**: 14+
   - **Datadog API Key**: Leave blank (optional)
4. Click "Create Database"
5. Note the Internal Database URL (starts with `postgresql://`)

## Step 2: Create a Web Service on Render

1. Go to Render Dashboard
2. Click "New +" > "Web Service"
3. Connect your GitHub repository
4. Fill in the service details:
   - **Name**: `store-management` or similar
   - **Runtime**: Python 3.11
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn store_management.wsgi:application --bind 0.0.0.0:$PORT`
   - **Region**: Same as your database

## Step 3: Add Environment Variables

In the Web Service settings, add the following environment variables:

### From your database (copy from PostgreSQL service details):
- `DB_ENGINE`: `postgresql`
- `DB_NAME`: (from internal connection string)
- `DB_USER`: (from internal connection string)
- `DB_PASSWORD`: (from internal connection string)
- `DB_HOST`: (from internal connection string - the hostname)
- `DB_PORT`: `5432`

### Django Configuration:
```
DEBUG=False
SECRET_KEY=<generate-a-new-secure-key>
ALLOWED_HOSTS=yourdomain.onrender.com,yourdomain.com
```

### To generate a new SECRET_KEY, run:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Step 4: Configure Health Check (Optional)

1. Set Health Check Path: `/admin/`
2. Set Health Check Protocol: `HTTP`

## Step 5: Deploy

1. Click "Create Web Service"
2. Render will automatically start building and deploying your application
3. Watch the logs in the Render Dashboard
4. Once deployed, you'll get a URL like `https://store-management.onrender.com`

## Step 6: Create Superuser on Render

Once deployed, you can create a superuser by:

1. Going to the Web Service shell/console in Render Dashboard
2. Running:
```bash
python manage.py createsuperuser
```

Or add these environment variables and they'll be auto-created:
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=your-password
DJANGO_SUPERUSER_EMAIL=admin@example.com
```

## Post-Deployment

1. Access your app at: `https://store-management.onrender.com`
2. Admin panel: `https://store-management.onrender.com/admin`
3. Add custom domain (optional) in Render settings

## Important Paths

- **Products**: `/products/`
- **Orders**: `/orders/`
- **Customers**: `/customers/`
- **Staff**: `/staff/`
- **Admin**: `/admin/`

## Troubleshooting

### Build Failed
- Check `build.sh` is executable
- Review the build logs in Render Dashboard
- Ensure all dependencies are in `requirements.txt`

### Database Connection Error
- Verify DATABASE_URL environment variable is set
- Check database password doesn't contain special characters
- Ensure PostgreSQL database is running

### Static Files Not Loading
- WhiteNoise should handle this
- Check STATIC_URL and STATIC_ROOT in settings.py
- Run `python manage.py collectstatic` locally to test

### Admin Panel Not Loading
- Create superuser using the shell method
- Check migrations ran: `python manage.py migrate`
- Check ALLOWED_HOSTS setting

## Automatic Deploys

Render watches your GitHub repository. Every push to `main` branch will trigger a new deployment.

To disable automatic deploys:
1. Go to Web Service settings
2. Under "Auto-Deploy", select "No"

## Scaling (Paid Plans)

- Render auto-scales based on resource usage
- Upgrade from free tier to add more resources
- Enable Horizontal Scaling for multiple instances

## Monitoring

- View logs in Render Dashboard
- Set up error notifications
- Monitor database performance

## Next Steps

1. Set up a custom domain
2. Enable SSL/HTTPS (automatic)
3. Configure email notifications
4. Set up backups for your database
5. Monitor application performance

---

For more information, visit [Render Documentation](https://render.com/docs)
