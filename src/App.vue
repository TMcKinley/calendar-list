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
                @refresh_todo="onRefreshEvent"
              ></TodoList>
              <TodoList
                :style="rightStyleObject"
                :date="nextDate"
                :todos="todos"
                @refresh_todo="onRefreshEvent"
              ></TodoList>
            </div>
            <SimpleLoadingDialog
              v-if="showLoadingDialog"
              :dialogText="loadingDialogText"
            />
          </v-card>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import TodoList from "./components/TodoList";
import SimpleLoadingDialog from "./components/SimpleLoadingDialog.vue";
import { mapState, mapActions } from "vuex";

export default {
  components: {
    TodoList,
    SimpleLoadingDialog
  },

  data() {
    return {
      todos: []
    };
  },

  computed: {
    ...mapState(["showLoadingDialog", "loadingDialogText"]),

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
    ...mapActions(["showLoading", "hideLoading"]),

    isWeekend: function(rawDate) {
      return rawDate.getDay() === 6 || rawDate.getDay() === 0;
    },
    onRefreshEvent: function() {
      this.fetchData();
    },
    fetchData: function() {
      this.showLoading("Retrieving Events...");

      fetch("eventlist.json")
        .then(response => {
          return response.json();
        })
        .then(data => {
          this.todos = data;

          this.hideLoading();
        });
    }
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
  mounted: function() {
    this.fetchData();
  }
};
</script>

<style>
.theme--dark.v-icon {
  color: unset;
}
</style>
