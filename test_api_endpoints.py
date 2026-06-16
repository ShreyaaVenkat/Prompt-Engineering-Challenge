#!/usr/bin/env python
"""Test the Flask API endpoints"""

import requests
import json

BASE_URL = "http://localhost:5000"

print("\n" + "="*80)
print("FLASK API ENDPOINTS - LIVE TESTING")
print("="*80)

# Test 1: Health Check
print("\n1️⃣ HEALTH CHECK ENDPOINT")
print("-"*80)
try:
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    print(f"✅ Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 2: Quick Chat
print("\n2️⃣ QUICK CHAT ENDPOINT (Fast Response)")
print("-"*80)
try:
    response = requests.post(
        f"{BASE_URL}/chat/quick",
        json={"query": "I forgot my password"},
        timeout=5
    )
    print(f"✅ Status: {response.status_code}")
    data = response.json()
    print(f"Category: {data.get('category')}")
    print(f"Response Preview: {data.get('response', '')[:100]}...")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 3: Full Chat with Reasoning
print("\n3️⃣ FULL CHAT ENDPOINT (With Reasoning)")
print("-"*80)
try:
    response = requests.post(
        f"{BASE_URL}/chat",
        json={"query": "I was charged twice"},
        timeout=5
    )
    print(f"✅ Status: {response.status_code}")
    data = response.json()
    print(f"Category: {data.get('category')}")
    print(f"ReAct Thought: {data.get('reasoning', {}).get('react', {}).get('thought')}")
    print(f"Quality Score: {data.get('reasoning', {}).get('self_review', {}).get('quality_score')}/10")
    print(f"Verdict: {data.get('reasoning', {}).get('self_review', {}).get('verdict')}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 4: Categories
print("\n4️⃣ CATEGORIES ENDPOINT")
print("-"*80)
try:
    response = requests.get(f"{BASE_URL}/categories", timeout=5)
    print(f"✅ Status: {response.status_code}")
    data = response.json()
    for category in list(data.get('categories', {}).keys())[:3]:
        print(f"   • {category}")
    print(f"   ... ({len(data.get('categories', {}))} total categories)")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 5: Patterns Info
print("\n5️⃣ PATTERNS INFORMATION ENDPOINT")
print("-"*80)
try:
    response = requests.get(f"{BASE_URL}/patterns", timeout=5)
    print(f"✅ Status: {response.status_code}")
    data = response.json()
    patterns = data.get('patterns', {})
    for pattern_name in patterns:
        print(f"   • {patterns[pattern_name]['name']}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 6: Summary/Statistics
print("\n6️⃣ SUMMARY/STATISTICS ENDPOINT")
print("-"*80)
try:
    response = requests.get(f"{BASE_URL}/summary", timeout=5)
    print(f"✅ Status: {response.status_code}")
    data = response.json()
    stats = data.get('statistics', {})
    print(f"Total Conversations: {stats.get('total_conversations')}")
    print(f"Average Quality: {stats.get('average_quality')}/10")
    print(f"Success Rate: {stats.get('success_rate')}%")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 7: History
print("\n7️⃣ CONVERSATION HISTORY ENDPOINT")
print("-"*80)
try:
    response = requests.get(f"{BASE_URL}/history?limit=5", timeout=5)
    print(f"✅ Status: {response.status_code}")
    data = response.json()
    print(f"Recent Conversations: {data.get('count')}")
    for i, convo in enumerate(data.get('history', [])[:2], 1):
        print(f"   {i}. {convo.get('query')[:50]}... (Quality: {convo.get('quality_score')}/10)")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "="*80)
print("✅ API TESTING COMPLETE")
print("="*80 + "\n")
