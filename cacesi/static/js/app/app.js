(function(){
  var app = angular.module('cacesi', [
  	'ngJsonExportExcel',

  ]).config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{$');
      $interpolateProvider.endSymbol('$}');
  });

}());
