<template>
  <div class="card bg-danger mt-2" v-if="error">
    <div class="card-header">
                    <span class="lead" v-if="error.type === 'ParseException'">
                        Parse Exception
                    </span>
      <span class="lead" v-if="error.type !== 'ParseException'">
                        Internal Error
                    </span>
    </div>
    <div class="card-body">
      <div v-if="error.type !== 'ParseException'">
        <span class="lead">Oops something went wrong and we dont really know what.</span><br>
        <span class="lead">This could help tho: {{error.error}}</span>
      </div>
      <div v-if="error.type === 'ParseException'">
        <span class="lead">We detected a error in the parsing process</span><br>
        <span class="lead">This are the errors we collected along the way:</span><br>
        <ul>
          <li v-for="c_error in error.list" :key="c_error">{{c_error}}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ErrorBox",
  props: ["error"]
}
</script>

<style scoped>

</style>