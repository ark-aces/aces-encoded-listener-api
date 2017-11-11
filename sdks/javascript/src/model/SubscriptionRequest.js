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


import ApiClient from '../ApiClient';





/**
* The SubscriptionRequest model module.
* @module model/SubscriptionRequest
* @version 0.1.0
*/
export default class SubscriptionRequest {
    /**
    * Constructs a new <code>SubscriptionRequest</code>.
    * @alias module:model/SubscriptionRequest
    * @class
    * @param callbackUrl {String} Target target URL to POST Encoded Listener events to.
    * @param minConfirmations {Number} Confirmations required before event is sent to subscriber.
    */

    constructor(callbackUrl, minConfirmations) {
        

        
        

        this['callbackUrl'] = callbackUrl;this['minConfirmations'] = minConfirmations;

        
    }

    /**
    * Constructs a <code>SubscriptionRequest</code> from a plain JavaScript object, optionally creating a new instance.
    * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
    * @param {Object} data The plain JavaScript object bearing properties of interest.
    * @param {module:model/SubscriptionRequest} obj Optional instance to populate.
    * @return {module:model/SubscriptionRequest} The populated <code>SubscriptionRequest</code> instance.
    */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SubscriptionRequest();

            
            
            

            if (data.hasOwnProperty('callbackUrl')) {
                obj['callbackUrl'] = ApiClient.convertToType(data['callbackUrl'], 'String');
            }
            if (data.hasOwnProperty('minConfirmations')) {
                obj['minConfirmations'] = ApiClient.convertToType(data['minConfirmations'], 'Number');
            }
        }
        return obj;
    }

    /**
    * Target target URL to POST Encoded Listener events to.
    * @member {String} callbackUrl
    */
    callbackUrl = undefined;
    /**
    * Confirmations required before event is sent to subscriber.
    * @member {Number} minConfirmations
    */
    minConfirmations = undefined;








}


