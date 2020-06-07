<template>
  <div>
    <v-container>
      <div class="d-flex justify-space-between align-center">
        <v-subheader class="pl-1 headline">{{ calculateDate() }}</v-subheader>

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
            class="primary--text"
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
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: {
    date: {
      type: Date,
      required: true
    },
    todos: {
      type: Array,
      required: true
    }
  },

  data() {
    return {};
  },

  computed: {
    isToday: function() {
      return this.date.getDate() === new Date().getDate()
        ? "Today"
        : "Tomorrow";
    },
    filteredTodos: function() {
      // Jank to get a date in this format: 2020-05-02.
      let rawDate = new Intl.DateTimeFormat("en-GB")
        .format(this.date)
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
    ...mapActions(["showLoading", "hideLoading"]),

    calculateDate: function() {
      const date = this.date;
      const formatter = new Intl.DateTimeFormat("en-US", {
        weekday: "long",
        month: "long",
        day: "numeric"
      });

      const fmtDate = formatter.format(date);

      return fmtDate + this.nth(date.getDate()) + ` (${this.isToday})`;
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
      this.showLoading("Saving Event...");

      fetch("/api/save", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ id: dataObject.id })
      })
        .then(response => {
          return response.json();
        })
        .then(() => {
          this.hideLoading();

          this.$emit("refresh_todo");
        });

      $event.preventDefault();
      $event.stopPropagation();
    }
  },
  mounted: function() {}
};
</script>

<style></style>
