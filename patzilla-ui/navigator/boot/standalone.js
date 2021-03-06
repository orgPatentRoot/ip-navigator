// -*- coding: utf-8 -*-
// (c) 2013-2015 Andreas Motl, Elmyra UG
require('./loader.js');

$(document).ready(function() {

    console.info("Start application [standalone]");

    // process and propagate application ingress parameters
    //var url = $.url(window.location.href);
    //var query = url.param('query');
    //query = 'applicant=IBM';
    //query = 'publicationnumber=US2013255753A1';

    navigatorApp.start();
    navigatorApp.trigger('application:init');

    // Automatically run search after bootstrapping application.
    // However, from now on [2014-05-21] this gets triggered by "project:ready" events.
    // We keep this here in case we want to switch gears / provide a non-persistency
    // version of the tool for which the chance is likely, i.e. for a website embedding
    // component.
    //navigatorApp.perform_search();

});
