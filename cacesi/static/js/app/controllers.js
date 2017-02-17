(function(){
  angular.module('cacesi')
    .controller('clientesCtrl', ['$scope', 'clientesSrvc', function($scope, clientesSrvc) {
		$scope.clientes = {};

      	clientesSrvc.getClienteById().then(function(data) {
        	$scope.clientes = data;
      	});
    }])

    .controller('filtersCtrl', ['$scope', 'getInfoService', function($scope, getInfoService) {
    	var meses =[];
    	var mesesName = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    	
    	getInfoService.getInfoByIdCliente($scope.clienteid, 'inspeccion_extintores').then(function(data) {
	    	areasTodas = [];
	      $scope.cliente = data.data[0].extintor.cliente;
	      $scope.areaSelected = "Areas";
	      $scope.mesesFull = [];
	      $scope.mesSelected = {'id' : 'Meses', 'name' : 'Meses'};
	      $scope.inspeccionesTodas = data.data;

	      angular.forEach(data.data, function(value, key) {
	      	if(areasTodas.indexOf(value.extintor.area) === -1)
						areasTodas.push(value.extintor.area);

					var mes = value.fecha_revision.split('-')[1];
					
					if(meses.indexOf(mes) === -1)
							meses.push(mes);
	      });

	      angular.forEach(meses, function(value, key) {
					$scope.mesesFull.push({'id' : value, 'name' : mesesName[value-1]})
				});

	      areasTodas.push('Areas');
	      $scope.mesesFull.push({'id' : 'Meses', 'name' : 'Meses'})
				$scope.areasTodas = areasTodas.sort();

				//$scope.areaFilter($scope.areaSelected, $scope.mesSelected, $scope.inspeccionesTodas);

	    });
	  }])
	
  .controller('extintorTerceroCtrl', ['$scope', 'extintorTerceroSrvc', function($scope, extintorTerceroSrvc) {
		$scope.extintores = {};

    extintorTerceroSrvc.getExtintorByCliente($scope.clienteid).then(function(data) {
     	$scope.extintores = data.data;
     	$scope.cliente = data.data[0].cliente;
     	console.log($scope.extintores);
    });
  }])
}());

