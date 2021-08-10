import { createApp } from 'vue'
import {
    Layout,
    Col,
    Row,
    Card,
    Divider,
  } from 'ant-design-vue';
import App from './App.vue'

const app = createApp(App);
app.config.productionTip = false;
app.use(Layout);
app.use(Col);
app.use(Row);
app.use(Card);
app.use(Divider);
app.mount('#app');
