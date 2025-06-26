# 🚀 Render Deployment Guide for Schedule API

## Prerequisites
- ✅ GitHub repository with your code
- ✅ Render account (free tier available)

## Step-by-Step Deployment Guide

### Step 1: Prepare Your Repository
Make sure your GitHub repository contains these files:
- `main.py` - Main FastAPI application
- `requirements.txt` - Python dependencies
- `config.py` - Configuration management
- `render.yaml` - Render configuration (optional)
- `Procfile` - Process file for Render
- `runtime.txt` - Python version specification

### Step 2: Access Render Dashboard
1. Go to [render.com](https://render.com)
2. Sign up/Login with your GitHub account
3. Click "New +" button
4. Select "Web Service"

### Step 3: Connect Your Repository
1. **Connect Repository**: Click "Connect a repository"
2. **Select Repository**: Choose your GitHub repository
3. **Authorize**: Grant Render access to your repository

### Step 4: Configure Your Web Service

#### Basic Settings:
- **Name**: `schedule-api` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)

#### Build & Deploy Settings:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

#### Environment Variables (Optional):
Add these if you need to customize:
- `EXTERNAL_API_URL`: `https://test.lumeneo.ai/services/appointment/api/appointments`
- `REQUEST_TIMEOUT`: `30`
- `LOG_LEVEL`: `INFO`

### Step 5: Deploy
1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Install dependencies
   - Build your application
   - Deploy it

### Step 6: Monitor Deployment
1. Watch the build logs for any errors
2. Wait for "Deploy successful" message
3. Your API will be available at: `https://your-app-name.onrender.com`

## 🧪 Testing Your Deployed API

### Test the Health Endpoint:
```bash
curl https://your-app-name.onrender.com/health
```

### Test the Main Endpoint:
```bash
curl -X POST "https://your-app-name.onrender.com/restructure-appointment" \
     -H "Content-Type: application/json" \
     -d '{
       "site_id": 10,
       "title": "Car Repair and Wash Appointment",
       "start_time": "2025-06-23T10:00:00Z",
       "end_time": "2025-06-23T11:00:00Z",
       "license_plate_1": "MH 12 DF 8096",
       "description": "Car Repair and Wash Appointment for MH 12 DF 8096",
       "customer_id": 1,
       "customer_name": "Parish",
       "customer_email": "parish@lumeneo.ai",
       "customer_mobile": "+918920626776",
       "work_order_id": 1
     }'
```

### Access API Documentation:
- **Swagger UI**: `https://your-app-name.onrender.com/docs`
- **ReDoc**: `https://your-app-name.onrender.com/redoc`

## 🔧 Important Notes

### Free Tier Limitations:
- **Sleep after inactivity**: Your app will sleep after 15 minutes of inactivity
- **Cold start**: First request after sleep may take 30-60 seconds
- **Monthly hours**: Limited to 750 hours per month

### Environment Variables:
- `PORT`: Automatically set by Render (don't change)
- `EXTERNAL_API_URL`: Your external API endpoint
- `REQUEST_TIMEOUT`: HTTP request timeout in seconds

### Monitoring:
- **Logs**: Available in Render dashboard
- **Metrics**: Basic metrics provided
- **Health Checks**: Automatic health monitoring

## 🚨 Troubleshooting

### Common Issues:

1. **Build Fails**:
   - Check `requirements.txt` syntax
   - Verify Python version in `runtime.txt`
   - Check build logs for specific errors

2. **App Won't Start**:
   - Verify start command in Procfile
   - Check if port is correctly set to `$PORT`
   - Review application logs

3. **External API Errors**:
   - Verify `EXTERNAL_API_URL` is correct
   - Check if external API is accessible
   - Review timeout settings

### Getting Help:
- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Community Forum**: [community.render.com](https://community.render.com)
- **Support**: Available in Render dashboard

## 🎯 Success Checklist

- [ ] Repository connected to Render
- [ ] Build completed successfully
- [ ] Application deployed and running
- [ ] Health endpoint responding
- [ ] Main API endpoint working
- [ ] External API integration functional
- [ ] Documentation accessible

## 📞 Your API URLs

Once deployed, your API will be available at:
- **Base URL**: `https://your-app-name.onrender.com`
- **Health Check**: `https://your-app-name.onrender.com/health`
- **API Docs**: `https://your-app-name.onrender.com/docs`
- **Main Endpoint**: `https://your-app-name.onrender.com/restructure-appointment`

Replace `your-app-name` with the actual name you chose during deployment. 