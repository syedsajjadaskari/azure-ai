# 🚀 Deploy AI Chat Assistant to Azure

## Deployment Options

---

## Method 1: One-Command Deploy ⭐ (Easiest!)

```bash
chmod +x deploy.sh
./deploy.sh
```

**That's it!** Wait 5 minutes and your app is live!

The script automatically:
- Creates resource group
- Creates App Service plan
- Creates web app
- Configures settings
- Deploys your code

---

## Method 2: Azure CLI (Step-by-Step)

### Prerequisites
- Azure account
- Azure CLI installed
- Azure OpenAI resource already created

### Step 1: Login
```bash
az login
```

### Step 2: Create Resource Group
```bash
az group create \
  --name ai-chat-rg \
  --location eastus
```

### Step 3: Create App Service Plan
```bash
az appservice plan create \
  --name ai-chat-plan \
  --resource-group ai-chat-rg \
  --sku B1 \
  --is-linux
```

### Step 4: Create Web App
```bash
az webapp create \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg \
  --plan ai-chat-plan \
  --runtime "PYTHON:3.11"
```

### Step 5: Configure Startup
```bash
az webapp config set \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg \
  --startup-file "bash startup.sh"
```

### Step 6: Set Port
```bash
az webapp config appsettings set \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg \
  --settings WEBSITES_PORT=8000
```

### Step 7: Deploy Code
```bash
zip -r app.zip .
az webapp deployment source config-zip \
  --resource-group ai-chat-rg \
  --name my-ai-chat-app \
  --src app.zip
```

### Step 8: Visit Your App
```
https://my-ai-chat-app.azurewebsites.net
```

---

## Method 3: Azure Portal (Click-Based)

### Step 1: Create Web App
1. Go to portal.azure.com
2. Click "Create a resource"
3. Search "Web App"
4. Click Create

### Step 2: Configure
- **Resource Group**: Create new `ai-chat-rg`
- **Name**: Choose unique name (e.g., `my-ai-chat-123`)
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
3. Add setting: `WEBSITES_PORT=8000`
4. Save

---

## 🔒 Production Setup (Recommended)

### Store Credentials Securely

Instead of entering in the app, use environment variables:

### Step 1: Add App Settings
```bash
az webapp config appsettings set \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg \
  --settings \
    AZURE_OPENAI_KEY="your-key" \
    AZURE_OPENAI_ENDPOINT="your-endpoint" \
    AZURE_OPENAI_DEPLOYMENT="gpt-4o"
```

### Step 2: Update app.py
```python
import os

# Get from environment variables
api_key = os.getenv("AZURE_OPENAI_KEY", "")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

# Hide input fields in production
if api_key and endpoint:
    st.sidebar.success("✅ Using configured credentials")
else:
    # Show input fields
    api_key = st.sidebar.text_input("API Key", type="password")
    endpoint = st.sidebar.text_input("Endpoint")
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
  --resource-group ai-chat-rg \
  --name my-ai-chat-app \
  --src app.zip
```

---

## 📊 Monitor Your App

### View Logs
```bash
az webapp log tail \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg
```

### Download Logs
```bash
az webapp log download \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg
```

### Enable Application Insights
1. Go to your Web App in portal
2. Click "Application Insights"
3. Click "Turn on"
4. Create new resource
5. Apply

---

## 🐛 Troubleshooting

### App Not Starting

**Check Logs:**
```bash
az webapp log tail \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg
```

**Common Issues:**
1. Startup command not set
2. Port not configured
3. Requirements not installed

**Fix:**
```bash
# Set startup
az webapp config set \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg \
  --startup-file "bash startup.sh"

# Set port
az webapp config appsettings set \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg \
  --settings WEBSITES_PORT=8000
```

### App is Slow

**Solutions:**
1. **Scale Up**: Upgrade to better tier
   ```bash
   az appservice plan update \
     --name ai-chat-plan \
     --resource-group ai-chat-rg \
     --sku P1V2
   ```

2. **Enable Always On**:
   - Portal → Configuration → General settings
   - Turn on "Always On"

