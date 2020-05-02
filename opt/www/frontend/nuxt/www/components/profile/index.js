import axios from 'axios';
export default {
  components: {
  },
  name: 'app',
  data () {
    return { data: 'default' }
  },

  created() {
    this.getData();
  },

  mounted() {

  },

  methods: {

    async getData() {
      await this.$axios
        .$get('/api/v1/auth/profile/')
        .then(response => {
          this.data = response[0];
        });
    },


     
   
  }
}
