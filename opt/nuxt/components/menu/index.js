import axios from 'axios';
import VueCsrf from 'vue-csrf';
import Weather from '~/components/weather/index.vue'
export default {
  components: {
    Weather,
    VueCsrf,
  },
  name: 'app',
  data () {
    return {
    info: 'default',
    auth: false,
    key: 0,
    }
  },

  created() {
    this.key = this.getToken();
  },

  mounted() {
  this.key = this.getToken();
  },

  methods: {
    getToken() {
      var key = this.$store.getters['store/GET_KEY'];
      if (!key) {
        key = this.$cookies.get('token');
      }
      return key;
    },

    async logoutUser() {
      await this.$axios.$get('/api/v1/auth/logout/');
      this.$store.dispatch('store/SET_KEY', 0);
      this.$cookies.set('token', 0, {path:window.location.hostname});
      //this.$router.replace({ path: '/' });
      document.location.href = '/';
      this.auth=false;
    },


  }
}

