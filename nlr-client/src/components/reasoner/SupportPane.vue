<template>
    <div class="accordion mb-4" id="accordionSupport" v-if="support !== null">
      <div class="accordion-item">
        <h1 class="accordion-header" id="heading-support">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                  data-bs-target="#collapseSupport" aria-expanded="false"
                  aria-controls="collapseSupport">
            <span class="fs-3">
                Conclusion Support
            </span>
          </button>
        </h1>
        <div id="collapseSupport" class="accordion-collapse collapse"
             aria-labelledby="heading-support" data-bs-parent="#accordionSupport">
          <div class="accordion-body">
            The following expressions were used in order to prove the given problem. Keep in mind that the reasoner proves by disproving the opposite of the sentence to be proven.
            <ul class="list-group mt-2">
              <li class="list-group-item" v-for="(sentence, index) in support" :key="index">{{sentence}}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "SupportPane",
  props: ["support"]
}
</script>

<style scoped>

</style>