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
        urls: 'api/v1/auth/registration/',
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
    async createUser() {
      const data = { 'email': this.email, 'password': this.password }
      try{
      await this.$axios
        .post(this.data.urls, data)
        .then(response => {
          if (response.status==201){
            this.data.msg = "Успешно";

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
