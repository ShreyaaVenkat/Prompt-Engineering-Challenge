#!/usr/bin/env python
"""Test script to demonstrate the chatbot with all AI patterns"""

from chatbot_engine import get_chatbot

print("\n" + "="*70)
print("CUSTOMER SUPPORT CHATBOT - LIVE DEMONSTRATION")
print("="*70)
print("\nTesting with: 'I can\\'t log into my account'")
print("-"*70)

# Initialize chatbot
chatbot = get_chatbot()

# Generate response with all patterns
result = chatbot.generate_response("I can't log into my account")

print("\n✅ CUSTOMER QUERY:")
print(f"   {result['query']}")

print("\n📊 ISSUE CLASSIFICATION:")
print(f"   Category: {result['category'].upper()}")
print(f"   Confidence: {result['confidence']}/5")

print("\n🧠 ReAct PATTERN - REASONING & ACTION:")
print(f"   Thought: {result['react_reasoning']['thought']}")
print(f"   Observation: {result['react_reasoning']['observation']}")
print(f"   Action: {result['react_reasoning']['action']}")

print("\n🔗 CHAIN OF THOUGHT - STEP-BY-STEP REASONING:")
for i, step in enumerate(result['cot_steps'][:4], 1):
    print(f"   {step}")

print("\n💬 CHATBOT RESPONSE:")
print("-"*70)
print(result['response'])
print("-"*70)

print("\n🔍 SELF-REFLECTION REVIEW:")
print(f"   Quality Score: {result['review']['quality_score']}/10")
print(f"   Verdict: {result['review']['verdict']}")
if result['review']['issues_found']:
    print(f"   Issues Found: {result['review']['issues_found']}")
else:
    print(f"   ✅ No issues detected")

print("\n📈 CONVERSATION STATISTICS:")
stats = chatbot.get_conversation_summary()
print(f"   Total Conversations: {stats['total_conversations']}")
print(f"   Average Quality: {stats['average_quality']}/10")
print(f"   Success Rate: {stats['success_rate']}%")

print("\n" + "="*70)
print("✅ DEMONSTRATION COMPLETE")
print("="*70 + "\n")
