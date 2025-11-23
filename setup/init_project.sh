#!/bin/bash
# Setup Script for Project Enigma
# Usage: source setup/init_project.sh

echo "🕵️‍♂️ Initializing Project Enigma Environment..."

# 1. Check Google Cloud SDK
if ! command -v gcloud &> /dev/null;
then
    echo "❌ gcloud CLI not found. Please install it or use Cloud Shell."
    return
fi

# 2. Set Project
if [ -z "$GOOGLE_CLOUD_PROJECT" ];
then
    echo "⚠️  GOOGLE_CLOUD_PROJECT is not set."
    echo "   Please run: gcloud config set project YOUR_PROJECT_ID"
    echo "   Then run this script again."
    return
else
    echo "✅ Using Project: $GOOGLE_CLOUD_PROJECT"
fi

# 3. Enable Base APIs
echo "⏳ Enabling essential APIs (Service Usage, Cloud Build, Cloud Run)..."
gcloud services enable \
    serviceusage.googleapis.com \
    cloudbuild.googleapis.com \
    run.googleapis.com \
    sqladmin.googleapis.com \
    artifactregistry.googleapis.com \
    --project "$GOOGLE_CLOUD_PROJECT"

echo "✅ APIs Enabled."

# 4. Python Setup
if [ ! -d ".venv" ];
then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv .venv
fi

echo "✅ Environment initialized. Run 'source .venv/bin/activate' to begin."
