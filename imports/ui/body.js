import { Template } from 'meteor/templating';

import { hot_stocks } from '../api/hot_stocks.js';

import './body.html';

Template.body.helpers({
  hot_stocks() {
    return hot_stocks.find({});
  },
});
