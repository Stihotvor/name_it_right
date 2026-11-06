---
status: new
---

# Logistics

!!! success "General patterns"

    - Name the contract, the physical goods and the movement as separate entities: `consignment`, `parcel`, `shipment`
    - Name a tracking fact as an event: `tracking_event`, with a type, a time, a place and a status
    - Use the words of the standard in your field. GS1 EPCIS uses `what`, `when`, `where`, `why` for each event
    - Keep the planned time and the actual time apart: `planned_at`, `actual_at`, or `estimated_delivery_at` and `delivered_at`
    - Store weight and size with the unit in the name: `weight_grams`, `length_millimeters`

!!! tip "Useful tips"

    - Use a global code for places and goods: GLN for a location, GTIN for a product, SSCC for a pallet or another logistic unit
    - Give each leg of a route its own record. One shipment can have many legs
    - Use UN/LOCODE for a port or a city, and ISO 3166 for a country
    - Use the incoterm as a code: `incoterm_code` with `DAP`, `DDP`, `FOB`

!!! danger "General anti-patterns"

    - `shipment` for the order, the box and the trip at once
    - `status` that mixes the transport state and the customs state
    - `weight` with no unit
    - `address` as one free-text column for the sender, the receiver and the depot
    - `delivered` set by a person, not by a delivery event

The examples use the words of carriers and of GS1 EPCIS. EPCIS is a standard for events about objects in a supply chain. Its event types are `ObjectEvent`, `AggregationEvent`, `TransactionEvent`, `TransformationEvent` and `AssociationEvent`.

A shipment on this page is one transport of goods. In [E-commerce](ecommerce.md) a shipment is a group of packages sent together, and the tracking number is on the package. Carrier systems often keep the number on the shipment. Pick one owner for the number and keep it. This page names the first state `created`, where the e-commerce page uses `label_created`. The shipment owns the state `delivered`, and a parcel scan updates it.

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Shipper | The party that sends the goods. | `shippers` | |
| Consignee | The party that receives the goods. | `consignees` | |
| Carrier | The company that moves the goods. | `carriers` | |
| Consignment | A group of goods for one consignee under one transport contract. | `consignments` | The booking. |
| Shipment | One transport of goods from one place to another. | `shipments` | Has the tracking number of the carrier. |
| Parcel | One physical package. | `parcels` | Can have its own label code. |
| Pallet | A group of parcels on a base. | `pallets` | Has an SSCC. |
| Container | A sealed unit for sea or rail transport. | `containers` | Has a container number. |
| Leg | One part of the route of a shipment. | `legs` | |
| Route | The planned list of legs. | `routes` | |
| Tracking event | A fact about where a parcel is. | `tracking_events` | An EPCIS event. |
| Location | A place with a code. | `locations` | A GLN or a UN/LOCODE. |
| Depot | A place where parcels are sorted. | `depots` | |
| Vehicle | A truck, a van, a ship, a plane. | `vehicles` | |
| Driver | A person who drives a vehicle. | `drivers` | |
| Manifest | The list of parcels on a vehicle. | `manifests` | |
| Proof of delivery | The record that proves a delivery. | `proofs_of_delivery` | A signature or a photo. |
| Customs declaration | A filing for goods that cross a border. | `customs_declarations` | |
| Rate | A price for a service on a lane. | `rates` | |
| Surcharge | An extra fee on a rate. | `surcharges` | Fuel, remote area. |
| Delivery attempt | One try to hand over a parcel. | `delivery_attempts` | A parcel can have many. |
| Return shipment | A shipment that goes back to the sender. | `return_shipments` | |
| Pickup | A visit to collect parcels. | `pickups` | |

## States

| Entity | States |
|---|---|
| Consignment | `draft`, `booked`, `in_progress`, `completed`, `canceled` |
| Shipment | `created`, `picked_up`, `in_transit`, `out_for_delivery`, `delivered`, `delivery_failed`, `returned_to_sender`, `lost` |
| Leg | `planned`, `departed`, `arrived`, `skipped` |
| Pickup | `scheduled`, `completed`, `missed`, `canceled` |
| Customs declaration | `draft`, `submitted`, `cleared`, `held`, `rejected` |

