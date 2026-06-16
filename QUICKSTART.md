# Quick Start Guide - Customer Support Chatbot

## 🚀 Get Started in 5 Minutes

### Option 1: Run with Python (Recommended)

**Step 1: Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

**Step 2: Start the Server**
```bash
python app.py
```

Expected output:
```
🚀 Starting Customer Support Chatbot API Server
📝 Patterns: ReAct + Chain of Thought + Self-Reflection
🌐 Running on http://localhost:5000
```

**Step 3: Open the Website**
- Open `frontend/templates/chatbot.html` in your web browser
- Or navigate to: `http://localhost:5000` (if serving HTML through Flask)

**Step 4: Start Chatting!**
- Ask questions about login, billing, shipping, or technical issues
- Watch the AI reason through problems step-by-step

---

### Option 2: Jupyter Notebook (Interactive Learning)

**Step 1: Install Jupyter**
```bash
pip install jupyter
```

**Step 2: Start Jupyter**
```bash
cd notebooks
jupyter notebook
```

**Step 3: Open the notebook**
- Click on `customer_support_chatbot.ipynb`
- Run cells to see live demonstrations
- Modify code and experiment

---

## 📝 Test the Chatbot

### Using the Web Interface
1. Open `frontend/templates/chatbot.html`
2. Type a question:
   - "I can't log into my account"
   - "I was charged twice"
   - "Where is my order?"
   - "The app keeps crashing"

### Using the API (curl)

**Simple Query**
```bash
curl -X POST http://localhost:5000/chat/quick \
  -H "Content-Type: application/json" \
  -d '{"query": "I forgot my password"}'
```

**Full Response with Reasoning**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "I was charged twice for my order"}'
```

**Get Statistics**
```bash
curl http://localhost:5000/summary
```

**View Patterns**
```bash
curl http://localhost:5000/patterns
```

---

## 🎯 Key Features to Explore

### 1. Try Different Issue Types
- **Login Issue**: "Can't access my account"
- **Billing Issue**: "Duplicate charge on my card"
- **Shipping Issue**: "Package tracking not working"
- **Technical Issue**: "App crashes on startup"

### 2. Observe the Reasoning
- Watch how the chatbot thinks through problems
- See the step-by-step Chain of Thought
- Notice the self-review quality score

### 3. Check Performance
- Get conversation statistics: `GET /summary`
- View conversation history: `GET /history`
- Monitor quality scores

---

## 🧠 Understanding the AI Patterns

### ReAct Pattern
The chatbot **Reasons** about your problem, then takes **Action**:
1. **Think**: "What is this customer asking?"
2. **Observe**: "What information do we have?"
3. **Act**: "What should we do?"

### Chain of Thought
Problems are solved **step-by-step**:
1. Understand the issue
2. Analyze what might be wrong
3. Consider possible solutions
4. Decide on best approach
5. Explain clearly

### Self-Reflection
Every response is **reviewed for quality**:
- Is it accurate?
- Is it friendly?
- Is it clear?
- Did we address everything?

---

## 📊 Testing Scenarios

### Scenario 1: Simple Login Issue
**Your message**: "I forgot my password"
**What happens**:
1. Chatbot recognizes "login" category
2. Uses ReAct to think about password reset
3. Uses CoT to create step-by-step instructions
4. Self-review checks for quality
5. Delivers friendly, helpful response

### Scenario 2: Complex Billing Issue
**Your message**: "I see two charges on my card. The order is showing in my account but I was billed twice"
**What happens**:
1. Chatbot detects "billing" category
2. ReAct identifies duplicate charge concern
3. CoT breaks down: verify → process refund → timeline
4. Self-review ensures empathetic tone
5. Response includes reassurance + action steps

### Scenario 3: Escalation Needed
**Your message**: "Something weird is happening that I can't explain"
**What happens**:
1. Chatbot recognizes "general" category
2. ReAct observes: unclear issue, needs more info
3. CoT suggests: ask clarifying questions
4. Response offers to escalate if needed

---

## 🔧 Customization

### Add Your Own Issue Category

1. Open `backend/chatbot_engine.py`
2. Find `_build_knowledge_base()` method
3. Add a new category:

```python
"returns": {
    "keywords": ["return", "send back", "refund", "wrong item"],
    "solutions": [
        "Check return policy",
        "Initiate return request",
        "Print shipping label",
        "Ship back within 30 days"
    ],
    "priority": "high"
}
```

4. Restart the server
5. Test with: "I want to return my order"

### Modify Response Templates

In `backend/chatbot_engine.py`, edit `_build_customer_response()`:

```python
# Add emoji or customize greeting
greeting = "👋 Hi there! Thanks for contacting us."

# Change the numbering format
response += f"• {solution}\n"  # Instead of **Step {i}:**
```

---

## 📈 Next Steps

1. **Explore the Jupyter Notebook**
   - See detailed examples of each AI pattern
   - Run live demonstrations
   - Experiment with different prompts

2. **Integrate with OpenAI API**
   - Replace mock responses with real GPT models
   - Uncomment OpenAI imports in `chatbot_engine.py`
   - Add your API key

3. **Deploy to Production**
   - Use Gunicorn instead of Flask dev server
   - Add database for conversation history
   - Implement authentication
   - Set up logging and monitoring

4. **Analyze Performance**
   - Track quality scores
   - Monitor response times
   - Collect customer feedback
   - Iteratively improve

---

## ❓ Troubleshooting

### Port Already in Use
```bash
# Change port in backend/app.py
app.run(debug=True, host='0.0.0.0', port=5001)  # Use 5001 instead
```

### API Not Responding
```bash
# Check if server is running
curl http://localhost:5000/health

# Restart server
# Press Ctrl+C then run: python app.py
```

### HTML Won't Connect to API
- Check `API_BASE_URL` in `chatbot.html`
- Ensure backend is running on same port
- Check browser console for CORS errors

### Python Dependencies Error
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or create fresh environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🎓 Learning Path

1. **Day 1**: Run the chatbot, explore web interface
2. **Day 2**: Test API endpoints, read the documentation
3. **Day 3**: Study the Jupyter notebook in detail
4. **Day 4**: Examine source code in `backend/chatbot_engine.py`
5. **Day 5**: Customize categories and responses
6. **Day 6**: Integrate with OpenAI API
7. **Day 7**: Deploy and monitor

---

## 📞 Support

- See `README.md` for detailed documentation
- Check `notebooks/customer_support_chatbot.ipynb` for interactive examples
- Review inline code comments in Python files
- Test API endpoints with provided curl examples

---

**Happy Exploring! 🚀**

Questions? Run the notebook and experiment!
