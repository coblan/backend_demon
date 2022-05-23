var path = require( 'path' );

var webpack = require('D:/coblan/webcode/node_modules/webpack')

const VueLoaderPlugin = require('D:/coblan/webcode/node_modules/vue-loader/lib/plugin')
// const VueLoaderPlugin = require('vue-loader/lib/plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin
var {CleanWebpackPlugin} = require('clean-webpack-plugin');
// var MiniCssExtractPlugin = require('mini-css-extract-plugin')

var webpack = require('webpack')

module.exports =
{
    //context:__dirname,
    mode:'development', //'production', //
    entry: {
        ui_editor:'./main.js',
        // fields:'./fields_main.js'
    },
    output: {
        // path:path.resolve(__dirname, '../static/js'),
        // filename: '[name].pack.js'
        path:path.resolve(__dirname, '../static/js'),
        filename: '[name].pack.js',
        // chunkFilename: 'jb_admin/[id].[chunkhash].js',
        chunkFilename: 'jb_admin/[id].js?h=[chunkhash]',
        publicPath:'/static/js/'

        // path:path.resolve(__dirname, '../static/'),
        // filename: 'js/[name].pack.js',
        // chunkFilename: 'js/jb_admin/[id].[chunkhash].js',
        // publicPath:'/static/'

    },
    optimization: {
        namedChunks: true
    },
    externals: {
        'vue': 'Vue',
        'vue-router': 'VueRouter',
        '@vue/composition-api':'VueCompositionAPI',
        // 'axios': 'axios',
        'element-ui': 'Element',
    },
    watch: true,
    resolve:{
        alias: {
            jb_admin: path.resolve(__dirname,"../../case/jb_admin/js"),
            webcase:'D:/coblan/webcase',
            weblib:'D:/coblan/weblib'
        },
        modules:["D:/coblan/webcode/node_modules"],
    },
    resolveLoader: {
        //moduleExtensions:["D:/coblan/webcode/node_modules"],
        modules: ["D:/coblan/webcode/node_modules"],
        //resolver:["D:/coblan/webcode/node_modules"],
    },
    module: {
        rules: [
            { test: /\.pug$/,
                loader: 'pug-plain-loader'
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets:[
                            require.resolve('@babel/preset-env')
                        ],
                        plugins: [
                            require.resolve("@babel/plugin-transform-runtime")
                        ]

                    }
                },
            },
            {
                test: /\.scss$/,
                use: [{
                    loader: "style-loader" // creates style nodes from JS strings
                }, {
                    loader: "css-loader" // translates CSS into CommonJS
                }, {
                    loader: "sass-loader" // compiles Sass to CSS
                }]
            },
            {
                test: /\.styl$/,
                use: [
                    {
                        loader: "style-loader" // creates style nodes from JS strings
                    },
                    {
                        loader: "css-loader" // translates CSS into CommonJS
                    },
                    {
                        loader: "stylus-loader" // compiles Stylus to CSS
                    }
                ]
            },
            {
                test: /\.less$/,
                use: [{
                    loader: 'style-loader' // creates style nodes from JS strings
                }, {
                    loader: 'css-loader' // translates CSS into CommonJS
                }, {
                    loader: 'less-loader' // compiles Less to CSS
                }]
            },
            // {
            //     test: /\.css$/,
            //     use: [
            //         process.env.NODE_ENV !== 'production'
            //             ? 'vue-style-loader'
            //             : MiniCssExtractPlugin.loader,
            //         'css-loader'
            //     ]
            // }
        ]

    },
    plugins: [
        new VueLoaderPlugin(),
        new CleanWebpackPlugin(),

        // new BundleAnalyzerPlugin(),

    ]
}



