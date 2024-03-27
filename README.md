# ClaimVerifier
Custom Google Chrome extension utilising Tensorflow, custom trained BERT and Node.js


# Overview
The Fact Check Assistant is a Chrome extension designed to assist users in identifying factual claims within online articles. The extension utilizes natural language processing (NLP) techniques, including fine-tuning a BERT model, to analyze text content and highlight potential claims or statements requiring further verification.

# Project Goals
Develop a Chrome extension to aid users in fact-checking while browsing online articles.
Implement NLP techniques to automatically detect and highlight potential factual claims within text content.
Provide users with a tool to assess the credibility of information presented in online articles more effectively.
# Key Features
Automatically highlight potential factual claims within online articles.
Integrate a fine-tuned BERT model to analyze text content for factual statements.
Provide users with visual cues to identify and verify claims while reading articles.
 # Getting Started
 # Installation
To install the Fact Check Assistant Chrome extension:

Clone this repository to your local machine.
Open Google Chrome and navigate to chrome://extensions/.
Enable Developer Mode in the top right corner.
Click on "Load unpacked" and select the directory containing the extension files.
# Usage
Once installed, the extension will be available in your Chrome browser toolbar. Simply click on the extension icon while viewing an online article to activate the fact-checking functionality. The extension will automatically analyze the text content and highlight potential claims for further examination.

# Development
Data Preparation
Clean and preprocess the dataset containing articles and sentences.
Manually annotate sentences in the dataset to identify facts or claims.
Model Training
Fine-tune a BERT model on the annotated dataset to identify claims or facts within sentences.
# Extension Development
Set up the project structure, including manifest.json, background.js, content.js, and other necessary files.
Integrate the fine-tuned BERT model into the extension for claim detection.
Debug and troubleshoot issues related to file paths, manifest configuration, and dependencies.
# Testing
Load and test the extension in Chrome to ensure it loads and functions correctly.
Address any remaining issues and refine the extension's functionality based on user feedback.
Contributing
Contributions to the Fact Check Assistant Chrome extension are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
