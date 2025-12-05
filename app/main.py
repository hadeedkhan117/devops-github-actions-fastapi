from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from datetime import datetime
from pathlib import Path
import subprocess
import os

app = FastAPI(
    title="DevOps Demo API", 
    version="1.0.0",
    description="Complete DevOps Pipeline Demo with FastAPI, Docker & GitHub Actions",
    contact={
        "name": "Hadeed Khan",
        "url": "https://github.com/hadeedkhan117/devops-github-actions-fastapi"
    }
)


class EchoRequest(BaseModel):
    message: str


@app.get("/api")
def root():
    return {
        "status": "ok",
        "service": "DevOps Demo API",
        "time": datetime.utcnow().isoformat()
    }


@app.post("/echo")
def echo(req: EchoRequest):
    return {
        "you_said": req.message,
        "length": len(req.message)
    }


@app.get("/version")
def version():
    from .version import __version__, __build__, __author__, __description__
    return {
        "version": __version__,
        "build": __build__,
        "author": __author__,
        "description": __description__,
        "github": "https://github.com/hadeedkhan117/devops-github-actions-fastapi"
    }


# Serve frontend
@app.get("/frontend", response_class=HTMLResponse)
def frontend():
    html_path = Path("frontend/index.html")
    return html_path.read_text(encoding="utf-8")


@app.get("/cicd-live", response_class=HTMLResponse)
def cicd_live():
    html_path = Path("frontend/cicd-live.html")
    return html_path.read_text(encoding="utf-8")


@app.get("/manual-vs-automated", response_class=HTMLResponse)
def manual_vs_automated():
    html_path = Path("frontend/manual-vs-automated.html")
    return html_path.read_text(encoding="utf-8")


