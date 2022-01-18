<template>
  <div>
    <!-- Branches close or not card //-->
    <div class="card mb-4"
         :class="{'bg-success': tree_closes, 'bg-danger': !tree_closes}">
      <h2 v-if="tree_closes" class="display-5 text-center">The statement is valid</h2>
      <h2 v-if="!tree_closes" class="display-5 text-center">There is a branch that doesn't
        close</h2>
    </div>

    <SupportPane v-if="support.length > 0" v-bind:support="this.support"/>

    <AppliedRulesPane v-bind:applied-rules="this.applied_rules"/>

    <p>*You can hover over each node to receive a more detailed explanation of the
      applied rule.</p>
    <TreeGraph v-bind:graph-data="this.graph" :id="id" v-bind:applied-rules="this.applied_rules"/>

  </div>
</template>

<script>
import SupportPane from "@/components/reasoner/SupportPane";
import AppliedRulesPane from "@/components/reasoner/AppliedRulesPane";
import TreeGraph from "@/components/reasoner/TreeGraph";

export default {
  name: "SolutionPane",
  components: {SupportPane, AppliedRulesPane, TreeGraph},
  props: ["id", "tree_closes", "support", "applied_rules", "graph"]
}
</script>

<style scoped>

</style>