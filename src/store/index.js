import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    showLoadingDialog: "",
    loadingDialogText: ""
  },
  mutations: {
    setLoadingDialogVisibility(state, dataObject) {
      state.loadingDialogText = dataObject.message;
      state.showLoadingDialog = dataObject.visible;
    }
  },
  actions: {
    showLoading({ commit }, message) {
      // Workaround. Don't show loading dialog if browser window is not active/visible.
      if (!document.hidden) {
        commit("setLoadingDialogVisibility", {
          visible: true,
          message: message
        });
      }
    },
    hideLoading({ commit }) {
      // Workaround. Don't show loading dialog if browser window is not active/visible.
      if (!document.hidden) {
        commit("setLoadingDialogVisibility", {
          visible: false,
          message: ""
        });
      }
    }
  },
  modules: {}
});