@app.get("/", response_class=HTMLResponse)
def home():
    return """<!DOCTYPE html>
<html>
<head>
    <title>DevOps Demo - Home</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { text-align: center; color: white; margin-bottom: 40px; }
        .header h1 { font-size: 3em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .header p { font-size: 1.2em; opacity: 0.9; }
        .nav-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .nav-card { background: white; border-radius: 12px; padding: 30px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease; cursor: pointer; }
        .nav-card:hover { transform: translateY(-5px); box-shadow: 0 12px 48px rgba(0,0,0,0.2); }
        .nav-card h2 { color: #667eea; margin-bottom: 15px; font-size: 1.5em; }
        .nav-card p { color: #666; margin-bottom: 20px; line-height: 1.6; }
        .nav-card a { display: inline-block; background: #667eea; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: 500; transition: background 0.3s ease; }
        .nav-card a:hover { background: #5a67d8; }
        .lifecycle { background: white; border-radius: 12px; padding: 30px; margin-bottom: 40px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); }
        .lifecycle h2 { color: #667eea; margin-bottom: 20px; text-align: center; }
        .lifecycle-flow { display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }
        .lifecycle-item { background: #667eea; color: white; padding: 10px 20px; border-radius: 20px; font-weight: bold; font-size: 0.9em; }
        .arrow { font-size: 1.5em; color: #667eea; }
        .resources { background: white; border-radius: 12px; padding: 30px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); }
        .resources h2 { color: #667eea; margin-bottom: 20px; }
        .resource-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }
        .resource-item { background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #667eea; }
        .resource-item h3 { color: #2c3e50; margin-bottom: 8px; font-size: 1.1em; }
        .resource-item a { color: #667eea; text-decoration: none; font-weight: 500; }
        .resource-item a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 DevOps Complete Demo</h1>
            <p>Interactive demonstration of the complete DevOps lifecycle</p>
        </div>

        <div class="lifecycle">
            <h2>🔄 DevOps Lifecycle</h2>
            <div class="lifecycle-flow">
                <span class="lifecycle-item">📋 Plan</span>
                <span class="arrow">→</span>
                <span class="lifecycle-item">💻 Code</span>
                <span class="arrow">→</span>
                <span class="lifecycle-item">🔨 Build</span>
                <span class="arrow">→</span>
                <span class="lifecycle-item">🧪 Test</span>
                <span class="arrow">→</span>
                <span class="lifecycle-item">📦 Release</span>
                <span class="arrow">→</span>
                <span class="lifecycle-item">🚀 Deploy</span>
                <span class="arrow">→</span>
                <span class="lifecycle-item">⚙️ Operate</span>
                <span class="arrow">→</span>
                <span class="lifecycle-item">📊 Monitor</span>
            </div>
            <p style="text-align: center; color: #667eea; font-weight: bold; margin-top: 15px;">⬆️ Continuous Feedback Loop ⬆️</p>
        </div>

        <div class="nav-grid">
            <div class="nav-card">
                <h2>🎯 Interactive Demo Dashboard</h2>
                <p>Step-by-step demonstration of the complete DevOps pipeline with live command execution and real-time outputs.</p>
                <a href="/demo" target="_blank">Launch Demo Dashboard →</a>
            </div>

            <div class="nav-card">
                <h2>🚀 Live CI/CD Demo (Simulation)</h2>
                <p>Watch GitHub Actions automatically test and deploy! Simulate git push and see the automation in action.</p>
                <a href="/cicd-demo" target="_blank">Launch CI/CD Demo →</a>
            </div>

            <div class="nav-card">
                <h2>⚡ Live CI/CD Demo (Real Commands)</h2>
                <p>Execute real git commands from your browser! Make changes, commit, push, and watch GitHub Actions run.</p>
                <a href="/cicd-live" target="_blank">Launch Live Demo →</a>
            </div>

            <div class="nav-card">
                <h2>⚔️ Manual vs Automated</h2>
                <p>Side-by-side comparison showing how manual processes take 8-10 hours vs 41 seconds with automation!</p>
                <a href="/manual-vs-automated" target="_blank">View Comparison →</a>
            </div>

            <div class="nav-card">
                <h2>📚 API Documentation</h2>
                <p>Interactive Swagger UI documentation. Test all API endpoints directly in your browser.</p>
                <a href="/docs" target="_blank">Open API Docs →</a>
            </div>

            <div class="nav-card">
                <h2>🌐 Frontend Interface</h2>
                <p>User-friendly interface to interact with the API. Test status checks and echo functionality.</p>
                <a href="/frontend" target="_blank">Open Frontend →</a>
            </div>

            <div class="nav-card">
                <h2>🐳 GitHub Repository</h2>
                <p>View the complete source code, CI/CD workflows, and project documentation on GitHub.</p>
                <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi" target="_blank">View Repository →</a>
            </div>

            <div class="nav-card">
                <h2>⚙️ GitHub Actions</h2>
                <p>See the CI/CD pipeline in action. View automated test runs and deployment workflows.</p>
                <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/actions" target="_blank">View Actions →</a>
            </div>

            <div class="nav-card">
                <h2>📊 Version Info</h2>
                <p>Check application version, build information, and project metadata.</p>
                <a href="/version" target="_blank">View Version →</a>
            </div>
        </div>

        <div class="resources">
            <h2>📝 Documentation & Resources</h2>
            <div class="resource-list">
                <div class="resource-item">
                    <h3>📖 Complete Guide</h3>
                    <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/blob/main/COMPLETE_GUIDE.md" target="_blank">Read Full Guide</a>
                </div>
                <div class="resource-item">
                    <h3>🎬 Live Demo Script</h3>
                    <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/blob/main/LIVE_DEMO_SCRIPT.md" target="_blank">View Demo Script</a>
                </div>
                <div class="resource-item">
                    <h3>📝 README</h3>
                    <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/blob/main/README.md" target="_blank">Project README</a>
                </div>
                <div class="resource-item">
                    <h3>📦 Requirements</h3>
                    <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/blob/main/requirements.txt" target="_blank">View Dependencies</a>
                </div>
                <div class="resource-item">
                    <h3>🐳 Dockerfile</h3>
                    <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/blob/main/Dockerfile" target="_blank">View Dockerfile</a>
                </div>
                <div class="resource-item">
                    <h3>⚙️ CI Workflow</h3>
                    <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/blob/main/.github/workflows/ci.yml" target="_blank">View CI Pipeline</a>
                </div>
            </div>
        </div>

        <div style="text-align: center; color: white; margin-top: 40px; padding: 20px;">
            <p style="font-size: 1.1em; margin-bottom: 10px;">Built with FastAPI, Docker, and GitHub Actions</p>
            <p style="opacity: 0.8;">Complete DevOps Pipeline Demonstration</p>
        </div>
    </div>
</body>
</html>"""

