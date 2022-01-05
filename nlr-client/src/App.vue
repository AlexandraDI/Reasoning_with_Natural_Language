<template>
  <div id="app">
        <main>

            <application-header></application-header>

            <ModeSwitcher @switch-page="change_page"></ModeSwitcher>


            <div class="tab-content" id="pills-tabContent">
                <div class="tab-pane" id="reasoner" role="tabpanel" aria-labelledby="reasoner-tab">
                  <ReasonerPage @display-tree="display_tree"/>
                </div>
                <div class="tab-pane" id="language" role="tabpanel" aria-labelledby="language-tab">
                    <h3>Language Check</h3>
                    <p>
                        Here you can check out what our constrained natural language is able to parse.
                        You can either write your own sentences or checkout the examples that we provided.
                    </p>

                    <!-- This next part encapsulates the examples in an collapsable accordion -->
                    <div class="accordion mb-4" id="accordionFlushExample">
                        <div class="accordion-item">
                            <h1 class="accordion-header" id="flush-headingOne">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                        data-bs-target="#flush-collapseOne" aria-expanded="false"
                                        aria-controls="flush-collapseOne">
                                    <span class="fs-3">
                                        Examples
                                    </span>
                                </button>
                            </h1>
                            <div id="flush-collapseOne" class="accordion-collapse collapse"
                                 aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
                                <div class="accordion-body">
                                    <div class="input-group mb-2">
                                        <div class="input-group-text">
                                            <input class="form-check-input mt-0" type="checkbox"
                                                   :value="auto_send"
                                                   aria-label="Checkbox for automatically sending the language request">
                                        </div>
                                        <span class="form-control">When selecting a language example, automatically send the request to the server.</span>
                                    </div>

                                    <div class="accordion mb-4" id="language_examples_accordion">
                                        <div class="accordion-item" v-for="(group, group_index) in language_examples" :key="group_index">
                                            <h3 class="accordion-header" :id="'group_heading_' + group_index">
                                                <button class="accordion-button collapsed" type="button"
                                                        data-bs-toggle="collapse"
                                                        :data-bs-target="'#group_collapse_' + group_index"
                                                        aria-expanded="true"
                                                        :aria-controls="'group_collapse_' + group_index">
                                                    {{group['group_name']}}
                                                </button>
                                            </h3>
                                            <div :id="'group_collapse_' + group_index"
                                                 class="accordion-collapse collapse"
                                                 :aria-labelledby="'group_heading_' + group_index"
                                                 data-bs-parent="#language_examples_accordion">
                                                <div class="accordion-body">
                                                    <div class="d-flex flex-row justify-content-between flex-wrap">
                                                        <button 
                                                          type="button" class="btn m-1 text-nowrap flex-grow-1"
                                                          :class="{'btn-outline-success': sentence != language_example, 'btn-success': sentence == language_example}"
                                                          v-for="language_example in group['examples']"
                                                          v-on:click="select_language_example(language_example)"
                                                          :key="language_example"
                                                        >
                                                            {{language_example}}
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <fieldset name="form" class="list-group border p-4">
                        <div class="pb-3">
                            <label class="w-100">
                                <span class="form-label">Test sentence:</span>
                                <input type="text" placeholder="Next Expression" class="form-control"
                                       :value="sentence"/>
                            </label>
                        </div>
                        <button type="button" class="btn btn-primary" v-on:click="language_request"
                                :class="{disabled: !sentence}">
                            Check
                        </button>
                    </fieldset>

                    <div class="container-fluid p-4">

                        <div v-html="create_sentence_presentation"
                             v-if="!error"
                             style="position: absolute; left: 50%; transform: translateX(-50%);">
                        </div>
                    </div>
                </div>
            </div>

            <div class="card bg-danger mt-2" v-if="error">
                <div class="card-header">
                    <span class="lead" v-if="error.type == 'ParseException'">
                        Parse Exception
                    </span>
                    <span class="lead" v-if="error.type != 'ParseException'">
                        Internal Error
                    </span>
                </div>
                <div class="card-body">
                    <div v-if="error.type != 'ParseException'">
                        <span class="lead">Oops something went wrong and we dont really know what.</span><br>
                        <span class="lead">This could help tho: {{error.error}}</span>
                    </div>
                    <div v-if="error.type == 'ParseException'">
                        <span class="lead">We detected a error in the parsing process</span><br>
                        <span class="lead">This are the errors we collected along the way:</span><br>
                        <ul>
                            <li v-for="c_error in error.list" :key="c_error">{{c_error}}</li>
                        </ul>
                    </div>
                </div>
            </div>

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
                                    <span v-if="basic_in_expressions.length > 1 && index != basic_in_expressions.length - 1">,</span>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: center;">
                                <span v-for="(out_expression, index) in basic_out_expressions" :key="index">
                                    <span v-for="(out_inner_expression, index_2) in out_expression" :key="index_2">
                                        {{out_inner_expression}}<span
                                            v-if="out_expression.length > 1 && index_2 != out_expression.length - 1">,</span>
                                    </span>
                                    <span v-if="basic_out_expressions.length > 1 && index != basic_out_expressions.length - 1">|</span>
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
                                    <span v-if="in_expressions.length > 1 && index != in_expressions.length - 1">,</span>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: center;">
                                <span v-for="(out_expression, index) in out_expressions" :key="index">
                                    <span v-for="(out_inner_expression, index_2) in out_expression" :key="index_2">
                                        {{out_inner_expression}}
                                        <span v-if="out_expression.length > 1 && index_2 != out_expression.length - 1">,</span>
                                    </span>
                                    <span v-if="out_expressions.length > 1 && index != out_expressions.length - 1">|</span>
                                </span>
                            </td>
                        </tr>
                    </table>
                    <p class="m-2" v-html="tooltip_description"></p>
                </div>
            </div>
        </main>
        <div id="graph" class="graph" :class="{border: response}"></div>
        <div v-if="response || language_output" style="height: calc(0.5 * 100vh)"></div>
    </div>
