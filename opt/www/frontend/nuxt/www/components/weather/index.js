import axios from 'axios';
export default {
  components: {
  },
  name: 'app',
  data () {
    return { info: 'default' }
  },

  created() {
    this.getInfo();
  },

  mounted() {

  },

  methods: {

    async getInfo() {
      await this.$axios
        .$get('/api/v2/weather')
        .then(response => {
           this.info = response[0];
        });
    },


     
   
  }
}

