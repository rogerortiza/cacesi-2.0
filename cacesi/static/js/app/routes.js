(function () {

  angular
    .module('cacesi.routes', [])
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/about', {

      templateUrl: '/about'
    }).otherwise('/');
  }
})();