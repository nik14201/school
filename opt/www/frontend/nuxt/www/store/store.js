import Vue from 'vue';
import Vuex from 'vuex';

export const state = ()  => ({
	key: 0,
});

export const mutations =  {
  SET_KEY(state, payload) {
    console.log('mutations SET_KEY', payload);
    state.key=payload
  },

};

export const getters = {
    GET_KEY: state => {
        return state.key;
    }, 
};

export const actions = {
   SET_KEY(context, payload) {
    context.commit('SET_KEY', payload)
  },
};