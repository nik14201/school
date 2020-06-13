
export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },


  router: {
    extendRoutes (routes, resolve) {
      routes.push(
      {
        path: '/homework/read/:hw/',
        components: {
          default: resolve(__dirname, 'pages/homework/read/index.vue'), // or routes[index].component
        },
        chunkNames: {
          //modal: 'components/modal'
        }
      },

     {
        path: '/homework/',
        components: {
          default: resolve(__dirname, 'pages/homework/index.vue'), // or routes[index].component
        },
        chunkNames: {
          //modal: 'components/modal'
        }
      },
      )

    }
  },









  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [

   ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  { src: '~plugins/ym.js', mode: 'client' },
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
  '@nuxtjs/axios',
  'cookie-universal-nuxt',
  'nuxt-sass-resources-loader',
  'bootstrap-vue/nuxt',
  '@nuxtjs/axios',
    [
    '@nuxtjs/yandex-metrika',
    {
        id:56657455,
        webvisor: true,
        clickmap:true,
        useCDN:false,
        trackLinks:true,
        accurateTrackBounce:true,
        ecommerce:"dataLayer",
      }
  ],
  ],

axios: {
    proxy: true
  },

  /*
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
