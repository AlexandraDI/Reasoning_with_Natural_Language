<template>
    <ul class="nav nav-pills nav-fill pb-3" id="tab" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link border" id="reasoner-tab" @click="switchPage('reasoner')"
                    type="button" data-bs-toggle="tab" data-bs-target="#reasoner"
                    role="tab" aria-controls="reasoner" aria-selected="false">
                Reasoner
            </button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link border" id="language-tab" @click="switchPage('language')"
                    type="button" data-bs-toggle="tab" data-bs-target="#language"
                    role="tab" aria-controls="language" aria-selected="false">
                Language Check
            </button>
        </li>
    </ul>
</template>

<script>
    export default {
        methods: {
                switchPage(pageName) {
                    this.$emit('switch-page', pageName);
                }
        }
    }
</script>