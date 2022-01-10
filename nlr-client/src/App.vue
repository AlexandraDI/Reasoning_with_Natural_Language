<template>
  <div id="app">
        <main>

            <application-header></application-header>

            <ModeSwitcher @switch-page="change_page"></ModeSwitcher>


            <div class="tab-content" id="pills-tabContent">
                <div class="tab-pane" id="reasoner" role="tabpanel" aria-labelledby="reasoner-tab">
                  <ReasonerPage
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
        </main>
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
    };
  },
  mounted() {
    if (window.location.hash === "#/language")
      this.change_page("language");
    else
      this.change_page("reasoner");
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
</style>
