import Auth from '~/components/authentificate/index.vue'
import Youtube from '~/components/youtube/index.vue'
import Menus from '~/components/menu/index.vue'
import Profile from '~/components/profile/index.vue'
import profileedit from '~/components/profile-edit/index.vue'
export default {


  components: {
    Auth,
    Menus,
    Youtube,
    Profile,
    profileedit,
  },
  name: 'app',
  data() {
    return
      
  },


data() {
    return {
      data: {
      },
    }
  },

computed: {
  getKey() {
    return this.$store.getters.GET_KEY;
  },
},


  created() {

  },

  mounted() {
    var key = this.$store.getters['store/GET_KEY'];

  },

  methods: {
   
  }
}
