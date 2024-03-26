import * as tf from '@tensorflow/tfjs';
import { BertWordPieceTokenizer } from "tokenizers";

// Assuming you have a method to load the vocab file for the tokenizer.
// This might need to be adjusted based on how you're serving or bundling this file.
const tokenizer = new BertWordPieceTokenizer({ vocabFile: "my-chrome-extension/public/vocab.txt" });

let model;

async function loadModelAndTokenizer() {
    model = await tf.loadLayersModel(chrome.runtime.getURL('model/model.json'));
    await tokenizer.ready; // Make sure the tokenizer is ready before proceeding
    console.log("Model and tokenizer loaded successfully");
    // Additional setup or directly jump into processing
}

async function tokenizeText(text) {
    const encoded = await tokenizer.encode(text);
    console.log(encoded.tokens);
    // Use encoded.tokens, encoded.ids, etc., as needed for your model
}

async function highlightBasedOnModelPrediction(text) {
    // Tokenize the text
    const encoded = await tokenizer.encode(text);
    // Assuming you have a function to run model predictions and decide on what to highlight
    // This is a placeholder; you'll need logic here based on your model's specifics
}

// Load model and tokenizer when the script is loaded
loadModelAndTokenizer();

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    const exampleText = "Here's some text to tokenize and analyze with the model.";
    highlightBasedOnModelPrediction(exampleText);
});
