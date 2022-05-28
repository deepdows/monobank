<template>
  <main class="form-signin">
    <form @submit.prevent="setLogin">
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

      <div class="form-floating">
        <input
          v-model="username"
          type="text"
          class="form-control"
          id="floatingInput"
          placeholder="Username"
        />
        <label for="floatingInput">Username</label>
      </div>
      <div class="form-floating">
        <input
          v-model="password"
          type="password"
          class="form-control"
          id="floatingPassword"
          placeholder="Password"
        />
        <label for="floatingPassword">Password</label>
      </div>
      <p class="text-danger" v-if="message">{{ message }}</p>

      <button class="w-100 btn btn-lg btn-primary" type="submit">
        Sign in
      </button>
    </form>
  </main>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      login: "",
      password: "",
      message: "",
    };
  },
  methods: {
    setLogin() {
      const creds = {
        username: this.username,
        password: this.password,
      };
      fetch(window.location.origin + "/api/login/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
          "x-access-token": "token-value",
        },
        body: JSON.stringify(creds),
      })
        .then(async (response) => {
          const data = await response.json();
          if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
          }

          localStorage.setItem("auth_token", data.token);
          this.$router.push("/");
        })
        .catch((error) => {
          this.message = error;
          console.error("There was an error!", error);
        });
    },
  },
};
</script>

<style lang="scss">
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 100px auto;
}



.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>