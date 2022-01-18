<template>
  <div class="card my-3" v-if="numDefeatedExpressions > 0 || !contradictionInformation.is_contradiction_resolved">
    <Card
      title="Contradiction Information"
      icon="bi-lightning-charge-fill"
      :icon-color="contradictionInformation.is_contradiction_resolved ? 'green' : 'red'"
    >
      <div v-if="!contradictionInformation.is_contradiction_resolved">
        There is a contradiction which could not be resolved. Please check the input for contradictions and remove or fix them.
      </div>

      <div v-if="contradictionInformation.is_contradiction_resolved">
        There {{numDefeatedExpressions === 1 ? "is" : "are"}} {{numDefeatedExpressions}} defeasible {{numDefeatedExpressions === 1 ? "expression" : "expressions"}} which {{numDefeatedExpressions === 1 ? "is" : "are"}} overridden by non-defeasible information. In this overview you can see the defeasible expression and then the expressions which lead to this defeasible expression being overridden. There is also a reasoning graph explaining the process.

        <div class="mt-2" v-for="def_exp_index in contradictionInformation.defeated_defeasible_expressions.length" :key="def_exp_index">
          <Card
              :title="contradictionInformation.defeated_defeasible_expressions[def_exp_index-1]"
              class="my-3"
          >
            <ul class="list-group mb-3">
              <li class="list-group-item" v-for="(exp, list_item_index) in contradictionInformation.contradiction_information[def_exp_index-1]" :key="list_item_index">{{exp}}</li>
            </ul>
            <Collapsable
                :id="'defeasibleTreeGraph'+def_exp_index"
                title="Defeasible Tree Graph"
                :default-collapsed="true"
            >
              <TreeGraph
                  id="contradiction"
                  :graph-data="contradictionInformation.contradicting_graph[def_exp_index-1]"
              />
            </Collapsable>
          </Card>

        </div>
      </div>
    </Card>
  </div>
</template>

<script>
import TreeGraph from "@/components/reasoner/TreeGraph";
import Collapsable from "@/components/Collapsable";
import Card from "@/components/Card";
export default {
  name: "ContradictionCard",
  components: {Card, TreeGraph, Collapsable},
  props: ["contradictionInformation"],
  mounted() {
    console.log(this.contradictionInformation);
  },
  computed: {
    numDefeatedExpressions: function() {
      return this.contradictionInformation.defeated_defeasible_expressions.length;
    }
  }
}
</script>

<style scoped>

</style>