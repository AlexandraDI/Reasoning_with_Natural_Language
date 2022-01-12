<template>
  <div>
    <ReasoningExamplesMenu
      @on-select-example="set_reasoning_expression"
    />
    <ExpressionsForm
        v-bind:expressions="this.expressions"
        v-bind:to_be_shown="this.to_be_shown"
        @submit="send_request"
        @change-expression="this.modify_expression"
        @add-expression="this.add_expression"
        @remove-expression="this.remove_expression"
    />

    <div :style="{'display': response && error == null ? 'block' : 'none'}">
      <div class="card my-4"
           :class="{'bg-success': tree_closes, 'bg-danger': !tree_closes}">
        <h2 v-if="tree_closes" class="display-5 text-center">The statement is valid</h2>
        <h2 v-if="!tree_closes" class="display-5 text-center">There is a branch that doesn't
          close</h2>
      </div>

      <SupportPane
        v-bind:support="support"
        />

      <AppliedRulesPane
        v-bind:applied-rules="applied_rules"
        />


      <p v-if="response">*You can hover over each node to receive a more detailed explanation of the
        applied rule.</p>
    </div>
    <TreeGraph v-bind:graph-data="this.graphData" v-bind:applied-rules="this.applied_rules"/>
  </div>
</template>

<script>
import ReasoningExamplesMenu from "@/components/reasoner/ReasoningExamplesMenu";
import axios from "axios";
import ExpressionsForm from "@/components/ExpressionsForm";
import TreeGraph from "@/components/reasoner/TreeGraph";
import AppliedRulesPane from "@/components/reasoner/AppliedRulesPane";
import SupportPane from "@/components/reasoner/SupportPane";
export default {
  name: "ReasonerPage",
  components: {SupportPane, AppliedRulesPane, TreeGraph, ReasoningExamplesMenu, ExpressionsForm},
  data() {
    return {
      expressions: [""],
      to_be_shown: "",
      response: null,
      error: null,
      tree_closes: true,
      applied_rules: [],
      graphData: null,
      support: null
    };
  },
  methods: {
    set_reasoning_expression(expressions, to_be_shown) {
      this.expressions = expressions
      this.to_be_shown = to_be_shown

      /*let myDropdown = document.getElementById(selected_example)
      if (myDropdown)
        myDropdown.classList.remove("show");*/
    },
    modify_expression(index, value) {
      if(index < 0)
        this.to_be_shown = value;
      else
        this.expressions[index]["value"] = value;
    },
    add_expression() {
      this.expressions.push({value: ""});
    },
    remove_expression(index) {
      this.expressions.splice(index, 1);
    },
    send_request() {
      this.error = null
      let data = {expressions: this.expressions, to_be_shown: this.to_be_shown};

      axios
          .post('/solve-request', data)
          .then(response => {

            const responseData = response.data;

            // get body data
            this.response = responseData;
            this.applied_rules = responseData['applied_rules']
            this.tree_closes = JSON.parse(responseData['all_branches_closed'])
            this.support = responseData.support;

            this.$emit("set-error", null);
            this.graphData = responseData["dot_graph"];
          })
          .catch(error => {
            const data = error.response.data;
            this.$emit("set-error", data);
            this.graphData = null;
            this.response = null;
          });

    }
  },
}
</script>

<style scoped>

</style>