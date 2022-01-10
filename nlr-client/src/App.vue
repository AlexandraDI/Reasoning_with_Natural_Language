<template>
  <div id="app">
        <main>

            <application-header></application-header>

            <ModeSwitcher @switch-page="change_page"></ModeSwitcher>


            <div class="tab-content" id="pills-tabContent">
                <div class="tab-pane" id="reasoner" role="tabpanel" aria-labelledby="reasoner-tab">
                  <ReasonerPage
                      @display-tree="display_tree"
                      @set-error="set_error"
                  />
                </div>
                <div class="tab-pane" id="language" role="tabpanel" aria-labelledby="language-tab">
                  <LanguageCheckerPage
                    @set-error="set_error"
                    />
                </div>
            </div>

            <ErrorBox
              v-bind:error="this.error"
              />

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
        </main>
        <div id="graph" class="graph" :class="{border: graph_rendered}"></div>
        <div v-if="response || language_output" style="height: calc(0.5 * 100vh)"></div>
    </div>
</template>

<script>
import Vue from 'vue'
import VueRouter from 'vue-router'
import * as $ from 'jquery'


import 'jquery-ui-dist/jquery-ui.js'
import 'jquery-ui-dist/jquery-ui.min.css'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle';

import ApplicationHeader from './components/ApplicationHeader.vue'
import ModeSwitcher from "@/components/ModeSwitcher";
import ReasonerPage from "@/components/reasoner/ReasonerPage";
import LanguageCheckerPage from "@/components/languageChecker/LanguageCheckerPage";
import ErrorBox from "@/components/ErrorBox";

Vue.use(VueRouter)
const router = new VueRouter({});

export default {
  name: 'App',
  components: {
    ErrorBox,
    LanguageCheckerPage,
    ReasonerPage,
    ApplicationHeader,
    ModeSwitcher,
  },
  data() {
    return {
      expressions: [],
      to_be_shown: null,
      error: null,
      response: null,
      up: true,
      current_tab: 'Normal Examples',
      tabs: [],
      language_examples: [],
      sentence: 'When i love you then you love me',
      auto_send: true,
      language_output: null,
      tooltip_header: "",
      in_expressions: "",
      out_expressions: "",
      basic_in_expressions: "",
      basic_out_expressions: "",
      tooltip_description: "",
      tooltip_visible: false,
      topOffset: "0px",
      leftOffset: "0px",
      graph_rendered: false
    };
  },
  mounted() {
    if (window.location.hash === "#/language")
        this.change_page("language")
    else
        this.change_page("reasoner")

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
    change_page(to_page) {
      let reasoner_panel = document.getElementById("reasoner")
      let language_panel = document.getElementById("language")
      let reasoner_panel_tab = document.getElementById("reasoner-tab")
      let language_panel_tab = document.getElementById("language-tab")

      this.error = null;

      if (to_page === "reasoner") {
          reasoner_panel_tab.classList.add("active");
          reasoner_panel.classList.add("active");
          $("#graph").show();
          router.push("reasoner")
      } else {
          language_panel_tab.classList.add("active");
          language_panel.classList.add("active");

          $("#graph").hide();
          router.push("language")
      }

    },
    remove_field(index) {
        this.expressions.splice(index, 1);
    },
    add_field() {
        this.expressions.push(
            {value: ''}
        )
    },
    toggle_tooltip(element, enter) {
        let c_rule = this.applied_rules[element[0].id]['rule_desc_obj']
        let rule_object = JSON.parse(c_rule.replaceAll("\"", '`').replaceAll("'", '"'))

        this.tooltip_header = rule_object['name']
        this.in_expressions = rule_object['in_expression']
        this.out_expressions = rule_object['out_expression']
        this.basic_in_expressions = rule_object['basic_in_expression']
        this.basic_out_expressions = rule_object['basic_out_expression']
        this.tooltip_description = rule_object['description']

        this.tooltip_visible = enter
    },
    display_tree(dot_graph) {
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
    set_error(error) {
      this.error = error;
    }
  }
}
</script>

<style>
  html {
      height: 100%
  }

  main {
      max-width: 800px;
      min-width: 800px;
      margin-left: auto;
      margin-right: auto;
  }

  #graph > svg {
      width: 100%;
  }

  .graph {
      text-align: center;
      width: 70%;
      margin-left: auto;
      margin-right: auto;
  }
</style>
