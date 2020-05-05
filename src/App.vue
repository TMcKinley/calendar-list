<template>
  <v-app>
    <v-content>
      <v-container>
        <v-layout row justify-center class="ma-5">
          <v-card style="width:1400px;">
            <v-toolbar color="blue darken-4" dark>
              <v-toolbar-title class="headline">
                Calendar Checklist
              </v-toolbar-title>
            </v-toolbar>

            <div class="d-flex">
              <TodoList
                :style="leftStyleObject"
                :date="currentDate"
                :todos="todos"
              ></TodoList>
              <TodoList
                :style="rightStyleObject"
                :date="nextDate"
                :todos="todos"
              ></TodoList>
            </div>
          </v-card>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import TodoList from "./components/TodoList";

export default {
  components: {
    TodoList
  },

  data() {
    return {
      todos: []
    };
  },

  computed: {
    leftStyleObject: function() {
      let obj = {};
      obj.flex = "70";
      if (this.isWeekend(this.currentDate)) {
        obj.flex = "50";
      }

      return obj;
    },
    rightStyleObject: function() {
      let obj = {};
      obj.flex = "30";
      if (this.isWeekend(this.nextDate)) {
        obj.flex = "50";
      }

      return obj;
    },
    currentDate: function() {
      return new Date();
    },
    nextDate: function() {
      const today = new Date();
      const tomorrow = new Date(today);
      tomorrow.setDate(tomorrow.getDate() + 1);

      return tomorrow;
    }
  },
  methods: {
    isWeekend: function(rawDate) {
      return rawDate.getDay() === 6 || rawDate.getDay() === 0;
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
