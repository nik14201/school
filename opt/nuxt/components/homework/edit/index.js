import axios from 'axios';
export default {
  components: {},
  name: 'app',
  data() {
    return {
      hw: this.$router.currentRoute.params['hw'],
      data: {
      name: '',
      text: '',
      lesson: '',

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
        .$get('/api/v1/homework/'+this.hw, { headers: headers })
        .then(response => {
          this.data = response[0];
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

    async saveForm() {
      var formData = new FormData(formedit);
      var key = this.getToken();
      const headers = { 'Authorization': `Token ${key}` }
      await this.$axios
        .$patch('/api/v1/homework/'+this.hw, formData, { headers: headers })
        .then(response => {
          setTimeout(() => {
            this.$router.replace({ path: '/homework/' });
          }, 1000)
        });
    },
  }
}
