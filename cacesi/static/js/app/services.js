(function(){
  angular.module('cacesi')
    .factory('getInfoService', ['$http', '$q', function($http, $q) {

      function getInfoByIdCliente(clienteId, url) {
        var deferred = $q.defer();

        $http.get('../../api/clientes/'+clienteId+'/'+url)
          .then(function(data) {
            deferred.resolve(data);
          });

        return deferred.promise;
      }

      return {
        getInfoByIdCliente : getInfoByIdCliente
      }

    }])

}());