EPCIS describes each event with a business step (`bizStep`), such as `shipping`, `receiving` or `departing`, and a disposition, such as `in_transit` or `in_progress`. GS1 CBV defines these values as URNs, for example `urn:epcglobal:cbv:bizstep:shipping`. The short form is the choice of this guide. Many carriers show a shorter status list to the customer. The states above are the choice of this guide.

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Book a consignment | `book_consignment` | Confirms the transport order. | |
| Cancel a consignment | `cancel_consignment` | Stops a booked order before pickup. | |
| Create a shipment | `create_shipment` | Makes the record of one transport. | |
| Plan a route | `plan_route` | Chooses the legs. | |
| Schedule a pickup | `schedule_pickup` | Plans the collection. | |
| Pick up | `pick_up_parcel` | Records the collection. | `pickup` is the noun for the visit. The verb is two words: `pick_up`. |
| Scan a parcel | `scan_parcel` | Records a tracking event. | |
| Load a vehicle | `load_vehicle` | Adds parcels to a manifest. | |
| Depart | `depart_leg` | Starts a leg. | |
| Arrive | `arrive_leg` | Ends a leg. | |
| Attempt a delivery | `attempt_delivery` | Records a try. | One try is not a delivery. |
| Deliver | `deliver_parcel` | Records a successful handover. | Needs proof of delivery. |
| Return to sender | `return_to_sender` | Sends the parcel back. | |
| Declare to customs | `submit_customs_declaration` | Files the declaration. | |
| Calculate a rate | `calculate_rate` | Prices a shipment. | |
| Aggregate | `aggregate_parcels` | Puts parcels on a pallet. | EPCIS `AggregationEvent`. |

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `shipment` | The order, the box and the trip are different things. | `consignment` for the order, `parcel` for the box, `shipment` for the trip. |
| `package` and `parcel` | Two words for the box. | `parcel` for the carrier unit. Keep `package` for the software meaning. |
| `tracking_number` | Whose number? Two carriers can issue the same number. | `tracking_number` with `carrier_id`. A pair is unique. |
| `status` | Transport, customs and billing have different states. | `shipment_status`, `customs_status`, `billing_status` in code. Inside a table the column is `status`. A customs state lives in `customs_declarations.status`. |
| `delivery` and `shipment` | A delivery is the last step, not the whole move. | `shipment` for the move, `delivery_attempt` for a try. |
| `weight` | Gross, net or chargeable? | `gross_weight_grams`, `net_weight_grams`, `chargeable_weight_grams`. |
| `eta` | Estimated by whom? | `estimated_delivery_at` and `estimate_source` (carrier, model or manual). |
| `from` and `to` | `from` is a keyword in SQL and in Python imports. | `origin_location_id`, `destination_location_id`. |
| `address` | A place may be a depot, a home or a port. | `location_id` for a depot, `delivery_address_id` for a home. |
| `event` | An EPCIS event and a software event differ. | `tracking_event` for a fact on the move. |
| `leg` and `hop` | Two words for a part of a route. | `leg`. |
| `sscc` and `tracking_number` | A pallet code and a carrier code. | `sscc` for a pallet or a logistic unit, `tracking_number` for a carrier parcel. |
| `incoterm` as free text | The rule needs a fixed code. | `incoterm_code` with a check list. |

## Worked example

The tables `consignments`, `carriers`, `locations` and `parcels` are not shown. The table `consignments` holds `incoterm_code` with a check on the allowed codes (EXW, FCA, CPT, CIP, DAP, DPU, DDP, FAS, FOB, CFR, CIF).