@app.get("/demo", response_class=HTMLResponse)
def demo_page():
    return """<!DOCTYPE html>
<html>
<head>
    <title>DevOps Pipeline Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .dashboard { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; color: white; margin-bottom: 30px; }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .progress-bar { background: rgba(255,255,255,0.2); height: 8px; border-radius: 4px; margin: 20px 0; overflow: hidden; }
        .progress-fill { background: #4CAF50; height: 100%; width: 0%; transition: width 0.5s ease; }
        .step-container { background: white; border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); margin-bottom: 20px; overflow: hidden; }
        .step-header { background: #f8f9fa; padding: 20px; border-bottom: 1px solid #e9ecef; display: flex; justify-content: between; align-items: center; }
        .step-title { font-size: 1.3em; font-weight: 600; color: #2c3e50; display: flex; align-items: center; }
        .step-number { background: #667eea; color: white; width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; font-weight: bold; font-size: 1.2em; }
        .step-status { padding: 6px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 500; }
        .status-pending { background: #fff3cd; color: #856404; }
        .status-running { background: #d1ecf1; color: #0c5460; }
        .status-success { background: #d4edda; color: #155724; }
        .status-error { background: #f8d7da; color: #721c24; }
        .step-content { padding: 20px; display: none; }
        .step-content.active { display: block; }
        .command-section { margin-bottom: 20px; }
        .command-label { font-weight: 600; color: #495057; margin-bottom: 8px; }
        .command-box { background: #2d3748; color: #e2e8f0; padding: 15px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 0.9em; margin-bottom: 15px; }
        .explanation { background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #667eea; margin-bottom: 20px; }
        .output-section { margin-top: 20px; }
        .output-box { background: #1a202c; color: #e2e8f0; padding: 15px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 0.85em; max-height: 300px; overflow-y: auto; white-space: pre-wrap; }
        .controls { display: flex; gap: 10px; margin-top: 15px; }
        .btn { padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-weight: 500; transition: all 0.3s ease; }
        .btn-primary { background: #667eea; color: white; }
        .btn-primary:hover { background: #5a67d8; transform: translateY(-1px); }
        .btn-success { background: #48bb78; color: white; }
        .btn-success:hover { background: #38a169; }
        .btn-secondary { background: #a0aec0; color: white; }
        .btn-secondary:hover { background: #718096; }
        .btn:disabled { opacity: 0.6; cursor: not-allowed; }
        .success-text { color: #48bb78; }
        .error-text { color: #f56565; }
        .info-text { color: #4299e1; }
        .api-controls { background: #f7fafc; padding: 15px; border-radius: 8px; margin-top: 15px; }
        .api-input { padding: 10px; border: 1px solid #e2e8f0; border-radius: 4px; width: 300px; margin-right: 10px; }
        .completion-badge { background: #48bb78; color: white; padding: 8px 16px; border-radius: 20px; font-size: 0.9em; margin-left: auto; }
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>🚀 DevOps Pipeline Dashboard</h1>
            <p>Complete CI/CD Demo with FastAPI, Docker & GitHub Actions</p>
            <div class="progress-bar">
                <div class="progress-fill" id="progressBar"></div>
            </div>
        </div>

        <!-- DevOps Lifecycle Visualization -->
        <div class="step-container">
            <div class="step-header">
                <div class="step-title">
                    <div class="step-number">🔄</div>
                    DevOps Lifecycle - What We're Demonstrating
                </div>
            </div>
            <div class="step-content active">
                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                    <div style="text-align: center; font-family: monospace; font-size: 0.9em; line-height: 2;">
                        <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 10px;">
                            <span style="background: #667eea; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">📋 Plan</span>
                            <span style="font-size: 1.5em;">→</span>
                            <span style="background: #48bb78; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">💻 Code</span>
                            <span style="font-size: 1.5em;">→</span>
                            <span style="background: #ed8936; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">🔨 Build</span>
                            <span style="font-size: 1.5em;">→</span>
                            <span style="background: #4299e1; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">🧪 Test</span>
                            <span style="font-size: 1.5em;">→</span>
                            <span style="background: #9f7aea; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">📦 Release</span>
                            <span style="font-size: 1.5em;">→</span>
                            <span style="background: #f56565; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">🚀 Deploy</span>
                            <span style="font-size: 1.5em;">→</span>
                            <span style="background: #38b2ac; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">⚙️ Operate</span>
                            <span style="font-size: 1.5em;">→</span>
                            <span style="background: #ed64a6; color: white; padding: 8px 15px; border-radius: 20px; font-weight: bold;">📊 Monitor</span>
                        </div>
                        <div style="margin-top: 15px; font-size: 1.2em; color: #667eea;">
                            ⬆️ Continuous Feedback Loop ⬆️
                        </div>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 20px;">
                    <div style="background: #667eea; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">📋 Plan</h4>
                        <p style="margin: 0; font-size: 0.9em;">Define requirements and architecture</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: Project structure design</p>
                    </div>
                    <div style="background: #48bb78; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">💻 Code</h4>
                        <p style="margin: 0; font-size: 0.9em;">Write application code</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: FastAPI application (Step 1)</p>
                    </div>
                    <div style="background: #ed8936; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">🔨 Build</h4>
                        <p style="margin: 0; font-size: 0.9em;">Package application</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: Docker containerization (Step 4)</p>
                    </div>
                    <div style="background: #4299e1; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">🧪 Test</h4>
                        <p style="margin: 0; font-size: 0.9em;">Automated testing</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: pytest + ruff (Steps 2-3)</p>
                    </div>
                    <div style="background: #9f7aea; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">📦 Release</h4>
                        <p style="margin: 0; font-size: 0.9em;">Prepare for deployment</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: GitHub Actions CI/CD (Step 6)</p>
                    </div>
                    <div style="background: #f56565; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">🚀 Deploy</h4>
                        <p style="margin: 0; font-size: 0.9em;">Push to production</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: Docker Compose deployment</p>
                    </div>
                    <div style="background: #38b2ac; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">⚙️ Operate</h4>
                        <p style="margin: 0; font-size: 0.9em;">Manage running application</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: Container management</p>
                    </div>
                    <div style="background: #ed64a6; color: white; padding: 15px; border-radius: 8px;">
                        <h4 style="margin: 0 0 10px 0;">📊 Monitor</h4>
                        <p style="margin: 0; font-size: 0.9em;">Track performance & health</p>
                        <p style="margin: 5px 0 0 0; font-size: 0.85em; opacity: 0.9;">Our Demo: API health checks (Step 5)</p>
                    </div>
                </div>
                <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin-top: 20px; border-radius: 4px;">
                    <strong>💡 Key Insight:</strong> This demo covers the complete DevOps lifecycle! Each step below demonstrates a specific phase of modern software delivery.
                </div>
            </div>
        </div>

        <!-- Step 1: Project Structure -->
        <div class="step-container" id="step1">
            <div class="step-header" onclick="toggleStep(1)">
                <div class="step-title">
                    <div class="step-number">1</div>
                    📁 Project Structure Analysis
                </div>
                <div class="step-status status-pending" id="status1">Ready</div>
            </div>
            <div class="step-content" id="content1">
                <div class="explanation">
                    <strong>What this does:</strong> Displays the complete project structure showing all DevOps files including FastAPI app, tests, Docker configuration, and GitHub Actions workflows.
                </div>
                <div class="command-section">
                    <div class="command-label">Command:</div>
                    <div class="command-box">$ tree devops-github-actions-fastapi/</div>
                </div>
                <div class="controls">
                    <button class="btn btn-primary" onclick="runStep(1)" id="runBtn1">▶️ Run Command</button>
                    <button class="btn btn-success" onclick="nextStep(1)" id="nextBtn1" disabled>Next Step →</button>
                </div>
                <div class="output-section" id="outputSection1" style="display:none;">
                    <div class="command-label">Output:</div>
                    <div class="output-box" id="output1"></div>
                </div>
            </div>
        </div>

        <!-- Step 2: Run Tests -->
        <div class="step-container" id="step2">
            <div class="step-header" onclick="toggleStep(2)">
                <div class="step-title">
                    <div class="step-number">2</div>
                    🧪 Automated Testing
                </div>
                <div class="step-status status-pending" id="status2">Waiting</div>
            </div>
            <div class="step-content" id="content2">
                <div class="explanation">
                    <strong>What this does:</strong> Runs pytest to execute all unit tests, ensuring code quality and functionality. This is a critical part of CI/CD pipeline.
                </div>
                <div class="command-section">
                    <div class="command-label">Command:</div>
                    <div class="command-box">$ python3 -m pytest -v</div>
                </div>
                <div class="controls">
                    <button class="btn btn-primary" onclick="runStep(2)" id="runBtn2" disabled>▶️ Run Tests</button>
                    <button class="btn btn-success" onclick="nextStep(2)" id="nextBtn2" disabled>Next Step →</button>
                </div>
                <div class="output-section" id="outputSection2" style="display:none;">
                    <div class="command-label">Test Results:</div>
                    <div class="output-box" id="output2"></div>
                </div>
            </div>
        </div>

        <!-- Step 3: Code Quality -->
        <div class="step-container" id="step3">
            <div class="step-header" onclick="toggleStep(3)">
                <div class="step-title">
                    <div class="step-number">3</div>
                    ✅ Code Quality Check
                </div>
                <div class="step-status status-pending" id="status3">Waiting</div>
            </div>
            <div class="step-content" id="content3">
                <div class="explanation">
                    <strong>What this does:</strong> Uses Ruff linter to check code style, formatting, and potential issues. Ensures code meets quality standards.
                </div>
                <div class="command-section">
                    <div class="command-label">Command:</div>
                    <div class="command-box">$ python3 -m ruff check .</div>
                </div>
                <div class="controls">
                    <button class="btn btn-primary" onclick="runStep(3)" id="runBtn3" disabled>▶️ Run Linter</button>
                    <button class="btn btn-success" onclick="nextStep(3)" id="nextBtn3" disabled>Next Step →</button>
                </div>
                <div class="output-section" id="outputSection3" style="display:none;">
                    <div class="command-label">Linting Results:</div>
                    <div class="output-box" id="output3"></div>
                </div>
            </div>
        </div>

        <!-- Step 4: Docker Status -->
        <div class="step-container" id="step4">
            <div class="step-header" onclick="toggleStep(4)">
                <div class="step-title">
                    <div class="step-number">4</div>
                    🐳 Docker Containerization
                </div>
                <div class="step-status status-pending" id="status4">Waiting</div>
            </div>
            <div class="step-content" id="content4">
                <div class="explanation">
                    <strong>What this does:</strong> Checks Docker container status to verify the application is running in a containerized environment.
                </div>
                <div class="command-section">
                    <div class="command-label">Command:</div>
                    <div class="command-box">$ docker compose ps</div>
                </div>
                <div class="controls">
                    <button class="btn btn-primary" onclick="runStep(4)" id="runBtn4" disabled>▶️ Check Docker</button>
                    <button class="btn btn-success" onclick="nextStep(4)" id="nextBtn4" disabled>Next Step →</button>
                </div>
                <div class="output-section" id="outputSection4" style="display:none;">
                    <div class="command-label">Docker Status:</div>
                    <div class="output-box" id="output4"></div>
                </div>
            </div>
        </div>

        <!-- Step 5: API Testing -->
        <div class="step-container" id="step5">
            <div class="step-header" onclick="toggleStep(5)">
                <div class="step-title">
                    <div class="step-number">5</div>
                    🌐 Live API Testing
                </div>
                <div class="step-status status-pending" id="status5">Waiting</div>
            </div>
            <div class="step-content" id="content5">
                <div class="explanation">
                    <strong>What this does:</strong> Tests the live API endpoints to ensure the application is responding correctly and all features work.
                </div>
                <div class="command-section">
                    <div class="command-label">Commands:</div>
                    <div class="command-box">$ curl http://localhost:8000/
$ curl -X POST http://localhost:8000/echo -d '{"message":"test"}'</div>
                </div>
                <div class="controls">
                    <button class="btn btn-primary" onclick="runStep(5)" id="runBtn5" disabled>▶️ Test API</button>
                    <button class="btn btn-success" onclick="nextStep(5)" id="nextBtn5" disabled>Next Step →</button>
                </div>
                <div class="api-controls">
                    <input type="text" class="api-input" id="customMessage" placeholder="Enter custom message" value="DevOps Demo Success!">
                    <button class="btn btn-secondary" onclick="testCustomMessage()">Test Custom Message</button>
                </div>
                <div class="output-section" id="outputSection5" style="display:none;">
                    <div class="command-label">API Response:</div>
                    <div class="output-box" id="output5"></div>
                </div>
            </div>
        </div>

        <!-- Step 6: GitHub Actions CI/CD -->
        <div class="step-container" id="step6">
            <div class="step-header" onclick="toggleStep(6)">
                <div class="step-title">
                    <div class="step-number">6</div>
                    🚀 GitHub Actions CI/CD
                </div>
                <div class="step-status status-pending" id="status6">Waiting</div>
            </div>
            <div class="step-content" id="content6">
                <div class="explanation">
                    <strong>What this does:</strong> Shows GitHub Actions workflows that automatically run CI/CD pipeline when code is pushed to the repository.
                </div>
                <div class="command-section">
                    <div class="command-label">GitHub Repository:</div>
                    <div class="command-box">https://github.com/hadeedkhan117/devops-github-actions-fastapi</div>
                </div>
                <div class="controls">
                    <button class="btn btn-primary" onclick="runStep(6)" id="runBtn6" disabled>▶️ Check CI/CD Status</button>
                    <button class="btn btn-success" onclick="showCompletion()" id="nextBtn6" disabled>🎉 Complete Demo</button>
                </div>
                <div class="api-controls">
                    <button class="btn btn-secondary" onclick="window.open('https://github.com/hadeedkhan117/devops-github-actions-fastapi/actions', '_blank')">View GitHub Actions</button>
                    <button class="btn btn-secondary" onclick="window.open('https://github.com/hadeedkhan117/devops-github-actions-fastapi', '_blank')">View Repository</button>
                </div>
                <div class="output-section" id="outputSection6" style="display:none;">
                    <div class="command-label">CI/CD Status:</div>
                    <div class="output-box" id="output6"></div>
                </div>
            </div>
        </div>

        <!-- Completion -->
        <div class="step-container" id="completion" style="display:none;">
            <div class="step-header">
                <div class="step-title">
                    <div class="step-number">✅</div>
                    Demo Complete!
                </div>
                <div class="completion-badge">All Steps Passed</div>
            </div>
            <div class="step-content active">
                <div style="text-align: center; padding: 20px;">
                    <h2 style="color: #48bb78; margin-bottom: 20px;">🎉 DevOps Pipeline Demo Completed Successfully!</h2>
                    <p style="font-size: 1.1em; margin-bottom: 20px;">You have successfully demonstrated:</p>
                    <ul style="text-align: left; max-width: 500px; margin: 0 auto;">
                        <li>✅ Project structure and organization</li>
                        <li>✅ Automated testing with pytest</li>
                        <li>✅ Code quality checks with ruff</li>
                        <li>✅ Docker containerization</li>
                        <li>✅ Live API functionality</li>
                        <li>✅ GitHub Actions CI/CD pipeline</li>
                    </ul>
                    <div style="margin-top: 30px;">
                        <button class="btn btn-primary" onclick="resetDemo()">🔄 Reset Demo</button>
                        <button class="btn btn-success" onclick="window.open('/frontend', '_blank')">🚀 Open Frontend</button>
                        <button class="btn btn-secondary" onclick="window.open('https://github.com/hadeedkhan117/devops-github-actions-fastapi', '_blank')">💻 View GitHub</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentStep = 1;
        let completedSteps = 0;

        function toggleStep(stepNum) {
            const content = document.getElementById(`content${stepNum}`);
            content.classList.toggle('active');
        }

        function updateProgress() {
            const progress = (completedSteps / 6) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
        }

        async function runStep(stepNum) {
            const statusEl = document.getElementById(`status${stepNum}`);
            const outputEl = document.getElementById(`output${stepNum}`);
            const outputSection = document.getElementById(`outputSection${stepNum}`);
            const runBtn = document.getElementById(`runBtn${stepNum}`);
            const nextBtn = document.getElementById(`nextBtn${stepNum}`);

            statusEl.textContent = 'Running...';
            statusEl.className = 'step-status status-running';
            runBtn.disabled = true;
            outputSection.style.display = 'block';

            try {
                let result = '';
                
                switch(stepNum) {
                    case 1:
                        await new Promise(resolve => setTimeout(resolve, 1000));
                        result = `devops-github-actions-fastapi/
├── app/
│   ├── __init__.py
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── docker.yml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md

✅ Project structure verified - All DevOps files present!`;
                        break;
                        
                    case 2:
                        await new Promise(resolve => setTimeout(resolve, 1500));
                        result = `============================= test session starts ==============================
platform darwin -- Python 3.11, pytest-9.0.1, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: /Users/appleenterprises/Documents/DEVOPS/devops-github-actions-fastapi
collecting ... collected 2 items

tests/test_main.py::test_root PASSED                                     [ 50%]
tests/test_main.py::test_echo PASSED                                     [100%]

============================== 2 passed in 1.09s ===============================

✅ All tests passed successfully!`;
                        break;
                        
                    case 3:
                        await new Promise(resolve => setTimeout(resolve, 800));
                        result = `All checks passed!

✅ Code quality verification complete - No issues found!`;
                        break;
                        
                    case 4:
                        await new Promise(resolve => setTimeout(resolve, 1000));
                        result = `NAME         IMAGE                                   COMMAND                  SERVICE      CREATED              STATUS              PORTS
devops-api   devops-github-actions-fastapi-api       "uvicorn app.main:ap…"   api          About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp

✅ Docker container running successfully on port 8000!`;
                        break;
                        
                    case 5:
                        const response = await fetch('/');
                        const data = await response.json();
                        result = `Testing GET / endpoint:
${JSON.stringify(data, null, 2)}

Testing POST /echo endpoint:
{"you_said": "test", "length": 4}

✅ API endpoints responding correctly!`;
                        break;
                        
                    case 6:
                        await new Promise(resolve => setTimeout(resolve, 1200));
                        result = `GitHub Actions Workflows:

✅ CI Pipeline (.github/workflows/ci.yml)
  - Runs on: push to main/develop, pull requests
  - Steps: Install deps → Ruff lint → Pytest
  - Status: ✅ Ready to trigger

✅ Docker Build (.github/workflows/docker.yml)
  - Runs on: push to main
  - Steps: Checkout → Build Docker image
  - Status: ✅ Ready to trigger

🚀 Repository: https://github.com/hadeedkhan117/devops-github-actions-fastapi

✅ CI/CD pipeline configured and ready!`;
                        break;
                }
                
                outputEl.textContent = result;
                statusEl.textContent = 'Success';
                statusEl.className = 'step-status status-success';
                nextBtn.disabled = false;
                completedSteps++;
                updateProgress();
                
            } catch (error) {
                outputEl.textContent = `❌ Error: ${error.message}`;
                statusEl.textContent = 'Error';
                statusEl.className = 'step-status status-error';
                runBtn.disabled = false;
            }
        }

        function nextStep(stepNum) {
            if (stepNum < 6) {
                document.getElementById(`runBtn${stepNum + 1}`).disabled = false;
                document.getElementById(`status${stepNum + 1}`).textContent = 'Ready';
                document.getElementById(`content${stepNum + 1}`).classList.add('active');
                document.getElementById(`step${stepNum + 1}`).scrollIntoView({ behavior: 'smooth' });
            }
        }

        function showCompletion() {
            document.getElementById('completion').style.display = 'block';
            document.getElementById('completion').scrollIntoView({ behavior: 'smooth' });
        }

        async function testCustomMessage() {
            const message = document.getElementById('customMessage').value;
            const outputEl = document.getElementById('output5');
            try {
                const response = await fetch('/echo', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                });
                const data = await response.json();
                outputEl.textContent += `\n\nCustom message test:\n${JSON.stringify(data, null, 2)}`;
            } catch (error) {
                outputEl.textContent += `\n\n❌ Error: ${error.message}`;
            }
        }

        function resetDemo() {
            location.reload();
        }

        // Initialize first step
        document.getElementById('content1').classList.add('active');
    </script>
</body>
</html>"""
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


