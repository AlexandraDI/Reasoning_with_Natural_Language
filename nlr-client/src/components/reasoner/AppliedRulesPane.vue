<template>
  <div>
    <div class="accordion mb-4" id="accordionAppliedRule" v-if="appliedRules.length !== 0">
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
              <div class="accordion-item" v-for="(rule, index) in appliedRules" :key="index">
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
  </div>
</template>

<script>
export default {
  name: "AppliedRulesPane",
  props: ["appliedRules"]
}
</script>

<style scoped>

</style>