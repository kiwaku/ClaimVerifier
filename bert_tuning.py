from transformers import BertTokenizer, TFBertForSequenceClassification, BertConfig
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    # Load the dataset
    file_path = 'exported_cleaned.csv'  # Make sure to update this path
    data = pd.read_csv(file_path)

    # Initialize the tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Tokenize the sentences from the 'text' column
    tokenized_data = tokenizer(data['text'].tolist(), padding=True, truncation=True, max_length=512, return_tensors="tf")
    input_ids = tokenized_data['input_ids'].numpy()  # Convert to numpy for train_test_split
    attention_mask = tokenized_data['attention_mask'].numpy()  # Convert to numpy for train_test_split

    # Prepare labels from the 'label' column (assuming 'Y' is 1 and 'N' is 0)
    labels = data['label'].apply(lambda x: 1 if x == 'Y' else 0).to_numpy()  # Convert labels to numpy array

    # Split the data into training and validation sets
    train_inputs, val_inputs, train_labels, val_labels = train_test_split(input_ids, labels, test_size=0.1, random_state=42)
    train_masks, val_masks, _, _ = train_test_split(attention_mask, labels, test_size=0.1, random_state=42)

    # Load the BERT configuration and specify the number of labels
    config = BertConfig.from_pretrained('bert-base-uncased', num_labels=2)

    # Load the BERT model for sequence classification
    model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', config=config)

    # Compile the model
    optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5)
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

    # Train the model
    model.fit([train_inputs, train_masks], train_labels, batch_size=8, epochs=3, validation_data=([val_inputs, val_masks], val_labels))

    # Evaluate the model
    model.evaluate([val_inputs, val_masks], val_labels)

    # Save the model
    save_path = 'bert_model'  # Update this path
    model.save_pretrained(save_path)

if __name__ == "__main__":
    main()
