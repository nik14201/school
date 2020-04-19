import axios from 'axios';
export default {
  components: {
  },
  name: 'app',
  data() {
    
  },

  created() {
    
  },

  mounted() {
   	  var  data = {username:'user@gmail.com', password:'123456', password2:'123456'}
      this.axios
          .post('/api/v1/registrations', data)
          .then(response => {
            alert(response.data);
            
          });
  },

  methods: {

    CreateUser(){
      //alert("OK");
      var data={
              "username": "dfs@mail.ru",
              "password":"123456",
              "password2":"123456"
              }
          this.$axios
                .post('https://perspective.local/api/v1/registrations', data)
                .then(response => {
   
                })
                .catch(function(e){
                    this.error = e;
                });

    },

   
  }
}
