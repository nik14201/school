import Vue from 'vue';
import Vuex from 'vuex';
import counter from './modules/counter';

import actions from './actions';
import getters from './getters';
import mutations from './mutations';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    value: 0,
    images: [],
    dataprint: [],
    interior: false,
    current:0,
    blocks: 4,
  },
  getters,
  mutations,
  actions,
  modules: {
    counter
  }
});
