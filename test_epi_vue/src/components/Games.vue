<template>
  <div class="q-pa-md row items-start q-gutter-md" v-if="!loading && data && data.length">
    <q-card dark bordered class="bg-grey-9 my-card" v-for="game of data" v-bind:key="game.id">
      <q-card-section>
        <div class="text-h6">{{ game.name }}</div>
        <div class="text-subtitle2">by {{ game.developer }}</div>
      </q-card-section>

      <q-separator dark inset />

      <q-card-section>
        {{ game.platform }}
      </q-card-section>
    </q-card>
  </div>
  <p v-if="loading">
    Still Loading ...
  </p>
  <p v-if="error">
    Error !!!
  </p>
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
          loading.value = false;
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

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
</style>