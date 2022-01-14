<template>
  <div>
    <ReasoningExamplesMenu
      @on-select-example="set_reasoning_expression"
    />
    <ExpressionsForm
        v-bind:expressions="this.expressions"
        v-bind:to_be_shown="this.to_be_shown"
        v-bind:reasoning_method="this.reasoning_method"
        @submit="send_request"
        @change-expression="this.modify_expression"
        @add-expression="this.add_expression"
        @remove-expression="this.remove_expression"
    />



    <div :style="{'display': response && error == null ? 'block' : 'none'}">

      <div class="card mt-3 p-2">
        <div class="card-body">

          <div v-if="numSolutionTrees === 1">
            <SolutionPane id="singular_solution" :tree_closes="tree_closes[0]" :support="supports[0]" :applied_rules="applied_rules[0]" :graph="graphs[0]"/>
          </div>

          <div v-if="numSolutionTrees > 1">
            The proof of these expressions requires {{numSolutionTrees}} tableaus. You can watch these in the tabs below.

            <div class="accordion mt-4" id="accordionTableaus">

              <div class="accordion-item" v-for="index in numSolutionTrees" :id="'multipleTableausItem' + index-1" :key="(index-1)">
                <h2 class="accordion-header" :id="'multipleTableausItemHeading' + (index-1)">
                  <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="'#multipleTableausItemCollapse' + (index-1)" :aria-expanded="(index-1) !== numSolutionTrees - 1" :aria-controls="'multipleTableausItemCollapse' + (index-1)">
                    Tableau Nr. {{index}}
                  </button>
                </h2>
                <div :id="'multipleTableausItemCollapse' + (index-1)" class="accordion-collapse collapse" :class="{show: (index-1) === numSolutionTrees - 1}" :aria-labelledby="'multipleTableausItemHeading' + (index-1)" data-bs-parent="#accordionTableaus">
                  <div class="accordion-body">
                    <!-- Is the tree_closes property correct like this? Don't we need a property like this for every tableau that we have? //-->
                    <SolutionPane :id="(index-1)" :tree_closes="tree_closes[(index-1)]" :support="supports[(index-1)]" :applied_rules="applied_rules[(index-1)]" :graph="graphs[(index-1)]"/>
                  </div>
                </div>
              </div>

            </div>

          </div>

        </div>
      </div>
    </div>

  </div>
</template>

<script>
import ReasoningExamplesMenu from "@/components/reasoner/ReasoningExamplesMenu";
import axios from "axios";
import ExpressionsForm from "@/components/ExpressionsForm";
import SolutionPane from "@/components/reasoner/SolutionPane";
export default {
  name: "ReasonerPage",
  components: {SolutionPane, ReasoningExamplesMenu, ExpressionsForm},
  data() {
    return {
      expressions: [""],
      to_be_shown: "",
      reasoning_method: "complete",
      response: null,
      error: null,
      tree_closes: [],
      applied_rules: [],
      graphs: [],
      supports: []
    };
  },
  computed: {
    numSolutionTrees: function() {
      return this.applied_rules ? this.applied_rules.length : 0;
    }
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
      if(index === "reasoning_method")
        this.reasoning_method = value;
      else if(index < 0)
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
      let data = {expressions: this.expressions, to_be_shown: this.to_be_shown, reasoning_method: this.reasoning_method};

      axios
          .post('/solve-request', data)
          .then(response => {

            const responseData = response.data;

            // get body data
            this.response = responseData;
            this.applied_rules = responseData['applied_rules']
            this.tree_closes = responseData['all_branches_closed']
            this.supports = responseData["supports"];

            this.$emit("set-error", null);
            this.graphs = responseData["dot_graphs"];
          })
          .catch(error => {
            const data = error.response.data;
            this.$emit("set-error", data);
            this.graphs = [];
            this.response = null;
          });

    }
  },
}
</script>

<style scoped>

</style>