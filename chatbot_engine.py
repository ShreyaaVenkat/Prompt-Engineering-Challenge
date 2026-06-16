"""
Customer Support Chatbot Engine with ReAct, Chain of Thought, and Self-Reflection Patterns
"""

from typing import Dict, List, Tuple
from datetime import datetime
import json


class SelfReflectingAgent:
    """Evaluates and improves chatbot responses"""
    
    def __init__(self):
        self.review_history = []
    
    def review_response(self, query: str, response: str) -> Dict:
        """Review a response for quality and identify improvements"""
        issues = self._check_for_issues(query, response)
        quality_score = self._calculate_quality_score(response, issues)
        improvements = self._suggest_improvements(response, issues)
        
        review = {
            "query": query,
            "original_response": response,
            "quality_score": quality_score,
            "issues_found": issues,
            "improvements": improvements,
            "verdict": "APPROVED" if quality_score >= 8 else "NEEDS REVISION",
            "timestamp": datetime.now().isoformat()
        }
        
        self.review_history.append(review)
        return review
    
    def _check_for_issues(self, query: str, response: str) -> List[str]:
        """Check for common response quality issues"""
        issues = []
        
        if len(response) < 50:
            issues.append("Response too brief - needs more detail")
        
        if "I don't know" in response and len(response) < 200:
            issues.append("Could provide more helpful context")
        
        if "!!!" in response or "???" in response:
            issues.append("Excessive punctuation detected")
        
        if not any(response.startswith(phrase) for phrase in ["Hi", "Hello", "Thank", "I", "Sure", "Yes"]):
            issues.append("Missing warm greeting")
        
        if response.count("sorry") > 2:
            issues.append("Over-apologizing - be more solution-focused")
        
        return issues
    
    def _calculate_quality_score(self, response: str, issues: List[str]) -> int:
        """Calculate quality score from 1-10"""
        base_score = 10
        base_score -= len(issues) * 1.5
        return int(max(1, min(10, base_score)))
    
    def _suggest_improvements(self, response: str, issues: List[str]) -> List[str]:
        """Suggest specific improvements to the response"""
        improvements = []
        
        for issue in issues:
            if "too brief" in issue:
                improvements.append("Expand with more specific steps or context")
            elif "greeting" in issue:
                improvements.append("Add a warm, friendly greeting")
            elif "punctuation" in issue:
                improvements.append("Use single punctuation marks only")
            elif "apologies" in issue:
                improvements.append("Use action-oriented language instead")
        
        improvements.append("Consider asking a clarifying question")
        return improvements


