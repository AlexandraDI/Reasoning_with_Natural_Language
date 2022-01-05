<template>
  <ul class="nav nav-tabs" role="tablist">
    <li class="nav-item" :key="tab.tab_name" v-for="tab in data" :class="{ dropdown: tab.examples.length > 1}" role="presentation">
      <a v-if="tab.examples.length === 1" class="nav-link" :class="{ active: tab.tab_name === current_tab}" href="#"
         aria-current="page" v-on:click="selectExample(tab, 0)">{{tab.tab_name}}</a>

      <a v-if="tab.examples.length > 1" class="nav-link dropdown-toggle" data-toggle="dropdown"
         :class="{ active: tab.tab_name === current_tab}" data-bs-toggle="dropdown"
         data-bs-auto-close="true" href="#" aria-expanded="false">{{tab.tab_name}}</a>

      <ul v-if="tab.examples.length > 1" class="dropdown dropdown-menu" role="menu"
          v-bind:id="tab.tab_name">
        <li v-for="(example, index) in tab.examples" :key="index">
          <a class="dropdown-item" href="#" v-on:click="selectExample(tab, index)">{{example.name}}</a>
        </li>
      </ul>
    </li>
  </ul>
</template>

<script>
import axios from "axios";

export default {
  name: "ReasoningExamplesMenu",
  mounted() {
    axios
        .get('/examples?name=reasoner_examples.json')
        .then(response => {
          this.data = response['data'];
          this.selectExample(this.data[0], 0);
        });
  },
  data() {
    return {
      data: {},
      current_tab: ""
    };
  },
  methods: {
    selectExample(tab, index) {
      this.current_tab = tab.tab_name;
      const selectedExample = tab.examples[index];

      const to_be_shown = selectedExample["to_be_shown"];
      const expressions = selectedExample["expressions"];

      this.$emit("on-select-example", expressions, to_be_shown);

      //Little Hack: Otherwise dropdowns don't close :(
      let myDropdown = document.getElementById(tab.tab_name)
      if (myDropdown)
        myDropdown.classList.remove("show");
    }
  }
}
</script>

<style scoped>

</style>