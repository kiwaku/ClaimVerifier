const path = require('path');

module.exports = {
  entry: 'my-chrome-extension/src/index.js', // Adjust based on your project structure
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      }
    ]
  },
  resolve: {
    fallback: { "path": false, "fs": false } // Depending on tokenizer's dependencies, you might need to adjust fallbacks
  }
};
