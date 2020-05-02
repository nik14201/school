import axios from 'axios';
export default {
  components: {
  },
  name: 'app',
  data () {
    return { info: 'default' }
  },

  created() {
    this.getInfos();
  },

  mounted() {

  },

  methods: {

    async getInfos() {
      await this.$axios
        .$get('/api/v1/youtube/')
        .then(response => {
          this.info = response;
          console.log(response);
        });
    },


     
   
  }
}

