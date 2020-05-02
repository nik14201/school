import axios from 'axios';
import Weather from '~/components/weather/index.vue'
export default {
  components: {
    Weather,
  },
  name: 'app',
  data () {
    return { info: 'default' }
  },

  created() {
    //this.getInfo();
  },

  mounted() {

  },

  methods: {

    // async getInfo() {
    //   await this.$axios
    //     .$get('/api/v2/menu')
    //     .then(response => {
    //       this.info = response;
    //       console.log(response);
    //     });
    // },

    async logoutUser() {
      await this.$axios
        .$post('/api/v1/auth/logout/')
        .then(response => {
          this.info = response;
          document.cookie = "csrftoken=";
        });
    },


  }
}

