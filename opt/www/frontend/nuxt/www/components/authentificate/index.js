import axios from 'axios';
import { mapState } from 'vuex'
export default {
  components: {
  },
  name: 'app',
  data () {
    return { 
      data: 'default',
      login:false,

    }
  },

  created() {
        //this.getData();

  },

  mounted() {
    this.getData();
    setTimeout(() => {
                if(!this.login){
                  this.$router.replace({ path: '/login/' });
                }

              }, 1000)

    this.getData();
  },

  methods: {

    getToken(){
            var key =  this.$store.getters['store/GET_KEY'];
      if(!key){
        key=this.$cookies.get('token');
      }
      return key;
    },

    getData() {
      var key =  this.getToken();
      var headers = {'Authorization': `Token ${key}`}
      this.$axios
        .$get('api/v1/auth/isauth/', { headers: headers })
        .then(response => {
          console.log(response);
          this.login = response.authentificate;
        });
        console.log('222', this.login);
        
    },


     
   
  }
}
