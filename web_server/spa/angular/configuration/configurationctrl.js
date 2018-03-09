/**
 * @Date:   18-Feb-2018
 * @Project: Blueberry
 * @Last modified time: 04-Mar-2018
 * @License: GNU GPL v3
 */



var NodeChain = angular.module('NodeChain');

NodeChain.controller("ConfigurationCtrl", function($scope, $location, $http) {
  $http.get('./api-v0.0/parametre').
  then(function(response) {
    $scope.datafromapi = response.data;
  });
})