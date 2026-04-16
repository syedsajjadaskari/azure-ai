# Step 9: AI Foundry Playground
# No code needed - use the web interface!

## 🌐 What is AI Foundry Playground?

A web-based interface to test Azure OpenAI models without writing code!

**Access**: https://ai.azure.com

---

## 🎯 How to Use (5 Minutes!)

### Step 1: Go to AI Foundry
```
1. Visit: https://ai.azure.com
2. Sign in with your Azure account
3. Select your subscription
4. Select your Azure OpenAI resource
```

### Step 2: Choose a Playground

**3 Main Playgrounds:**

#### 1. Chat Playground
- Test GPT-4, GPT-4o, GPT-3.5-Turbo
- Have conversations
- Try different system messages

#### 2. Completions Playground
- Text completion
- Legacy models
- Code generation

#### 3. Images Playground  
- DALL-E image generation
- Test prompts
- Download images

---

## 💬 Chat Playground (Most Used!)

### Setup:
1. Click "Playgrounds" → "Chat"
2. Select deployment (GPT-4o recommended)
3. Start chatting!

### Features:

#### System Message
```
Set AI behavior:
"You are a helpful Python tutor"
"You are a creative writer"
"You are a pirate"
```

#### Parameters
- **Temperature**: 0-2 (creativity)
  - 0 = Consistent
  - 1 = Balanced
  - 2 = Very creative
  
- **Max Response**: Token limit

- **Top P**: Nucleus sampling

- **Frequency Penalty**: Reduce repetition

- **Presence Penalty**: Encourage new topics

#### Chat Session
- Type messages
- Get instant responses
- See token usage
- Clear and restart anytime

---

## 🎨 Images Playground

### Generate Images:
1. Go to Images Playground
2. Select DALL-E deployment
3. Enter prompt: "A futuristic city at sunset"
4. Click Generate
5. Download image!

### Tips for Good Prompts:
- Be specific: "photorealistic cat" vs "cat"
- Add style: "digital art", "oil painting"
- Add details: colors, mood, setting
- Use adjectives: "vibrant", "moody", "minimalist"

### Examples:
```
Good: "A serene mountain landscape at dawn, watercolor style"
Better: "Photorealistic image of Mount Fuji at sunrise with cherry blossoms"
```

---

## ⚙️ Deployment Management

### Create Deployment:
```
1. Go to "Deployments"
2. Click "Create new deployment"
3. Select model:
   - GPT-4o (recommended)
   - GPT-4
   - GPT-3.5-Turbo
   - text-embedding-ada-002
   - dall-e-3
4. Give it a name
5. Set tokens per minute (TPM)
6. Click Create
```

### Deployment Names:
Use these names in your code:
```python
model="gpt-4o"  # Your deployment name
```

---

## 📊 View Usage & Costs

### In AI Foundry:
1. Go to "Usage"
2. See:
   - Requests per day
   - Tokens consumed
   - Cost estimates
   - Model breakdown

---

## 🛡️ Content Filtering

### Safety Settings:
1. Go to "Content filters"
2. Set levels for:
   - Hate speech
   - Violence
   - Self-harm
   - Sexual content
3. Options:
   - Low (allow most)
   - Medium (balanced)
   - High (strict)

### Test Your Filters:
- Try prompts in playground
- See what gets blocked
- Adjust settings as needed

---

## 🎯 Quick Tasks to Try

### Task 1: Simple Chat
```
Deployment: GPT-4o
System: "You are a helpful assistant"
User: "Explain quantum computing simply"
```

### Task 2: Creative Writing
```
Deployment: GPT-4o
System: "You are a creative story writer"
Temperature: 1.5
User: "Write a short story about a robot"
```

### Task 3: Code Helper
```
Deployment: GPT-4o
System: "You are a Python programming expert"
Temperature: 0.3
User: "Write a function to sort a list"
```

### Task 4: Generate Image
```
Playground: Images
Prompt: "A cozy coffee shop interior, warm lighting, plants"
Size: 1024x1024
```

---

## 💡 Pro Tips

### Tip 1: Save Your Sessions
- Use "Clear chat" to restart
- Copy good responses
- Test different parameters

### Tip 2: Compare Models
- Try same prompt with GPT-4 vs GPT-3.5
- See quality difference
- Consider cost vs performance

### Tip 3: System Messages Matter
```
Bad: "Help me"
Good: "You are an expert in Azure who explains concepts clearly"
```

### Tip 4: Use View Code
- After chatting, click "View code"
- Get Python/C#/JS code
- Copy to your project!

---

## 🔑 Get Your Code

### From Playground:
1. Have a conversation
2. Click "View code"
3. Select language (Python/C#/JS)
4. Copy the code
5. Use in your app!

**Example output:**
```python
from openai import AzureOpenAI

client = AzureOpenAI(...)
response = client.chat.completions.create(...)
```

---

## 📚 Learn More

### Tutorials in AI Foundry:
- Click "Learn" tab
- Guided tutorials
- Sample code
- Best practices

### Documentation:
- In-portal docs
- API references
- Examples

---

## ✅ Practice Checklist

Try these in AI Foundry:
- [ ] Login to AI Foundry portal
- [ ] Create a deployment
- [ ] Use Chat playground
- [ ] Change system message
- [ ] Adjust temperature
- [ ] View token usage
- [ ] Try Images playground
- [ ] Check content filters
- [ ] View code samples
- [ ] Test different models

---

## 🎉 Benefits of AI Foundry

### Why Use It?
1. ✅ No code needed to test
2. ✅ See results instantly
3. ✅ Experiment with parameters
4. ✅ Get code samples
5. ✅ Manage deployments
6. ✅ View costs
7. ✅ All in one place!

**Perfect for:**
- Testing before coding
- Demos
- Learning
- Prototyping

---

## 🚀 Next Steps

After mastering the playground:
1. Use "View code" feature
2. Copy code to your project
3. Integrate into applications
4. Build amazing AI features!

---

**AI Foundry = Fastest way to get started with Azure OpenAI!**

No installation, no setup, just start using! 🎯