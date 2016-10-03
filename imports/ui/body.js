import { Template } from 'meteor/templating';

import { hot_stocks } from '../api/hot_stocks.js';

import './body.html';

Template.body.helpers({
  hot_stocks() {
    return hot_stocks.find({});
  },
});

Template.registerHelper('chgRate', function(param1, param2) {
  if(param1>param2){
    return true;
  } else {
    return false;
  }
});

Template.registerHelper('hottest', function(name, chg){
  if(chg>20){
    var msgHotStock = sAlert.success('Stock very Hot(+20%): ' + name);
  }
});
