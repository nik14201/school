import Hello from '~/components/hello/index.vue'

export default {


  components: {

  },
  name: 'app',
  data() {
    return
      
  },


data() {
    return {
      data: {
         username: false,
         email: false,
         password: false,
      },
    }
  },

  created() {

  },

  mounted() {


  },

  methods: {
    createUser(){
      //alert("OK");
       const data = {'email':this.email, 'password': this.password}
       console.log(data);
       const {response} = this.$axios.post('/api/v2/auth/users/', data)

    }
   
  }
}
