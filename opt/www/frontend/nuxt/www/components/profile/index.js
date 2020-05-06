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

 getToken(){
            var key =  this.$store.getters['store/GET_KEY'];
      if(!key){
        key=this.$cookies.get('token');
      }
      return key;
    },

    async getData() {
      var key =  this.getToken();
      const headers = {'Authorization': `Token ${key}`}
      await this.$axios
        .$get('/api/v1/auth/profile/', { headers: headers })
        .then(response => {
          this.data = response;
        });
    },


     
   
  }
}
