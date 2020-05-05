<template>
  <v-app>
    <v-content>
      <v-container>
        <v-layout row justify-center class="ma-5">
          <v-card style="width:700px;">
            <v-toolbar color="blue darken-4" dark>
              <v-toolbar-title class="headline">
                Calendar Checklist
              </v-toolbar-title>
            </v-toolbar>

            <v-container>
              <div class="d-flex justify-space-between align-center">
                <v-subheader class="pl-1 headline">{{
                  calculateDate()
                }}</v-subheader>

                <div>{{ filteredTodos.length }} Tasks</div>
              </div>
            </v-container>

            <v-divider class="ml-4 mr-4" style="height:1px;"></v-divider>

            <v-list two-line subheader>
              <v-subheader inset class="subheading" v-if="todos.length == 0"
                >You have 0 Tasks due today, congrats!</v-subheader
              >

              <v-list-item dense v-for="(todo, i) in filteredTodos" :key="i">
                <v-list-item-icon class="mt-0 mr-2">
                  <v-checkbox
                    class="red--text"
                    off-icon="fas fa-square"
                    @click="onCheckClick(todo, $event)"
                  ></v-checkbox>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title class="title"
                    >{{ todo.description }}
                  </v-list-item-title>
                  <v-list-item-subtitle
                    >Start: {{ formatDate(todo.start_time) }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      todos: []
    };
  },

  computed: {
    filteredTodos: function() {
      // Jank to get a date in this format: 2020-05-02.
      let rawDate = new Intl.DateTimeFormat("en-GB")
        .format(new Date())
        .split("/")
        .reverse()
        .join("-");

      let notCompleted = this.todos.filter(obj => obj.completed === 0);
      let filteredArray = notCompleted.filter(obj => {
        let datePart = obj.start_time.split("T")[0];

        return rawDate === datePart;
      });

      return filteredArray;
    }
  },
  methods: {
    calculateDate: function() {
      const date = new Date();
      const formatter = new Intl.DateTimeFormat("en-US", {
        weekday: "long",
        month: "long",
        day: "numeric"
      });

      const fmtDate = formatter.format(date);

      return fmtDate + this.nth(date.getDate()) + " (Today)";
    },
    formatDate: function(rawDate) {
      const date = new Date(rawDate);
      const formatter = new Intl.DateTimeFormat("en-US", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
      });

      return formatter.format(date);
    },
    nth(d) {
      if (d > 3 && d < 21) return "th";
      switch (d % 10) {
        case 1:
          return "st";
        case 2:
          return "nd";
        case 3:
          return "rd";
        default:
          return "th";
      }
    },
    onCheckClick: function(dataObject, $event) {
      if (dataObject.completed === 0) {
        dataObject.completed = 1;
      }
      $event.preventDefault();
      $event.stopPropagation();
    }
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
  mounted: function() {
    fetch("eventlist.json")
      .then(response => {
        return response.json();
      })
      .then(data => {
        this.todos = data;
      });
  }
};
</script>

<style>
.theme--dark.v-icon {
  color: unset;
}
</style>
