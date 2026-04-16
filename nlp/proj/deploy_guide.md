# Deploy Text Analytics Dashboard to Azure

## 🚀 Deployment Options

---

## Method 1: One-Command Deploy ⭐ (Easiest!)

```bash
chmod +x deploy.sh
./deploy.sh
```

That's it! Wait 5 minutes and your app is live!

---

## Method 2: Azure CLI (Step-by-Step)

### Prerequisites
- Azure account
- Azure CLI installed
- Resource already created (Language service)

### Step 1: Login
```bash
az login
```

### Step 2: Create Resource Group
```bash
az group create --name text-analytics-rg --location eastus
```

### Step 3: Create App Service Plan
```bash
az appservice plan create \
  --name text-analytics-plan \
  --resource-group text-analytics-rg \
  --sku B1 \
  --is-linux
```

### Step 4: Create Web App
```bash
az webapp create \
  --name my-text-analytics \
  --resource-group text-analytics-rg \
  --plan text-analytics-plan \
  --runtime "PYTHON:3.11"
```

### Step 5: Configure Startup
```bash
az webapp config set \
  --name my-text-analytics \
  --resource-group text-analytics-rg \
  --startup-file "bash startup.sh"
```

### Step 6: Set Port
```bash
az webapp config appsettings set \
  --name my-text-analytics \
  --resource-group text-analytics-rg \
  --settings WEBSITES_PORT=8000
```

### Step 7: Deploy Code
```bash
zip -r app.zip .
az webapp deployment source config-zip \
  --resource-group text-analytics-rg \
  --name my-text-analytics \
  --src app.zip
```

### Step 8: Visit Your App
```
https://my-text-analytics.azurewebsites.net
```

---

## Method 3: Azure Portal (Click-Based)

### Step 1: Create Web App
1. Go to portal.azure.com
2. Click "Create a resource"
3. Search for "Web App"
4. Click Create

### Step 2: Configure
- **Subscription**: Choose yours
- **Resource Group**: Create new `text-analytics-rg`
- **Name**: Choose unique name
- **Publish**: Code
- **Runtime**: Python 3.11
- **Region**: East US
- **Pricing**: Basic B1

### Step 3: Review + Create
Click "Review + Create" → "Create"

### Step 4: Upload Code
1. Go to your Web App
2. Click "Deployment Center"
3. Choose "Local Git" or "GitHub"
4. Push your code

### Step 5: Configure
1. Go to "Configuration"
2. Set startup command: `bash startup.sh`
3. Add application setting: `WEBSITES_PORT=8000`
4. Save

---

## 🔒 Environment Variables (Production)

Instead of entering credentials in the app, use environment variables:

### Add to Azure App Service
1. Go to Configuration → Application settings
2. Add:
   - Name: `AZURE_LANGUAGE_ENDPOINT`
   - Value: `https://your-resource.cognitiveservices.azure.com/`
3. Add:
   - Name: `AZURE_LANGUAGE_KEY`
   - Value: Your API key
4. Save

### Update app.py
```python
import os

# In sidebar section, replace:
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT", "")
api_key = os.getenv("AZURE_LANGUAGE_KEY", "")

# Remove text_input for credentials
if not endpoint or not api_key:
    st.sidebar.warning("⚠️ Credentials not configured")
```

---

## 🔄 Update Your Deployed App

### Via Git
```bash
git add .
git commit -m "Update app"
git push azure master
```

### Via ZIP
```bash
zip -r app.zip .
az webapp deployment source config-zip \
  --resource-group text-analytics-rg \
  --name my-text-analytics \
  --src app.zip
```

---

## 📊 Monitor Your App

### View Logs
```bash
az webapp log tail \
  --name my-text-analytics \
  --resource-group text-analytics-rg
```

### Download Logs
```bash
az webapp log download \
  --name my-text-analytics \
  --resource-group text-analytics-rg
```

### Enable Application Insights
1. Go to your Web App
2. Click "Application Insights"
3. Click "Turn on"
4. Create new resource
5. Apply

---

## 🐛 Troubleshooting

### App Not Starting
**Check Logs:**
```bash
az webapp log tail --name my-text-analytics --resource-group text-analytics-rg
```

**Common Issues:**
- Startup command not set
- Port not configured
- Python version mismatch

### Fix Startup Issues
```bash
# Set startup command
az webapp config set \
  --name my-text-analytics \
  --resource-group text-analytics-rg \
  --startup-file "bash startup.sh"

# Set port
az webapp config appsettings set \
  --name my-text-analytics \
  --resource-group text-analytics-rg \
  --settings WEBSITES_PORT=8000
```

### App is Slow
- Upgrade from Free to Basic tier
- Enable "Always On" in Configuration
- Scale up to more instances

### Deployment Failed
- Check requirements.txt exists
- Verify all files are included
- Check for syntax errors in app.py

---

## 💰 Pricing

### Free Tier (F1)
- $0/month
- 60 CPU minutes/day
- Goes to sleep after 20 min idle
- Good for testing

### Basic Tier (B1) - Recommended
- ~$13/month
- Always on
- Better performance
- Custom domain support

### Language API
- Free: 5,000 transactions/month
- Standard: $1-2 per 1,000 transactions

---

## 🌐 Custom Domain (Optional)

### Step 1: Buy Domain
Use GoDaddy, Namecheap, etc.

### Step 2: Add to Azure
1. Go to Web App → Custom domains
2. Click "Add custom domain"
3. Enter your domain
4. Add DNS records as shown

### Step 3: SSL Certificate
- Azure provides free SSL
- Or upload your own certificate

---

## 📈 Scale Your App

### Vertical Scaling (More Power)
```bash
az appservice plan update \
  --name text-analytics-plan \
  --resource-group text-analytics-rg \
  --sku P1V2
```

### Horizontal Scaling (More Instances)
```bash
az appservice plan update \
  --name text-analytics-plan \
  --resource-group text-analytics-rg \
  --number-of-workers 3
```

---

## 🔐 Security Best Practices

### 1. Use Managed Identity
- Enable managed identity for Web App
- Grant access to Language resource
- Remove API keys from code

### 2. Network Security
- Enable VNET integration
- Configure firewall rules
- Use private endpoints

### 3. Authentication
- Enable Azure AD authentication
- Restrict access to specific users
- Use App Service authentication

---

## ✅ Pre-Deployment Checklist

- [ ] Tested app locally
- [ ] Have Azure account
- [ ] Created Language resource
- [ ] Have endpoint and key
- [ ] Installed Azure CLI
- [ ] All files in place
- [ ] requirements.txt correct
- [ ] startup.sh executable

---

## 🎯 Post-Deployment

1. Visit your app URL
2. Test all features
3. Share with team/stakeholders
4. Monitor usage and costs
5. Gather feedback
6. Iterate and improve!

---

**Your Text Analytics Dashboard is ready to deploy! 🚀**