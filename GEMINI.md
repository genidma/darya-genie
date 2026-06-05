# Darya Genie Project Instructions

This project is associated with the Google Cloud Project: `darya-genie`.

## Google Cloud Configuration
- **Project ID:** `darya-genie`
- **Region:** `us-central1` (Default)

## Gemini CLI Extension: Vertex AI
The Vertex AI extension is used for prompt management and optimization. Ensure the following APIs are enabled in the `darya-genie` project:
- Vertex AI API (aiplatform.googleapis.com)

## Branching Strategy
- Features are developed in isolated branches, integrated into `main-dev` for consolidated testing and security validation, and promoted to `main` only for stable releases.
