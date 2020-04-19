import Weather from '~/components/weather/index.vue'
import Profile from '~/components/profile/index.vue'
import Youtube from '~/components/youtube/index.vue'
import Menus from '~/components/menu/index.vue'
export default {
  head: {
    title: 'Web разработчик Django',
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'Web - разработчик  - Django  - python - docker - golang - купить сайт - разработка на django - создать сайт - web разработчик' },
    { name: 'yandex-verification', content: 'a98cac2d5ce2e9a9' }
  ],
},
  components: {
    Weather,
    Profile,
    Youtube,
    Menus,
  },
  name: 'app',
  data() {
    
  },

  created() {

  },

  mounted() {
   this.ym(56657455, "init", {});

  },

  methods: {

}
}

