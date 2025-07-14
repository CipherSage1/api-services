package com.organization.sage.model.payment;

import java.math.BigDecimal;
import java.util.Map;

import com.organization.sage.model.organisation.ParcelType;
import com.organization.sage.model.organisation.ShipmentType;

public class Pricing {
    private String from;
    private String to;
    private Map<ShipmentType, BigDecimal> shipmentTypesPricing;
    private Map<ParcelType, BigDecimal> parcelTypesPricing;

    public String getFrom() {
        return from;
    }

    public void setFrom(String from) {
        this.from = from;
    }

    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
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
                "from: '" + from + '\'' +
                ", to: '" + to + '\'' +
                ", shipmentTypesPricing: " + shipmentTypesPricing +
                ", parcelTypesPricing: " + parcelTypesPricing +
                '}';
    }
}
