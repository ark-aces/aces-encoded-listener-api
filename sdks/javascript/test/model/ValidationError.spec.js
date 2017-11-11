/**
 * Aces Encoded Listener API
 * API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.AcesEncodedListenerApi);
  }
}(this, function(expect, AcesEncodedListenerApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AcesEncodedListenerApi.ValidationError();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('ValidationError', function() {
    it('should create an instance of ValidationError', function() {
      // uncomment below and update the code to test ValidationError
      //var instane = new AcesEncodedListenerApi.ValidationError();
      //expect(instance).to.be.a(AcesEncodedListenerApi.ValidationError);
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instane = new AcesEncodedListenerApi.ValidationError();
      //expect(instance).to.be();
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instane = new AcesEncodedListenerApi.ValidationError();
      //expect(instance).to.be();
    });

    it('should have the property fieldErrors (base name: "fieldErrors")', function() {
      // uncomment below and update the code to test the property fieldErrors
      //var instane = new AcesEncodedListenerApi.ValidationError();
      //expect(instance).to.be();
    });

  });

}));
