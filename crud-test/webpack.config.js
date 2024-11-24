const path = require('path');

module.exports = {
    entry: './apps/static/src/js/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'apps/static/dist'), 
    },
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                },
            },
            {
                test: /\.css$/, 
                use: [
                    'style-loader',
                    'css-loader',
                    'postcss-loader', 
                ],
            },
        ],
    },
    resolve: {
        extensions: ['.js'],
    },
};
