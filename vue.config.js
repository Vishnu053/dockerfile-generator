module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  
  devServer: {
    proxy: 'https://hub.docker.com/',
}
}