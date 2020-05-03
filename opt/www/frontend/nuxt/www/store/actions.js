import * as types from './types';

export default {
  [types.UPDATE_VALUE]: ({ commit }, payload) => {
    commit(types.MUTATE_UPDATE_VALUE, payload)
  },


  set_loves(context, payload) {
    context.commit('set_loves', payload)
  },

  add_images(context, payload) {
    context.commit('add_images', payload)
  },


  clear_images(context, payload){
    context.commit('clear_images', payload)
  },

  add_print(context,payload){
    context.commit('add_print', payload)
  },

  set_interior(context, payload){
    context.commit('set_interior', payload)
  },

  set_current(context,payload){
    context.commit('set_current', payload)
  },
  set_blocks(context, payload){
    context.commit('set_blocks', payload)
  },

};
