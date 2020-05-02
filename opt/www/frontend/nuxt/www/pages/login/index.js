import Hello from '~/components/hello/index.vue'
import axios from 'axios';
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
        urls: '/api/v1/auth/login/',
        username: false,
        email: false,
        password: false,
        msg: '',
      },
    }
  },

  created() {

  },

  mounted() {


  },

  methods: {
    async loginUser() {
      const data = { 'email': this.email, 'password': this.password }
      //const headers = {'Authorization': `Token ${token}`}
      try{
      await this.$axios
        .post(
          this.data.urls,
          data, 
          )
        .then(response => {
        console.log(response);
          if (response.status==200){
            this.data.msg = "Успешно";
            document.cookie = "token="+response.data.key;

          setTimeout(() => {
            //this.$nuxt.$router.replace({ path: '/'});
            // или
                //this.$router.replace({ path: '/' });
                window.location.href = '/'
              }, 1000)

          }else{
            this.data.msg = "Ошибка";
          }

        });
      } catch (err) {
      this.data.msg = "Ошибка";
      }

    },

  }
}
