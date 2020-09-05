<template>
    <div>
      <v-btn 
      color="primary"
        @click="handleClickSignIn"
        v-if="!isSignIn"
        :disabled="!isInit"
        dark
        text
      >sign in</v-btn >
      <v-btn 
      color="primary"
        @click="handleClickSignOut"
        v-if="isSignIn"
        :disabled="!isInit"
        dark
      >sign out</v-btn >
    </div>
</template>

<script>
/* eslint-disable */
export default {
  props: {
    msg: String,
  },
  data() {
    return {
      isInit: false,
      isSignIn: false,
    };
  },
  methods: {
    handleClickLogin() {
      this.$gAuth
        .getAuthCode()
        .then((authCode) => {
          //on success
          console.log("authCode", authCode);
        })
        .catch((error) => {
          //on fail do something
        });
    },

    async handleClickSignIn() {
      try {
        const googleUser = await this.$gAuth.signIn();
        if (!googleUser) {
          return null;
        }
        console.log("googleUser", googleUser);
        console.log("getId", googleUser.getId());
        console.log("getBasicProfile", googleUser.getBasicProfile());
        console.log("getAuthResponse", googleUser.getAuthResponse());
        console.log(
          "getAuthResponse",
          this.$gAuth.GoogleAuth.currentUser.get().getAuthResponse()
        );
        this.isSignIn = this.$gAuth.isAuthorized;
      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },

    async handleClickSignOut() {
      try {
        await this.$gAuth.signOut();
        this.isSignIn = this.$gAuth.isAuthorized;
        console.log("isSignIn", this.$gAuth.isAuthorized);
      } catch (error) {
        console.error(error);
      }
    },
  },

  created() {
    let that = this;
    let checkGauthLoad = setInterval(function () {
      that.isInit = that.$gAuth.isInit;
      that.isSignIn = that.$gAuth.isAuthorized;
      if (that.isInit) clearInterval(checkGauthLoad);
    }, 1000);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
</style>
