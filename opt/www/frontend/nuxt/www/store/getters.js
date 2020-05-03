import * as types from './types';

export default {
    [types.VALUE]: state => {
        return state.value;
    },
    getImageLove: state => {
    	var item;
    	var rez=[];
    	for(item of state.images){
    		if(item.love){
    			rez.push(item);
    		}
    	}
    	console.log(rez);
        return rez;
    },

    getImages: state => {
        return state.images;
    },

    get_interior: state => {
        return state.interior;
    },

    get_current: state => {
        return state.current;
    },
    get_blocks: state => {
        return state.blocks;
    },

};