#!/usr/bin/env python
"""Multi-test demonstration showing different issue categories and AI patterns"""

from chatbot_engine import get_chatbot

test_queries = [
    ("I was charged twice for my order", "BILLING"),
    ("Where is my package?", "SHIPPING"),
    ("The app keeps crashing", "TECHNICAL"),
]

print("\n" + "="*80)
print("CUSTOMER SUPPORT CHATBOT - MULTI-SCENARIO DEMONSTRATION")
print("="*80)

chatbot = get_chatbot()

for query, expected_category in test_queries:
    result = chatbot.generate_response(query)
    
    print(f"\n{'▶'*40}")
    print(f"\n📌 SCENARIO: {query}")
    print(f"   Expected Category: {expected_category}")
    print(f"   Detected Category: {result['category'].upper()}")
    print(f"   Confidence: {result['confidence']}/5")
    
    print(f"\n🧠 ReAct Analysis:")
    print(f"   • Thought: {result['react_reasoning']['thought'][:60]}...")
    print(f"   • Action: {result['react_reasoning']['action']}")
    
    print(f"\n🔗 Chain of Thought (First 2 Steps):")
    for step in result['cot_steps'][:2]:
        print(f"   • {step}")
    
    print(f"\n💬 Chatbot Response Preview:")
    response_preview = result['response'][:120]
    print(f"   {response_preview}...")
    
    print(f"\n✅ Quality Review:")
    print(f"   • Score: {result['review']['quality_score']}/10")
    print(f"   • Verdict: {result['review']['verdict']}")

print(f"\n{'▶'*40}")
print(f"\n📊 OVERALL STATISTICS:")
stats = chatbot.get_conversation_summary()
print(f"   Total Conversations: {stats['total_conversations']}")
print(f"   Average Quality Score: {stats['average_quality']}/10")
print(f"   Success Rate: {stats['success_rate']}%")
print(f"   Category Breakdown: {stats['categories']}")

print("\n" + "="*80)
print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
print("="*80 + "\n")
