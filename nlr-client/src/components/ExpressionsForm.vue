<template>
  <fieldset name="form" class="list-group p-4 border-end border-bottom border-start tab-content">
    <div v-for="(item, index) in expressions" :key="index" class="expression_input pb-1">
      <label class="form-label">{{index + 1}}. input:</label>
      <input type="text" :value="item.value" placeholder="Next Expression"
             class="form-control" v-on:input="propagate_modification($event, index)"/>
      <button v-on:click="remove_field($event, index)"  type="button" class="btn btn-danger"
              :class="{disabled: expressions.length === 1}">-
      </button>
      <button v-if="index === expressions.length-1" v-on:click="add_field" type="button"
              class="btn btn-success">+
      </button>
      <br>
    </div>

    <div class="expression_input">
      <label>To be shown:</label>
      <input type="text" :value="to_be_shown" v-on:input="propagate_modification($event, -1)" class="form-control"/>
      <br>
    </div>
    <button v-on:click="submit" type="button" class="btn btn-primary"
            style="margin-top: 8px;">Solve
    </button>
  </fieldset>
</template>

<script>
export default {
  name: "ExpressionsForm",
  props: {
    expressions: Array,
    to_be_shown: String
  },
  methods: {
    submit() {
      this.$emit("submit");
    },
    add_field() {
      this.$emit("add-expression");
    },
    remove_field(event, index) {
      this.$emit("remove-expression", index);
    },
    propagate_modification(event, index) {
      this.$emit("change-expression", index, event.target.value);
    }
  }
}
</script>

<style scoped>
  .expression_input > label {
    display: inline-block;
    width: 100px;
  }

  .expression_input > input {
    display: inline-block;
    width: 500px;
    transform: translateY(2px);
  }
</style>