class CustomerSupportChatbot:
    """Main chatbot combining ReAct, CoT, and Self-Reflection patterns"""
    
    def __init__(self):
        self.reflection_agent = SelfReflectingAgent()
        self.knowledge_base = self._build_knowledge_base()
        self.conversation_history = []
    
    def _build_knowledge_base(self) -> Dict:
        """Build knowledge base with common support issues"""
        return {
            "login": {
                "keywords": ["login", "password", "account", "access", "sign in", "can't log"],
                "solutions": [
                    "Verify the email address you're using",
                    "Click 'Forgot Password' and check your email",
                    "Clear your browser cache and cookies",
                    "Try using an incognito/private browser window",
                    "Contact support if issue persists"
                ],
                "priority": "high"
            },
            "billing": {
                "keywords": ["charge", "billing", "payment", "refund", "invoice", "charged twice", "money"],
                "solutions": [
                    "Check your transaction history in Account Settings",
                    "Verify if the charge appears twice or once",
                    "Duplicate charges are automatically reversed in 3-5 business days",
                    "Request an itemized invoice if you need details",
                    "Reply with your order number for manual investigation"
                ],
                "priority": "high"
            },
            "shipping": {
                "keywords": ["shipping", "delivery", "order", "track", "package", "where", "arrive", "delayed"],
                "solutions": [
                    "Find your tracking number in your confirmation email",
                    "Check estimated delivery date on carrier website",
                    "Most packages arrive within 3-5 business days",
                    "Contact carrier directly for delivery delays",
                    "Verify your address was correct at checkout"
                ],
                "priority": "high"
            },
            "technical": {
                "keywords": ["bug", "error", "crash", "doesn't work", "broken", "issue", "problem", "not working"],
                "solutions": [
                    "Restart the application completely",
                    "Update to the latest version",
                    "Check your internet connection",
                    "Clear your browser cache and cookies",
                    "Try a different browser or device"
                ],
                "priority": "medium"
            },
            "account": {
                "keywords": ["account", "profile", "settings", "information", "update", "change"],
                "solutions": [
                    "Go to Account Settings to update profile info",
                    "Changes typically take effect immediately",
                    "Verify your email change with confirmation link",
                    "Password updates require re-login",
                    "Contact support for sensitive account changes"
                ],
                "priority": "medium"
            }
        }
    
    def _identify_category(self, query: str) -> Tuple[str, int]:
        """Identify issue category based on keywords"""
        query_lower = query.lower()
        scores = {}
        
        for category, info in self.knowledge_base.items():
            keyword_matches = sum(1 for keyword in info["keywords"] if keyword in query_lower)
            scores[category] = keyword_matches
        
        if max(scores.values()) > 0:
            best_category = max(scores, key=scores.get)
            return best_category, scores[best_category]
        return "general", 0
    
    def _apply_react_reasoning(self, query: str, category: str) -> Dict:
        """Apply ReAct Pattern: Reasoning + Action"""
        thought = f"Customer has a {category} issue requiring specific guidance."
        observation = f"Common {category} concerns include: {', '.join(self.knowledge_base[category]['keywords'][:3])}"
        action = "Provide step-by-step troubleshooting guide with clear next steps"
        
        return {
            "thought": thought,
            "observation": observation,
            "action": action
        }
    
    def _apply_cot_reasoning(self, query: str, solutions: List[str]) -> List[str]:
        """Apply Chain of Thought: Sequential reasoning steps"""
        reasoning_steps = [
            f"1. Understand: Customer issue - {query[:50]}...",
            f"2. Analyze: {len(solutions)} proven solutions available",
            f"3. Prioritize: Order by likelihood to resolve",
            f"4. Structure: Format as clear numbered steps",
            f"5. Communicate: Friendly, actionable response"
        ]
        return reasoning_steps
    
    def _build_customer_response(self, query: str, category: str, solutions: List[str]) -> str:
        """Build friendly, structured customer response"""
        greeting = "Hi there! 👋 Thank you for reaching out. "
        
        if category != "general":
            greeting += f"I can help with your {category} issue.\n\n"
        else:
            greeting += "I'll do my best to help.\n\n"
        
        response = greeting + "Here's what I recommend:\n\n"
        
        for i, solution in enumerate(solutions, 1):
            response += f"**Step {i}:** {solution}\n"
        
        response += "\n✨ If these steps don't resolve your issue, I'm here to help further!"
        
        return response
    
    def _improve_response(self, response: str, improvements: List[str]) -> str:
        """Improve response based on review feedback"""
        improved = response
        
        # Replace excessive apologies
        improved = improved.replace("sorry, sorry", "let me help you").replace("sorry sorry", "helping you")
        
        # Ensure proper formatting
        if not improved.endswith("!") and not improved.endswith("?"):
            improved += " 😊"
        
        return improved
    
    def generate_response(self, query: str, apply_reflection: bool = True) -> Dict:
        """Generate complete chatbot response with all reasoning patterns"""
        
        # Step 1: Identify issue category
        category, confidence = self._identify_category(query)
        
        # Step 2: Apply ReAct reasoning
        react_output = self._apply_react_reasoning(query, category)
        
        # Step 3: Get solutions and apply CoT
        solutions = self.knowledge_base[category]["solutions"]
        cot_steps = self._apply_cot_reasoning(query, solutions)
        
        # Step 4: Generate initial response
        response = self._build_customer_response(query, category, solutions)
        
        # Step 5: Self-reflect if enabled
        review = None
        if apply_reflection:
            review = self.reflection_agent.review_response(query, response)
            
            # Improve if needed
            if review["verdict"] == "NEEDS REVISION":
                response = self._improve_response(response, review["improvements"])
                review = self.reflection_agent.review_response(query, response)
        
        # Step 6: Store in history
        entry = {
            "query": query,
            "category": category,
            "confidence": confidence,
            "react_reasoning": react_output,
            "cot_steps": cot_steps,
            "response": response,
            "review": review,
            "timestamp": datetime.now().isoformat()
        }
        
        self.conversation_history.append(entry)
        
        return entry
    
    def get_conversation_summary(self) -> Dict:
        """Get statistics about all conversations"""
        if not self.conversation_history:
            return {
                "total_conversations": 0,
                "average_quality": 0,
                "categories": {},
                "success_rate": 0
            }
        
        total = len(self.conversation_history)
        categories_count = {}
        total_quality = 0
        approved_count = 0
        
        for entry in self.conversation_history:
            category = entry["category"]
            categories_count[category] = categories_count.get(category, 0) + 1
            
            if entry["review"]:
                total_quality += entry["review"]["quality_score"]
                if entry["review"]["verdict"] == "APPROVED":
                    approved_count += 1
        
        return {
            "total_conversations": total,
            "average_quality": round(total_quality / total, 1) if total > 0 else 0,
            "categories": categories_count,
            "success_rate": round((approved_count / total) * 100, 1) if total > 0 else 0
        }


# Singleton instance
_chatbot_instance = None


def get_chatbot() -> CustomerSupportChatbot:
    """Get or create chatbot singleton instance"""
    global _chatbot_instance
    if _chatbot_instance is None:
        _chatbot_instance = CustomerSupportChatbot()
    return _chatbot_instance
