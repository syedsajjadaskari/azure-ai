# Deploy Streamlit App to Azure - Simple Guide

## 🚀 Quick Deploy (3 Methods)

---

## Method 1: Azure App Service (Recommended - Easiest!)

### Step 1: Prepare Your Files
Make sure you have these files:
```
streamlit_app/
├── app.py
├── requirements.txt
├── startup.sh
└── .streamlit/
    └── config.toml
```

### Step 2: Deploy via Azure Portal

#### A. Create App Service
1. Go to **portal.azure.com**
2. Click **"Create a resource"**
3. Search for **"Web App"**
4. Click **Create**

#### B. Fill Basic Settings
- **Subscription**: Choose your subscription
- **Resource Group**: Create new (e.g., `streamlit-rg`)
- **Name**: Choose unique name (e.g., `my-vision-app`)
- **Publish**: **Code**
- **Runtime stack**: **Python 3.11**
- **Region**: Choose closest to you
- **Pricing**: **Free F1** (for testing) or **Basic B1**

#### C. Click "Review + Create" → "Create"
Wait 1-2 minutes for deployment

#### D. Upload Your Code
1. Go to your App Service
2. Click **"Deployment Center"** (left menu)
3. Choose **"Local Git"** or **"GitHub"**

**Option A: Local Git**
```bash
cd streamlit_app
git init
git add .
git commit -m "Initial commit"
git remote add azure <YOUR_GIT_URL>
git push azure master
```

**Option B: GitHub** (Simpler!)
1. Push code to your GitHub repo
2. In Deployment Center, select GitHub
3. Authorize and select your repo
4. Click Save

#### E. Configure Startup Command
1. Go to **"Configuration"** (left menu)
2. Click **"General settings"**
3. Set **Startup Command**: `bash startup.sh`
4. Click **Save**

#### F. Set Environment (Optional)
1. Go to **"Configuration"** → **"Application settings"**
2. Add settings:
   - `SCM_DO_BUILD_DURING_DEPLOYMENT` = `true`
   - `WEBSITES_PORT` = `8000`
3. Click **Save**

### Step 3: Access Your App
- URL: `https://YOUR-APP-NAME.azurewebsites.net`
- Wait 2-3 minutes for first startup

---

## Method 2: Azure CLI (Fast!)

### Install Azure CLI
```bash
# Install (if not already)
# Mac: brew install azure-cli
# Windows: Download from microsoft.com
```

### Deploy Commands
```bash
# Login
az login

# Create resource group
az group create --name streamlit-rg --location eastus

# Create App Service Plan
az appservice plan create \
  --name streamlit-plan \
  --resource-group streamlit-rg \
  --sku B1 \
  --is-linux

# Create Web App
az webapp create \
  --name my-vision-app \
  --resource-group streamlit-rg \
  --plan streamlit-plan \
  --runtime "PYTHON:3.11"

# Configure startup
az webapp config set \
  --name my-vision-app \
  --resource-group streamlit-rg \
  --startup-file "bash startup.sh"

# Deploy code (from streamlit_app folder)
cd streamlit_app
zip -r app.zip .
az webapp deployment source config-zip \
  --resource-group streamlit-rg \
  --name my-vision-app \
  --src app.zip

# Done! Visit: https://my-vision-app.azurewebsites.net
```

---

## Method 3: Docker Container (Advanced)

### Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
```

### Deploy
```bash
# Build
docker build -t vision-app .

az provider register --namespace Microsoft.ContainerRegistry

# Push to Azure Container Registry
az acr create --resource-group streamlit-rg --name myvisionregistry --sku Basic
az acr login --name myvisionregistry
docker tag vision-app myvisionregistry.azurecr.io/vision-app:v1
docker push myvisionregistry.azurecr.io/vision-app:v1

# Create Web App
az webapp create \
  --resource-group streamlit-rg \
  --plan streamlit-plan \
  --name my-vision-app \
  --deployment-container-image-name myvisionregistry.azurecr.io/vision-app:v1
```

---

## 🧪 Test Locally First

Before deploying, test locally:

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

Open: http://localhost:8501

---

## 🔧 Troubleshooting

### App Won't Start
- Check logs: `az webapp log tail --name my-vision-app --resource-group streamlit-rg`
- Verify startup command: `bash startup.sh`
- Check Python version: Must be 3.11

### Port Issues
- Make sure WEBSITES_PORT = 8000 in app settings
- Streamlit config has `port = 8000`

### Deployment Failed
- Check requirements.txt is present
- Make sure all files are committed (Git)
- Verify Python runtime is set

### App is Slow
- Upgrade from Free tier to Basic B1
- Cold start takes 30-60 seconds (first request)

---

## 💰 Pricing

**Free Tier (F1)**:
- ✅ Good for testing
- ✅ 60 CPU minutes/day
- ⚠️ Goes to sleep after 20 min idle
- ⚠️ Slower performance

**Basic Tier (B1)** - ~$13/month:
- ✅ Always on
- ✅ Better performance
- ✅ Custom domain support
- ✅ SSL certificate

**Recommended**: Start with Free, upgrade to Basic for production

---

## 🔒 Security Best Practices

### Don't Hardcode Credentials!

**Bad** ❌:
```python
endpoint = "https://myendpoint.com"
api_key = "abc123"
```

**Good** ✅:
Use Azure App Settings:
1. Go to Configuration → Application settings
2. Add:
   - `AZURE_VISION_ENDPOINT` = your endpoint
   - `AZURE_VISION_KEY` = your key
3. Update app.py:
```python
import os
endpoint = os.getenv("AZURE_VISION_ENDPOINT", "")
api_key = os.getenv("AZURE_VISION_KEY", "")
```

---

## 📊 Monitoring

### View Logs
```bash
# Real-time logs
az webapp log tail --name my-vision-app --resource-group streamlit-rg

# Download logs
az webapp log download --name my-vision-app --resource-group streamlit-rg
```

### App Insights (Advanced)
1. Enable Application Insights in Azure Portal
2. Monitor performance, errors, usage

---

## 🔄 Update Your App

### Via Git
```bash
git add .
git commit -m "Update"
git push azure master
```

### Via CLI
```bash
zip -r app.zip .
az webapp deployment source config-zip \
  --resource-group streamlit-rg \
  --name my-vision-app \
  --src app.zip
```

---

## 🌐 Custom Domain (Optional)

1. Buy domain (GoDaddy, Namecheap, etc.)
2. In App Service → Custom domains
3. Add domain
4. Update DNS records
5. Add SSL certificate (free with App Service)

---

## 📱 App Features

Your deployed app will have:
- ✅ Image upload
- ✅ AI caption generation
- ✅ Auto-tagging
- ✅ Object detection
- ✅ Beautiful UI
- ✅ Responsive design

---

## 🎯 Next Steps

After deployment:
1. Share your app URL
2. Add more Azure Vision features
3. Integrate other Azure AI services
4. Add user authentication
5. Save analysis history

---

## 🆘 Need Help?

**Azure Portal**: portal.azure.com → Your app → Diagnose and solve problems

**Logs**: Configuration → App Service logs → Enable

**Support**: Create support ticket in Azure Portal

---

## ✅ Deployment Checklist

- [ ] Created Azure account
- [ ] Created Computer Vision resource
- [ ] Tested app locally
- [ ] Created App Service
- [ ] Deployed code
- [ ] Configured startup command
- [ ] Set port to 8000
- [ ] Tested live URL
- [ ] Added environment variables (optional)
- [ ] Configured custom domain (optional)

---

**Your app is live! 🎉**

Share it: `https://YOUR-APP-NAME.azurewebsites.net`