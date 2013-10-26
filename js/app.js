App = Ember.Application.create();

/****************************
* ROUTES
* **************************/

App.Router.map(function() {
    this.resource('signup');
});

App.IndexRoute = Ember.Route.extend({
    model: function() {
        return ['red', 'yellow', 'blue'];
    }
});

/****************************
* CONTROLLERS
* **************************/

 App.ApplicationController = Ember.Controller.extend({
    isLoggedIn: false
});

App.SignupController = Ember.Controller.extend({
    email: '',
    password: '',
    passwordDidChange: function() {
        this.set('hashedPw', CryptoJS.SHA3(this.get('password'), {outputLength: 128}));
    }.observes('password'),
    hashedPw: null,
    isEmailValid: true,
    isPwValid: true,
    actions: {
        submit: function() {
            // send auth to server
            var obj = {
                email: this.get('email'),
                pwhash: this.get('hashedPw').toString()
            }
            console.log(JSON.stringify(obj));
        }
    }

});

/****************************
* VIEWS
* **************************/
