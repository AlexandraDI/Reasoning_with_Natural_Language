<template>
  <div>
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
                          :class="{'btn-outline-success': sentence !== language_example, 'btn-success': sentence === language_example}"
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
                 v-model="sentence"/>
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
</template>

<script>
import axios from "axios";

export default {
  name: "LanguageCheckerPage",
  data() {
    return {
      response: null,
      error: null,
      language_examples: [],
      sentence: 'When i love you then you love me',
      language_output: null,
    };
  },
  mounted() {
    axios
        .get('/examples?name=language_examples.json')
        .then(response => {
          this.language_examples = response['data']
          this.sentence = this.language_examples[0]["examples"][0]
        });
  },
  methods: {
    select_language_example(example) {
      this.sentence = example;
      this.language_request();
    },
    language_request() {
      this.error = null
      console.log(this.sentence)
      // GET /someUrl
      let data = {sentence: this.sentence};
      axios
        .post('/language-request', data)
        .then(response => {
          console.log(response)
          // get body data
          this.language_output = response.data;
          this.$emit("set-error", null);
        })
        .catch(error => {
          const data = error.response.data;
          this.language_output = null;
          this.$emit("set-error", data);
        });
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
  },
  computed: {
    create_sentence_presentation() {
      if (this.language_output == null)
        return "<div></div>"

      return this.recursive_sentence_structure(this.language_output)
    }
  },
}
</script>

<style scoped>

</style>