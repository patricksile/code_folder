angular.module("todoListApp", [])
.controller('mainCtrl', function($scope) {
    $scope.helloWorld = function() {
        console.log('Hello there! This the hellowrold controller function, in the mainCtrl');
    };
})
.controller('coolCtrl', function($scope) {
    $scope.whoAmI = function() {
        console.log("hello there, this is the coolCtrl function!");
    };
});