</template>

<script>
import axios from 'axios'
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

Vue.use(VueRouter)
const router = new VueRouter({});

export default {
  name: 'App',
  components: {
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
    axios
        .get('/examples?name=language_examples.json')
        .then(response => {
            this.language_examples = response['data']
            this.sentence = this.language_examples[0]["examples"][0]
        })
  },
  computed: {
    create_sentence_presentation() {
        if (this.language_output == null)
            return "<div></div>"

        return this.recursive_sentence_structure(this.language_output)
    }
  },
  methods: {
    select_language_example(example) {
        this.sentence = example
        if (this.auto_send) {
            this.language_request()
        }
    },
    change_page(to_page) {
        let reasoner_panel = document.getElementById("reasoner")
        let language_panel = document.getElementById("language")
        let reasoner_panel_tab = document.getElementById("reasoner-tab")
        let language_panel_tab = document.getElementById("language-tab")

        if (to_page === "reasoner") {
            reasoner_panel_tab.classList.add("active");
            reasoner_panel.classList.add("active");
            router.push("reasoner")
        } else {
            language_panel_tab.classList.add("active");
            language_panel.classList.add("active");
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
    language_request() {
        this.error = null
        console.log(this.sentence)
        // GET /someUrl
        let data = {sentence: this.sentence};
        this.$http.post('/language-request', data).then(response => {
            console.log(this.sentence)
            // get body data
            this.language_output = response.body;
        }, response => {
            // error callback
            this.error = JSON.parse(response.bodyText.replaceAll("\"", '`').replaceAll("'", '"'))
        });
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
    get_color(type) {
        let color = "#a5363b"
        if (type === -1) color = "#fd8f55"
        else if (type === 1) color = "#c66432"
        else if (type === 2) color = "#4f7e5f"
        else if (type === -2) color = "#6dc88a"
        else if (type === 3) color = "#586983"
        else if (type === -3) color = "#8aa1cb"
        else if (type === 4) color = "#b161b1"
        else if (type === -4) color = "#ffb8ff"
        else if (type === 5) color = "#b39986"
        else if (type === -5) color = "#fdb78a"
        else if (type === 6) color = "#1281d6"
        else if (type === -6) color = "#68a8ec"
        return color
    },
    get_border_color(type) {
        let color = "#8a1f25"
        if (type === 1) color = "#ca5e26"
        else if (type === -1) color = "#602007"
        else if (type === 2) color = "#285f42"
        else if (type === -2) color = "#2f854a"
        else if (type === 3) color = "#354d77"
        else if (type === -3) color = "#40567e"
        else if (type === 4) color = "#452245"
        else if (type === -4) color = "#8f488f"
        else if (type === 5) color = "#836550"
        else if (type === -5) color = "#9d6640"
        else if (type === 6) color = "#064673"
        else if (type === -6) color = "#284877"
        return color
    },
    recursive_sentence_structure(sentence_part) {
        let c_type = sentence_part['type']

        let ret_html = "<div " +
            "class=\"p-1 m-1 rounded align-middle d-flex flex-column align-content-center justify-content-center\" " +
            "style=\"background-color: " + this.get_color(c_type) +
            "; border: 3px solid " + this.get_border_color(c_type) + "\">\n"
        ret_html += "<h4 class='flex-row' style='margin: 0.25em 0.25em 0 0.25em'>" + sentence_part['name'] + "</h4>"
        ret_html += "<div class='d-flex flex-row d-inline-flex align-content-center justify-content-center'>"
        if (sentence_part['tokens'])
            ret_html += "<span class=\"text-center text-nowrap\"><strong>" + sentence_part['tokens'] + "</strong></span>"
        for (let i = 0; i < sentence_part['list'].length; i++) {
            let current_sentence_part = sentence_part['list'][i]
            if (current_sentence_part['list'] && current_sentence_part['list'].length >= 1) {
                ret_html += this.recursive_sentence_structure(current_sentence_part)
            } else {
                let cs_type = current_sentence_part['type'];
                ret_html += "<div class=\"p-1 m-1 rounded align-middle\" " +
                    "style=\"background-color: " + this.get_color(cs_type) +
                    "; display: flex; justify-content: center; flex-direction: column; " +
                    "border: 2px solid " + this.get_border_color(cs_type) + "\">\n"
                if (cs_type === 0)
                    ret_html += "<span class=\"text-center\"><strong>¬</strong></span>"
                else {
                    if (current_sentence_part['name'])
                        ret_html += "<span class=\"text-center text-nowrap\">" + current_sentence_part['name'] + "</span>"
                    if (current_sentence_part['tokens'])
                        ret_html += "<span class=\"text-center text-nowrap\"><strong>" + current_sentence_part['tokens'] + "</strong></span>"
                }
                ret_html += "</div>"
            }
        }
        ret_html += "</div></div>\n"
        return ret_html
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

  .heading {
      font-family: 'Dancing Script', cursive;
      font-size: 4.5rem;
      text-align: center;
      margin-bottom: 3rem;
  }

  .applied_rules {
      margin-top: 3rem;
  }

  .graph {
      text-align: center;
      width: 70%;
      margin-left: auto;
      margin-right: auto;
  }
</style>
