<template>
  <div class="accordion mb-4" :id="accordionId">
    <div class="accordion-item">
      <h1
          class="accordion-header"
          :id="headingId"
      >
        <button
            class="accordion-button"
            :class="{collapsed: defaultCollapsed}"
            type="button"
            data-bs-toggle="collapse"
            :data-bs-target="'#'+collapseId"
            :aria-expanded="!defaultCollapsed"
            :aria-controls="collapseId"
        >
          <span class="fs-3">
              {{this.title}}
          </span>
        </button>
      </h1>
      <div
          :id="collapseId"
          class="accordion-collapse collapse"
          :class="{show: !defaultCollapsed}"
          :aria-labelledby="headingId"
          :data-bs-parent="'#'+accordionId"
      >
        <div class="accordion-body">
          <slot/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Collapsable",
  props: ["title", "id", "defaultCollapsed"],
  mounted() {
    console.log(this);
  },
  computed: {
    collapseId: function() {
      return 'collapse'+this.id;
    },
    accordionId: function () {
      return 'accordion' + this.id;
    },
    headingId: function () {
      return 'heading-' + this.id;
    }
  }
}
</script>

<style scoped>

</style>