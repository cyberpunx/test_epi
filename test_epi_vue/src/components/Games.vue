<template>
    <div id="components-layout-demo-basic">
        <a-layout>
            <a-layout-header>
                <p><strong>Lista de Juegos</strong></p>
            </a-layout-header>
            <a-layout-content>
                <a-card title="Juegos">
                    <a-card v-for="game of data" v-bind:key="game.id">
                        <p>{{ game.name }}</p>
                        <span>Desarrollador: {{ game.developer }}</span>
                        <br/>
                        <span>Plataforma: {{ game.platform }}</span>
                    </a-card>
                    <br />
                </a-card>
            </a-layout-content>
            <a-layout-footer>Epidata</a-layout-footer>
        </a-layout>
    </div>
</template>


<script>
import { onMounted, ref } from "vue";
export default {
  name: 'Games',
  props: {
  },
  setup() {
    const data = ref(null);
    const loading = ref(true);
    const error = ref(null);

    function fetchData() {
        loading.value = true;
        // I prefer to use fetch
        // you can use use axios as an alternative
        return fetch('http://localhost:8000/api/games/', {
            method: 'get',
            headers: {
            'content-type': 'application/json'
            }
        })
        .then(res => {
        // a non-200 response code
          if (!res.ok) {
              // create error instance with HTTP status text
              const error = new Error(res.statusText);
              error.json = res.json();
              throw error;
          }
          return res.json();
        })
        .then(json => {
          // set the response data
          data.value = json;
          loading.value = false;
        })
        .catch(err => {
          error.value = err;
          // In case a custom JSON error response was provided
          if (err.json) {
            return err.json.then(json => {
            // set the JSON response message
            error.value.message = json.message;
            });
          }
        });
    }

    onMounted(() => {
      fetchData();
    });


    return {
      data,
      loading,
      error
    };
  }
}
</script>

<style>
#components-layout-demo-basic {
  text-align: center;
}
#components-layout-demo-basic .ant-layout-header,
#components-layout-demo-basic .ant-layout-footer {
  background: #7dbcea;
  color: #fff;
}
#components-layout-demo-basic .ant-layout-footer {
  line-height: 1.5;
}
#components-layout-demo-basic .ant-layout-sider {
  background: #3ba0e9;
  color: #fff;
  line-height: 120px;
}
#components-layout-demo-basic .ant-layout-content {
  background: rgba(16, 142, 233, 1);
  color: #fff;
  min-height: 120px;
  line-height: 120px;
}
#components-layout-demo-basic > .ant-layout {
  margin-bottom: 48px;
}
#components-layout-demo-basic > .ant-layout:last-child {
  margin: 0;
}
</style>