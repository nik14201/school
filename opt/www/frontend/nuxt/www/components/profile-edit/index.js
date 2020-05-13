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
      var formData = new FormData(avatar);
      var key = this.getToken();
      const headers = { 'Authorization': `Token ${key}` }
      this.$axios
        .$patch('/api/v1/auth/profile/', formData, { headers: headers })
        .then(response => {
          setTimeout(() => {
            this.getData();
            this.$router.replace({ path: '/profile/edit' });
          }, 1000)
        });

    },

    async saveProfile() {
      var formData = new FormData(profile);
      var key = this.getToken();
      const headers = { 'Authorization': `Token ${key}` }
      await this.$axios
        .$patch('/api/v1/auth/profile/', formData, { headers: headers })
        .then(response => {
          setTimeout(() => {
            this.$router.replace({ path: '/profile/' });
          }, 1000)
        });
    },
  }
}
