/* 
 * Aces Encoded Listener API
 *
 * API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 
 *
 * OpenAPI spec version: 0.1.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// SubscriptionRequest
    /// </summary>
    [DataContract]
    public partial class SubscriptionRequest :  IEquatable<SubscriptionRequest>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SubscriptionRequest" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected SubscriptionRequest() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="SubscriptionRequest" /> class.
        /// </summary>
        /// <param name="Host">Target host implementing Encoded Listener Subscriber API interface. (required).</param>
        /// <param name="MinConfirmations">Confirmations required before event is sent to subscribers. (required).</param>
        public SubscriptionRequest(string Host = default(string), int? MinConfirmations = default(int?))
        {
            // to ensure "Host" is required (not null)
            if (Host == null)
            {
                throw new InvalidDataException("Host is a required property for SubscriptionRequest and cannot be null");
            }
            else
            {
                this.Host = Host;
            }
            // to ensure "MinConfirmations" is required (not null)
            if (MinConfirmations == null)
            {
                throw new InvalidDataException("MinConfirmations is a required property for SubscriptionRequest and cannot be null");
            }
            else
            {
                this.MinConfirmations = MinConfirmations;
            }
        }
        
        /// <summary>
        /// Target host implementing Encoded Listener Subscriber API interface.
        /// </summary>
        /// <value>Target host implementing Encoded Listener Subscriber API interface.</value>
        [DataMember(Name="host", EmitDefaultValue=false)]
        public string Host { get; set; }

        /// <summary>
        /// Confirmations required before event is sent to subscribers.
        /// </summary>
        /// <value>Confirmations required before event is sent to subscribers.</value>
        [DataMember(Name="min_confirmations", EmitDefaultValue=false)]
        public int? MinConfirmations { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class SubscriptionRequest {\n");
            sb.Append("  Host: ").Append(Host).Append("\n");
            sb.Append("  MinConfirmations: ").Append(MinConfirmations).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as SubscriptionRequest);
        }

        /// <summary>
        /// Returns true if SubscriptionRequest instances are equal
        /// </summary>
        /// <param name="input">Instance of SubscriptionRequest to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SubscriptionRequest input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Host == input.Host ||
                    (this.Host != null &&
                    this.Host.Equals(input.Host))
                ) && 
                (
                    this.MinConfirmations == input.MinConfirmations ||
                    (this.MinConfirmations != null &&
                    this.MinConfirmations.Equals(input.MinConfirmations))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Host != null)
                    hashCode = hashCode * 59 + this.Host.GetHashCode();
                if (this.MinConfirmations != null)
                    hashCode = hashCode * 59 + this.MinConfirmations.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