```sql
CREATE TABLE shipments (
    id                          bigint GENERATED ALWAYS AS IDENTITY,
    consignment_id              bigint NOT NULL,
    carrier_id                  bigint NOT NULL,
    tracking_number             text NOT NULL,
    origin_location_id          bigint NOT NULL,
    destination_location_id     bigint NOT NULL,
    status                      text NOT NULL DEFAULT 'created',
    estimated_delivery_at       timestamptz,
    delivered_at                timestamptz,
    created_at                  timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_shipments PRIMARY KEY (id),
    CONSTRAINT uq_shipments_carrier_id_tracking_number UNIQUE (carrier_id, tracking_number),
    CONSTRAINT fk_shipments_consignments FOREIGN KEY (consignment_id) REFERENCES consignments (id),
    CONSTRAINT fk_shipments_carriers FOREIGN KEY (carrier_id) REFERENCES carriers (id),
    CONSTRAINT fk_shipments_origin_location FOREIGN KEY (origin_location_id) REFERENCES locations (id),
    CONSTRAINT fk_shipments_destination_location FOREIGN KEY (destination_location_id) REFERENCES locations (id),
    CONSTRAINT chk_shipments_status_allowed CHECK (status IN (
        'created', 'picked_up', 'in_transit', 'out_for_delivery',
        'delivered', 'delivery_failed', 'returned_to_sender', 'lost'
    ))
);

CREATE INDEX idx_shipments_consignment_id ON shipments (consignment_id);
CREATE INDEX idx_shipments_origin_location_id ON shipments (origin_location_id);
CREATE INDEX idx_shipments_destination_location_id ON shipments (destination_location_id);

CREATE TABLE tracking_events (
    id                  bigint GENERATED ALWAYS AS IDENTITY,
    shipment_id         bigint NOT NULL,
    parcel_id           bigint,
    event_type          text NOT NULL,
    business_step       text NOT NULL,
    disposition         text,
    location_id         bigint,
    occurred_at         timestamptz NOT NULL,
    recorded_at         timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_tracking_events PRIMARY KEY (id),
    CONSTRAINT fk_tracking_events_shipments FOREIGN KEY (shipment_id) REFERENCES shipments (id),
    CONSTRAINT fk_tracking_events_parcels FOREIGN KEY (parcel_id) REFERENCES parcels (id),
    CONSTRAINT fk_tracking_events_locations FOREIGN KEY (location_id) REFERENCES locations (id),
    CONSTRAINT chk_tracking_events_event_type_allowed CHECK (event_type IN (
        'ObjectEvent', 'AggregationEvent', 'TransactionEvent',
        'TransformationEvent', 'AssociationEvent'
    ))
);

CREATE INDEX idx_tracking_events_shipment_id_occurred_at ON tracking_events (shipment_id, occurred_at);
CREATE INDEX idx_tracking_events_parcel_id ON tracking_events (parcel_id);
CREATE INDEX idx_tracking_events_location_id ON tracking_events (location_id);
```

```
POST /v1/consignments                                  create a consignment
POST /v1/consignments/{consignment_id}:book             book a consignment
POST /v1/consignments/{consignment_id}:cancel           cancel a consignment
GET  /v1/shipments/{shipment_id}                        get one shipment
GET  /v1/shipments/{shipment_id}/tracking-events        list the tracking events
```

```
ConsignmentBooked   ConsignmentCanceled   ShipmentCreated   ParcelPickedUp
ParcelScanned   DeliveryAttempted   DeliveryFailed   ParcelDelivered
```

```py
def record_scan(
    shipment: Shipment,
    location_id: int,
    business_step: str,
    occurred_at: datetime,
    parcel_id: int | None = None,
) -> TrackingEvent:
    if shipment.shipment_status in {"delivered", "returned_to_sender", "lost"}:
        raise ShipmentClosedError(shipment.id)
    return TrackingEvent(
        shipment_id=shipment.id,
        parcel_id=parcel_id,
        event_type="ObjectEvent",
        business_step=business_step,
        location_id=location_id,
        occurred_at=occurred_at,
    )
```

## Related patterns

- [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) for `weight_grams` and `estimated_delivery_at`
- [Action and context](../patterns/action-context.md) for `scan_parcel` and `deliver_parcel`
- [Events](../systems/events.md) for names such as `ParcelDelivered`

!!! info "See also"

    - [Examples overview](index.md), [E-commerce](ecommerce.md) and [Tables](../databases/tables.md)
    - [GS1 EPCIS and CBV](https://www.gs1.org/standards/epcis), [UN/LOCODE](https://unece.org/trade/uncefact/unlocode), [Incoterms](https://iccwbo.org/business-solutions/incoterms-rules/)
