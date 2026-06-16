# System Architecture & Workflow

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER                           │
├─────────────────────────────────────────────────────────────┤
│  chatbot.html (JavaScript + CSS)                            │
│  ├── User Interface                                          │
│  ├── Message Display                                         │
│  ├── API Communication                                       │
│  └── Offline Fallback Responses                              │
└────────────────┬────────────────────────────────────────────┘
                 │ HTTP/CORS
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                    API LAYER (Flask)                        │
├─────────────────────────────────────────────────────────────┤
│  app.py - REST Endpoints                                    │
│  ├── POST /chat                  (Full response + reasoning) │
│  ├── POST /chat/quick            (Response only)             │
│  ├── GET /summary                (Statistics)                │
│  ├── GET /patterns               (AI patterns info)          │
│  ├── GET /categories             (Issue categories)          │
│  ├── GET /history                (Conversations)             │
│  └── GET /health                 (Health check)              │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                 BUSINESS LOGIC LAYER                        │
├─────────────────────────────────────────────────────────────┤
│  chatbot_engine.py - Core Algorithms                        │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ CustomerSupportChatbot                                 │ │
│  │ ├── _identify_category()        [Keyword matching]     │ │
│  │ ├── _apply_react_reasoning()    [ReAct pattern]        │ │
│  │ ├── _apply_cot_reasoning()      [CoT pattern]          │ │
│  │ ├── _build_customer_response()  [Response generation]  │ │
│  │ └── generate_response()         [Main orchestrator]    │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ SelfReflectingAgent                                    │ │
│  │ ├── review_response()           [Quality evaluation]   │ │
│  │ ├── _check_for_issues()         [Issue detection]      │ │
│  │ ├── _calculate_quality_score()  [Scoring logic]        │ │
│  │ └── _suggest_improvements()     [Improvement ideas]    │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Knowledge Base                                         │ │
│  │ ├── Login Issues                                       │ │
│  │ ├── Billing Issues                                     │ │
│  │ ├── Shipping Issues                                    │ │
│  │ ├── Technical Issues                                   │ │
│  │ └── Account Issues                                     │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 📊 Data Flow Diagram

```
┌──────────────────────┐
│  Customer Query      │
│  "I forgot my        │
│   password"          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 1. IDENTIFICATION    │
│ Keyword Matching     │
│ Category: "login"    │
│ Confidence: 5/5      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 2. ReAct Reasoning   │
│ - Thought            │
│ - Observation        │
│ - Action             │
│ - Reasoning          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 3. CoT Reasoning     │
│ - Step-by-step       │
│ - Sequential logic   │
│ - Clear structure    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 4. Response Gen      │
│ - Friendly greeting  │
│ - Numbered steps     │
│ - Actionable advice  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 5. Self-Review       │
│ - Accuracy check     │
│ - Tone verification  │
│ - Clarity review     │
│ - Quality score      │
└──────────┬───────────┘
           │
      ┌────┴────┐
      ▼         ▼
  APPROVED   REVISE
      │         │
      │         ▼
      │    ┌─────────────┐
      │    │ Improve &   │
      │    │ Re-review   │
      │    └──────┬──────┘
      │           │
      └─────┬─────┘
            ▼
    ┌──────────────────┐
    │ Send Response to │
    │ Customer         │
    └──────────────────┘
```

## 🔄 Detailed Processing Workflow

### Phase 1: Issue Identification

```
Input: Customer Query
  ↓
Parse Query
  ↓
Extract Keywords
  ↓
Score Against Categories:
  - login:      5 matches ✓ WINNER
  - billing:    0 matches
  - shipping:   0 matches
  - technical:  0 matches
  ↓
Output: Category = "login", Confidence = 5/5
```

### Phase 2: ReAct Pattern Application

```
Input: Query + Category + Knowledge Base
  ↓
THINK PHASE:
  "Customer needs password recovery help"
  ↓
OBSERVE PHASE:
  - Common login keywords: login, password, account, access, sign in
  - Available solutions: 5 different troubleshooting steps
  - Customer profile: Standard user with login issue
  ↓
ACT PHASE:
  "Provide step-by-step password reset guide"
  ↓
REASON PHASE:
  "Password reset is #1 solution for login issues
   This approach maximizes success rate"
  ↓
Output: Clear action plan
```

### Phase 3: Chain of Thought Application

