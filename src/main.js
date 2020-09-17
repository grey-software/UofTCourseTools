/* eslint-disable */

import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import "@mdi/font/css/materialdesignicons.css";
import ToggleButton from "vue-js-toggle-button";
import VueMobileDetection from "vue-mobile-detection";
import VueAnalytics from "vue-analytics";
import VueHtml2Canvas from 'vue-html2canvas';
import SmoothScrollbar from 'vue-smooth-scrollbar'
import GAuth from 'vue-google-oauth2'

Vue.config.productionTip = false;

const gauthOption = {
    clientId: '159393917339-7748u4ult18di6d9cosejo4kbcva0bpj.apps.googleusercontent.com',
    scope: 'profile email',
    prompt: 'select_account'
}
Vue.use(GAuth, gauthOption)
Vue.use(SmoothScrollbar)
Vue.use(VueHtml2Canvas);
Vue.use(ToggleButton);
Vue.use(VueMobileDetection);
Vue.use(VueAnalytics, {
    id: "UA-165919387-2",
    router
});

new Vue({
    router,
    store,
    vuetify,
    render: (h) => h(App),
}).$mount("#app");
