<template>
  <v-dialog persistent :value="true" width="300">
    <v-card color="blue darken-4">
      <v-card-text class="white--text">
        {{ dialogText }}
        <v-progress-linear
          indeterminate
          color="white"
          class="mb-0"
        ></v-progress-linear>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    dialogText: String
  }
};
</script>
