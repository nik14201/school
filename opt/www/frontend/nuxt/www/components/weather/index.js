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

    async getInfo() {
      await this.$axios
        .$get('/api/v1/weather/')
        .then(response => {
           this.info = response[0];
        });
    },


     
   
  }
}

