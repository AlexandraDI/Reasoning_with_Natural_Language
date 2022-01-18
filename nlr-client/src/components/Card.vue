<template>
  <div class="card">
    <div class="card-body">
      <i v-if="icon" :class="'bi ' + icon" style="font-size: 30px; position: absolute; top: 10px; right:20px"></i>
      <h5 class="card-title">{{title}}</h5>
      <h6 v-if="subTitle" class="card-subtitle mb-2 text-muted">{{subTitle}}</h6>
      <slot/>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: ["title", "subTitle", "icon"]
}
</script>

<style scoped>

</style>