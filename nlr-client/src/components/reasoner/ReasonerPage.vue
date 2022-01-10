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

      <div class="accordion mb-4" id="accordionAppliedRule" v-if="applied_rules.length !== 0">
        <div class="accordion-item">
          <h1 class="accordion-header" id="heading-applied-rule">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapseAppliedRule" aria-expanded="false"
                    aria-controls="collapseAppliedRule">
                                      <span class="fs-3">
                                          Applied Rules
                                      </span>
            </button>
          </h1>
          <div id="collapseAppliedRule" class="accordion-collapse collapse"
               aria-labelledby="heading-applied-rule" data-bs-parent="#accordionAppliedRule">
            <div class="accordion-body">
              <div id="accordion" class="accordion">
                <div class="accordion-item" v-for="(rule, index) in applied_rules" :key="index">
                  <h1 class="accordion-header" :id="'heading-applied-rule-' + index"
                      v-if="index !== 'root_node'">
                    <button class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse"
                            :data-bs-target="'#collapseAppliedRule-' + index"
                            aria-expanded="false"
                            :aria-controls="'collapseAppliedRule-' + index">
                                                      <span class="fs-5">
                                                          {{rule.rule_name}}
                                                      </span>
                    </button>
                  </h1>
                  <div :id="'collapseAppliedRule-' + index"
                       class="accordion-collapse collapse" data-bs-parent="#accordion">
                    <div class="accordion-body">
                      <table class="table">
                        <thead>
                        <tr>
                          <th scope="col">Referenced Line</th>
                          <th scope="col" v-if="rule.created_expressions">Created
                            Expressions
                          </th>
                          <th scope="col">Used Expression</th>
                          <th scope="col"
                              v-if="rule.matched_expression !== 'None'">
                            Matched
                            Expression
                          </th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td>{{rule.referenced_line}}</td>
                          <td v-if="rule.created_expressions">
                            <ul>
                              <li v-for="(expression_list, index) in rule.created_expressions" :key="index">
                                {{expression_list}}
                              </li>
                            </ul>
                          </td>
                          <td>{{rule.c_expression}}</td>
                          <td v-if="rule.matched_expression !== 'None'">
                            {{rule.matched_expression}}
                          </td>
                        </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

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
export default {
  name: "ReasonerPage",
  components: {TreeGraph, ReasoningExamplesMenu, ExpressionsForm},
  data() {
    return {
      expressions: [""],
      to_be_shown: "",
      response: null,
      error: null,
      tree_closes: true,
      applied_rules: [],
      graphData: null
    };
  },
  methods: {
    set_reasoning_expression(expressions, to_be_shown) {
      console.log("set_example_reasoning_expression", expressions, to_be_shown);
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
      console.log("send_request");
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

            this.$emit("set-error", null);
            this.graphData = responseData["dot_graph"];
          })
          .catch(error => {
            const data = error.response.data;
            this.$emit("set-error", data);
            this.$emit("display-tree", null);
          });

    }
  },
}
</script>

<style scoped>

</style>