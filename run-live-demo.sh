#!/bin/bash

# 🚀 LIVE CI/CD DEMO AUTOMATION SCRIPT
# This script demonstrates the complete CI/CD workflow

set -e

echo "🚀 LIVE CI/CD AUTOMATION DEMO"
echo "================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Navigate to project directory
cd "$(dirname "$0")"

echo -e "${BLUE}📍 Current directory: $(pwd)${NC}"
echo ""

# Step 1: Show current status
echo -e "${YELLOW}STEP 1: Current Git Status${NC}"
echo "----------------------------"
git status
echo ""

# Step 2: Make a code change
echo -e "${YELLOW}STEP 2: Adding New Feature${NC}"
echo "----------------------------"
echo "Adding a new DevOps facts API endpoint..."

# Backup original file
cp app/main.py app/main.py.backup

# Add new endpoint to main.py
cat >> app/main.py << 'EOF'

@app.get("/api/devops-fact")
async def devops_fact():
    """Returns a random DevOps fact"""
    import random
    facts = [
        "DevOps reduces deployment failures by 60%",
        "Automated testing catches 85% of bugs before production",
        "CI/CD pipelines save developers 10+ hours per week",
        "Companies using DevOps deploy 200x more frequently",
        "Automated deployments are 50x faster than manual ones"
    ]
    return {
        "fact": random.choice(facts),
        "timestamp": "2024-01-15T10:30:00Z",
        "source": "DevOps Research and Assessment (DORA)"
    }
EOF

echo -e "${GREEN}✅ New endpoint added to app/main.py${NC}"
echo ""

# Step 3: Show the diff
echo -e "${YELLOW}STEP 3: Code Changes (git diff)${NC}"
echo "----------------------------"
git diff app/main.py
echo ""

# Step 4: Commit changes
echo -e "${YELLOW}STEP 4: Committing Changes${NC}"
echo "----------------------------"
git add app/main.py
git commit -m "feat: Add DevOps facts API endpoint for live demo"
echo -e "${GREEN}✅ Changes committed${NC}"
echo ""

# Step 5: Push to GitHub
echo -e "${YELLOW}STEP 5: Pushing to GitHub${NC}"
echo "----------------------------"
echo "⚡ This will trigger GitHub Actions automatically!"
echo ""
read -p "Press ENTER to push to GitHub and trigger CI/CD..."
echo ""

git push origin main

echo ""
echo -e "${GREEN}✅ Code pushed to GitHub!${NC}"
echo ""

# Step 6: Open GitHub Actions
echo -e "${YELLOW}STEP 6: Opening GitHub Actions${NC}"
echo "----------------------------"
echo "Opening GitHub Actions page in your browser..."
sleep 2
open "https://github.com/hadeedkhan117/devops-github-actions-fastapi/actions"

echo ""
echo -e "${GREEN}🎉 DEMO COMPLETE!${NC}"
echo ""
echo "What just happened:"
echo "  1. ✅ Added new API endpoint"
echo "  2. ✅ Committed changes"
echo "  3. ✅ Pushed to GitHub"
echo "  4. ⚡ GitHub Actions triggered automatically"
echo ""
echo "Watch your browser - you should see:"
echo "  • CI Pipeline running (testing your code)"
echo "  • Docker Build running (building container)"
echo "  • Both completing in ~30 seconds"
echo ""
echo "Test the new endpoint locally:"
echo "  uvicorn app.main:app --reload"
echo "  curl http://localhost:8000/api/devops-fact"
echo ""
echo "To restore original code:"
echo "  mv app/main.py.backup app/main.py"
echo ""
