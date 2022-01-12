<template>
  <div>
    <div id="graph" class="graph" :class="{border: graph_rendered}"></div>
    <div id="tooltip" class="card"
         :style="{'display': tooltip_visible ? 'block' : 'none', 'top': topOffset, 'left': leftOffset}"
         style="position: fixed">
      <div class="card-header">{{tooltip_header}}</div>
      <div class="card-body">
        <table class="m-2" v-if="basic_in_expressions">
          <tr style="border-bottom: 2px solid black">
            <td style="text-align: center;">
                                <span v-for="(in_expression, index) in basic_in_expressions" :key="index">
                                    {{in_expression}}
                                    <span v-if="basic_in_expressions.length > 1 && index !== basic_in_expressions.length - 1">,</span>
                                </span>
            </td>
          </tr>
          <tr>
            <td style="text-align: center;">
                                <span v-for="(out_expression, index) in basic_out_expressions" :key="index">
                                    <span v-for="(out_inner_expression, index_2) in out_expression" :key="index_2">
                                        {{out_inner_expression}}<span
                                        v-if="out_expression.length > 1 && index_2 !== out_expression.length - 1">,</span>
                                    </span>
                                    <span v-if="basic_out_expressions.length > 1 && index !== basic_out_expressions.length - 1">|</span>
                                </span>
            </td>
          </tr>
        </table>
        <p v-if="basic_in_expressions">This rule applied looks like this:</p>
        <table class="m-2" v-if="in_expressions">
          <tr style="border-bottom: 2px solid black">
            <td style="text-align: center;">
                                <span v-for="(in_expression, index) in in_expressions" :key="index">
                                    {{in_expression}}
                                    <span v-if="in_expressions.length > 1 && index !== in_expressions.length - 1">,</span>
                                </span>
            </td>
          </tr>
          <tr>
            <td style="text-align: center;">
                                <span v-for="(out_expression, index) in out_expressions" :key="index">
                                    <span v-for="(out_inner_expression, index_2) in out_expression" :key="index_2">
                                        {{out_inner_expression}}
                                        <span v-if="out_expression.length > 1 && index_2 !== out_expression.length - 1">,</span>
                                    </span>
                                    <span v-if="out_expressions.length > 1 && index !== out_expressions.length - 1">|</span>
                                </span>
            </td>
          </tr>
        </table>
        <p class="m-2" v-html="tooltip_description"></p>
      </div>
    </div>
  </div>
</template>

<script>
import * as $ from "jquery";

export default {
  name: "TreeGraph",
  data() {
    return {
      graph_rendered: false,
      tooltip_visible: false,
      tooltip_description: "",
      topOffset: "0px",
      leftOffset: "0px",
      tooltip_header: "",
      in_expressions: "",
      out_expressions: "",
      basic_in_expressions: "",
      basic_out_expressions: "",
    };
  },
  mounted() {
    window.onmousemove = (e) => {
      if (this.tooltip_visible) {
        let x = e.clientX,
            y = e.clientY;
        this.topOffset = (y + 20) + 'px';
        this.leftOffset = (x + 20) + 'px';
      }
    };
  },
  methods: {
    display_tree(dot_graph) {
      if(dot_graph === null) {
        $("#graph").hide();
        return;
      }
      else
        $("#graph").show();

      if (this.graph_rendered)
          // eslint-disable-next-line no-undef
        d3.select("#graph").graphviz({useWorker: false}).resetZoom();
      // eslint-disable-next-line no-undef
      d3.select("#graph")
          .graphviz({useWorker: false})
          .on("renderEnd", () => {
            this.graph_rendered = true
            // eslint-disable-next-line no-undef
            let nodes = d3.selectAll(".node");
            for (let i = 0; i < nodes._groups[0].length; i++) {
              let c_node = nodes._groups[0][i]
              let c_node_children = $(c_node).children()
              $($(c_node_children[1]).children()[0]).children("polygon")[0].setAttribute("fill", "#ffffff")
              c_node_children[1].onpointerenter = (event) => {
                this.toggle_tooltip($(event.target).parent(), true);
              };
              c_node_children[1].onpointerleave = (event) => {
                this.toggle_tooltip($(event.target).parent(), false);
              };
            }
          })
          .renderDot(dot_graph);
    },
    toggle_tooltip(element, enter) {
      const rule_object = this.appliedRules[element[0].id]['rule_desc_obj']

      this.tooltip_header = rule_object['name']
      this.in_expressions = rule_object['in_expression']
      this.out_expressions = rule_object['out_expression']
      this.basic_in_expressions = rule_object['basic_in_expression']
      this.basic_out_expressions = rule_object['basic_out_expression']
      this.tooltip_description = rule_object['description']

      this.tooltip_visible = enter
    },
  },
  props: ["graphData", "appliedRules"],
  watch: {
    graphData: function (newVal, oldVal) {
        if(newVal !== oldVal)
          this.display_tree(newVal);
      }
  },

}
</script>

<style scoped>
  /deep/ svg {
    width: 100%;
  }

  .graph {
    text-align: center;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
</style>