3. **Scale Out**: Add more instances
   ```bash
   az appservice plan update \
     --name ai-chat-plan \
     --resource-group ai-chat-rg \
     --number-of-workers 3
   ```

### Deployment Failed

**Check:**
- All files included in zip
- requirements.txt correct
- startup.sh executable
- No syntax errors in app.py

**Retry:**
```bash
rm app.zip
zip -r app.zip .
az webapp deployment source config-zip \
  --resource-group ai-chat-rg \
  --name my-ai-chat-app \
  --src app.zip
```

---

## 💰 Pricing

### Free Tier (F1)
- $0/month
- 60 CPU minutes/day
- Sleeps after idle
- Good for testing

### Basic Tier (B1) - Recommended
- ~$13/month
- Always on
- Better performance
- Custom domain support

### OpenAI API
- GPT-4o: $5 / 1M tokens
- Average chat: 500 tokens
- 1000 chats: ~$2.50

**Total**: ~$15-16/month for production

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
- Or upload your own

---

## 📈 Scale Your App

### Vertical Scaling (More Power)
```bash
# Upgrade to Premium
az appservice plan update \
  --name ai-chat-plan \
  --resource-group ai-chat-rg \
  --sku P1V2
```

### Horizontal Scaling (More Instances)
```bash
# Add more workers
az appservice plan update \
  --name ai-chat-plan \
  --resource-group ai-chat-rg \
  --number-of-workers 3
```

### Auto-Scaling
1. Portal → Scale out (App Service plan)
2. Enable autoscale
3. Set rules based on:
   - CPU usage
   - Memory usage
   - HTTP queue length

---

## 🔐 Security Best Practices

### 1. Use Managed Identity
```bash
# Enable managed identity
az webapp identity assign \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg

# Grant access to Azure OpenAI
az role assignment create \
  --assignee <managed-identity-id> \
  --role "Cognitive Services OpenAI User" \
  --scope <azure-openai-resource-id>
```

### 2. Enable HTTPS Only
```bash
az webapp update \
  --name my-ai-chat-app \
  --resource-group ai-chat-rg \
  --https-only true
```

### 3. Restrict Access
- Use VNET integration
- Configure firewall rules
- Enable authentication

### 4. Protect API Keys
- Use Key Vault for secrets
- Rotate keys regularly
- Never commit keys to git

---

## ✅ Pre-Deployment Checklist

- [ ] Tested locally and works
- [ ] Have Azure account
- [ ] Have Azure OpenAI resource
- [ ] Deployed GPT-4o model
- [ ] Azure CLI installed (for CLI method)
- [ ] All files ready
- [ ] requirements.txt correct
- [ ] startup.sh executable

---

## 🎯 Post-Deployment

### 1. Test Your App
```
https://YOUR-APP-NAME.azurewebsites.net
```

### 2. Monitor Usage
- Check Application Insights
- Monitor costs in Azure portal
- Review logs regularly

### 3. Share
- Share URL with team
- Add to portfolio
- Demo to stakeholders

### 4. Maintain
- Update dependencies
- Monitor performance
- Scale as needed

---

## 📊 Monitoring Dashboard

### Key Metrics to Watch
- **Response Time**: Should be < 5 seconds
- **Error Rate**: Should be < 1%
- **CPU Usage**: Should be < 70%
- **Memory**: Should be < 80%

### Set Up Alerts
1. Portal → Alerts
2. Create alert rule
3. Set conditions:
   - CPU > 80%
   - Memory > 80%
   - 5xx errors > 10

---

## 🚀 Advanced Features

### Add CI/CD
1. Connect GitHub repository
2. Enable GitHub Actions
3. Auto-deploy on push

### Add Redis Cache
- Cache responses
- Improve performance
- Reduce API calls

### Add Database
- Store conversations
- User management
- Analytics

---

## ✅ Deployment Success

Your AI Chat Assistant should now be:
- ✅ Live on Azure
- ✅ Accessible via HTTPS
- ✅ Running 24/7
- ✅ Scalable
- ✅ Monitored

**Next**: Share your app and start building more features!

---

**Questions? Check README.md or QUICK_START.md**