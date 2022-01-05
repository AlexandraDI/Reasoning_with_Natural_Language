module.exports = {
    devServer: {
        /*proxy: {
            '^/api': {
                target: 'http://localhost:6543',
                ws: true,
                changeOrigin: true,
                logLevel: "debug"
            }
        }*/
        proxy: "http://localhost:6543"
    }
}