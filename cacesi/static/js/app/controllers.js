(function(){
  angular.module('cacesi.controllers', [])
    .controller('clientesCtrl', ['$scope', 'clientesSrvc', function($scope, clientesSrvc) {
		$scope.clientes = {};

      	clientesSrvc.getClienteById().then(function(data) {
        	$scope.clientes = data;
      	});
    }])

    .controller('inspextintoresCtrl', ['$scope', 'inspextintoresSrvc', function($scope, inspextintoresSrvc) {
	    var makeBarGraph = function(title, container, data) {
	    	document.getElementById(container).innerHTML="";
	    	d3plus.viz()
			    .container("#status")
			    .data(data)
			    .type("bar")
			    .id("anomalia")
			    .x("anomalia")
			    .y("extintores")
			    .title(title)
			    .resize(true)
			    .draw()
	    }

			var makeDonutGraph = function(title, container, data) {
				document.getElementById(container).innerHTML="";
				d3plus.viz()
				    .container('#'+container)
				    .data(data)
				    .type("pie")
				    .tooltip(false)
				    .id("name")
				    .size("value")
				    .title(title)
				    .color("color")
				    .resize(true)
				    .draw()
			}

			$scope.areaFilter = function(areaSelected, mesSelected, data) {
      	areas = [];
      	anomalias = [];
      	meses =[];
      	mesesName = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
      	$scope.mesesFull = [];
      	$scope.inspecciones = [];

				angular.forEach(data, function(value, key) {
					if(areaSelected == 'Todas' || areaSelected == value.extintor.area) {
						mes = value.fecha_revision.split('-')[1];

						if(meses.indexOf(mes) === -1)
							meses.push(mes);

						if(mes == mesSelected.id || mesSelected.id == 'Todos') {
							$scope.inspecciones.push(value);

							if(areas.indexOf(value.extintor.area) === -1)
								areas.push(value.extintor.area);

							if(value.altura === true)
								anomalias.push({"anomalia":"altura", "extintores": 1});

							if(value.etiqueta === true)
								anomalias.push({"anomalia":"etiqueta", "extintores": 1});

							if(value.limpieza === true)
								anomalias.push({"anomalia":"limpieza", "extintores": 1});

							if(value.manguera === true)
								anomalias.push({"anomalia":"manguera", "extintores": 1});	

							if(value.nanometro === true)
								anomalias.push({"anomalia":"nanometro", "extintores": 1});

							if(value.obstruido === true)
								anomalias.push({"anomalia":"obstruido", "extintores": 1});	

							if(value.operable === true)
								anomalias.push({"anomalia":"operable", "extintores": 1});			
				
							if(value.peso == true)
								anomalias.push({"anomalia":"peso", "extintores": 1});

							if(value.pintura === true)
								anomalias.push({"anomalia":"pintura", "extintores": 1});		

							if(value.proteccion === true)
								anomalias.push({"anomalia":"proteccion", "extintores": 1});	

							if(value.seguro === true)
								anomalias.push({"anomalia":"seguro", "extintores": 1});	

							if(value.senalamiento === true)
								anomalias.push({"anomalia":"senalamiento", "extintores": 1});	

							if(value.valvula === true)
								anomalias.push({"anomalia":"valvula", "extintores": 1});	
						}		
					}				
				});
			
				angular.forEach(meses, function(value, key) {
					$scope.mesesFull.push({'id' : value, 'name' : mesesName[value-1]})
				});
				$scope.mesesFull.push({'id' : 'Todos', 'name' : 'Todos'})

				var  noAreas = [
				  {"value": 100, "name": areas.length, "color": "#ACEC00"},
				]
				var noInspecciones = [
					{"value": 100, "name": $scope.inspecciones.length, "color": "#BA65C9"},
				]

				makeDonutGraph('Areas', 'areas', noAreas);
				makeDonutGraph('Revisiones','revisiones', noInspecciones);
				makeBarGraph('Extintores sin Anomalias', 'status', anomalias)
			}

    inspextintoresSrvc.getInspExtintoresByClienteId().then(function(data) {
    	areasTodas = [];
      $scope.cliente = data.data[0].extintor.cliente;
      $scope.areaSelected = "Todas";
      $scope.mesSelected = {'id' : 'Todos', 'name' : 'Todos'};
      $scope.inspeccionesTodas = data.data;

      angular.forEach(data.data, function(value, key) {
      	if(areasTodas.indexOf(value.extintor.area) === -1)
					areasTodas.push(value.extintor.area);
      });

      areasTodas.push('Todas');
			$scope.areasTodas = areasTodas.sort();

			$scope.areaFilter($scope.areaSelected, $scope.mesSelected, $scope.inspeccionesTodas);

    });
  }])
	
  .controller('extintorTerceroCtrl', ['$scope', 'extintorTerceroSrvc', function($scope, extintorTerceroSrvc) {
		$scope.extintores = {};

    extintorTerceroSrvc.getExtintorByCliente().then(function(data) {
     	$scope.extintores = data.data;
     	$scope.cliente = data.data[0].cliente;
     	console.log($scope.extintores);
    });
  }])
}());