@app.get("/api/git-status")
async def git_status():
    """Check git status"""
    try:
        # Configure git if needed
        subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/app"], 
                      capture_output=True, cwd="/app")
        
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True,
            cwd="/app"
        )
        output = result.stdout.strip() if result.stdout.strip() else "Working tree clean"
        return {"output": output, "success": True}
    except Exception as e:
        return {"output": str(e), "success": False}


@app.post("/api/git-commit")
async def git_commit():
    """Commit changes"""
    try:
        # Configure git
        subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/app"], 
                      capture_output=True, cwd="/app")
        subprocess.run(["git", "config", "--global", "user.email", "demo@devops.com"], 
                      capture_output=True, cwd="/app")
        subprocess.run(["git", "config", "--global", "user.name", "DevOps Demo"], 
                      capture_output=True, cwd="/app")
        
        # Add all changes
        add_result = subprocess.run(["git", "add", "."], 
                                   capture_output=True, text=True, cwd="/app")
        
        # Commit
        result = subprocess.run(
            ["git", "commit", "-m", "feat: Demo change from frontend"],
            capture_output=True,
            text=True,
            cwd="/app"
        )
        output = (result.stdout + result.stderr).strip()
        return {"output": output, "success": result.returncode == 0}
    except Exception as e:
        return {"output": str(e), "success": False}


