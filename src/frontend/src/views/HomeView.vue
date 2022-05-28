<template>
  <div class="home">
    <button @click="getCards">Refresh</button>
    <div v-for="card in cards" :key="card.balance">
      <div class="card">
        <p class='card__num'>{{card.card}}</p>
        <p class='card__balance'>{{card.balance}} UAH</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      cards: []
    };
  },
  mounted() {
    this.getCards()
  },
  computed: {
    auth() {
      if (localStorage.getItem("auth_token")) {
        return true;
      }
    },
  },
  methods: {
    goLogin() {
      this.$router.push({ name: "login" });
    },
    logout() {
      localStorage.removeItem("auth_token");
      this.$router.push({ name: "home" });
    },
    getCards(){
      fetch(window.location.origin + "/api/cards/", {
        method: "get",
        headers: {
          "Content-Type": "application/json",
          "x-access-token": "token-value",
          "Authorization": "Bearer " + localStorage.getItem("auth_token")
        },
      })
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }
          this.cards = data
        })
        .catch((error) => {
          console.log(error)
          if (error === 'Unauthorized'){
            this.goLogin()
          }
          this.message = error;
          console.error("There was an error!", error);
        });
    }
  },
};
</script>

<style lang="scss">
  .card{
    margin: 10px;
    border-radius: 10px;
    background: rgb(124, 239, 214);
    max-width: 400px;
    aspect-ratio: 5/3;
    font-weight: 500;
    &__num{
      margin: 20px 10px;
    }
    &__balance{
      font-size: 26px;
      margin: 70px 10px 0;
    }
  }
</style>