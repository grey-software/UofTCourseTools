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
import VueAgile from 'vue-agile'

Vue.config.productionTip = false;

Vue.use(VueAgile)
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