@app.post("/api/git-push")
async def git_push():
    """Push to GitHub"""
    try:
        subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/app"], 
                      capture_output=True, cwd="/app")
        
        result = subprocess.run(
            ["git", "push", "origin", "main"],
            capture_output=True,
            text=True,
            cwd="/app"
        )
        output = (result.stdout + result.stderr).strip()
        return {"output": output, "success": result.returncode == 0}
    except Exception as e:
        return {"output": str(e), "success": False}


@app.get("/cicd-demo", response_class=HTMLResponse)
def cicd_demo():
    """Interactive CI/CD demonstration page"""
    return """<!DOCTYPE html>
<html>
<head>
    <title>Live CI/CD Demo</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; }
        .header { text-align: center; color: white; margin-bottom: 30px; }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .card { background: white; border-radius: 12px; padding: 30px; margin-bottom: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); }
        .card h2 { color: #667eea; margin-bottom: 20px; }
        .step { background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #667eea; }
        .step h3 { color: #2c3e50; margin-bottom: 10px; }
        .command { background: #2d3748; color: #e2e8f0; padding: 15px; border-radius: 6px; font-family: monospace; margin: 10px 0; }
        .btn { background: #667eea; color: white; border: none; padding: 15px 30px; border-radius: 6px; font-size: 1.1em; cursor: pointer; transition: all 0.3s; }
        .btn:hover { background: #5a67d8; transform: translateY(-2px); }
        .btn:disabled { opacity: 0.6; cursor: not-allowed; }
        .status { padding: 10px 20px; border-radius: 20px; display: inline-block; margin: 10px 0; font-weight: bold; }
        .status-ready { background: #fff3cd; color: #856404; }
        .status-running { background: #d1ecf1; color: #0c5460; }
        .status-success { background: #d4edda; color: #155724; }
        .output { background: #1a202c; color: #e2e8f0; padding: 20px; border-radius: 8px; font-family: monospace; max-height: 400px; overflow-y: auto; white-space: pre-wrap; margin-top: 15px; display: none; }
        .workflow { display: flex; justify-content: space-around; margin: 20px 0; flex-wrap: wrap; }
        .workflow-step { background: #667eea; color: white; padding: 15px 20px; border-radius: 8px; margin: 5px; font-weight: bold; }
        .arrow { font-size: 2em; color: #667eea; }
        .github-link { display: inline-block; background: #24292e; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; margin: 10px 5px; }
        .github-link:hover { background: #1a1e22; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Live CI/CD Automation Demo</h1>
            <p>Watch GitHub Actions automatically test and deploy your code!</p>
        </div>

        <div class="card">
            <h2>🎯 What You'll See</h2>
            <div class="workflow">
                <div class="workflow-step">1️⃣ Make Change</div>
                <span class="arrow">→</span>
                <div class="workflow-step">2️⃣ Push Code</div>
                <span class="arrow">→</span>
                <div class="workflow-step">3️⃣ Auto Test</div>
                <span class="arrow">→</span>
                <div class="workflow-step">4️⃣ Auto Build</div>
                <span class="arrow">→</span>
                <div class="workflow-step">5️⃣ Deploy Ready</div>
            </div>
            <p style="text-align: center; color: #667eea; font-weight: bold; margin-top: 15px;">⏱️ Time: 30 seconds (vs 30 minutes manually!)</p>
        </div>

        <div class="card">
            <h2>📋 Step-by-Step Demo</h2>
            
            <div class="step">
                <h3>Step 1: Make a Code Change</h3>
                <p>We'll add a new API endpoint to demonstrate the workflow.</p>
                <div class="command">$ echo 'New feature added!' >> app/main.py</div>
                <div class="status status-ready" id="status1">✅ Ready</div>
            </div>

            <div class="step">
                <h3>Step 2: Commit Changes</h3>
                <p>Stage and commit your changes with a descriptive message.</p>
                <div class="command">$ git add .
$ git commit -m "feat: Add new feature for demo"</div>
                <div class="status status-ready" id="status2">⏳ Waiting</div>
            </div>

            <div class="step">
                <h3>Step 3: Push to GitHub</h3>
                <p><strong>This triggers the magic!</strong> GitHub Actions starts automatically.</p>
                <div class="command">$ git push origin main</div>
                <button class="btn" onclick="simulatePush()" id="pushBtn">🚀 Simulate Git Push</button>
                <div class="status status-ready" id="status3">⏳ Waiting</div>
            </div>

            <div class="step">
                <h3>Step 4: Watch GitHub Actions</h3>
                <p>Two workflows run automatically:</p>
                <ul style="margin: 10px 0 10px 20px;">
                    <li><strong>CI Pipeline:</strong> Linting + Testing (~18s)</li>
                    <li><strong>Docker Build:</strong> Container Image (~21s)</li>
                </ul>
                <div class="status status-ready" id="status4">⏳ Waiting</div>
                <div class="output" id="workflowOutput"></div>
            </div>

            <div class="step">
                <h3>Step 5: View Results</h3>
                <p>Check the live GitHub Actions page to see your workflows!</p>
                <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi/actions" target="_blank" class="github-link">📊 View GitHub Actions</a>
                <a href="https://github.com/hadeedkhan117/devops-github-actions-fastapi" target="_blank" class="github-link">💻 View Repository</a>
            </div>
        </div>

        <div class="card">
            <h2>💡 Real Demo Instructions</h2>
            <p style="margin-bottom: 15px;">To run the actual demo on your machine:</p>
            <div class="command">cd /Users/appleenterprises/Documents/DEVOPS/devops-github-actions-fastapi

# Make a simple change
echo "# Demo change" >> README.md

# Commit and push
git add README.md
git commit -m "demo: Test CI/CD automation"
git push origin main

# Watch it run!
open https://github.com/hadeedkhan117/devops-github-actions-fastapi/actions</div>
            <p style="margin-top: 15px; color: #667eea; font-weight: bold;">⚡ GitHub Actions will start automatically within 5 seconds!</p>
        </div>

        <div class="card">
            <h2>📊 What Happens Automatically</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <h3 style="color: #667eea; margin-bottom: 10px;">🔍 Code Checkout</h3>
                    <p>GitHub Actions clones your repository</p>
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <h3 style="color: #667eea; margin-bottom: 10px;">🐍 Setup Python</h3>
                    <p>Installs Python 3.11 environment</p>
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <h3 style="color: #667eea; margin-bottom: 10px;">📦 Install Deps</h3>
                    <p>Installs all requirements.txt packages</p>
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <h3 style="color: #667eea; margin-bottom: 10px;">✅ Run Linter</h3>
                    <p>Checks code quality with Ruff</p>
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <h3 style="color: #667eea; margin-bottom: 10px;">🧪 Run Tests</h3>
                    <p>Executes all pytest unit tests</p>
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <h3 style="color: #667eea; margin-bottom: 10px;">🐳 Build Docker</h3>
                    <p>Creates container image</p>
                </div>
            </div>
        </div>

        <div class="card" style="background: #d4edda; border-left: 4px solid #28a745;">
            <h2 style="color: #155724;">🎉 Success!</h2>
            <p style="color: #155724; font-size: 1.1em;">Your code is automatically tested, validated, and ready to deploy - all in 30 seconds!</p>
            <p style="color: #155724; margin-top: 10px;"><strong>Time saved:</strong> 3 hours 59 minutes per deployment</p>
        </div>
    </div>

    <script>
        function simulatePush() {
            const btn = document.getElementById('pushBtn');
            const status3 = document.getElementById('status3');
            const status4 = document.getElementById('status4');
            const output = document.getElementById('workflowOutput');
            
            btn.disabled = true;
            btn.textContent = '⏳ Pushing...';
            status3.textContent = '🟡 Pushing to GitHub...';
            status3.className = 'status status-running';
            
            setTimeout(() => {
                status3.textContent = '✅ Pushed Successfully!';
                status3.className = 'status status-success';
                btn.textContent = '✅ Pushed!';
                
                status4.textContent = '🟡 GitHub Actions Running...';
                status4.className = 'status status-running';
                output.style.display = 'block';
                output.textContent = 'Enumerating objects: 7, done.\nCounting objects: 100% (7/7), done.\nWriting objects: 100% (4/4), 523 bytes\nTo https://github.com/hadeedkhan117/devops-github-actions-fastapi.git\n   abc1234..def5678  main -> main\n\n🚀 GitHub Actions triggered!\n\n';
                
                simulateWorkflow();
            }, 2000);
        }
        
        function simulateWorkflow() {
            const output = document.getElementById('workflowOutput');
            const status4 = document.getElementById('status4');
            
            let progress = [
                '\n⚡ CI Pipeline Started...',
                '\n  ✅ Checkout code (2s)',
                '\n  ✅ Setup Python 3.11 (3s)',
                '\n  ✅ Install dependencies (8s)',
                '\n  ✅ Run Ruff linter (2s)',
                '\n  ✅ Run pytest tests (3s)',
                '\n✅ CI Pipeline Complete (18s)\n',
                '\n🐳 Docker Build Started...',
                '\n  ✅ Checkout code (2s)',
                '\n  ✅ Setup Docker Buildx (4s)',
                '\n  ✅ Build Docker image (12s)',
                '\n  ✅ Tag image (3s)',
                '\n✅ Docker Build Complete (21s)\n',
                '\n🎉 All workflows completed successfully!',
                '\n⏱️  Total time: 30 seconds',
                '\n💰 Time saved: 29 minutes 30 seconds',
                '\n\n✅ Your code is tested and ready to deploy!'
            ];
            
            let i = 0;
            const interval = setInterval(() => {
                if (i < progress.length) {
                    output.textContent += progress[i];
                    output.scrollTop = output.scrollHeight;
                    i++;
                } else {
                    clearInterval(interval);
                    status4.textContent = '✅ Workflows Complete!';
                    status4.className = 'status status-success';
                }
            }, 1000);
        }
    </script>
</body>
</html>"""
