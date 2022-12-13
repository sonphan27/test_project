module.exports = {
  devServer: {
    proxy: {
      '^/(api|docs|openapi.json|redoc)': {
        target: 'http://api:8000',
        ws: true,
        changeOrigin: true
      },
    }
  }
}