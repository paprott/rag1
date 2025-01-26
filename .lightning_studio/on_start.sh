
#!/bin/bash

# This script runs every time your Studio starts, from your home directory.

# List files under fast_load that need to load quickly on start (e.g. model checkpoints).
#
# ! fast_load
# /teamspace/studios/this_studio/qdrant_storage/**

# Add your startup commands below.
#
# Example: streamlit run my_app.py
# Example: gradio my_app.py

# pip install langchain_ollama
docker-compose up -d