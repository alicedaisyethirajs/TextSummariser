Overview

This project is a simple yet powerful AI-driven text summarization web application built using Hugging Face Transformers and Gradio. The application takes long-form text as input and generates a concise, meaningful summary using a pre-trained transformer model.

It demonstrates how to integrate a state-of-the-art NLP model into an interactive web interface with minimal setup.

Model Details

Model Used: sshleifer/distilbart-cnn-12-6

Architecture: Distilled BART (optimized for summarization tasks)

Framework: PyTorch

Library: Hugging Face Transformers

The selected model is a lightweight, distilled version of BART fine-tuned specifically for text summarization, offering a strong balance between performance and efficiency.

Tech Stack

Python

PyTorch

Hugging Face Transformers

Gradio


Features

Instant Summarization
Converts long paragraphs into concise summaries in seconds.

Optimized Performance
Utilizes torch.bfloat16 to reduce memory usage while maintaining output quality.

Clean and Interactive UI
Built with Gradio for a simple and user-friendly interface.

Pre-trained Transformer Deployment
Demonstrates real-world usage of a production-ready NLP model.