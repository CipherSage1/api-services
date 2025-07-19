package com.organization.sage.model.payment;

import java.math.BigDecimal;
import java.util.Map;

import com.organization.sage.model.organisation.ParcelType;
import com.organization.sage.model.organisation.ShipmentType;

public class Pricing {
    private String fromLocation; 
    private String toLocation;
    private Map<ShipmentType, BigDecimal> shipmentTypesPricing;
    private Map<ParcelType, BigDecimal> parcelTypesPricing;

    public String getFromLocation() {
        return fromLocation;
    }

    public void setFrom(String fromLocation) {
        this.fromLocation = fromLocation;
    }

    public String getToLocation() {
        return toLocation;
    }

    public void setTo(String toLocation) {
        this.toLocation = toLocation;
    }

    public Map<ShipmentType, BigDecimal> getShipmentTypesPricing() {
        return shipmentTypesPricing;
    }

    public void setShipmentTypesPricing(Map<ShipmentType, BigDecimal> shipmentTypesPricing) {
        this.shipmentTypesPricing = shipmentTypesPricing;
    }

    public Map<ParcelType, BigDecimal> getparcelTypesPricing() {
        return parcelTypesPricing;
    }

    public void setparcelTypesPricing(Map<ParcelType, BigDecimal> parcelTypesPricing) {
        this.parcelTypesPricing = parcelTypesPricing;
    }

    @Override
    public String toString() {
        return "{ " +
                "from: '" + fromLocation + '\'' +
                ", to: '" + toLocation + '\'' +
                ", shipmentTypesPricing: " + shipmentTypesPricing +
                ", parcelTypesPricing: " + parcelTypesPricing +
                '}';
    }
}
