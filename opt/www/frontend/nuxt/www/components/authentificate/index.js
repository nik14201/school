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
                  window.location.href = '/login/'
                }
              }, 1000)

    this.getData();
  },

  methods: {

    getData() {
      console.log('111');
      this.$axios
        .$get('api/v1/auth/isauth/')
        .then(response => {
          console.log(response);
          this.login = response.authentificate;
        });
        console.log('222', this.login);
        
    },


     
   
  }
}
