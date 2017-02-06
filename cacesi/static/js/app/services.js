(function(){
  angular.module('cacesi.services', [])
     .factory('clientesSrvc', ['$http', '$q', function($http, $q) {

      function getClienteById() {
        var deferred = $q.defer();

        $http.get('../api/clientes/1')
          .then(function(data) {
            deferred.resolve(data);
          });

        return deferred.promise;
      }

      return {
        getClienteById : getClienteById
      }

    }])
    .factory('inspextintoresSrvc', ['$http', '$q', function($http, $q) {

      function getInspExtintoresByClienteId() {
        var deferred = $q.defer();

        $http.get('../api/clientes/1/inspeccion_extintores')
          .then(function(data) {
            deferred.resolve(data);
          });

        return deferred.promise;
      }

      return {
        getInspExtintoresByClienteId : getInspExtintoresByClienteId
      }

    }])

    .factory('extintorTerceroSrvc', ['$http', '$q', function($http, $q) {

      function getExtintorByCliente() {
        var deferred = $q.defer();

        $http.get('../../api/clientes/1/extintores_terceros')
          .then(function(data) {
            deferred.resolve(data);
          });

        return deferred.promise;
      }

      return {
        getExtintorByCliente : getExtintorByCliente
      }

    }])

}());