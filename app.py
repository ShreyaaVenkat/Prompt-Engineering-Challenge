"""
Flask API server for Customer Support Chatbot
Provides endpoints for chatbot functionality
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_engine import get_chatbot
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize chatbot
chatbot = get_chatbot()


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        "status": "success",
        "message": "Customer Support Chatbot API",
        "endpoints": {
            "POST /chat": "Send a customer query",
            "GET /summary": "Get conversation statistics",
            "GET /health": "Health check"
        },
        "patterns": ["ReAct", "Chain of Thought", "Self-Reflection"]
    })


@app.route('/chat', methods=['POST'])
def chat():
    """Process customer query and return chatbot response"""
    try:
        data = request.get_json()
        
        if not data or 'query' not in data:
            return jsonify({
                "status": "error",
                "message": "Missing 'query' field"
            }), 400
        
        query = data['query'].strip()
        
        if not query:
            return jsonify({
                "status": "error",
                "message": "Query cannot be empty"
            }), 400
        
        # Generate response with all reasoning patterns
        result = chatbot.generate_response(query, apply_reflection=True)
        
        # Format response for frontend
        response_data = {
            "status": "success",
            "customer_query": result["query"],
            "category": result["category"],
            "confidence": result["confidence"],
            "chatbot_response": result["response"],
            "reasoning": {
                "react": result["react_reasoning"],
                "chain_of_thought": result["cot_steps"],
                "self_review": {
                    "quality_score": result["review"]["quality_score"] if result["review"] else 0,
                    "verdict": result["review"]["verdict"] if result["review"] else "NOT_REVIEWED",
                    "issues": result["review"]["issues_found"] if result["review"] else []
                }
            },
            "timestamp": result["timestamp"]
        }
        
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/chat/quick', methods=['POST'])
def chat_quick():
    """Quick chat endpoint - returns only response, no reasoning details"""
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({
                "status": "error",
                "message": "Query cannot be empty"
            }), 400
        
        result = chatbot.generate_response(query, apply_reflection=True)
        
        return jsonify({
            "status": "success",
            "response": result["response"],
            "category": result["category"]
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/summary', methods=['GET'])
def summary():
    """Get chatbot conversation summary and statistics"""
    try:
        stats = chatbot.get_conversation_summary()
        
        return jsonify({
            "status": "success",
            "statistics": stats,
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Customer Support Chatbot",
        "timestamp": datetime.now().isoformat()
    })


@app.route('/patterns', methods=['GET'])
def patterns():
    """Get information about AI patterns used"""
    return jsonify({
        "status": "success",
        "patterns": {
            "react": {
                "name": "ReAct Pattern",
                "description": "Reasoning + Action - breaks down problems logically",
                "benefits": [
                    "Transparent decision-making",
                    "Clear reasoning shown to customers",
                    "Improved trust in responses"
                ]
            },
            "chain_of_thought": {
                "name": "Chain of Thought (CoT)",
                "description": "Step-by-step reasoning for complex problems",
                "benefits": [
                    "Easy-to-follow solutions",
                    "Multiple steps clearly explained",
                    "Higher solution success rate"
                ]
            },
            "self_reflection": {
                "name": "Self-Reflection",
                "description": "Automatic review and improvement of responses",
                "benefits": [
                    "Better quality responses",
                    "Fewer errors before delivery",
                    "Continuous improvement"
                ]
            }
        }
    })


@app.route('/categories', methods=['GET'])
def categories():
    """Get supported issue categories"""
    knowledge_base = chatbot.knowledge_base
    
    categories_info = {}
    for category, info in knowledge_base.items():
        categories_info[category] = {
            "keywords": info["keywords"],
            "priority": info["priority"],
            "solution_count": len(info["solutions"])
        }
    
    return jsonify({
        "status": "success",
        "categories": categories_info
    })


@app.route('/history', methods=['GET'])
def history():
    """Get conversation history"""
    try:
        limit = request.args.get('limit', default=10, type=int)
        
        # Return last N conversations (without detailed reasoning)
        recent = chatbot.conversation_history[-limit:]
        
        history_data = []
        for entry in recent:
            history_data.append({
                "query": entry["query"],
                "category": entry["category"],
                "timestamp": entry["timestamp"],
                "quality_score": entry["review"]["quality_score"] if entry["review"] else 0
            })
        
        return jsonify({
            "status": "success",
            "count": len(history_data),
            "history": history_data
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "available_endpoints": [
            "POST /chat",
            "POST /chat/quick",
            "GET /summary",
            "GET /health",
            "GET /patterns",
            "GET /categories",
            "GET /history"
        ]
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


if __name__ == '__main__':
    print("🚀 Starting Customer Support Chatbot API Server")
    print("📝 Patterns: ReAct + Chain of Thought + Self-Reflection")
    print("🌐 Running on http://localhost:5000")
    print("\nAvailable endpoints:")
    print("  POST /chat - Full response with reasoning")
    print("  POST /chat/quick - Quick response only")
    print("  GET /summary - Conversation statistics")
    print("  GET /health - Health check")
    print("  GET /patterns - AI patterns information")
    print("  GET /categories - Supported issue categories")
    print("  GET /history - Recent conversation history")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
