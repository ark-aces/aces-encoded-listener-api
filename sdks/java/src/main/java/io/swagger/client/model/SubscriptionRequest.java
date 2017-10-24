/*
 * Aces Encoded Listener API
 * API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * SubscriptionRequest
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2017-10-23T23:56:49.035-07:00")
public class SubscriptionRequest {
  @SerializedName("host")
  private String host = null;

  @SerializedName("min_confirmations")
  private Integer minConfirmations = null;

  public SubscriptionRequest host(String host) {
    this.host = host;
    return this;
  }

   /**
   * Target host implementing Encoded Listener Subscriber API interface.
   * @return host
  **/
  @ApiModelProperty(required = true, value = "Target host implementing Encoded Listener Subscriber API interface.")
  public String getHost() {
    return host;
  }

  public void setHost(String host) {
    this.host = host;
  }

  public SubscriptionRequest minConfirmations(Integer minConfirmations) {
    this.minConfirmations = minConfirmations;
    return this;
  }

   /**
   * Confirmations required before event is sent to subscribers.
   * @return minConfirmations
  **/
  @ApiModelProperty(required = true, value = "Confirmations required before event is sent to subscribers.")
  public Integer getMinConfirmations() {
    return minConfirmations;
  }

  public void setMinConfirmations(Integer minConfirmations) {
    this.minConfirmations = minConfirmations;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SubscriptionRequest subscriptionRequest = (SubscriptionRequest) o;
    return Objects.equals(this.host, subscriptionRequest.host) &&
        Objects.equals(this.minConfirmations, subscriptionRequest.minConfirmations);
  }

  @Override
  public int hashCode() {
    return Objects.hash(host, minConfirmations);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SubscriptionRequest {\n");
    
    sb.append("    host: ").append(toIndentedString(host)).append("\n");
    sb.append("    minConfirmations: ").append(toIndentedString(minConfirmations)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

