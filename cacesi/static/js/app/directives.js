'use strict';

angular.module('cacesi')
	.directive('inspeccionExtintores', function() {
		return {
			templateUrl : '/dashboard/inspextintores',
			restrict : 'E',
			scope : {
				area : '=',
				mes : '=', 
				inspecciones : '='
			},
			controller : ['$scope', function($scope) {
				$scope.$watch('[area, mes]', function(newValue, oldValue) {
					areaFilter($scope.area, $scope.mes, $scope.inspecciones);
					/* if(angular.equals(newValue, oldValue)){
				        return false; // simply skip that
				    }
				    else {
				    	 areaFilter($scope.area, $scope.mes, $scope.inspecciones);
				    }*/
				   
    		}, true);

				$('ul.tabs').tabs();
				$('.materialboxed').materialbox();

				var data4 = [
    			{"value": 100, "name": "140", "color": "#00BBD6"},
  			]

			  d3plus.viz()
			    .container("#onle2")
			    .data(data4)
			    .type("pie")
			    .id("name")
			    .size("value")
			    .title("Extintores")
			    .color("color")
			    .resize(true)
			    .draw()

	    	var makeBarGraph = function(title, container, data) {
		    	document.getElementById(container).innerHTML="";
		    	d3plus.viz()
				    .container('#'+container)
				    .data(data)
				    .type("bar")
				    .id("anomalia")
				    .x("anomalia")
				    .y("extintores")
				    .title({value : title})
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

				var areaFilter = function(areaSelected, mesSelected, data) {
	      	var areas = [];
	      	var anomalias = [];
	      	var totalObseraciones = 0;
	      	$scope.inspeccionesByArea = [];

					angular.forEach(data, function(value, key) {
						if(areaSelected == 'Areas' || areaSelected == value.extintor.area) {
							var mes = value.fecha_revision.split('-')[1];

							if(mes == mesSelected.id || mesSelected.id == 'Meses') {
								$scope.inspeccionesByArea.push(value);

								if(value.observaciones != '')
									totalObseraciones = totalObseraciones + 1;

								if(areas.indexOf(value.extintor.area) === -1)
									areas.push(value.extintor.area);

								if(value.altura === false)
									anomalias.push({"anomalia":"altura", "extintores": 1});

								if(value.etiqueta === false)
									anomalias.push({"anomalia":"etiqueta", "extintores": 1});

								if(value.limpieza === false)
									anomalias.push({"anomalia":"limpieza", "extintores": 1});

								if(value.manguera === false)
									anomalias.push({"anomalia":"manguera", "extintores": 1});	

								if(value.nanometro === false)
									anomalias.push({"anomalia":"nanometro", "extintores": 1});

								if(value.obstruido === false)
									anomalias.push({"anomalia":"obstruido", "extintores": 1});	

								if(value.operable === false)
									anomalias.push({"anomalia":"operable", "extintores": 1});			
					
								if(value.peso == false)
									anomalias.push({"anomalia":"peso", "extintores": 1});

								if(value.pintura === false)
									anomalias.push({"anomalia":"pintura", "extintores": 1});		

								if(value.proteccion === false)
									anomalias.push({"anomalia":"proteccion", "extintores": 1});	

								if(value.seguro === false)
									anomalias.push({"anomalia":"seguro", "extintores": 1});	

								if(value.senalamiento === false)
									anomalias.push({"anomalia":"senalamiento", "extintores": 1});	

								if(value.valvula === false)
									anomalias.push({"anomalia":"valvula", "extintores": 1});	
							}		
						}				
					});

					var  noAreas = [
					  {"value": 100, "name": areas.length, "color": "#ACEC00"},
					]
					var noInspecciones = [
						{"value":  $scope.inspeccionesByArea.length, "name": $scope.inspeccionesByArea.length, "color": "#BA65C9"},
					]

					var noObseraciones = [
						{"value": 100, "name": totalObseraciones, "color": "#EF3C79"},
					]

					var noStatus = [
						{"extintores": 100, "anomalia": "En su Lugar"},
						{"extintores": 200, "anomalia": "No encontrado"},
						{"extintores": 10, "anomalia": "R. por caducidad"},
						{"extintores": 450, "anomalia": "R. po falta presion"}
					]

					makeDonutGraph('Areas', 'areas', noAreas);
					makeDonutGraph('Revisiones','revisiones', noInspecciones);
					makeDonutGraph('Observaciones','observaciones', noObseraciones);
					makeBarGraph('Anomalias', 'kaka', anomalias)
					makeBarGraph('Status', 'status', noStatus)
				}	
			}],
		};
	})
	.directive('areasCliente', function() {
		return {
			templateUrl : '/dashboard/areas',
			restrict : 'EA',
			scope : {
				cliente : '='
			},
			controller : ['$scope', 'getInfoService', function($scope, getInfoService) {
				getInfoService.getInfoByIdCliente($scope.cliente, 'areas').then(function(data) {
					$scope.areasByCliente = data.data;
				})
			}],
		}
	})
