import * as types from './types';

export default {
  [types.MUTATE_UPDATE_VALUE]: (state, payload) => {
    state.value = payload;
  },
  // Тут хранятся понравившиеся обои
  set_loves(state, payload) {
    var bl = true;
    for (var item of state.images) {
      if (item.id == payload.id) {
        item.love = !item.love;
        bl = false;
        break;
      }
    }
    if (bl) {
      state.images.push(payload);
    }
  },

  clear_images(state) {
    state.images = []
  },

  add_images(state, payload) {
    for(var item of state.images){
      //if(item.id==payload.id) return;
    }
    state.images.push(payload);
  },

  // Тут должны храниться итерьер и обои, но не используется
  add_print(state,payload){
    state.dataprint = []
    state.dataprint.push(payload);
  },

  //Тут хранится интерьер для печати
  set_interior(state, payload){
    state.interior = payload
  },

  set_current(state,payload){
    state.current = payload
  },
  set_blocks(state,payload){
    state.blocks = payload
  },

};
