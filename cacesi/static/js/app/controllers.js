(function(){
  angular.module('cacesi')
    .controller('filtersCtrl', ['$scope', 'getInfoService', function($scope, getInfoService) {
      getInfoService.getInfoByIdCliente($scope.clienteid, '').then(function(data) {
        $scope.cliente = data.data;
      });

      getInfoService.getInfoByIdCliente($scope.clienteid, 'extintores_terceros').then(function(data) {
        $scope.extintoresByCliente = data.data;
      });

    	var meses =[];
    	var mesesName = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

    	getInfoService.getInfoByIdCliente($scope.clienteid, 'inspeccion_extintores').then(function(data) {
	    	areasTodas = [];
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
     	console.log($scope.extintores);
    });
  }])
}());
