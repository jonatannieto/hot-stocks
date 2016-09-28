import { Mongo } from 'meteor/mongo';

export const hot_stocks = new Mongo.Collection('hot_active_stocks');
