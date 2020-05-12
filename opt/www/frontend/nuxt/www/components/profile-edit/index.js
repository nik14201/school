import axios from 'axios';
export default {
  components: {},
  name: 'app',
  data() {
    return {
      data: {
        url_facebook: '',
        url_vk: '',
        email: '',
        skype: '',
        avatar: '',

      }
    }
  },

  created() {
    this.getData();
  },

  mounted() {

  },

  methods: {

    getToken() {
      var key = this.$store.getters['store/GET_KEY'];
      if (!key) {
        key = this.$cookies.get('token');
      }
      return key;
    },

    async getData() {
      var key = this.getToken();
      const headers = { 'Authorization': `Token ${key}` }
      await this.$axios
        .$get('/api/v1/auth/profile/', { headers: headers })
        .then(response => {
          this.data = response;
        });
    },


    handleFileUpload() {
      this.data.avatar = this.$refs.file.files[0];
    },

    async saveProfile() {
      var formData = new FormData(profile);
      const data = {
        'url_facebook': this.data.url_facebook,
        'url_vk': this.data.url_vk,
        'email': this.data.email,
        'skype': this.data.skype,
      }

      var key = this.getToken();
      const headers = { 'Authorization': `Token ${key}` }
      //const headers = {'Authorization': `Token ${key}`, 'Content-Type': 'multipart/form-data', 'Content-Disposition': 'attachment; filename=this.data.avatar.name'}
      await this.$axios
        .$patch('/api/v1/auth/profile/', formData, { headers: headers })
        .then(response => {
          //this.data = response;
          setTimeout(() => {
            //this.$nuxt.$router.replace({ path: '/'});
            this.$router.replace({ path: '/profile/' });
            //window.location.href = '/'
          }, 1000)
        });
    },
  }
}
