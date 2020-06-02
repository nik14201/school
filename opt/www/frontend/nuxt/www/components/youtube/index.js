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
    getToken(){
            var key =  this.$store.getters['store/GET_KEY'];
      if(!key){
        key=this.$cookies.get('token');
      }
      return key;
    },

    async getInfos() {
      await this.$axios
        .$get('/api/v1/youtube/')
        .then(response => {
          this.info = response;
        });
    },




  }
}

