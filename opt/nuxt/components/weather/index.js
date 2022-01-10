import axios from 'axios';
import bsidebar from 'bootstrap-vue'
export default {
  components: {
    bsidebar,
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
    getToken(){
            var key =  this.$store.getters['store/GET_KEY'];
      if(!key){
        key=this.$cookies.get('token');
      }
      return key;
    },

    async getInfo() {
      var key =  this.getToken();
      const headers = {'Authorization': `Token ${key}`}
      await this.$axios
        .$get('/api/v1/weather/',  { headers: headers })
        .then(response => {
           this.info = response[0];
        });
    },


     
   
  }
}

