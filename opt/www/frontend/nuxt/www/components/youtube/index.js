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
      var key =  this.getToken();
      const headers = {'Authorization': `Token ${key}`}
      await this.$axios
        .$get('/api/v1/youtube/', { headers: headers })
        .then(response => {
          this.info = response;
          console.log(response);
        });
    },


     
   
  }
}