```
Input: Action Plan + Solutions
  ↓
STEP 1 - UNDERSTAND:
  "Customer is locked out of account"
  ↓
STEP 2 - ANALYZE:
  "Root causes: forgot password, account lock,
   browser cache, wrong email"
  ↓
STEP 3 - CONSIDER:
  "Possible solutions: password reset,
   cache clear, incognito mode, support contact"
  ↓
STEP 4 - REASON:
  "Optimal sequence: Start with most likely solutions,
   escalate to support if needed"
  ↓
STEP 5 - COMMUNICATE:
  "Format as numbered steps for clarity"
  ↓
Output: Structured solution steps
```

### Phase 4: Response Generation

```
Input: Reasoning + Solutions
  ↓
CREATE GREETING:
  "Hi there! 👋 Thank you for reaching out."
  + "I can help with your login issue."
  ↓
ADD SOLUTIONS:
  "Here's what I recommend:"
  "**Step 1:** Verify email address..."
  "**Step 2:** Click 'Forgot Password'..."
  ... (5 steps total)
  ↓
ADD CLOSING:
  "✨ If these steps don't resolve it,
   I'm here to help further! 😊"
  ↓
Output: Customer-friendly response
```

### Phase 5: Self-Review & Improvement

```
Input: Generated Response
  ↓
ACCURACY CHECK:
  ✓ Information correct
  ✓ Solutions are verified
  ✓ No false claims
  ↓
TONE CHECK:
  ✓ Friendly language
  ✓ Empathetic approach
  ✓ Professional tone
  ↓
CLARITY CHECK:
  ✓ Instructions clear
  ✓ Steps numbered
  ✓ Easy to follow
  ↓
COMPLETENESS CHECK:
  ✓ Addresses all concerns
  ✓ Provides alternatives
  ✓ Offers next steps
  ↓
SCORING:
  Issues Found: 0
  Quality Score: 10/10
  Verdict: APPROVED ✓
  ↓
Output: Ready to send
```

## 📈 Performance Optimization

### Query Processing Time
```
Typical Response Time Breakdown:
├── Issue Identification:    10ms
├── ReAct Reasoning:         15ms
├── CoT Processing:          20ms
├── Response Generation:     25ms
├── Self-Review:             30ms
├── API Response:            50ms
└── TOTAL:                   150ms (0.15 seconds)

With OpenAI Integration:     3000ms (3 seconds)
- Plus API latency:         2000-3000ms
```

### Quality Improvement Path
```
Iteration 1 (Auto-generated):
├── Quality Score: 7/10
├── Issues: Tone could be warmer
└── Actions: Improve greeting

After Improvement:
├── Quality Score: 9/10
├── Issues: None significant
└── Verdict: APPROVED ✓
```

## 🔐 Security Considerations

```
├── Input Validation
│  ├── Check query length
│  ├── Sanitize special characters
│  └── Prevent injection attacks
│
├── Rate Limiting
│  ├── Max 100 requests/minute per IP
│  ├── Prevent brute force attacks
│  └── Fair resource usage
│
├── Data Privacy
│  ├── No permanent storage (by default)
│  ├── HTTPS only in production
│  └── GDPR compliant
│
└── API Security
   ├── API key authentication (production)
   ├── CORS restrictions
   └── Request signing
```

## 📚 Knowledge Base Structure

```
{
  "category_name": {
    "keywords": ["keyword1", "keyword2", ...],
    "solutions": [
      "Solution 1",
      "Solution 2",
      "Solution 3",
      ...
    ],
    "priority": "high" | "medium" | "low"
  }
}

Example: Login Category
{
  "login": {
    "keywords": ["login", "password", "account", "access", ...],
    "solutions": [
      "Verify email address",
      "Use password reset",
      "Clear cache/cookies",
      "Try incognito mode",
      "Contact support"
    ],
    "priority": "high"
  }
}
```

## 🎯 Integration Points

### With OpenAI API
```python
# Replace response generation
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": formatted_query}
    ]
)
```

### With Database (Future)
```python
# Store conversations
db.conversations.insert({
    "query": query,
    "response": response,
    "quality_score": score,
    "timestamp": now(),
    "user_id": user_id
})
```

### With Sentiment Analysis
```python
# Detect customer emotion
sentiment = analyze_sentiment(query)
if sentiment == "frustrated":
    response = add_extra_empathy(response)
```

### With Ticketing System
```python
# Create ticket for complex issues
if complexity_score > 7:
    ticket = create_support_ticket(
        query=query,
        priority="high",
        assigned_to="senior_support"
    )
```

---

This architecture enables scalable, maintainable customer support with AI-driven reasoning!
