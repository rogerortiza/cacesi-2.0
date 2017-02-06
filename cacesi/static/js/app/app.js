(function(){
  var app = angular.module('cacesi', [
    'cacesi.controllers',
    'cacesi.services'
  ]).config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{$');
      $interpolateProvider.endSymbol('$}');
  });

}());
