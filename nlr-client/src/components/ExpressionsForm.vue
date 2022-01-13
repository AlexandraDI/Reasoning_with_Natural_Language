<template>
  <fieldset name="form" class="list-group p-4 border-end border-bottom border-start tab-content">

    <div v-for="(item, index) in expressions" :key="index" class="expression_input pb-1">
      <label class="form-label">{{index + 1}}. input:</label>
      <input type="text" :value="item.value" placeholder="Next Expression"
             class="form-control" v-on:input="propagate_modification($event, index)"/>
      <i role="button" class="icon-button mx-1 bi bi-dash-circle" v-on:click="remove_field($event, index)" :class="{disabled: expressions.length === 1}"></i>
      <i role="button" class="icon-button mx-1 bi bi-plus-circle" v-on:click="add_field" :class="{disabled: expressions.length === 1}" v-if="index === expressions.length-1"></i>
      <br>
    </div>

    <div class="expression_input mt-3">
      <label class="form-label">To be shown:</label>
      <input type="text" :value="to_be_shown" v-on:input="propagate_modification($event, -1)" class="form-control"/>
      <br>
    </div>

    <div class="expression_input mt-3">
      <label class="form-label">Reasoning method:</label>
      <select class="form-select" :value="reasoning_method" v-on:input="propagate_modification($event, 'reasoning_method')">
        <option value="complete">Multiple Tableaus ("complete way")</option>
        <option value="reasoningbycases">Reasoning by Cases</option>
      </select>
    </div>

    <div class="card my-3">
      <div class="card-body">
        <i class="bi bi-question-circle" style="font-size: 30px; position: absolute; top: 10px; right:20px"></i>
        <h5 class="card-title">Proof-Algorithm</h5>
        <h6 class="card-subtitle mb-2 text-muted">{{reasoning_method_title}}</h6>
        {{reasoning_method_description}}
      </div>
    </div>

    <button v-on:click="submit" type="button" class="btn btn-primary"
            style="margin-top: 8px;">Solve
    </button>
  </fieldset>
</template>

<script>
import * as assert from "assert";
import "bootstrap-icons/font/bootstrap-icons.css";

export default {
  name: "ExpressionsForm",
  props: {
    expressions: Array,
    to_be_shown: String,
    reasoning_method: String
  },
  computed: {
    reasoning_method_title: function() {
      switch (this.reasoning_method) {
        case "complete":
          return "Multiple Tableaus (Complete Way)";
        case "reasoningbycases":
          return "Reasoning by Cases";
        default:
          assert(false);
          return "";
      }
    },
    reasoning_method_description: function() {
      switch (this.reasoning_method) {
        case "complete":
          return "This method solves proves by solving multiple tableaus.";
        case "reasoningbycases":
          return "This method solves by doing a reasoning by cases.";
        default:
          assert(false);
          return "";
      }
    }
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
    width: 150px;
  }

  .expression_input > input, select {
    display: inline-block;
    width: 450px;
    transform: translateY(2px);
  }

  .icon-button {
    font-size: 25px;
  }
</style>