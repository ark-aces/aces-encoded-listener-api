/*
 * Aces Encoded Listener API
 *
 * API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 
 *
 * API version: 0.1.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package swagger

import (
	"time"
)

type Subscription struct {

	// Unique identifier for a Subscription.
	Id string `json:"id,omitempty"`

	// Date the Subscription was created.
	CreatedAt time.Time `json:"created_at,omitempty"`

	Status string `json:"status,omitempty"`
}
